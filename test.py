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
    def test_rejects_invalid_name(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng-cat-spa'])

    def test_rejects_twoc_without_hfst(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--with-twoc'])

    def test_no_rlx_and_no_prob(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--no-rlx1', '--no-prob1'])

    def test_invalid_analyser(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--analyser=bloop'])

    def test_dir_already_exists(self):
        path = make_path('eng')
        os.makedirs(path)
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng'])
        shutil.rmtree(path)


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


class TestUnknownCodeModule(TestModule, unittest.TestCase):
    name = 'bkl'
    path = make_path(name)

    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name])


class TestPair(TestModule, unittest.TestCase):
    name = 'eng-cat'
    path = make_path(name)

    name1 = 'eng'
    path1 = make_path(name1)
    analyser1 = ''

    name2 = 'cat'
    path2 = make_path(name2)
    analyser2 = ''

    @classmethod
    def setUpClass(cls):
        for name, path, analyser in [(cls.name1, cls.path1, cls.analyser1), (cls.name2, cls.path2, cls.analyser2)]:
            if analyser:
                apertium_init.main([name, '--analyser={}'.format(analyser)])
            else:
                apertium_init.main([name])
            build(path)
        pair_args = [cls.name]
        if cls.analyser1:
            pair_args.append('--analyser1={}'.format(cls.analyser1))
        if cls.analyser2:
            pair_args.append('--analyser2={}'.format(cls.analyser2))
        apertium_init.main(pair_args)

    @classmethod
    def tearDownClass(cls):
        for path in [cls.path, cls.path1, cls.path2]:
            shutil.rmtree(path)

    def test_builds(self):
        autogen_args = ['--with-lang1=../{}'.format(self.path1), '--with-lang2=../{}'.format(self.path2)]
        build(self.path, autogen_args=autogen_args)


class TestUnspecifiedPair(TestPair, unittest.TestCase):
    pass


class TestLttoolboxPair(TestPair, unittest.TestCase):
    analyser1 = 'lt'
    analyser2 = 'lttoolbox'


class TestHfstPair(TestPair, unittest.TestCase):
    analyser1 = 'hfst'
    analyser2 = 'hfst'


class TestHfstLtPair(TestPair, unittest.TestCase):
    analyser1 = 'hfst'
    analyser2 = 'lttoolbox'


class TestLtHfstPair(TestPair, unittest.TestCase):
    analyser1 = 'lt'
    analyser2 = 'hfst'


if __name__ == '__main__':
    unittest.main(buffer=True, verbosity=2)
