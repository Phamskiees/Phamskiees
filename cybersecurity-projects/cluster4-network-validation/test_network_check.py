import ipaddress
import json
import tempfile
import unittest
from pathlib import Path

import network_check


class NetworkCheckTests(unittest.TestCase):
    def write_config(self, data):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "services.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_rejects_target_outside_allowlist(self):
        path = self.write_config(
            {
                "allowed_networks": ["198.18.0.0/24"],
                "services": [{"name": "bad target", "host": "198.19.0.1", "port": 80}],
            }
        )
        with self.assertRaises(network_check.ConfigError):
            network_check.load_config(path)

    def test_accepts_valid_service(self):
        path = self.write_config(
            {
                "allowed_networks": ["198.18.0.0/24"],
                "services": [{"name": "SSH", "host": "198.18.0.10", "port": 22}],
            }
        )
        networks, services = network_check.load_config(path)
        self.assertEqual(networks, [ipaddress.ip_network("198.18.0.0/24")])
        self.assertEqual(services[0]["port"], 22)

    def test_documentation_target_is_skipped(self):
        status, detail = network_check.check_service("192.0.2.10", 443, 0.01)
        self.assertEqual(status, "SKIP")
        self.assertIn("documentation", detail)

    def test_writes_structured_outputs(self):
        report = {
            "checked_at": "2026-06-09T00:00:00+10:00",
            "timeout_seconds": 1,
            "summary": {"pass": 0, "fail": 0, "skip": 1},
            "results": [
                {
                    "name": "example",
                    "host": "192.0.2.1",
                    "port": 443,
                    "status": "SKIP",
                    "detail": "documentation-only address",
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            json_path = Path(directory) / "result.json"
            csv_path = Path(directory) / "result.csv"
            network_check.write_json(json_path, report)
            network_check.write_csv(csv_path, report)
            self.assertEqual(json.loads(json_path.read_text())["summary"]["skip"], 1)
            self.assertIn("documentation-only address", csv_path.read_text())


if __name__ == "__main__":
    unittest.main()
