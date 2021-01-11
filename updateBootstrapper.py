#!/usr/bin/env python3

import argparse
import fileinput
import os
import re
import sys

if __name__ == '__main__':
    script_path = os.path.dirname(os.path.realpath(__file__))
    init_script_path = os.path.join(script_path, 'apertium-init.py')

    parser = argparse.ArgumentParser(description='Update the bootstraper script for an Apertium bilingual language modules')
    parser.add_argument('-d', '--vanillaDirectory', help='location of directory with vanilla files', default=script_path)
    parser.add_argument('-f', '--bootstraperScript', help='location of bootstraper script', default=init_script_path)
    args = parser.parse_args()

    names = {}
    codes = {}

    lang_file = os.path.join(args.vanillaDirectory, 'languages.tsv')
    for line in fileinput.input([lang_file], inplace=False):
        if '\t' in line:
            code3, code2, name = line.strip().split('\t')
            names[code3] = name
            codes[code2] = code3

    for line in fileinput.input([args.bootstraperScript], inplace=True):
        line = re.sub(r'^english_lang_names = {.*?}  # noqa: E501$', 'english_lang_names = %s  # noqa: E501' % repr(names), line)
        line = re.sub(r'^iso639_codes = {.*?}  # noqa: E501$', 'iso639_codes = %s  # noqa: E501' % repr(codes), line)
        sys.stdout.write(line)
