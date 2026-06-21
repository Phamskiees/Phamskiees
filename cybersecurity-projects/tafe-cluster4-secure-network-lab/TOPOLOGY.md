# Sanitized Topology

The private lab used a segmented design. This diagram avoids real hostnames,
student details, credentials, and unnecessary internal addresses.

```mermaid
flowchart LR
    Internet["Internet / NAT"]
    Firewall["pfSense firewall<br/>Routing, NAT, VPN, segmentation"]
    Staff["Staff network<br/>Client endpoint"]
    Server["Server network<br/>AAA service"]
    DMZ["DMZ network<br/>Communication service"]
    VPN["OpenVPN remote access"]

    Internet --> Firewall
    VPN --> Firewall
    Firewall --> Staff
    Firewall --> Server
    Firewall --> DMZ
    Staff -->|"Allowed admin and app access"| DMZ
    Staff -->|"Allowed authentication tests"| Server
    DMZ -. "Restricted by firewall policy" .-> Server
```

## Design Notes

- Staff systems were separated from server and DMZ services.
- pfSense acted as the control point for routing, NAT, firewall policy, and VPN.
- Rocket.Chat was placed in a DMZ-style zone to separate the communication
  service from internal authentication infrastructure.
- FreeRADIUS was placed in a server zone for AAA testing.
- OpenVPN provided the remote-access control point.
- Final testing checked both allowed access and blocked paths.
