AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName1}}-{{languageName2}}], [0.1.0], [https://github.com/apertium/apertium-{{languageCode1}}-{{languageCode2}}/issues], [apertium-{{languageCode1}}-{{languageCode2}}], [https://wiki.apertium.org/wiki/Apertium-{{languageCode1}}-{{languageCode2}}])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.8.1)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.6.9)

{{if_hfst
PKG_CHECK_MODULES(HFST, hfst >= 3.16.0)
if_hfst}}

PKG_CHECK_MODULES(CG3, cg3 >= 1.3.6)
PKG_CHECK_MODULES(APERTIUM_LEX_TOOLS, apertium-lex-tools >= 0.4.0)
{{if_lsx
PKG_CHECK_MODULES(APERTIUM_SEPARABLE, apertium-separable >= 0.5.0)
if_lsx}}
{{if_anaphora
PKG_CHECK_MODULES(APERTIUM_ANAPHORA, apertium-anaphora >= 1.1.0)
if_anaphora}}
{{if_rtx
PKG_CHECK_MODULES(APERTIUM_RECURSIVE, apertium-recursive >= 1.1.0)
if_rtx}}

AC_ARG_ENABLE([linter], AC_HELP_STRING([--enable-linter], [Lint files when compiling]))
AM_CONDITIONAL([ENABLE_LINTER], [test "x$enable_linter" = "xyes"])

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

PKG_CHECK_MODULES(REGTEST, apertium-regtest >= 0.9.1, [],
                  [AC_MSG_WARN([Running tests requires apertium-regtest])])

AP_MKINCLUDE

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
