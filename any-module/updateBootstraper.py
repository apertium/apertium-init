#!/usr/bin/env python3

import argparse, base64, sys, re, fileinput, os

files = [
    'AUTHORS',
    'autogen.sh',
    'COPYING',
    'NEWS',
    'ChangeLog'
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update the bootstraper script for any Apertium module')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with vanilla files', default=os.getcwd())
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default='../apertium-init.py')
    args = parser.parse_args()

    encodedFiles = {}

    for filename in files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encodedFiles[filename] = base64.b85encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        sys.stdout.write(re.sub(r'^any_module_files = {.*?}$', 'any_module_files = %s' % repr(encodedFiles), line))

