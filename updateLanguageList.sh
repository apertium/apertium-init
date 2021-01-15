#!/bin/bash

mv languages.tsv languages.tsv.bak
wget -O - https://iso639-3.sil.org/sites/iso639-3/files/downloads/iso-639-3.tab | cut -f "1,4,7" | tail -n +2 > languages.tsv
