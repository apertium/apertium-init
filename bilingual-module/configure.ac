AC_PREREQ(2.52)

AC_INIT([Apertium {{languageName1}}-{{languageName2}}], [0.2.0], [{{email}}], [apertium-{{languageCode1}}-{{languageCode2}}], [http://wiki.apertium.org/wiki/Apertium-{{languageCode1}}-{{languageCode2}}])
AM_INIT_AUTOMAKE

AC_PROG_LN_S
AC_PROG_AWK

m4_define([required_apertium_version], [3.4.0])
PKG_CHECK_MODULES(APERTIUM, apertium >= required_apertium_version, [], [PKG_CHECK_MODULES(APERTIUM, apertium-3.2 >= required_apertium_version)])

{{if_hfst
AC_PATH_PROG([HFSTLEXC], [hfst-lexc], [false], [$PATH$PATH_SEPARATOR$with_hfst_lexc/bin])
AS_IF([test x$HFSTLEXC = xfalse], [AC_MSG_ERROR([You don't have hfst-lexc installed])])

AC_PATH_PROG([HFSTTWOLC], [hfst-twolc], [false], [$PATH$PATH_SEPARATOR$with_hfst_twolc/bin])
AS_IF([test x$HFSTTWOLC = xfalse], [AC_MSG_ERROR([You don't have hfst-twolc installed])])
if_hfst}}

AC_PATH_PROG([CGCOMP], [cg-comp], [false], [$PATH$PATH_SEPARATOR$with_cg_comp/bin])
AS_IF([test x$CGCOMP = xfalse], [AC_MSG_ERROR([You don't have cg-comp installed])])

AC_PATH_PROG([CGPROC], [cg-proc], [false], [$PATH$PATH_SEPARATOR$with_cg_proc/bin])
AS_IF([test x$CGPROC = xfalse], [AC_MSG_ERROR([You don't have cg-proc installed])])

AC_PATH_PROG([LRXCOMP], [lrx-comp], [false], [$PATH$PATH_SEPARATOR$with_lrx_comp/bin])
AS_IF([test x$LRXCOMP = xfalse], [AC_MSG_ERROR([You don't have lrx-comp installed])])

AC_PATH_PROG([LRXPROC], [lrx-proc], [false], [$PATH$PATH_SEPARATOR$with_lrx_proc/bin])
AS_IF([test x$LRXPROC = xfalse], [AC_MSG_ERROR([You don't have lrx-proc installed])])

AC_PATH_PROGS(ZCAT, [gzcat zcat], [false])
AS_IF([test x$ZCAT = xfalse], [AC_MSG_ERROR([You don't have zcat nor gzcat installed])])

m4_ifdef([AP_CHECK_LING],[],[AC_MSG_ERROR([AP_CHECK_LING not defined, is apertium.m4 in ACLOCAL_PATH? See: http://wiki.apertium.org/wiki/Installation_troubleshooting])])

AP_CHECK_LING([1], [apertium-{{languageCode1}}])
AP_CHECK_LING([2], [apertium-{{languageCode2}}])

AP_MKINCLUDE

AC_OUTPUT([Makefile])

