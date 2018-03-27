PREFIX ?= /usr/local

all:
	./any-module/updateBootstraper.py
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py

apertium_init.py: apertium-init.py
	cp $< $@

dist: all apertium_init.py
	python3 setup.py sdist

release: all apertium_init.py
	python3 setup.py sdist bdist_wheel upload --sign

test-release: all apertium_init.py
	python3 setup.py sdist bdist_wheel upload --repository https://test.pypi.org/legacy/ --sign

test: apertium_init.py
	flake8 *.py **/*.py
	mypy --strict *.py
	git diff --exit-code apertium-init.py

install:
	@install -d $(DESTDIR)$(PREFIX)/bin
	install -m755 apertium-init.py $(DESTDIR)$(PREFIX)/bin/apertium-init

clean:
	rm -rf dist/ build/ *.egg-info/ .mypy_cache/ apertium_init.py
