#!/usr/bin/env python3

import argparse
import base64
import fileinput
import os
import re
import sys

files = [
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
    'Makefile.am',
    'README',
    'configure.ac',
]

if __name__ == '__main__':
    script_path = os.path.dirname(os.path.realpath(__file__))
    init_script_path = os.path.join(script_path, os.pardir, 'apertium-init.py')

    parser = argparse.ArgumentParser(description='Update the bootstraper script for an Apertium bilingual language modules')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with vanilla files', default=script_path)
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default=init_script_path)
    args = parser.parse_args()

    encoded_files = {}

    for filename in files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encoded_files[filename] = base64.b85encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        sys.stdout.write(re.sub(r'^bilingual_module_files = {.*?}  # noqa: E501$', 'bilingual_module_files = %s  # noqa: E501' % repr(encoded_files), line))
