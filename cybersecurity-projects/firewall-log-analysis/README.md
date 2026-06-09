# Windows Firewall Log Analyzer

A PowerShell project that converts Windows Firewall text logs into concise,
repeatable summaries for network-security and incident-response evidence.

## Assessment connection

- Course: Certificate IV in Cyber Security
- Units: `VU23216` Perform basic cyber security data analysis;
  `VU23218` Implement network security infrastructure for an organisation
- Relevant task: Part 1 Task 3, firewall configuration, functionality
  verification, and analysis of permitted/denied traffic
- Supporting lab: `C2T05L1 - Windows Firewall Log Setup and Analysis`
- Source folder:
  `E:\TAFE\cert 4 cyber security\cert iv\cert iv\network security`

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\Analyze-FirewallLog.ps1 `
  -Path .\sample-data\pfirewall-sanitized.log `
  -OutputDirectory .\evidence
```

`-ExecutionPolicy Bypass` applies only to that PowerShell process and does not
change the machine or user execution policy.

Outputs:

- `events.csv`: normalized event records
- `summary.json`: counts by action, protocol, source, and destination port

## Checklist

- [x] Parse standard `#Fields` header
- [x] Ignore comments and malformed records
- [x] Export normalized events
- [x] Summarize allow/drop activity
- [x] Include synthetic test data
- [ ] Run against a private copy of a real lab firewall log
- [ ] Explain expected versus unexpected dropped traffic
- [ ] Correlate a selected event with a Wireshark capture
- [ ] Add a sanitized incident-analysis narrative

## Resources

- [Microsoft Windows Firewall logging](https://learn.microsoft.com/windows/security/operating-system-security/network-security/windows-firewall/configure-logging):
  official logging configuration and log location guidance.
- [PowerShell Import-Csv](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/import-csv):
  structured data handling concepts used by the parser.
- [PowerShell ConvertTo-Json](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/convertto-json):
  machine-readable report export.
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/index.html):
  display filters and packet inspection.
- [Wireshark display filter reference](https://www.wireshark.org/docs/dfref/):
  authoritative protocol/field names.

## Public safety

The sample log is synthetic. Real logs can expose internal addresses,
hostnames, users, applications, and activity patterns. Keep raw logs private
and publish only redacted or regenerated evidence.
