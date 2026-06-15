import unittest

from packet_summary import anonymize_ip, summarize


class PacketSummaryTests(unittest.TestCase):
    def test_anonymizes_ipv4_and_ipv6(self):
        self.assertEqual(anonymize_ip("10.10.10.25"), "192.0.2.25")
        self.assertEqual(anonymize_ip("2001:db8:abcd::7"), "2001:db8::7")

    def test_summarizes_protocols_and_indicators(self):
        rows = [
            {
                "frame.number": "1",
                "frame.time_epoch": "100.0",
                "ip.src": "10.0.0.10",
                "ip.dst": "10.0.0.20",
                "_ws.col.Protocol": "TCP",
                "frame.len": "60",
                "tcp.flags.syn": "1",
                "tcp.flags.ack": "0",
                "tcp.analysis.retransmission": "",
                "dns.qry.name": "",
            },
            {
                "frame.number": "2",
                "frame.time_epoch": "101.5",
                "ip.src": "10.0.0.20",
                "ip.dst": "10.0.0.10",
                "_ws.col.Protocol": "DNS",
                "frame.len": "90",
                "tcp.flags.syn": "",
                "tcp.flags.ack": "",
                "tcp.analysis.retransmission": "1",
                "dns.qry.name": "example.test",
            },
        ]
        result = summarize(rows)
        self.assertEqual(result["packet_count"], 2)
        self.assertEqual(result["total_bytes"], 150)
        self.assertEqual(result["capture_duration_seconds"], 1.5)
        self.assertEqual(result["protocols"], {"TCP": 1, "DNS": 1})
        self.assertEqual(result["indicators"]["tcp_syn_without_ack"], 1)
        self.assertEqual(result["indicators"]["tcp_retransmissions"], 1)
        self.assertTrue(result["privacy"]["ip_addresses_anonymized"])


if __name__ == "__main__":
    unittest.main()
