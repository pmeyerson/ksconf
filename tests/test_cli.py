#!/usr/bin/env python
from __future__ import absolute_import, print_function, unicode_literals

import os
import sys

# Allow interactive execution from CLI,  cd tests; ./test_cli.py
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

from ksconf.consts import EXIT_CODE_NO_SUCH_FILE, EXIT_CODE_SUCCESS, EXIT_CODE_USER_QUIT
from tests.cli_helper import FakeStdin, TestWorkDir, ksconf_cli


class CliSimpleTestCase(unittest.TestCase):
    """ Test some very simple CLI features. """

    def test_help(self):
        out = ksconf_cli("--help")
        with ksconf_cli:
            self.assertIn("Ksconf Splunk CONFig tool", out.stdout)
            self.assertIn("usage: ", out.stdout)
            self.assertEqual(out.returncode, EXIT_CODE_SUCCESS)

    def test_conffileproxy_invalid_arg(self):
        bad_conf = """
        [dangling stanza
        attr = 1
        bad file =  very true"""
        twd = TestWorkDir()
        badfile = twd.write_file("bad_conf.conf", bad_conf)
        with ksconf_cli:

            # A command that uses ConfFileType() with mode="load"
            base_cmd = ["rest-export"]

            ko = ksconf_cli(*base_cmd + [twd.get_path("a_non_existent_file.conf")])
            self.assertIn(ko.returncode, (EXIT_CODE_USER_QUIT, EXIT_CODE_NO_SUCH_FILE))
            self.assertRegex(ko.stderr, r".*\b(can't open '[^']+\.conf'|invalid ConfFileType).*")

            ko = ksconf_cli(*base_cmd + [badfile])
            self.assertIn(ko.returncode, (EXIT_CODE_USER_QUIT, EXIT_CODE_NO_SUCH_FILE))
            self.assertRegex(ko.stderr, ".*(failed to parse|invalid ConfFileType).*")

            with FakeStdin(bad_conf):
                ko = ksconf_cli(*base_cmd + ["-"])
                self.assertIn(ko.returncode, (EXIT_CODE_USER_QUIT, EXIT_CODE_NO_SUCH_FILE))
                self.assertRegex(ko.stderr, ".*(failed to parse|invalid ConfFileType).*")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
