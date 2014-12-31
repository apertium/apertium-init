all:
	@cd "$( dirname "${BASH_SOURCE[0]}" )"
	./bilingual-module/updateBootstraper.py
	./hfst-language-module/updateBootstraper.py
	./lttoolbox-language-module/updateBootstraper.py
