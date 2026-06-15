#!/usr/bin/env python3
"""Audit a sanitized Cisco IOS-style site-to-site VPN configuration."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    severity: str
    rule: str
    message: str
    line: int | None = None


WEAK_PATTERNS = (
    ("high", "IKE_ENCRYPTION", re.compile(r"^\s*encr(?:yption)?\s+(des|3des)\b", re.I),
     "Replace DES/3DES with an approved AES-based proposal."),
    ("high", "IKE_HASH", re.compile(r"^\s*hash\s+(md5|sha)\b", re.I),
     "Replace MD5/SHA-1 with an approved SHA-2 integrity algorithm."),
    ("high", "IKE_DH_GROUP", re.compile(r"^\s*group\s+(1|2|5)\b", re.I),
     "Replace the legacy Diffie-Hellman group with an approved stronger group."),
    ("high", "IPSEC_TRANSFORM", re.compile(r"\besp-(des|3des|md5-hmac)\b", re.I),
     "Replace the legacy IPsec transform with an approved AES/SHA-2 proposal."),
    ("medium", "IKEV1", re.compile(r"^\s*crypto\s+isakmp\s+policy\b", re.I),
     "Document the IKEv1 dependency and plan migration to IKEv2 where supported."),
)


def audit_config(text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.splitlines()

    for number, line in enumerate(lines, start=1):
        for severity, rule, pattern, message in WEAK_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(severity, rule, message, number))
        if re.search(r"crypto\s+isakmp\s+key\s+\S+", line, re.I):
            value = re.split(r"\s+", line.strip(), maxsplit=4)
            key_value = value[3] if len(value) > 3 else ""
            if key_value.upper() not in {"<REDACTED>", "REDACTED"}:
                findings.append(
                    Finding(
                        "critical",
                        "EXPOSED_PSK",
                        "Remove the pre-shared key before sharing configuration evidence.",
                        number,
                    )
                )

    lower = text.lower()
    if "crypto map" not in lower:
        findings.append(
            Finding("high", "MISSING_CRYPTO_MAP", "No crypto map was detected.")
        )
    elif "set pfs" not in lower:
        findings.append(
            Finding(
                "medium",
                "MISSING_PFS",
                "No Perfect Forward Secrecy setting was detected in the crypto map.",
            )
        )
    if not re.search(r"^\s*match\s+address\b", text, re.I | re.M):
        findings.append(
            Finding(
                "high",
                "MISSING_INTERESTING_TRAFFIC",
                "No crypto-map traffic selector was detected.",
            )
        )
    if "show crypto" not in lower:
        findings.append(
            Finding(
                "info",
                "MISSING_VERIFICATION_NOTES",
                "Add sanitized verification commands such as show crypto ikev2 sa and show crypto ipsec sa.",
            )
        )
    return sorted(findings, key=lambda item: ("critical", "high", "medium", "low", "info").index(item.severity))


def build_report(path: Path, findings: list[Finding]) -> dict:
    counts = {level: 0 for level in ("critical", "high", "medium", "low", "info")}
    for finding in findings:
        counts[finding.severity] += 1
    return {
        "source": path.name,
        "finding_count": len(findings),
        "severity_counts": counts,
        "findings": [asdict(item) for item in findings],
        "scope": "offline configuration review only",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="sanitized Cisco IOS-style config")
    parser.add_argument("--json", type=Path, help="write JSON report")
    args = parser.parse_args()

    report = build_report(
        args.config, audit_config(args.config.read_text(encoding="utf-8"))
    )
    output = json.dumps(report, indent=2)
    print(output)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output + "\n", encoding="utf-8")
    return 1 if report["severity_counts"]["critical"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
