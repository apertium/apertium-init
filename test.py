#!/usr/bin/env python3

import importlib
import os
import shutil
import subprocess
import unittest

apertium_init = importlib.import_module('apertium-init')


class TestModule:
    name = 'eng'

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.path)

    def test_created(self):
        os.path.exists('eng')

    def test_builds(self):
        subprocess.check_call('./autogen.sh', cwd=self.path)
        subprocess.check_call('make', cwd=self.path)


class TestLttoolboxModule(TestModule, unittest.TestCase):
    name = 'eng'

    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name])
        cls.path = '{}-{}'.format(apertium_init.default_prefix, cls.name)


class TestHfstModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '--analyser=hfst'])
        cls.path = '{}-{}'.format(apertium_init.default_prefix, cls.name)
