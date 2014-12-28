AC_PREREQ(2.52)

AC_INIT([apertium-{{languageCode}}], [0.1.0], [])
AM_INIT_AUTOMAKE([apertium-{{languageCode}}], [0.1.0], no-define)
AC_PROG_LN_S
AC_PROG_AWK

m4_define([required_apertium_version], [3.2.0])
PKG_CHECK_MODULES(APERTIUM, apertium >= required_apertium_version, [], [PKG_CHECK_MODULES(APERTIUM, apertium-3.2 >= required_apertium_version)])

AC_PATH_PROG(LTPRINT, lt-print, no)
if test x$ac_cv_path_LTPRINT = x
then
  AC_MSG_ERROR([You don't have lt-print installed.])
fi
if test x$ac_cv_path_LTPRINT = xno
then
  AC_MSG_ERROR([You don't have lt-print installed.])
fi

AC_PATH_PROG(CGCOMP, cg-comp, no)
if test x$ac_cv_path_CGCOMP = x
then
  AC_MSG_ERROR([You don't have cg-comp installed.])
fi
if test x$ac_cv_path_CGPROC = xno
then
  AC_MSG_ERROR([You don't have cg-comp installed.])
fi

AC_PATH_PROG(PKG_CONFIG, pkg-config, no)
if test x$ac_cv_path_PKG_CONFIG = x
then
  AC_MSG_ERROR([You don't have pkg-config installed.])
fi
if test x$ac_cv_path_PKG_CONFIG = xno
then
  AC_MSG_ERROR([You don't have pkg-config installed.])
fi

AC_OUTPUT([Makefile apertium-{{languageCode}}.pc])
