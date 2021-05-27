AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName1}}-{{languageName2}}], [0.1.0], [{{email}}], [apertium-{{languageCode1}}-{{languageCode2}}], [https://wiki.apertium.org/wiki/Apertium-{{languageCode1}}-{{languageCode2}}])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.6.1)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.5.1)

{{if_hfst
PKG_CHECK_MODULES(HFST, hfst >= 3.15.1)
if_hfst}}

PKG_CHECK_MODULES(CG3, cg3 >= 1.3.1)
PKG_CHECK_MODULES(APERTIUM_LEX_TOOLS, apertium-lex-tools >= 0.2.3)
{{if_lsx
PKG_CHECK_MODULES(APERTIUM_SEPARABLE, apertium-separable >= 0.3.3)
if_lsx}}
{{if_anaphora
PKG_CHECK_MODULES(APERTIUM_ANAPHORA, apertium-anaphora >= 0.0.4)
if_anaphora}}
{{if_rtx
PKG_CHECK_MODULES(APERTIUM_RECURSIVE, apertium-recursive >= 0.0.1)
if_rtx}}

AC_PATH_PROGS(ZCAT, [gzcat zcat], [false])
AS_IF([test x$ZCAT = xfalse], [AC_MSG_ERROR([You don't have zcat nor gzcat installed])])

m4_ifdef([AP_CHECK_LING],[],[AC_MSG_ERROR([AP_CHECK_LING not defined, is apertium.m4 in ACLOCAL_PATH? See: https://wiki.apertium.org/wiki/Installation_troubleshooting])])

{{if_giella1
AP_CHECK_LING([1], [giella-{{languageCode1}}])
if_giella1}}{{ifnot_giella1
AP_CHECK_LING([1], [apertium-{{languageCode1}}])
ifnot_giella1}}
{{if_giella2
AP_CHECK_LING([2], [giella-{{languageCode2}}])
if_giella2}}{{ifnot_giella2
AP_CHECK_LING([2], [apertium-{{languageCode2}}])
ifnot_giella2}}

AP_MKINCLUDE

AC_OUTPUT([Makefile])
