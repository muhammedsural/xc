/* shrunk.f -- translated by f2c (version 20160102).
   You must link the resulting object file with libf2c:
	on Microsoft Windows system, link with libf2c.lib;
	on Linux or Unix systems, link with .../path/to/libf2c.a -lm
	or, if you install libf2c.a in a standard place, with -lf2c -lm
	-- in that order, at the end of the command line, as in
		cc *.o -lf2c -lm
	Source for libf2c is in /netlib/f2c/libf2c.zip, e.g.,

		http://www.netlib.org/f2c/libf2c.zip
*/

#ifdef __cplusplus
extern "C" {
#endif
#include "f2c.h"

/*    Copyright(C) 1999-2020 National Technology & Engineering Solutions */
/*    of Sandia, LLC (NTESS).  Under the terms of Contract DE-NA0003525 with */
/*    NTESS, the U.S. Government retains certain rights in this software. */

/*    See packages/seacas/LICENSE for details */
logical shrunk_(real *ratio, integer *nrow)
{
    /* Initialized data */

    static real toler1 = (float).85;
    static real toler2 = (float).75;
    static real toler3 = (float).6;

    /* System generated locals */
    logical ret_val;

/* *********************************************************************** */
/*  FUNCTION SHRUNK = LOGICAL FUNCTION THAT RETURNS TRUE IF THE ELEMENT */
/*                    SIZE IS DIMINISHING WITH ROW DEPTH */
/* *********************************************************************** */
    if (*nrow >= 3 && *ratio < toler1) {
	ret_val = TRUE_;
    } else if (*nrow >= 2 && *ratio < toler2) {
	ret_val = TRUE_;
    } else if (*nrow >= 1 && *ratio < toler3) {
	ret_val = TRUE_;
    } else {
	ret_val = FALSE_;
    }
    return ret_val;
} /* shrunk_ */

#ifdef __cplusplus
	}
#endif