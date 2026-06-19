# Home Cybersecurity Lab

Small isolated lab built with VirtualBox, Kali Linux, Ubuntu Server, Apache,
and Nmap. The goal was to practise legal network setup, basic service
deployment, connectivity testing, and service discovery inside a private lab.

## What This Demonstrates

- Built a separate NAT lab network for security practice.
- Deployed Kali Linux as the testing workstation.
- Deployed Ubuntu Server as the target/server host.
- Installed and verified Apache2 on Ubuntu.
- Tested host-to-host connectivity before scanning.
- Used Nmap to identify open TCP services and service versions.
- Captured evidence while keeping the work legal, isolated, and repeatable.

## Lab Topology

```text
Kali Linux tester
        |
VirtualBox NAT lab network
        |
Ubuntu Server target
        |
Apache2 web service
```

All testing was performed against my own local virtual machines. This project
does not include exploitation steps, credentials, private assessment answers, or
production-system targets.

## Evidence

Selected public-safe screenshots are in
[`evidence/screenshots`](evidence/screenshots). Screenshots that contained
personal identifiers, student numbers, or unnecessary VM inventory details were
kept out of the public repository.

See [`EVIDENCE.md`](EVIDENCE.md) for the evidence map.

## Skills Practised

- VirtualBox network configuration
- Linux command-line basics
- Apache service installation and validation
- ICMP connectivity testing
- Nmap host and service discovery
- Portfolio-safe evidence handling

## Safe Reproduction Notes

Only scan systems you own or are explicitly authorized to test. For a portfolio
version, use private lab IP addresses, redact usernames and student IDs, and do
not publish credentials, VPN profiles, VM disk images, or full machine exports.
