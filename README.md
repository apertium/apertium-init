# Apertium-Init (a.k.a. Apertium Bootstrap)

[![Build Status](https://travis-ci.org/apertium/apertium-init.svg)](https://travis-ci.org/apertium/apertium-init)
[![Coverage Status](https://coveralls.io/repos/github/apertium/apertium-init/badge.svg?branch=master)](https://coveralls.io/github/apertium/apertium-init?branch=master)
[![PyPI](https://img.shields.io/pypi/v/apertium-init.svg)](https://pypi.org/project/apertium-init/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apertium-init.svg)](https://pypi.org/project/apertium-init/)

Bootstrap Apertium language modules and pairs using `apertium-init.py`.

## Usage

First, <a href="https://raw.githubusercontent.com/apertium/bootstrap/master/apertium-init.py" download>download the script</a>
or install from [PyPi](https://pypi.org/project/apertium-init/) with `pip install apertium-init`.

Usage depends on the desired module and is described below. Remember to
search for `TODO` in the generated module to add example sentences, etc.

### Monolingual Lttoolbox module

To bootstrap a monolingual language module `apertium-foo` using the
[lttoolbox](http://wiki.apertium.org/wiki/Lttoolbox) formalism,

```bash
$ python3 apertium-init.py foo
```

To bootstrap and compile it at the same time,

```bash
$ python3 apertium-init.py foo && ( cd apertium-foo/ && ./autogen.sh && make )
```

### Monlingual HFST module

To bootstrap a monolingual language module `apertium-foo` using the
[HFST](http://wiki.apertium.org/wiki/HFST) formalism,

```bash
$ python3 apertium-init.py foo --analyser=hfst
```

To bootstrap and compile it at the same time,

```bash
$ python3 apertium-init.py foo --analyser=hfst && ( cd apertium-foo/ && ./autogen.sh && make )
```

### Bilingual Lttoolbox module

To bootstrap a bilingual language module `apertium-foo-bar` where the
monolingual packages `apertium-foo` and `apertium-bar` both use the
[lttoolbox](http://wiki.apertium.org/wiki/Lttoolbox) formalism,

```bash
$ python3 apertium-init.py foo-bar
```

To bootstrap and compile it at the same time,

```bash
$ python3 apertium-init.py foo-bar && ( cd apertium-foo-bar/ && ./autogen.sh && make test)
```

### Bilingual HFST/Lttoolbox module

To bootstrap a bilingual language module `apertium-foo-bar` where the
monolingual packages `apertium-foo` and `apertium-bar` use the
[HFST](http://wiki.apertium.org/wiki/Lttoolbox) formalism and/or the
[lttoolbox](http://wiki.apertium.org/wiki/Lttoolbox) formalism,

```bash
$ python3 apertium-init.py foo-bar --analysers=hfst # Both foo and bar use HFST
$ python3 apertium-init.py foo-bar --analyser1=hfst # Only foo (first language) uses HFST
$ python3 apertium-init.py foo-bar --analyser2=hfst # Only bar (second language) uses HFST
```

To bootstrap and compile it at the same time,

```bash
$ python3 apertium-init.py foo-bar --analysers=hfst && ( cd apertium-foo-bar/ && ./autogen.sh && make test) # Both foo and bar use HFST
$ python3 apertium-init.py foo-bar --analyser1=hfst && ( cd apertium-foo-bar/ && ./autogen.sh && make test) # Only foo (first language) uses HFST
$ python3 apertium-init.py foo-bar --analyser2=hfst && ( cd apertium-foo-bar/ && ./autogen.sh && make test) # Only bar (second language) uses HFST
```

## Development

After updating vanilla files, run `./updateBootstraper.py` to update the
relevant encoded files in `apertium-init.py`. Or, run `make` in the root
of the repository to update all the encoded files.

You can also do `sudo make install` to install to `/usr/local/bin/apertium-init`
or e.g. `PREFIX=$HOME/local make install` to install to `$HOME/local/bin/apertium-init`.

Use `pipenv install --dev` to install the requirements required for
development, e.g. linters.

## Releasing

After installing development resources following the instructions above,
deploying to PyPi is relatively straightforward.

Use `make dist` to create a source distributable inside the `dist` directory
that can be installed locally via `pip`.

Use `make test-release` and `make release` to deploy to the [testing PyPi instance](https://test.pypi.org/)
and the [production PyPi instance](https://pypi.org/) respectively. Either
step requires PyPi authentication credentials with access to the apertium-init
package.
