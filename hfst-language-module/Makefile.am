###############################################################################
## Makefile for apertium-{{languageCode}}
###############################################################################

LANG1={{languageCode}}
BASENAME=apertium-$(LANG1)

TARGETS_COMMON =			\
	$(LANG1).automorf.hfst		\
	$(LANG1).automorf.bin		\
	$(LANG1).automorf.att.gz	\
	$(LANG1).autogen.hfst		\
	$(LANG1).autogen.bin		\
	$(LANG1).autogen.att.gz		\
	$(LANG1).autopgen.bin		\
	$(LANG1).rlx.bin

if ENABLE_SPELLER
TARGETS_COMMON += $(LANG1).zhfst
endif

# This include defines goals for install-modes, .deps/.d, autobil.prefixes and .mode files:
@ap_include@

{{ifnot_lexd
LEXCFLAGS=-v --Werror
ifnot_lexd}}

###############################################################################
## {{languageName}} transducer
###############################################################################

.deps/$(LANG1).twol.hfst: $(BASENAME).$(LANG1).twol .deps/.d
	hfst-twolc $< -o $@
{{if_twoc
.deps/$(LANG1).twoc.hfst: $(BASENAME).$(LANG1).twoc .deps/.d
	hfst-twolc $< -o $@

if_twoc}}{{if_lexd
.deps/$(LANG1).RL.lexd: $(BASENAME).$(LANG1).lexd .deps/.d
	cat $< | grep -v 'Dir/LR' > $@

.deps/$(LANG1).LR.lexd: $(BASENAME).$(LANG1).lexd .deps/.d
	cat $< | grep -v 'Dir/RL' > $@

.deps/$(LANG1).RL.lexd.hfst: .deps/$(LANG1).RL.lexd
	lexd $< .deps/$(LANG1).RL.lexd.att
	hfst-txt2fst .deps/$(LANG1).RL.lexd.att -o $@

.deps/$(LANG1).LR.lexd.hfst: .deps/$(LANG1).LR.lexd
	lexd $< .deps/$(LANG1).LR.lexd.att
	hfst-txt2fst .deps/$(LANG1).LR.lexd.att -o $@
if_lexd}}{{ifnot_lexd
.deps/$(LANG1).RL.lexc: $(BASENAME).$(LANG1).lexc .deps/.d
	cat $< | grep -v 'Dir/LR' > $@

.deps/$(LANG1).LR.lexc: $(BASENAME).$(LANG1).lexc .deps/.d
	cat $< | grep -v 'Dir/RL' > $@

.deps/$(LANG1).RL.lexc.hfst: .deps/$(LANG1).RL.lexc
	hfst-lexc $< -o $@ $(LEXCFLAGS)

.deps/$(LANG1).LR.lexc.hfst: .deps/$(LANG1).LR.lexc
	hfst-lexc $< -o $@ $(LEXCFLAGS)
ifnot_lexd}}{{ifnot_twoc
{{if_lexd

.deps/$(LANG1).RL.hfst: .deps/$(LANG1).RL.lexd.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).RL.lexd.hfst -2 .deps/$(LANG1).twol.hfst -o $@

.deps/$(LANG1).LR.hfst: .deps/$(LANG1).LR.lexd.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).LR.lexd.hfst -2 .deps/$(LANG1).twol.hfst -o $@
if_lexd}}{{ifnot_lexd

.deps/$(LANG1).RL.hfst: .deps/$(LANG1).RL.lexc.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).RL.lexc.hfst -2 .deps/$(LANG1).twol.hfst -o $@

.deps/$(LANG1).LR.hfst: .deps/$(LANG1).LR.lexc.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).LR.lexc.hfst -2 .deps/$(LANG1).twol.hfst -o $@
ifnot_lexd}}
ifnot_twoc}}{{if_twoc

.deps/$(LANG1).RL.lexc-twoc.hfst: .deps/$(LANG1).RL.lexc.hfst .deps/$(LANG1).twoc.hfst
	hfst-invert .deps/$(LANG1).RL.lexc.hfst | hfst-compose-intersect -1 - -2 .deps/$(LANG1).twoc.hfst | hfst-invert -o $@

.deps/$(LANG1).LR.lexc-twoc.hfst: .deps/$(LANG1).LR.lexc.hfst .deps/$(LANG1).twoc.hfst
	hfst-invert .deps/$(LANG1).LR.lexc.hfst | hfst-compose-intersect -1 - -2 .deps/$(LANG1).twoc.hfst | hfst-invert -o $@

.deps/$(LANG1).RL.hfst: .deps/$(LANG1).RL.lexc-twoc.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).RL.lexc-twoc.hfst -2 .deps/$(LANG1).twol.hfst -o $@

.deps/$(LANG1).LR.hfst: .deps/$(LANG1).LR.lexc-twoc.hfst .deps/$(LANG1).twol.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).LR.lexc-twoc.hfst -2 .deps/$(LANG1).twol.hfst | hfst-minimise -o $@
if_twoc}}

$(LANG1).autogen.hfst: .deps/$(LANG1).RL.hfst
	hfst-fst2fst -O $< -o $@{{if_spellrelax

.deps/$(LANG1).spellrelax.hfst: $(BASENAME).$(LANG1).spellrelax .deps/.d
	hfst-regexp2fst -S -o $@ $<

$(LANG1).automorf.hfst: .deps/$(LANG1).LR.hfst .deps/$(LANG1).spellrelax.hfst
	hfst-compose -1 $< -2 .deps/$(LANG1).spellrelax.hfst | hfst-invert | hfst-fst2fst -O -o $@
if_spellrelax}}{{ifnot_spellrelax

$(LANG1).automorf.hfst: .deps/$(LANG1).LR.hfst
	hfst-invert $< | hfst-fst2fst -O -o $@
ifnot_spellrelax}}

$(LANG1).autogen.att.gz: $(LANG1).autogen.hfst
	hfst-fst2txt $< | gzip -9 -c -n > $@

$(LANG1).automorf.att.gz: $(LANG1).automorf.hfst
	hfst-fst2txt $< | gzip -9 -c -n > $@

$(LANG1).autogen.bin: $(LANG1).autogen.att.gz .deps/.d
	zcat < $< > .deps/$(LANG1).autogen.att
	lt-comp lr .deps/$(LANG1).autogen.att $@

$(LANG1).automorf.bin: $(LANG1).automorf.att.gz .deps/.d
	zcat < $< > .deps/$(LANG1).automorf.att
	lt-comp lr .deps/$(LANG1).automorf.att $@

$(LANG1).autopgen.bin: $(BASENAME).post-$(LANG1).dix
	lt-comp lr $< $@

###############################################################################
## Debugging transducers (for testvoc)
###############################################################################

{{ifnot_lexd
debug: .deps/$(LANG1).LR-debug.hfst .deps/$(LANG1).lexc.hfst
ifnot_lexd}}{{if_lexd
debug: .deps/$(LANG1).LR-debug.hfst .deps/$(LANG1).lexd.hfst
if_lexd}}

{{ifnot_lexd
.deps/$(LANG1).LR-debug.hfst: $(BASENAME).$(LANG1).lexc .deps/.d
	cat $< | grep -v 'Dir/RL' | grep -v 'Use/Circ' > .deps/$(LANG1).LR-debug.lexc
	hfst-lexc .deps/$(LANG1).LR-debug.lexc -o .deps/$(LANG1).LR-debug.lexc.hfst $(LEXCFLAGS)
	hfst-compose-intersect -1 .deps/$(LANG1).LR-debug.lexc.hfst -2 .deps/$(LANG1).twol.hfst -o $@

.deps/$(LANG1).lexc.hfst: .deps/$(LANG1).RL.lexc.hfst
	hfst-fst2fst -O -i $< -o $@
ifnot_lexd}}{{if_lexd
.deps/$(LANG1).LR-debug.hfst: $(BASENAME).$(LANG1).lexd .deps/.d
	cat $< | grep -v 'Dir/RL' | grep -v 'Use/Circ' > .deps/$(LANG1).LR-debug.lexd
	lexd .deps/$(LANG1).LR-debug.lexd .deps/$(LANG1).LR-debug.lexd.att
	hfst-txt2fst .deps/$(LANG1).LR-debug.lexd.att -o .deps/$(LANG1).LR-debug.lexd.hfst
	hfst-compose-intersect -1 .deps/$(LANG1).LR-debug.lexd.hfst -2 .deps/$(LANG1).twol.hfst -o $@

.deps/$(LANG1).lexd.hfst: .deps/$(LANG1).RL.lexd.hfst
	hfst-fst2fst -O -i $< -o $@
if_lexd}}
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

.deps/acceptor.default.hfst: $(LANG1).autogen.hfst
	cat $< | hfst-fst2fst -t | hfst-project --project=lower | hfst-minimise | hfst-fst2fst  -f olw -o $@


###############################################################################
## Unigram tagger
###############################################################################

#$(LANG1).prob: corpus/$(LANG1).tagged
#	apertium-tagger -s 0 -u 2 $@ $<

###############################################################################
## Distribution
###############################################################################

EXTRA_DIST= \{{ifnot_lexd
		$(BASENAME).$(LANG1).lexc	\{{if_twoc
		$(BASENAME).$(LANG1).twoc	\
if_twoc}}
ifnot_lexd}}{{if_lexd
		$(BASENAME).$(LANG1).lexd	\
if_lexd}}
		$(BASENAME).$(LANG1).twol	\
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

apertium_{{languageCode}}_DATA=$(TARGETS_COMMON) \{{ifnot_lexd
	$(BASENAME).$(LANG1).lexc	\{{if_twoc
	$(BASENAME).$(LANG1).twoc	\
if_twoc}}
ifnot_lexd}}{{if_lexd
	$(BASENAME).$(LANG1).lexd	\
if_lexd}}
	$(BASENAME).$(LANG1).twol	\
	$(BASENAME).$(LANG1).rlx	\
	$(BASENAME).post-$(LANG1).dix	\
	$(LANG1).prob

pkgconfigdir = $(prefix)/share/pkgconfig
pkgconfig_DATA = $(BASENAME).pc

noinst_DATA=modes/$(LANG1)-morph.mode

install-data-local: install-modes
uninstall-local: uninstall-modes

###############################################################################
## Cleanup
###############################################################################

CLEANFILES = $(TARGETS_COMMON)
clean-local:
	-rm -rf .deps modes

###############################################################################
## Test
###############################################################################

test: all
	apertium-regtest test
