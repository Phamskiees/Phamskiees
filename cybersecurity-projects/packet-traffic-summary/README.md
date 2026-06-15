# Packet Traffic Summary

Python CLI that converts a sanitized TShark CSV field export into a compact
JSON and Markdown traffic summary. It counts protocols, endpoints, DNS queries,
bytes, TCP retransmissions, and SYN packets while anonymizing IP addresses by
default.

## Portfolio purpose

This is an original extension of:

- Certificate III Wireshark and Ethernet-frame labs.
- Certificate IV Cluster 1, Topic 7 Wireshark practice.
- Certificate IV units `VU23213`, `VU23214`, and `VU23217`.
- Advanced Diploma `VU23216` data-analysis concepts.

It does not contain answers from the supplied PCAP exercises and does not
redistribute TAFE captures.

## Run the sample

```powershell
python packet_summary.py sample-data/tshark-fields-synthetic.csv `
  --json evidence/summary.json `
  --markdown evidence/summary.md
python -m unittest -v
```

## Export fields from an authorized capture

Use only captures you own or are authorized to analyze:

```text
tshark -r lab-capture.pcapng -T fields -E header=y -E separator=, -E quote=d \
  -e frame.number -e frame.time_epoch -e ip.src -e ip.dst \
  -e _ws.col.Protocol -e frame.len -e tcp.flags.syn -e tcp.flags.ack \
  -e tcp.analysis.retransmission -e dns.qry.name > tshark-fields.csv
```

Review and sanitize the CSV before publishing. Do not publish packet payloads,
credentials, tokens, private hostnames, or identifying addresses.
