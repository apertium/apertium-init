#!/usr/bin/env python3

import argparse, base64, sys, re, fileinput, os, collections

files = {
    'any-bilingual-module': [
        'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.lrx',
    'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.lrx',
        'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.t1x',
    'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.t1x',
        'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.t2x',
    'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.t2x',
        'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.t3x',
    'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.t3x',
        'modes.xml',
        'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.dix',
    ],
    'hfst-bilingual-module': [
        'Makefile.am',
        'configure.ac'
    ],
    'lttoolbox-bilingual-module': [
        'Makefile.am',
        'configure.ac'
    ],
    'hfst-lttoolbox-bilingual-module': [
        'Makefile.am',
        'configure.ac'
    ],
    'lttoolbox-hfst-bilingual-module': [
        'Makefile.am',
        'configure.ac'
    ]
}

if __name__ == '__main__':
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    initScriptPath = os.path.join(scriptPath, os.pardir, 'apertium-init.py')

    parser = argparse.ArgumentParser(description='Update the bootstraper script for an Apertium bilingual module')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with vanilla files', default=scriptPath)
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default=initScriptPath)
    args = parser.parse_args()

    encodedFilesets = collections.defaultdict(dict)

    for fileset, files in files.items():
        for filename in files:
            with open(os.path.join(args.vanillaDirectory, fileset, filename), 'rb') as f:
                encodedFilesets[fileset][filename] = base64.b85encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        printed = False
        for fileset, encodedFiles in encodedFilesets.items():
            setname = fileset.replace('-', '_') + '_files'
            if line.startswith(setname):
                sys.stdout.write(re.sub(r'^%s = {.*?}$' % setname, '%s = %s' % (setname, repr(encodedFiles)), line))
                printed = True

        if not printed:
            sys.stdout.write(line)

