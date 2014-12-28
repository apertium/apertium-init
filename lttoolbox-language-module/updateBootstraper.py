#!/usr/bin/env python3

import argparse, base64, sys, re, fileinput, os

files = [
    '{{languageCode}}.prob',
    'apertium-{{languageCode}}.{{languageCode}}.acx',
    'apertium-{{languageCode}}.{{languageCode}}.dix',
    'apertium-{{languageCode}}.{{languageCode}}.rlx',
    'apertium-{{languageCode}}.pc.in',
    'AUTHORS',
    'autogen.sh',
    'configure.ac',
    'COPYING',
    'Makefile.am',
    'modes.xml',
    'README'
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update the bootstraper script for an Apertium lttoolbox-based language module')
    parser.add_argument('-d', '--vanillaDirectory', help='Location of directory with vanilla files', default=os.getcwd())
    parser.add_argument('-f', '--bootstraperScript', help='Location of bootstraper script', default='../apertium-init.py')
    args = parser.parse_args()

    encodedFiles = {}

    for filename in files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encodedFiles[filename] = base64.b64encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        sys.stdout.write(re.sub(r'^lttoolbox_language_module_files = {.*?}$', 'lttoolbox_language_module_files = %s' % repr(encodedFiles), line))
