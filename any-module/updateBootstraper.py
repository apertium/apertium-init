#!/usr/bin/env python3

import argparse
import base64
import fileinput
import os
import re
import sys
import zlib

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
    script_path = os.path.dirname(os.path.realpath(__file__))
    init_script_path = os.path.join(script_path, os.pardir, 'apertium-init.py')

    parser = argparse.ArgumentParser(description='Update the bootstraper script for any Apertium module')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with vanilla files', default=script_path)
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default=init_script_path)
    args = parser.parse_args()

    encoded_files = {}

    for filename in files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encoded_files[filename] = base64.b85encode(zlib.compress(f.read()))

    for line in fileinput.input((args.bootstraperScript, ), inplace=True):
        sys.stdout.write(re.sub(r'^any_module_files = {.*?}  # noqa: E501$', 'any_module_files = %s  # noqa: E501' % repr(encoded_files), line))
