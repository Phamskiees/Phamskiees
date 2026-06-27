# Junior Cyber Security Portfolio Roadmap

This roadmap prioritizes the projects that best support junior cyber security
analyst, SOC analyst, and junior security engineer applications.

## Priority 1 - Polish Existing Strong Projects

### 1. Cluster 4 Network Validation Prototype

**Why it matters:** Shows Python, network validation, allowlisting, testing,
and structured evidence.

**Next improvements:**

- Run the tool against a private lab service list.
- Capture one allowed service and one intentionally blocked service.
- Compare results with firewall logs.
- Add a short "What I would investigate next" section to the report.

### 2. Site-to-Site VPN Configuration Auditor

**Why it matters:** Strong junior security engineer evidence. It shows config
review, crypto risk awareness, and defensive automation.

**Next improvements:**

- Add an approved-algorithm policy file.
- Add IKEv2 keyring/profile parsing.
- Add a short remediation table for common findings.
- Add one screenshot of a test run with synthetic data.

### 3. Packet Traffic Summary

**Why it matters:** Strong SOC analyst evidence. It shows packet metadata
analysis, anonymisation, and reporting.

**Next improvements:**

- Analyze one new private lab capture.
- Add one sanitized Wireshark screenshot.
- Write a short case note explaining one TCP retransmission or connection
  attempt.
- Add a "Detection questions" section: what looks normal, what looks unusual,
  and what more data would be needed.

### 4. Windows Firewall Log Analyzer

**Why it matters:** Very relevant to SOC analyst work. It shows log parsing,
summary reporting, and Windows security monitoring.

**Next improvements:**

- Run against a private lab firewall log.
- Correlate one firewall event with Wireshark or Windows Event Viewer.
- Add a sanitized incident-style timeline.
- Add basic tests for malformed log lines and expected summary counts.

## Priority 2 - Add One SOC Lab Project

Build one detection-focused lab with Wazuh, Splunk Free, Elastic, or Microsoft
Sentinel.

**Recommended first version:**

- Collect Windows or Linux authentication logs.
- Generate failed logins in your own lab.
- Create an alert or saved search for repeated failures.
- Add screenshots of the dashboard and alert.
- Write a one-page incident triage note.

**Portfolio title idea:**

`SOC Failed Login Detection Lab`

**Skills shown:**

- SIEM basics
- log collection
- detection logic
- alert triage
- analyst documentation

## Priority 3 - Add One Vulnerability Management Project

Build a small lab using OpenVAS/Greenbone or Nessus Essentials.

**Recommended first version:**

- Scan one owned vulnerable VM or intentionally configured lab host.
- Rank findings by severity and business risk.
- Write a remediation plan.
- Rescan after fixing one or two items.
- Document what changed.

**Portfolio title idea:**

`Vulnerability Management Lab`

**Skills shown:**

- vulnerability scanning
- risk ranking
- remediation planning
- before/after validation
- clear reporting

## Priority 4 - Improve GitHub Presentation

- Add a short description to the GitHub repository About section.
- Add repository topics: `cybersecurity`, `soc`, `python`, `powershell`,
  `network-security`, `blue-team`, `linux`, `portfolio`.
- Pin the profile repository and 3 strongest standalone projects if you split
  them into separate repos later.
- Keep public evidence sanitized.
- Use screenshots only when they show meaningful proof.

## Best Four Projects To Mention In Applications

1. Cluster 4 Network Validation Prototype
2. Site-to-Site VPN Configuration Auditor
3. Packet Traffic Summary
4. Windows Firewall Log Analyzer

These give the best balance of scripting, network security, analysis,
documentation, and safe testing.
