#!/usr/bin/env python3

import importlib
import os
import shutil
import subprocess
import unittest

apertium_init = importlib.import_module('apertium-init')


def make_path(name, prefix=apertium_init.default_prefix):
    return '{}-{}'.format(prefix, name)


def build(path, autogen_args=[]):
    try:
        subprocess.check_output(['./autogen.sh'] + autogen_args, cwd=path, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as error:
        print(error.output)
        raise

    try:
        subprocess.check_output('make', cwd=path, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as error:
        print(error.output)
        raise


class TestModule:
    name = 'eng'
    path = make_path(name)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.path)

    def test_created(self):
        os.path.exists('eng')

    def test_builds(self):
        build(self.path)


class TestInvalidModule(unittest.TestCase):
    name = 'eng-cat-spa'

    def test_init(self):
        with self.assertRaises(SystemExit):
            apertium_init.main([self.name])


class TestLttoolboxModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name])


class TestHfstModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '--analyser=hfst'])


class TestTwocModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '--analyser=hfst', '--with-twoc'])


class TestLttoolboxPair(TestModule, unittest.TestCase):
    name = 'eng-cat'
    path = make_path(name)

    name1 = 'eng'
    path1 = make_path(name1)

    name2 = 'cat'
    path2 = make_path(name2)

    @classmethod
    def setUpClass(cls):
        for name, path in [(cls.name1, cls.path1), (cls.name2, cls.path2)]:
            apertium_init.main([name])
            build(path)
        apertium_init.main([cls.name])

    @classmethod
    def tearDownClass(cls):
        for path in [cls.path, cls.path1, cls.path2]:
            shutil.rmtree(path)

    def test_builds(self):
        autogen_args = ['--with-lang1=../{}'.format(self.path1), '--with-lang2=../{}'.format(self.path2)]
        build(self.path, autogen_args=autogen_args)


if __name__ == '__main__':
    unittest.main(buffer=True, verbosity=2)
