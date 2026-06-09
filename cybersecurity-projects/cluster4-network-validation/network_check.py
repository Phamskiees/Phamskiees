"""Validate approved TCP services in an isolated lab."""

from __future__ import annotations

import argparse
import csv
import ipaddress
import json
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_CONFIG = Path(__file__).with_name("services.json")
DOCUMENTATION_NETWORKS = (
    ipaddress.ip_network("192.0.2.0/24"),
    ipaddress.ip_network("198.51.100.0/24"),
    ipaddress.ip_network("203.0.113.0/24"),
)


class ConfigError(ValueError):
    """Raised when a configuration is unsafe or invalid."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check approved TCP services and produce reusable evidence."
    )
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--timeout", type=float, default=3.0)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--csv-out", type=Path)
    return parser.parse_args()


def load_config(path: Path) -> tuple[list[ipaddress.IPv4Network | ipaddress.IPv6Network], list[dict[str, Any]]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ConfigError(f"cannot read configuration: {error}") from error

    if not isinstance(data, dict):
        raise ConfigError("configuration root must be an object")

    try:
        allowed_networks = [ipaddress.ip_network(item) for item in data["allowed_networks"]]
        services = data["services"]
    except (KeyError, TypeError, ValueError) as error:
        raise ConfigError(f"invalid allowed_networks or services: {error}") from error

    if not allowed_networks:
        raise ConfigError("at least one allowed network is required")
    if not isinstance(services, list) or not services:
        raise ConfigError("at least one service is required")

    validated_services: list[dict[str, Any]] = []
    for index, service in enumerate(services, start=1):
        if not isinstance(service, dict):
            raise ConfigError(f"service {index} must be an object")
        try:
            name = str(service["name"]).strip()
            host = ipaddress.ip_address(service["host"])
            port = int(service["port"])
        except (KeyError, TypeError, ValueError) as error:
            raise ConfigError(f"service {index} is invalid: {error}") from error
        if not name:
            raise ConfigError(f"service {index} has an empty name")
        if not 1 <= port <= 65535:
            raise ConfigError(f"service {index} has an invalid port")
        if not any(host in network for network in allowed_networks):
            raise ConfigError(f"service {index} target {host} is outside allowed networks")
        validated_services.append({"name": name, "host": str(host), "port": port})

    return allowed_networks, validated_services


def check_service(host: str, port: int, timeout: float) -> tuple[str, str]:
    address = ipaddress.ip_address(host)
    if any(address in network for network in DOCUMENTATION_NETWORKS):
        return "SKIP", "documentation-only address"
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return "PASS", "connection accepted"
    except OSError as error:
        return "FAIL", str(error)


def build_report(services: list[dict[str, Any]], timeout: float) -> dict[str, Any]:
    checked_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    results = []
    for service in services:
        status, detail = check_service(service["host"], service["port"], timeout)
        results.append({**service, "status": status, "detail": detail})

    return {
        "checked_at": checked_at,
        "timeout_seconds": timeout,
        "summary": {
            status.lower(): sum(result["status"] == status for result in results)
            for status in ("PASS", "FAIL", "SKIP")
        },
        "results": results,
    }


def write_json(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=("checked_at", "name", "host", "port", "status", "detail")
        )
        writer.writeheader()
        for result in report["results"]:
            writer.writerow({"checked_at": report["checked_at"], **result})


def print_report(report: dict[str, Any]) -> None:
    print(f"Lab service validation - {report['checked_at']}")
    print("=" * 72)
    for result in report["results"]:
        print(
            f"{result['status']:4} | {result['name']} | "
            f"{result['host']}:{result['port']} | {result['detail']}"
        )
    summary = report["summary"]
    print("=" * 72)
    print(
        f"Passed: {summary['pass']} | Failed: {summary['fail']} | "
        f"Skipped: {summary['skip']}"
    )


def main() -> int:
    args = parse_args()
    if args.timeout <= 0:
        print("ERROR: timeout must be greater than zero", file=sys.stderr)
        return 2
    try:
        _, services = load_config(args.config)
    except ConfigError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    report = build_report(services, args.timeout)
    print_report(report)
    if args.json_out:
        write_json(args.json_out, report)
    if args.csv_out:
        write_csv(args.csv_out, report)
    return 1 if report["summary"]["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
