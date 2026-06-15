import unittest

from vpn_audit import audit_config


class VpnAuditTests(unittest.TestCase):
    def test_flags_weak_algorithms_and_missing_pfs(self):
        config = """
crypto isakmp policy 10
 encr 3des
 hash md5
 group 2
crypto isakmp key <REDACTED> address 192.0.2.2
crypto ipsec transform-set LEGACY esp-3des esp-md5-hmac
crypto map LAB 10 ipsec-isakmp
 match address VPN-TRAFFIC
"""
        rules = {finding.rule for finding in audit_config(config)}
        self.assertIn("IKE_ENCRYPTION", rules)
        self.assertIn("IKE_HASH", rules)
        self.assertIn("IKE_DH_GROUP", rules)
        self.assertIn("IPSEC_TRANSFORM", rules)
        self.assertIn("MISSING_PFS", rules)
        self.assertNotIn("EXPOSED_PSK", rules)

    def test_accepts_redacted_modern_example(self):
        config = """
crypto ikev2 proposal LAB-PROPOSAL
 encryption aes-cbc-256
 integrity sha256
 group 14
crypto ipsec transform-set LAB-SET esp-aes 256 esp-sha256-hmac
crypto map LAB 10 ipsec-isakmp
 set pfs group14
 match address VPN-TRAFFIC
! verification: show crypto ikev2 sa
! verification: show crypto ipsec sa
"""
        self.assertEqual(audit_config(config), [])

    def test_flags_unredacted_pre_shared_key(self):
        config = """
crypto isakmp key UnsafeExample address 192.0.2.2
crypto map LAB 10 ipsec-isakmp
 set pfs group14
 match address VPN-TRAFFIC
"""
        rules = {finding.rule for finding in audit_config(config)}
        self.assertIn("EXPOSED_PSK", rules)


if __name__ == "__main__":
    unittest.main()
