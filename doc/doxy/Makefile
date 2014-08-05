############################################################
# file: Makefile (for doxygen)
# 	CORE Library version 2.0
# 	$Id: Makefile,v 1.1.1.1 2007/04/09 23:35:53 exact Exp $
############################################################

p=p

DOXYGEN=/usr/unsupported/installers/exact/doxygen-1.3/bin/doxygen
DOXYGEN=doxygen

############################################################
# targets
############################################################


manual: clean
	umask 022; \
	${DOXYGEN} doxygen.cfg

ps:
	cd latex; make ps

clean clean-manual:
	rm -rf html latex

veryclean: clean

############################################################
# make sure there is a .dvipsrc in the home directory
#	to use only type 1 font.
############################################################

