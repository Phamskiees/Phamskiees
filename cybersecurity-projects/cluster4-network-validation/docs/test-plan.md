\# Test Plan



\## Purpose



The purpose of this test plan is to validate approved TCP services inside an isolated enterprise lab environment and produce repeatable evidence for network testing.



\## Scope



This project validates selected TCP services only. It does not directly test UDP-based services such as RADIUS or OpenVPN.



\## Test Environment



\- Firewall: pfSense

\- Server: Ubuntu Server

\- Client: Ubuntu Desktop

\- Services tested:

&#x20; - pfSense web interface

&#x20; - Rocket.Chat

&#x20; - SSH

&#x20; - One intentionally blocked or closed service



\## Test Method



1\. Define approved lab networks in `allowed\_networks`.

2\. Define approved TCP services in the services configuration file.

3\. Run the Python validation script.

4\. Export results to JSON and CSV.

5\. Compare reachability results with pfSense firewall rules and logs.

6\. Save screenshots as supporting evidence.



\## Expected Results



| Test | Expected Result |

|---|---|

| Approved pfSense web interface | PASS |

| Approved Rocket.Chat service | PASS |

| Approved SSH service | PASS |

| Blocked or closed service | FAIL |



\## Evidence Collected



\- Terminal output

\- JSON result file

\- CSV result file

\- Unit test screenshot

\- pfSense firewall log screenshot

\- Redacted lab validation screenshot

