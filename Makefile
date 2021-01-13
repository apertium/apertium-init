SHELL := /bin/bash
TRAVIS_PYTHON_VERSION ?= $(shell python3 --version | cut -d ' ' -f 2)
PREFIX ?= /usr/local

all:
	cp main.py apertium-init.py
	./any-module/updateBootstraper.py
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py
	./updateBootstrapper.py

apertium_init.py: all
	cp $< $@

dist: all apertium_init.py
	./setup.py sdist

release: all apertium_init.py
	./setup.py sdist bdist_wheel
	twine upload --sign dist/*

test-release: all apertium_init.py
	./setup.py sdist bdist_wheel
	twine upload --sign --repository-url https://test.pypi.org/legacy/ dist/*

test: all
	flake8 *.py **/*.py
	mypy --strict apertium-init.py
	coverage run -m unittest --verbose --buffer
	coverage report --show-missing --fail-under 70
	if [[ "$(TRAVIS_PYTHON_VERSION)" != '3.4'* && $(TRAVIS_PYTHON_VERSION) != '3.5'*  ]]; then \
		git diff --exit-code apertium-init.py; \
	fi

install: all
	@install -d $(DESTDIR)$(PREFIX)/bin
	install -m755 apertium-init.py $(DESTDIR)$(PREFIX)/bin/apertium-init

clean:
	rm -rf dist/ build/ *.egg-info/ .mypy_cache/ apertium-init.py apertium_init.py
