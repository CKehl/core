############################################################
# file: Makefile (for documentation)
# 	CORE Library version 2.0
# 	$Id: Makefile,v 1.2 2007/04/10 00:48:22 exact Exp $
############################################################


############################################################
# targets
############################################################


all:	tut dox

tut:
	cd tutorial; make

dox:
	cd doxy; make

clean:
	cd tutorial; make clean
	cd doxy; make clean

veryclean: clean
	cd tutorial; make veryclean
	cd doxy; make veryclean
