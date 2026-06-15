# Site-to-Site VPN Configuration Auditor

Offline Python scanner for sanitized Cisco IOS-style VPN configuration. It
identifies legacy IKE/IPsec algorithms, weak Diffie-Hellman groups, exposed
pre-shared keys, missing traffic selectors, missing PFS, and absent verification
notes.

## Portfolio purpose

This project turns VPN configuration knowledge into a defensive review tool.
It is not an exploitation tool and does not connect to routers or VPN peers.

Relevant study sources include:

- Advanced Diploma Network Security project: `ICTNWK537`, `ICTNWK544`,
  `ICTNWK618`.
- Advanced Diploma Cluster 2 VPN labs and Cisco Packet Tracer activities.
- Separate `VU23216` / `VU23218` network-security and data-analysis project.
- Certificate IV Network Security VPN Server and tunnel-forwarding labs.

## Run

```powershell
python vpn_audit.py sample-data/vpn-legacy-sanitized.cfg `
  --json evidence/legacy-report.json
python vpn_audit.py sample-data/vpn-modern-sanitized.cfg `
  --json evidence/modern-report.json
python -m unittest -v
```

The scanner is a learning aid. Validate findings against the platform version,
organizational cryptographic policy, vendor guidance, and approved change
process before modifying a production device.
