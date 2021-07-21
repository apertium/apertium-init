AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName}}], [0.1.0], [{{email}}], [apertium-{{languageCode}}], [https://wiki.apertium.org/wiki/Apertium-{{languageCode}}])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.8.0)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.6.0)
PKG_CHECK_MODULES(CG3, cg3 >= 1.3.1)

PKG_CHECK_MODULES(REGTEST, apertium-regtest >= 0.0.1, [],
                  [AC_MSG_WARN([Running tests requires apertium-regtest])])

AP_MKINCLUDE

AC_OUTPUT([Makefile apertium-{{languageCode}}.pc])
