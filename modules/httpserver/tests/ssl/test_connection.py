import basetest
import subprocess
import unittest

@unittest.skipUnless(basetest.Basetest._client.is_ssl(), "applies only when using SSL")
class test_connection(basetest.Basetest):
    def setUp(self):
        self.some_valid_url = self.get_url('/os/version')

    def test_client_connection_is_accepted_when_cert_and_key_is_passed(self):
        subprocess.check_call(['curl',
            '--cert', self.get_client_cert_path(),
            '--key', self.get_client_key_path(),
            '--cacert', self.get_ca_cert_path(),
            self.some_valid_url])

    def test_client_connection_is_rejected_when_no_client_certificate_is_passed(self):
        try:
            subprocess.check_call(['curl',
                '--cacert', self.get_ca_cert_path(), self.some_valid_url])
        except:
            pass # expected
        else:
            raise Exception('The command should fail!')
