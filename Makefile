all:
	./any-module/updateBootstraper.py
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py

dist:
	python3 setup.py sdist

release:
	python3 setup.py sdist bdist_wheel upload --sign

test-release:
	python3 setup.py sdist bdist_wheel upload --repository https://test.pypi.org/legacy/ --sign

test:
	flake8 *.py **/*.py
	mypy --strict *.py

PREFIX ?= /usr/local
install:
	@install -d $(DESTDIR)$(PREFIX)/bin
	install -m755 apertium-init.py $(DESTDIR)$(PREFIX)/bin/apertium-init

clean:
	rm -rf dist/ build/ *.egg-info/
