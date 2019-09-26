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

{{if_lsx
AC_PATH_PROG([LSXCOMP], [lsx-comp], [false], [$PATH$PATH_SEPARATOR$with_lsx_comp/bin])
AS_IF([test x$LSXCOMP = xfalse], [AC_MSG_ERROR([You don't have lsx-comp installed])])

AC_PATH_PROG([LSXPROC], [lsx-proc], [false], [$PATH$PATH_SEPARATOR$with_lsx_proc/bin])
AS_IF([test x$LSXPROC = xfalse], [AC_MSG_ERROR([You don't have lsx-proc installed])])
if_lsx}}

{{if_anaphora
AC_PATH_PROG([ANAPHORA], [apertium-anaphora], [false], [$PATH$PATH_SEPARATOR$with_apertium_anaphora/bin])
AS_IF([test x$ANAPHORA = xfalse], [AC_MSG_ERROR([You don't have apertium-anaphora installed])])
if_anaphora}}

{{if_rtx
AC_PATH_PROG([RTXCOMP], [rtx-comp], [false], [$PATH$PATH_SEPARATOR$with_rtx_comp/bin])
AS_IF([test x$RTXCOMP = xfalse], [AC_MSG_ERROR([You don't have rtx-comp installed])])

AC_PATH_PROG([RTXPROC], [rtx-proc], [false], [$PATH$PATH_SEPARATOR$with_rtx_proc/bin])
AS_IF([test x$RTXPROC = xfalse], [AC_MSG_ERROR([You don't have rtx-proc installed])])
if_rtx}}

AC_PATH_PROGS(ZCAT, [gzcat zcat], [false])
AS_IF([test x$ZCAT = xfalse], [AC_MSG_ERROR([You don't have zcat nor gzcat installed])])

m4_ifdef([AP_CHECK_LING],[],[AC_MSG_ERROR([AP_CHECK_LING not defined, is apertium.m4 in ACLOCAL_PATH? See: http://wiki.apertium.org/wiki/Installation_troubleshooting])])

AP_CHECK_LING([1], [apertium-{{languageCode1}}])
AP_CHECK_LING([2], [apertium-{{languageCode2}}])

AP_MKINCLUDE

AC_OUTPUT([Makefile])

