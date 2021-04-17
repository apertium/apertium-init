# Apertium-Init (a.k.a. Apertium Bootstrap)

[![Build Status](https://travis-ci.org/apertium/apertium-init.svg?branch=master)](https://travis-ci.org/apertium/apertium-init)
[![Coverage Status](https://coveralls.io/repos/github/apertium/apertium-init/badge.svg?branch=master)](https://coveralls.io/github/apertium/apertium-init?branch=master)
[![PyPI](https://img.shields.io/pypi/v/apertium-init.svg)](https://pypi.org/project/apertium-init/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apertium-init.svg)](https://pypi.org/project/apertium-init/)

Bootstrap Apertium language modules and pairs using `apertium-init.py`.

## Installation

There are 3 ways to obtain Apertium-Init:

- Download the script from https://apertium.org/apertium-init to your local directory
- Clone this repository and run `make install`
- Install from [PyPi](https://pypi.org/project/apertium-init/) with `pip install apertium-init`

If the script was downloaded directly, it can be run with `python3 apertium-init.py`. Otherwise it will be installed as `apertium-init`.

## Usage

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
$ python3 apertium-init.py foo && ( cd apertium-foo/ && make )
```

### Monlingual HFST module

To bootstrap a monolingual language module `apertium-foo` using the
[HFST](http://wiki.apertium.org/wiki/HFST) formalism,

```bash
$ python3 apertium-init.py foo --analyser=hfst
```

To bootstrap and compile it at the same time,

```bash
$ python3 apertium-init.py foo --analyser=hfst && ( cd apertium-foo/ && make )
```

To include a twoc file for handling prefixes,

```bash
$ python3 apertium-init.py foo --analyser=hfst --with-twoc
```

To include a spellrelax file for handling typographical variance,

```bash
$ python3 apertium-init.py foo --analyser=hfst --with-spellrelax
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

### Bilingual module for monolinguals that don't use apertium-tagger or CG

To bootstrap a bilingual module when one or both of the monolingual modules
don't use apertium-tagger,

```bash
$ python3 apertium-init.py foo-bar --no-prob1            # Only foo doesn't have .prob
$ python3 apertium-init.py foo-bar --no-prob2            # Only bar doesn't have .prop
$ python3 apertium-init.py foo-bar --no-prob1 --no-prob2 # Neither foo nor bar have .prob
```

To bootstrap a bilingual module when one or both of the monolingual modules
don't use [CG](http://wiki.apertium.org/wiki/Constraint_Grammar),

```bash
$ python3 apertium-init.py foo-bar --no-rlx1           # Only foo doesn't have .rlx
$ python3 apertium-init.py foo-bar --no-rlx2           # Only bar doesn't have .rlx
$ python3 apertium-init.py foo-bar --no-rlx1 --no-rlx2 # Neither foo nor bar have .rlx
```

### Bilingual module using recursive transfer

To bootstrap a bilingual module which uses apertium-recursive,

```bash
$ python3 apertium-init.py foo-bar --transfer=rtx
```

### Bilingual module with anaphora resolution

To bootstrap a bilingual module which uses apertium-anaphora,

```bash
$ python3 apertium-init.py foo-bar --with-anaphora
```

### Bilingual module with discontiguous multiwords

To bootstrap a bilingual module which uses apertium-separable,

```bash
$ python3 apertium-init.py foo-bar --with-separable
```

### Adding features to an existing module

Apertium-init can reconfigure an existing module or pair. For example, to add
apertium-separable to an existing pair:

```bash
$ python3 apertium-init.py foo-bar -r --with-separable
```

Note that all desired options must be specified. If the foo-bar pair used
apertium-anaphora, the above command would remove it.

### Pushing to Github

To bootstrap a module or pair and also add it to the [apertium
incubator](https://github.com/apertium/apertium-incubator),

```bash
$ python3 apertium-init.py foo -p     # Bootstrap module apertium-foo and push to Github
$ python3 apertium-init.py foo-bar -p # Bootstrap pair apertium-foo-bar and push to Github
```

To specify what username to push as (rather than relying on `git config`),

```bash
$ python3 apertium-init.py foo -p -u bar # Bootstrap module apertium-foo and push to Github under username bar
```

## Development

After updating vanilla files, run `make` in the root of the repository to
generate `apertium-init.py`.

You can also do `sudo make install` to install to `/usr/local/bin/apertium-init`
or e.g. `PREFIX=$HOME/local make install` to install to
`$HOME/local/bin/apertium-init`.

Use `pipenv install --dev` to install the requirements required for development,
e.g. linters.

## Releasing

After installing development resources following the instructions above,
deploying to PyPi is relatively straightforward.

Use `make dist` to create a source distributable inside the `dist` directory
that can be installed locally via `pip`.

Use `make test-release` and `make release` to deploy to the [testing PyPi
instance](https://test.pypi.org/) and the [production PyPi
instance](https://pypi.org/) respectively. Either step requires PyPi
authentication credentials with access to the apertium-init package.
