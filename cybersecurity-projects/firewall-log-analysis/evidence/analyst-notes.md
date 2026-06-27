# Analyst Notes - Synthetic Firewall Log Review

## Scope

This review uses the sanitized sample Windows Firewall log in
`sample-data/pfirewall-sanitized.log`. The addresses are documentation ranges
and do not represent a real organisation or public target.

## Summary

The parser normalized 5 firewall events:

- 3 allowed events
- 2 dropped events
- 3 TCP events
- 2 UDP events

The allowed traffic is consistent with expected web and DNS-style activity in a
small lab sample. The dropped traffic highlights connection attempts to services
that would normally deserve review in a Windows environment.

## Notable Events

| Event | Observation | Analyst interpretation |
|---|---|---|
| Dropped TCP to port 3389 | External documentation address attempted RDP | Expected firewall block; review whether RDP should be exposed anywhere |
| Dropped UDP to port 161 | External documentation address attempted SNMP | Expected firewall block; confirm SNMP is disabled or restricted |
| Allowed TCP to port 443 | Lab client reached HTTPS service | Expected allowed service traffic |
| Allowed UDP to port 53 | Host sent DNS-style traffic | Expected name-resolution style traffic |

## Recommended Follow-Up

- Confirm that RDP is restricted to approved management networks only.
- Confirm that SNMP is disabled or limited to approved monitoring systems.
- Compare firewall drops with Windows Event Logs or endpoint telemetry.
- If this were a real incident, check whether the same source repeats across a
  longer time window.

## Portfolio Value

This evidence demonstrates basic SOC-style workflow:

- parse raw logs into structured data;
- summarize traffic patterns;
- identify notable denied services;
- explain likely analyst actions;
- keep public evidence sanitized.
