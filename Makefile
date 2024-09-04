SHELL := /bin/bash
PREFIX ?= /usr/local

all:
	cp main.py apertium-init.py
	./any-module/updateBootstraper.py
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py
	./updateBootstrapper.py

apertium_init.py: apertium-init.py all
	cp $< $@

dist: all apertium_init.py
	./setup.py sdist

release: all apertium_init.py
	./setup.py sdist bdist_wheel
	twine upload --sign dist/*

test-release: all apertium_init.py
	./setup.py sdist bdist_wheel
	twine upload --sign --repository-url https://test.pypi.org/legacy/ dist/*

lint: all
	flake8 *.py **/*.py
	mypy --strict apertium-init.py

unit-test: all
	python3 -m unittest --verbose

coverage:
	coverage run -m unittest --verbose --buffer
	coverage report --show-missing

test: lint unit-test coverage

install: all
	@install -d $(DESTDIR)$(PREFIX)/bin
	install -m755 apertium-init.py $(DESTDIR)$(PREFIX)/bin/apertium-init

clean:
	rm -rf dist/ build/ *.egg-info/ .mypy_cache/ apertium-init.py apertium_init.py
