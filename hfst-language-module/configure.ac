AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName}}], [0.1.0], [{{email}}], [apertium-{{languageCode}}], [https://wiki.apertium.org/wiki/Apertium-{{languageCode}}])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.6.1)
PKG_CHECK_MODULES(HFST, hfst >= 3.15.1)
PKG_CHECK_MODULES(CG3, cg3 >= 1.3.1){{if_lexd
PKG_CHECK_MODULES(LEXD, lexd >= 0.0.1)
if_lexd}}

PKG_CHECK_MODULES(HFSTOSPELL, hfstospell >= 0.2, [], [
      AC_MSG_NOTICE([You will need hfst-ospell installed to use the compiled speller])
])

AP_MKINCLUDE

AC_OUTPUT([Makefile apertium-{{languageCode}}.pc])
