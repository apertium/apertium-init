###############################################################################
## Makefile for apertium-{{languageCode}}
###############################################################################

LANG1={{languageCode}}
BASENAME=apertium-$(LANG1)

TARGETS_COMMON =			\
	$(LANG1).automorf.bin		\
	$(LANG1).automorf.att.gz	\
	$(LANG1).autogen.bin		\
	$(LANG1).autogen.att.gz		\
	$(LANG1).autopgen.bin		\
	$(LANG1).rlx.bin

if ENABLE_SPELLER
TARGETS_COMMON += $(LANG1).zhfst
endif

# This include defines goals for install-modes, .deps/.d, autobil.prefixes and .mode files:
@ap_include@

if ENABLE_LINTER
TARGETS_COMMON += lint
endif

.PHONY: lint

lint:
	apertium-lint

###############################################################################
## {{languageName}} transducer
###############################################################################

$(LANG1).autogen.bin: $(BASENAME).$(LANG1).dix .deps/.d
	apertium-validate-dictionary $<
	lt-comp rl $< $@

$(LANG1).automorf.bin: $(BASENAME).$(LANG1).dix
	apertium-validate-dictionary $<
	lt-comp lr $< $@ $(srcdir)/$(BASENAME).$(LANG1).acx

$(LANG1).autogen.att.gz: $(LANG1).autogen.bin
	lt-print $< | gzip -9 -c -n > $@

$(LANG1).automorf.att.gz: $(LANG1).automorf.bin
	lt-print $< | gzip -9 -c -n > $@

$(LANG1).autopgen.bin: $(BASENAME).post-$(LANG1).dix
	lt-comp lr $< $@

###############################################################################
## Disambiguation rules
###############################################################################

$(LANG1).rlx.bin: $(BASENAME).$(LANG1).rlx
	cg-comp $< $@

###############################################################################
## Spell checker
###############################################################################

$(LANG1).zhfst: .deps/acceptor.default.hfst .deps/errmodel.default.hfst speller/index.xml
	rm -f $@
	zip -j $@ $^

.deps/editdist.default.att: speller/editdist.default.txt .deps/acceptor.default.hfst
	apertium-editdist -v -s -d 1 -e '@0@' -i $(srcdir)/speller/editdist.default.txt -a .deps/acceptor.default.hfst > $@

.deps/editdist.default.hfst: .deps/editdist.default.att
	hfst-txt2fst -e '@0@' $< -o $@

.deps/editstrings.default.hfst: .deps/strings.default.hfst .deps/editdist.default.hfst
	hfst-disjunct $^ | hfst-minimise | hfst-repeat -f 1 -t 2 -o $@

.deps/errmodel.default.hfst: .deps/words.default.hfst .deps/editstrings.default.hfst
	hfst-disjunct $^ | hfst-fst2fst -f olw -o $@

.deps/words.default.hfst: speller/words.default.txt
	grep -v -e "^#" -e "^$$" $< | hfst-strings2fst  -j -o $@

.deps/strings.default.hfst: speller/strings.default.txt .deps/anystar.hfst
	grep -v -e "^#" -e "^$$" $< | hfst-strings2fst  -j | hfst-concatenate .deps/anystar.hfst - |\
	hfst-concatenate - .deps/anystar.hfst -o $@

.deps/anystar.hfst:
	echo "?*;" | hfst-regexp2fst -S -o $@

.deps/acceptor.default.hfst: $(LANG1).autogen.bin
	lt-print -H $< | hfst-txt2fst | hfst-fst2fst -t | hfst-project --project=lower | hfst-minimise | hfst-fst2fst  -f olw -o $@

###############################################################################
## Unigram tagger
###############################################################################

#$(LANG1).prob: corpus/$(LANG1).tagged
#	apertium-tagger -s 0 -u 2 $@ $<

###############################################################################
## Distribution
###############################################################################
EXTRA_DIST=$(BASENAME).$(LANG1).dix		\
		$(BASENAME).$(LANG1).acx	\
		$(BASENAME).$(LANG1).rlx	\
		$(BASENAME).post-$(LANG1).dix	\
		$(LANG1).prob			\
		modes.xml

###############################################################################
## Installation stuff
###############################################################################
#
#   apertium_{{languageCode}}_dir: This is where the compiled binaries go
#   apertium_{{languageCode}}_srcdir: This is where the source files go

apertium_{{languageCode}}dir=$(prefix)/share/apertium/$(BASENAME)/
apertium_{{languageCode}}_srcdir=$(prefix)/share/apertium/$(BASENAME)/

apertium_{{languageCode}}_DATA=$(TARGETS_COMMON) \
	$(LANG1).prob \
	$(BASENAME).$(LANG1).dix \
	$(BASENAME).$(LANG1).rlx \
	$(BASENAME).post-$(LANG1).dix

pkgconfigdir = $(prefix)/share/pkgconfig
pkgconfig_DATA = $(BASENAME).pc

noinst_DATA=modes/$(LANG1)-morph.mode

install-data-local: install-modes
uninstall-local: uninstall-modes

CLEANFILES = $(TARGETS_COMMON)
clean-local:
	-rm -rf .deps modes

###############################################################################
## Test
###############################################################################

test: all
	apertium-regtest test
