# TAFE Cluster 4 Secure Network Lab

Sanitized portfolio summary of my TAFE NSW Diploma of Information Technology
Cluster 4 lab. The lab built a secure enterprise communication platform using
virtual machines, segmented networks, firewall rules, AAA, VPN access, secure
administration, MFA, backup, disaster recovery, and final validation.

This is a public-safe summary of the skills demonstrated in my private TAFE lab
work. It does not include assessment answers, raw screenshots, student ID,
credentials, shared secrets, real configuration backups, VM images, or private
lab exports.

## Lab Scenario

The private lab was built as an enterprise-style secure communication platform.
The environment used a firewall/router VM to separate staff, server, and DMZ
networks, then deployed communication and authentication services behind those
controls.

## Main Components

| Component | Portfolio-safe role |
|---|---|
| VirtualBox | Hypervisor used to run the isolated lab VMs |
| pfSense | Firewall, router, NAT, segmentation, and OpenVPN platform |
| Rocket.Chat | Internal communication server placed in a DMZ-style zone |
| FreeRADIUS | AAA service for authentication testing |
| Ubuntu Desktop | Staff/client endpoint for access and validation |
| OpenVPN | Remote-access VPN service managed through pfSense |
| SSH | Secure administrative access to Linux servers |
| TOTP/MFA | Additional login protection for communication access |

## Skills Demonstrated

- Designed a segmented virtual network with separate staff, server, and DMZ
  zones.
- Configured pfSense interfaces, firewall rules, NAT, and service access.
- Deployed and tested a Rocket.Chat communication server.
- Deployed FreeRADIUS and validated AAA authentication behavior.
- Configured OpenVPN remote-access services and supporting firewall rules.
- Hardened SSH administration for Linux service hosts.
- Enabled and validated MFA/TOTP behavior in the communication workflow.
- Created backup and restore evidence for lab services and firewall
  configuration.
- Performed final validation of connectivity, service access, firewall blocking,
  authentication, VPN status, SSH access, and recovery evidence.

## Public Evidence Approach

The private lab report and screenshots contain sensitive details, so the public
portfolio version uses sanitized descriptions instead of raw evidence. A safe
public version can include:

- a redrawn topology using generic network labels;
- a task-to-skill evidence table;
- sanitized command examples with placeholder addresses;
- lessons learned and defensive design notes;
- links to original supporting tools, such as the Cluster 4 network validator.

Do not publish raw screenshots unless they have been redacted for usernames,
student details, browser state, internal addressing, shared secrets, passwords,
and private lab labels.

## Related Portfolio Project

- [TAFE Cluster 4 Network Validation Prototype](../cluster4-network-validation):
  supporting Python CLI for validating approved TCP services in an isolated lab.

## What I Learned

This project connected multiple security-administration skills into one lab:
network segmentation, firewall rule design, secure service placement, identity
and access testing, VPN access, secure remote administration, backup planning,
disaster recovery, and professional validation reporting.
