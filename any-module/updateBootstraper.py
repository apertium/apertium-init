#!/usr/bin/env python3

import argparse
import base64
import fileinput
import os
import re
import sys

files = [
    '.gitattributes',
    '.gitignore',
    'AUTHORS',
    'autogen.sh',
    'COPYING',
    'NEWS',
    'ChangeLog',
]

if __name__ == '__main__':
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    initScriptPath = os.path.join(scriptPath, os.pardir, 'apertium-init.py')

    parser = argparse.ArgumentParser(description='Update the bootstraper script for any Apertium module')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with vanilla files', default=scriptPath)
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default=initScriptPath)
    args = parser.parse_args()

    encodedFiles = {}

    for filename in files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encodedFiles[filename] = base64.b85encode(f.read())

    for line in fileinput.input((args.bootstraperScript, ), inplace=True):
        sys.stdout.write(re.sub(r'^any_module_files = {.*?}  # noqa: E501$', 'any_module_files = %s  # noqa: E501' % repr(encodedFiles), line))
