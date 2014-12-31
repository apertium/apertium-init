#! /bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )"
./hfst-bilingual-module/updateBootstraper.py
./lttoolbox-bilingual-module/updateBootstraper.py
./hfst-lttoolbox-bilingual-module/updateBootstraper.py

