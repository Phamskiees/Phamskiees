#!/usr/bin/env python3
"""Summarize sanitized TShark field exports without requiring packet payloads."""

from __future__ import annotations

import argparse
import csv
import ipaddress
import json
from collections import Counter
from pathlib import Path
from typing import Iterable


REQUIRED_FIELDS = {
    "frame.number",
    "frame.time_epoch",
    "ip.src",
    "ip.dst",
    "_ws.col.Protocol",
    "frame.len",
}


def anonymize_ip(value: str) -> str:
    """Map an IP address to a stable documentation prefix."""
    if not value:
        return "unknown"
    try:
        address = ipaddress.ip_address(value)
    except ValueError:
        return "invalid"
    if address.version == 4:
        final_octet = int(str(address).split(".")[-1])
        return f"192.0.2.{final_octet}"
    suffix = int(address) & 0xFFFF
    return f"2001:db8::{suffix:x}"


def truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "set"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_FIELDS - fields
        if missing:
            raise ValueError(f"missing required fields: {', '.join(sorted(missing))}")
        return list(reader)


def summarize(rows: Iterable[dict[str, str]], anonymize: bool = True) -> dict:
    protocol_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    destination_counts: Counter[str] = Counter()
    dns_queries: Counter[str] = Counter()
    total_bytes = 0
    retransmissions = 0
    syn_without_ack = 0
    first_time: float | None = None
    last_time: float | None = None
    packet_count = 0

    for row in rows:
        packet_count += 1
        protocol_counts[row["_ws.col.Protocol"].strip().upper() or "UNKNOWN"] += 1
        source = row["ip.src"].strip()
        destination = row["ip.dst"].strip()
        source_counts[anonymize_ip(source) if anonymize else source or "unknown"] += 1
        destination_counts[
            anonymize_ip(destination) if anonymize else destination or "unknown"
        ] += 1
        total_bytes += int(row["frame.len"] or 0)

        timestamp = float(row["frame.time_epoch"])
        first_time = timestamp if first_time is None else min(first_time, timestamp)
        last_time = timestamp if last_time is None else max(last_time, timestamp)

        if truthy(row.get("tcp.analysis.retransmission", "")):
            retransmissions += 1
        if truthy(row.get("tcp.flags.syn", "")) and not truthy(
            row.get("tcp.flags.ack", "")
        ):
            syn_without_ack += 1
        query = row.get("dns.qry.name", "").strip().lower()
        if query:
            dns_queries[query] += 1

    duration = 0.0
    if first_time is not None and last_time is not None:
        duration = round(last_time - first_time, 6)

    return {
        "packet_count": packet_count,
        "total_bytes": total_bytes,
        "capture_duration_seconds": duration,
        "protocols": dict(protocol_counts.most_common()),
        "top_sources": dict(source_counts.most_common(10)),
        "top_destinations": dict(destination_counts.most_common(10)),
        "dns_queries": dict(dns_queries.most_common(20)),
        "indicators": {
            "tcp_retransmissions": retransmissions,
            "tcp_syn_without_ack": syn_without_ack,
        },
        "privacy": {
            "ip_addresses_anonymized": anonymize,
            "payloads_processed": False,
        },
    }


def render_markdown(summary: dict) -> str:
    protocols = "\n".join(
        f"| {name} | {count} |" for name, count in summary["protocols"].items()
    )
    return (
        "# Traffic Summary\n\n"
        f"- Packets: {summary['packet_count']}\n"
        f"- Bytes: {summary['total_bytes']}\n"
        f"- Duration: {summary['capture_duration_seconds']} seconds\n"
        f"- TCP retransmissions: {summary['indicators']['tcp_retransmissions']}\n"
        f"- SYN packets without ACK: {summary['indicators']['tcp_syn_without_ack']}\n\n"
        "## Protocols\n\n| Protocol | Count |\n|---|---:|\n"
        f"{protocols}\n\n"
        "This report was generated from packet metadata only. Packet payloads were "
        "not processed.\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="TShark CSV field export")
    parser.add_argument("--json", type=Path, help="write JSON summary")
    parser.add_argument("--markdown", type=Path, help="write Markdown summary")
    parser.add_argument(
        "--keep-ips",
        action="store_true",
        help="retain source and destination IPs (not recommended for public evidence)",
    )
    args = parser.parse_args()

    summary = summarize(load_rows(args.input), anonymize=not args.keep_ips)
    output = json.dumps(summary, indent=2)
    print(output)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(render_markdown(summary), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
