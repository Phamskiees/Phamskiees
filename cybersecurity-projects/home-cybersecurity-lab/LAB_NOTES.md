# Lab Notes

## Scope

This was a local, self-owned virtual lab. The target was an Ubuntu Server VM
running Apache2. The testing host was Kali Linux. Nmap was used only inside the
lab network.

## Process

1. Created a VirtualBox NAT network for the lab.
2. Connected the Kali and Ubuntu Server VMs to the same lab network.
3. Confirmed each VM had an expected private lab address.
4. Tested connectivity with ping.
5. Installed and started Apache2 on Ubuntu Server.
6. Opened the Apache default page from Kali.
7. Ran Nmap scans to confirm exposed services.

## Observed Services

The lab scan identified:

- `22/tcp` open for SSH.
- `80/tcp` open for HTTP / Apache.

This is expected for a basic Linux server lab. A defensive follow-up would be to
document which services are required, disable unused services, and apply host
firewall rules for the intended lab traffic only.

## Portfolio-Safe Treatment

The public version keeps only safe screenshots and generalized notes. It avoids
publishing usernames, student numbers, unnecessary VM names, credentials, VM
images, or private assessment material.
