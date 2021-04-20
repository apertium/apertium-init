#!/usr/bin/env python3

import importlib
import os
import shutil
import subprocess
import unittest

apertium_init = importlib.import_module('apertium-init')


def make_path(name, prefix=apertium_init.default_prefix):
    return '{}-{}'.format(prefix, name)


def autogen(path, autogen_args):
    try:
        subprocess.check_output(['./autogen.sh'] + autogen_args, cwd=path, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as error:
        print(error.output)
        raise


def build(path):
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

    def test_rejects_spellrelax_without_hfst(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--with-spellrelax'])

    def test_no_rlx_and_no_prob(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng-cat', '--no-rlx1', '--no-prob1'])

    def test_invalid_analyser(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--analyser=bloop'])

    def test_lexd_twoc(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--analyser=lexd', '--with-twoc'])

    def test_lang_with_pair_options(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--with-anaphora'])

    def test_pair_with_lang_options(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng-cat', '--with-spellrelax'])

    def test_no_mono_giella(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--analyser=giella'])

    def test_rebuild_nonexistent(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng', '--rebuild'])

    def test_dir_already_exists(self):
        path = make_path('eng')
        os.makedirs(path)
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng'])
        shutil.rmtree(path)


class TestInvalidPair(unittest.TestCase):
    def test_no_giella_with_tagger_args_left(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng-spa', '--analyser1=giella', '--no-prob1'])

    def test_no_giella_with_tagger_args_right(self):
        with self.assertRaises(SystemExit):
            apertium_init.main(['eng-spa', '--analyser2=giella', '--no-rlx2'])


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


class TestSpellrelaxModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '--analyser=hfst', '--with-spellrelax'])


class TestTwocAndSpellrelaxModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '--analyser=hfst', '--with-twoc', '--with-spellrelax'])


class TestLexdModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '--analyser=lexd'])


class TestUnknownCodeModule(TestModule, unittest.TestCase):
    name = 'qaa'
    path = make_path(name)

    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name])


class TestRebuildModule(TestModule, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        apertium_init.main([cls.name, '-a=hfst'])
        apertium_init.main([cls.name, '-a=hfst', '-r', '--with-twoc'])


class TestPair(TestModule, unittest.TestCase):
    name = 'eng-cat'
    path = make_path(name)

    name1 = 'eng'
    path1 = make_path(name1)
    analyser1 = ''

    name2 = 'cat'
    path2 = make_path(name2)
    analyser2 = ''

    other_args = []

    @classmethod
    def setUpClass(cls):
        for name, path, analyser in [(cls.name1, cls.path1, cls.analyser1), (cls.name2, cls.path2, cls.analyser2)]:
            if analyser:
                apertium_init.main([name, '--analyser={}'.format(analyser)])
            else:
                apertium_init.main([name])
            build(path)
        pair_args = [cls.name] + cls.other_args
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
        autogen(self.path, autogen_args)
        build(self.path)


class TestDefaultPair(TestPair, unittest.TestCase):
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


class TestPairWithSeparable(TestPair, unittest.TestCase):
    other_args = ['--with-lsx']


class TestPairWithAnaphora(TestPair, unittest.TestCase):
    other_args = ['--with-anaphora']


class TestPairWithChunking(TestPair, unittest.TestCase):
    other_args = ['--transfer=chunk']


class TestPairWithRecursive(TestPair, unittest.TestCase):
    other_args = ['--transfer=rtx']


class TestRebuildPair(TestPair, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestPair.setUpClass()
        apertium_init.main([cls.name, '-r', '--with-anaphora'])


if __name__ == '__main__':
    unittest.main(buffer=True, verbosity=2)
