# Cyber Security Portfolio - Paul Pham

I am studying cyber security at TAFE NSW and building a practical portfolio for
junior cyber security analyst, SOC analyst, and junior security engineer roles.

My projects focus on safe lab work, defensive security, network validation, log
analysis, vulnerability review, scripting, and clear evidence reporting. All
public examples use synthetic, sanitized, or documentation-only data.

## Target Roles

- Junior Cyber Security Analyst
- SOC Analyst Level 1
- Junior Security Engineer
- IT Support / Security Support
- Network Security Trainee

## Core Skills Demonstrated

| Area | Evidence in this portfolio |
|---|---|
| Network security | Firewall rules, VPN concepts, segmentation, service validation |
| Security monitoring | Firewall log parsing, packet metadata summaries, analyst reporting |
| Python automation | Network checks, VPN config auditing, packet-summary tooling |
| PowerShell automation | Windows Firewall log analysis |
| Linux hardening | SSH hardening, UFW firewall rules, Nmap validation |
| Safe testing | Scope checking, rules of engagement, sanitized evidence |
| Documentation | Test plans, methodology notes, evidence reports, remediation guidance |

## Featured Cyber Security Projects

See the [junior cyber portfolio roadmap](JUNIOR_CYBER_PORTFOLIO_ROADMAP.md)
for the next project improvements I am working through.

### [TAFE Cluster 4 Network Validation Prototype](cybersecurity-projects/cluster4-network-validation)

Python CLI tool that checks approved TCP services in an isolated lab and exports
JSON/CSV evidence. Demonstrates network validation, allowlisting, structured
evidence, defensive input checks, unit testing, and pfSense-oriented testing
planning.

**Best role fit:** junior security engineer, network security trainee, SOC
analyst with scripting duties.

### [Site-to-Site VPN Configuration Auditor](cybersecurity-projects/vpn-config-audit)

Offline Python auditor for sanitized Cisco IOS-style IKE/IPsec configuration.
Flags legacy algorithms, weak Diffie-Hellman groups, exposed pre-shared keys,
missing PFS, and missing traffic selectors.

**Best role fit:** junior security engineer, network security analyst.

### [Packet Traffic Summary](cybersecurity-projects/packet-traffic-summary)

Python and TShark workflow that turns sanitized packet metadata into compact
JSON and Markdown summaries. Includes endpoint anonymisation, protocol counts,
DNS query summaries, TCP indicators, synthetic sample data, and tests.

**Best role fit:** SOC analyst, cyber security analyst, blue-team trainee.

### [Windows Firewall Log Analyzer](cybersecurity-projects/firewall-log-analysis)

PowerShell tool that parses Windows Firewall logs and exports normalized events
and summary data. Demonstrates log analysis, PowerShell automation, synthetic
test data, and incident-response evidence handling.

**Best role fit:** SOC analyst, cyber security analyst, Windows security
support.

### [Ubuntu Server Hardening and Validation Lab](cybersecurity-projects/ubuntu-server-hardening)

Sanitized Ubuntu hardening project from a private VirtualBox lab. Demonstrates
SSH hardening, UFW firewall controls, before/after Nmap validation, service
testing, and safe evidence handling.

**Best role fit:** junior security engineer, Linux support, security support.

### [Home Cybersecurity Lab](cybersecurity-projects/home-cybersecurity-lab)

VirtualBox lab using Kali Linux, Ubuntu Server, Apache2, and Nmap. Demonstrates
isolated lab networking, legal service discovery, basic Linux service
validation, and screenshot-based evidence.

**Best role fit:** entry-level cyber security, IT support moving into security.

### [Authorized Penetration-Test Lab Workbook](cybersecurity-projects/authorized-pentest-lab)

Authorization-first workbook with scope checks, rules of engagement, stop
conditions, and a security assessment report template. It focuses on ethical
testing boundaries, evidence handling, risk reporting, and remediation planning.

**Best role fit:** junior cyber analyst, security consultant trainee,
application security trainee.

### [TAFE Cluster 4 Secure Network Lab](cybersecurity-projects/tafe-cluster4-secure-network-lab)

Sanitized summary of a segmented enterprise-style lab using pfSense,
Rocket.Chat, FreeRADIUS, OpenVPN, SSH, MFA/TOTP, backups, disaster recovery,
and final validation.

**Best role fit:** junior security engineer, network security trainee.

## Training Profiles

- [LinkedIn](https://www.linkedin.com/in/paul-pham-96463a257/)
- [TryHackMe](https://tryhackme.com/r/p/paulpham097)
- [HackerRank](https://www.hackerrank.com/profile/paulpham097)

## Certifications

- [Certificate III of Information Technology at TAFE](Certificate%20III%20of%20Information%20Technology.pdf)
- [Certificate IV of Cyber Security at TAFE](Certificate%20IV%20of%20Cyber%20Security.pdf)

## Portfolio Safety

This repository does not publish passwords, private keys, VPN profiles, raw
firewall backups, unredacted internal addresses, student identifiers, assessment
answer sheets, or third-party target data. Public files are original portfolio
work based on private lab practice, synthetic examples, or sanitized evidence.
