\# Methodology



\## Overview



This project uses a Python command-line tool to validate approved TCP services in an isolated lab. The tool checks whether each service is inside an authorised network range before attempting a connection.



\## Safety Controls



The script uses an explicit network allowlist. Any service target outside the approved range is rejected before testing. This prevents accidental scanning of unauthorised networks.



\## Why This Matters



In a real network environment, validation must be controlled, documented, and repeatable. This project demonstrates safe testing by limiting checks to approved lab addresses and exporting structured evidence.



\## Testing Approach



The tool performs TCP connection checks against approved hosts and ports. Results are marked as:



\- `PASS` when a connection is accepted

\- `FAIL` when the connection fails

\- `SKIP` when the address is documentation-only and should not be tested



\## Limitations



This project checks TCP reachability only. UDP services such as RADIUS and OpenVPN require separate validation using service logs, VPN status pages, authentication tests, or packet captures.



\## Portfolio Value



This project demonstrates:



\- Python scripting

\- Network validation

\- Safe scope control

\- Firewall testing support

\- Evidence collection

\- JSON and CSV reporting

\- Unit testing

\- Security documentation

