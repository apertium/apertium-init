#!/usr/bin/env python3

import argparse, base64, sys, re, fileinput, os

files = [
    'apertium-{{languageCode}}.{{languageCode}}.lexc',
    'apertium-{{languageCode}}.{{languageCode}}.twol',
    'apertium-{{languageCode}}.{{languageCode}}.rlx',
    'apertium-{{languageCode}}.pc.in',
    'AUTHORS',
    'autogen.sh',
    'configure.ac',
    'COPYING',
    'Makefile.am',
    'modes.xml',
    'README',
    'NEWS',
    'ChangeLog'
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update the bootstraper script for an Apertium lttoolbox-based language module')
    parser.add_argument('-d', '--vanillaDirectory', help='Location of directory with vanilla files', default=os.getcwd())
    parser.add_argument('-f', '--bootstraperScript', help='Location of bootstraper script', default='../apertium-init.py')
    args = parser.parse_args()

    encodedFiles = {}

    for filename in files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encodedFiles[filename] = base64.b85encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        sys.stdout.write(re.sub(r'^hfst_language_module_files = {.*?}$', 'hfst_language_module_files = %s' % repr(encodedFiles), line))
