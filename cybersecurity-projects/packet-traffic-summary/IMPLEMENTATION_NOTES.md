# Implementation Notes

## Assessment boundary

- Course: Certificate IV in Cyber Security (`22603VIC`).
- Cluster/topic: Fundamentals of Cyber Security, Cluster 1 Topic 7.
- Units: `VU23213`, `VU23214`, `VU23217`.
- Supporting source folder:
  `cert 4 cyber security\cert iv\fundamentals of cyber`.
- Related but separate foundation: Certificate III Wireshark labs.
- Related Advanced Diploma skill: `VU23216` basic cyber security data analysis.

The TAFE Wireshark labs ask students to investigate supplied captures. This
portfolio project does not answer those questions. It implements a new
metadata-only reporting workflow using synthetic data.

## Design decisions

- CSV input keeps the Python project dependency-free.
- TShark performs packet decoding; Python performs repeatable summarization.
- IP anonymization is enabled by default.
- Payload fields are deliberately excluded.
- RFC 5737 and RFC 3849 documentation prefixes are used in output.

## Evidence to add later

Create a small isolated capture by generating known DNS and TCP traffic between
lab systems. Export only the documented metadata fields, verify the output, and
publish the summary rather than the raw capture.
