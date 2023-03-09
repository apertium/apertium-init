AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName}}], [0.1.0], [https://github.com/apertium/apertium-{{languageCode}}/issues], [apertium-{{languageCode}}], [https://wiki.apertium.org/wiki/Apertium-{{languageCode}}])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.7.4)
PKG_CHECK_MODULES(APERTIUM, apertium >= 3.9.0)
PKG_CHECK_MODULES(HFST, hfst >= 3.16.0)
PKG_CHECK_MODULES(CG3, cg3 >= 1.4.0){{if_lexd
PKG_CHECK_MODULES(LEXD, lexd >= 1.3.0)
if_lexd}}

AC_ARG_ENABLE([speller], AC_HELP_STRING([--enable-speller], [Build spellchecker from morphological analyser]))

AM_CONDITIONAL([ENABLE_SPELLER], [test "x$enable_speller" = "xyes"])
AM_COND_IF([ENABLE_SPELLER], [
  PKG_CHECK_MODULES(HFSTOSPELL, hfstospell >= 0.5.3, [],
     [AC_MSG_NOTICE([You will need hfst-ospell installed to use the compiled speller])])
])

PKG_CHECK_MODULES(REGTEST, apertium-regtest >= 0.9.1, [],
   [AC_MSG_WARN([Running tests requires apertium-regtest])])

AP_MKINCLUDE

AC_CONFIG_FILES([Makefile apertium-{{languageCode}}.pc])
AC_OUTPUT
