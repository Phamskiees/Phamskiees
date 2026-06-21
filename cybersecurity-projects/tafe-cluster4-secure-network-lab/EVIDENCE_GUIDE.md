# Evidence Guide

This guide maps the private Cluster 4 lab evidence into public-safe portfolio
language. It does not reproduce the private report or screenshots.

| Area | Private evidence type | Public-safe summary |
|---|---|---|
| Virtualisation | VM setup and resource screenshots | Built an isolated multi-VM lab in VirtualBox |
| Network design | Topology and interface evidence | Designed staff, server, and DMZ segments behind pfSense |
| pfSense | Interface, firewall, NAT, and rule screenshots | Configured firewall-controlled access between lab zones |
| Rocket.Chat | Installer, dashboard, user/channel, and access tests | Deployed and validated an internal communication service |
| FreeRADIUS | Service status, client config, and authentication tests | Configured AAA service and verified authentication behavior |
| OpenVPN | Server, certificate, export, rule, and status screenshots | Built remote-access VPN capability through pfSense |
| SSH | Service status and access tests | Validated secure administration to Linux service hosts |
| MFA/TOTP | Setup and login validation screenshots | Added multi-factor authentication to the communication workflow |
| Backup/DR | Backup files, restore pages, and recovery checks | Demonstrated backup, restore, and disaster-recovery validation |
| Final testing | Connectivity, blocking, service, VPN, SSH, and backup checks | Confirmed expected access worked and restricted paths were blocked |

## Redaction Rules

Before any evidence is made public, remove or replace:

- student name, student ID, email addresses, and personal usernames;
- shared secrets, test passwords, private keys, tokens, and recovery codes;
- browser tabs, profile details, downloads paths, and local desktop context;
- real pfSense exports, VPN profiles, VM disks, and configuration backups;
- assessment templates or copied answer text.

## Safe Portfolio Evidence Ideas

- Recreate the topology as a neutral diagram.
- Create a generic firewall rule matrix.
- Write a short validation table showing "allowed", "blocked", and "restored"
  outcomes without exposing raw screenshots.
- Use placeholder addresses such as `10.0.10.0/24`, `10.0.20.0/24`, and
  `10.0.30.0/24` for public examples.
