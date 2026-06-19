# Evidence Map

| Evidence | What it shows | Public-safety note |
|---|---|---|
| [`virtualbox-nat-network.png`](evidence/screenshots/virtualbox-nat-network.png) | Dedicated VirtualBox NAT network for the lab | Shows lab-only RFC1918 addressing |
| [`apache-default-page.png`](evidence/screenshots/apache-default-page.png) | Kali browser reaching Ubuntu Apache2 | No credentials or personal identifiers shown |
| [`basic-nmap-scan.png`](evidence/screenshots/basic-nmap-scan.png) | Nmap identifying SSH and HTTP on the Ubuntu host | Authorized local VM target only |
| [`service-version-scan.png`](evidence/screenshots/service-version-scan.png) | Nmap service-version detection for SSH and Apache | Useful for defensive asset inventory practice |

## Local Evidence Not Published

Some original screenshots were intentionally excluded because they showed a
personal username, student number, broader VM inventory, or unnecessary local
details. They can remain in the local TAFE workspace as private study evidence,
but they are not suitable for a public GitHub portfolio.

## Learning Summary

The evidence supports a simple but important workflow:

1. Build an isolated network.
2. Confirm host addressing and connectivity.
3. Start a known service.
4. Validate the service from another host.
5. Run an authorized Nmap scan.
6. Record findings in a way that is clear and safe to publish.
