# TAFE Cluster 4 Network Validation Prototype

A Python CLI prototype that checks approved TCP services in an isolated
enterprise-style lab and exports timestamped JSON/CSV evidence.

## TAFE NSW portfolio note

This project was developed for my public cybersecurity portfolio from skills
practised during TAFE NSW Diploma of Information Technology Cluster 4,
Advanced Network Management and Security. It is original supporting work for
learning and demonstration. It is not a copied assessment answer, not a PEAS
submission file, and does not include private lab credentials or assessment
templates.

## Assessment connection

- Course: Diploma of Information Technology (Cyber Security)
- Cluster: Cluster 4, Advanced Network Management and Security
- Units: `ICTNWK536`, `ICTNWK546`, `ICTNWK557`, `ICTNWK559`
- Relevant task: PEAS Task 13 testing and validation, with supporting value
  for firewall, VPN, SSH, AAA, communication-server, backup, and recovery tests
- Source folder: `E:\TAFE\diploma cyber\cluster 4`

This is a portfolio implementation inspired by learned testing methods. It is
not a copy of the assessment answer or template.

## Usage

1. Copy `services.json` to a private working file.
2. Replace the documentation addresses with addresses from your isolated lab.
3. Set `allowed_networks` to the exact authorized lab CIDRs.
4. Run:

```powershell
python network_check.py `
  --config services.private.json `
  --json-out evidence/results.json `
  --csv-out evidence/results.csv
```

The committed sample uses RFC 5737 documentation addresses and is skipped
without making network connections.

## Evidence checklist

- [x] Safe sample configuration
- [x] Explicit network allowlist
- [x] TCP reachability results
- [x] Timestamped console report
- [x] JSON and CSV export
- [x] Unit tests for scope validation and output
- [x] Test plan and methodology documentation
- [x] Screenshot evidence for safe sample run, unit tests, generated evidence,
  Git tracking checks, and project structure
- [x] Evidence report prepared for portfolio review
- [ ] Run against the completed PEAS lab
- [ ] Capture an allowed service and an intentionally blocked service
- [ ] Compare results with pfSense firewall logs

## Evidence report

- [Cluster 4 Network Validation Evidence Report](report/Cluster4_Network_Validation_Evidence_Report.docx)
- [Test plan](docs/test-plan.md)
- [Methodology](docs/methodology.md)
- [Sample JSON evidence](evidence/results.sample.json)
- [Sample CSV evidence](evidence/results.sample.csv)

Screenshots in `screenshots/` show the safe sample run, unit tests, generated
evidence files, project structure, and Git tracking checks. They use
documentation-only sample data rather than private PEAS lab targets.

## Portfolio-safe evidence

Publish only synthetic or redacted examples. Do not commit the real PEAS IP
plan, credentials, VPN profiles, pfSense `config.xml`, private keys, tokens,
student identifiers, or screenshots containing personal data.

## Resources

- [Python argparse](https://docs.python.org/3/library/argparse.html): CLI design.
- [Python ipaddress](https://docs.python.org/3/library/ipaddress.html): validates
  targets against explicitly allowed networks.
- [pfSense firewall rules](https://docs.netgate.com/pfsense/en/latest/firewall/configure.html):
  supports interpretation of pass, block, and reject results.
- [pfSense OpenVPN troubleshooting](https://docs.netgate.com/pfsense/en/latest/troubleshooting/openvpn.html):
  connects reachability tests with VPN status, routes, and firewall logs.
- [pfSense backup and recovery](https://docs.netgate.com/pfsense/en/latest/backup/index.html):
  supports repeatable before/after recovery validation.
