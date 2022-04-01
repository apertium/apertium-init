AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName}}], [0.1.0], [https://github.com/apertium/apertium-{{languageCode}}/issues], [apertium-{{languageCode}}], [https://wiki.apertium.org/wiki/Apertium-{{languageCode}}])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.8.1)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.6.1)
PKG_CHECK_MODULES(CG3, cg3 >= 1.3.6)

PKG_CHECK_MODULES(REGTEST, apertium-regtest >= 0.9.1, [],
                  [AC_MSG_WARN([Running tests requires apertium-regtest])])

AP_MKINCLUDE

AC_CONFIG_FILES([Makefile apertium-{{languageCode}}.pc])
AC_OUTPUT
