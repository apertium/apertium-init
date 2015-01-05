all:
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py


PREFIX ?= /usr/local
install:
	@install -d $(DESTDIR)$(PREFIX)/bin
	install -m755 apertium-init.py $(DESTDIR)$(PREFIX)/bin/apertium-init
