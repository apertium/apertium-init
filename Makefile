all:
	./any-module/updateBootstraper.py
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py

test:
	flake8 *.py **/*.py

PREFIX ?= /usr/local
install:
	@install -d $(DESTDIR)$(PREFIX)/bin
	install -m755 apertium-init.py $(DESTDIR)$(PREFIX)/bin/apertium-init
