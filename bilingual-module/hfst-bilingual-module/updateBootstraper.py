#!/usr/bin/env python3

import argparse, base64, sys, re, fileinput, os

common_files = [
    'AUTHORS',
    'autogen.sh',
    'COPYING',
    'NEWS',
    'ChangeLog'
]

files = [
    'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.lrx',
    'apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.lrx'
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update the bootstraper script for an Apertium HFST-based bilingual language module')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with common vanilla files', default='../')
    parser.add_argument('-s', '--specificVanillaDirectory', help='location of directory with specific vanilla files', default=os.getcwd())
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default='../../apertium-init.py')
    args = parser.parse_args()

    encodedFiles = {}

    for filename in common_files:
        with open(os.path.join(args.vanillaDirectory, filename), 'rb') as f:
            encodedFiles[filename] = base64.b85encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        sys.stdout.write(re.sub(r'^bilingual_module_files = {.*?}$', 'bilingual_module_files = %s' % repr(encodedFiles), line))

    encodedFiles = {}

    for filename in files:
        with open(os.path.join(args.specificVanillaDirectory, filename), 'rb') as f:
            encodedFiles[filename] = base64.b85encode(f.read())

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        sys.stdout.write(re.sub(r'^hfst_bilingual_module_files = {.*?}$', 'hfst_bilingual_module_files = %s' % repr(encodedFiles), line))

