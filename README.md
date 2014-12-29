# Apertium Bootstrap

Bootstrap Apertium language modules and pairs using `apertium-init.py`.

## Usage

First, <a href="https://raw.githubusercontent.com/apertium/bootstrap/master/apertium-init.py" download>download the script</a>. Usage depends on the desired module and is described below. Remember to search for `TODO` in the generated module to add example sentences, etc.

### Monlingual Lttoolbox module

To bootstrap a monolingual language module `apertium-foo` using the [lttoolbox](http://wiki.apertium.org/wiki/Lttoolbox) formalism,

    python3 apertium-init.py foo

### Monlingual HFST module

To bootstrap a monolingual language module `apertium-foo` using the [HFST](http://wiki.apertium.org/wiki/HFST) formalism,

    python3 apertium-init.py foo --analyser=hfst

### Bilingual Lttoolbox module

To bootstrap a bilingual language module `apertium-foo-bar` using the [lttoolbox](http://wiki.apertium.org/wiki/Lttoolbox) formalism,

    python3 apertium-init.py foo-bar

### Bilingual HFST/Lttoolbox module

To bootstrap a bilingual language module `apertium-foo-bar` using the [HFST](http://wiki.apertium.org/wiki/Lttoolbox) formalism and/or the [lttoolbox](http://wiki.apertium.org/wiki/Lttoolbox) formalism,

    python3 apertium-init.py foo-bar --analysers=hfst # Both foo and bar will use HFST
    python3 apertium-init.py foo-bar --analyser1=hfst # Only foo (first language) will use HFST
    python3 apertium-init.py foo-bar --analyser2=hfst # Only bar (second language) will use HFST
    
## Development

After updating vanilla files, run `./updateBootstraper.py` to update the encoded files in `apertium-init.py`.
