# Makefile for mesh/CXY
#
# The point of this code is that we guarantee topology
# of our curves (if nonsingular).  If the curve looks zagged, it
# is really a continuous line -- you must zoom into the image to see this.
#
# (1) COMPILING THE PROGRAM:
# You can compile the program at various levels (level 1 is fast,
# but possibly incorrect for difficult cases, level 3 is always
# correct, but can be very slow).
#
# To make the program "cxy" at level n, do:
#
# 	> make veryclean	-- removes out previously compiled objects
# 	> make cxy LEV=n	-- n=1, 2 or 3
# 	> make eg10		-- run example 10
#
# To compile all three levels of accuracy in one shot, do:
#
# 	> make all		-- compiles cxy_1, cxy_2, cxy_3 (3 levels)
# 	> make testall		-- runs eg1 in all 3 levels
# 	> make LEV=2 eg4	-- runs eg4 in level 2
#
# (2) RUNNING THE PROGRAM:
#
# There are several simple examples you can try:
#
# 	> make eg1
# 	> make eg2
# 	> ...
#
#  Currently, you can do "make eg<n>" (where <n>=1-6, 10-12).
#  Note that you can pan and zoom when viewing the displayed curve:
#
#  Of course, you can create more targets of your own.
#
# (3) TODO:  We should create examples that exceed the
# 	accuracy of Level 1, so that Level 2 is
# 	really needed.
#
# --Chee (May 2010)
#
# Since Core Library Version 2.0
# 	$Id: Makefile,v 1.27 2010/07/14 14:54:12 exact Exp $

#=================================================
# VARIABLES
#=================================================
#CHOOSE THE LINKAGE 
LINKAGE=static
LINKAGE=shared

# file extension
ext= 
ext=.c
ext=.cc
ext=.cpp

CORE_PATH=../../..
include ../Make.options

#=================================================
# VARIABLES 
#=================================================

SUFFIX=

ifdef LEV
	SUFFIX=_$(LEV)
else
	LEV=2
	LEV=3
	LEV=1
endif

DEPEND=
TARGETS= cxy

CORE_LEVEL=2
CORE_LEVEL=3
CORE_LEVEL=1

p=cxy

ifile=plot

verbose=1
verbose=

#=================================================
# TARGETS
#=================================================


# We just compile, but do not run the tests because these
#     programs are interactive, NOT suitable for automatic testing
default: all

test: all
	-@echo "We compile ./cxy but not run it in automatic tests,"
	-@echo "    because the program is interactive."
	-@echo "You may directly call \"make eg1\" or \"make eg2\", etc."

moretest: all
	-@echo "We compile ./cxy but not run it in automatic tests,"
	-@echo "    because the program is interactive."
	-@echo "You may directly call \"make eg12\" or \"make eg20\", etc."

# These are interactive tests... not suitable for automatic testing!
no=11
no=2
no=1
testall: cxy1 cxy2 cxy3
	make LEV=1 eg$(no)
	make LEV=2 eg$(no)
	make LEV=3 eg$(no)

# ********************************************************************** 
# THESE FOUR TESTS USES THE SAME CURVE:
# 		x^2 -3x^4 -2y^2 +1	(a modified ellipse)
#
# COMMENTS: if the curve looks "wriggly" it is not an issue, as
# we introduce vertices in the middle of box edges.  We could
# improve this by simply linear interpolation.  But the isotopy
# type of the curve is guaranteed correct!
# You can zoom into the curve to see how the wriggly-ness arise.
# ********************************************************************** 
# eg1 -- show the subdiv boxes (default), refined to 0.2
eg eg1:  $(TARGETS)
	./cxy$(SUFFIX) "x^2 - 3x^4 - 2y^2 + 1" -1.5 -1.5 1.5 1.5 0.1 0.0001 0 1 

# eg2 -- do not show the subdiv boxes, refined to 0.2
eg2:  $(TARGETS)
	./cxy$(SUFFIX) "x^2 - 3x^4 - 2y^2 + 1" -1.5 -1.5 1.5 1.5 0.1 0.0001 0 0

# eg3 -- max size is 10000 (this basically stops the subdivision when isotopy is achieved)
# 	Thus, this should be the fastest
eg3:  $(TARGETS)
	./cxy$(SUFFIX) "x^2 - 3x^4 - 2y^2 + 1" -1.5 -1.5 1.5 1.5 10000 0.0001 0 0 

# eg4 -- like eg1, but min size is 0.01 (this forces subdivision until at least 0.01)
# 	This can be slow unless in Level 1!
# 	On the platform in the README file, takes 379 ms.
# 	You can zoom into the image to see the fine details.
eg4:  $(TARGETS)
	./cxy$(SUFFIX) "x^2 - 3x^4 - 2y^2 + 1" -1.5 -1.5 1.5 1.5 0.01 0.0001 0 1

# eg5 -- like eg1, but min size is 0.0001 (this forces subdivision until at least 0.0001)
# 	This can be very slow even in Level 1! 
# 	On the platform in the README file, it takes 20892 ms.
# 	You can zoom into the image to see the fine details.
eg5:  $(TARGETS)
	./cxy$(SUFFIX) "x^2 - 3x^4 - 2y^2 + 1" -1.5 -1.5 1.5 1.5 0.001 0.0001 0 1

# ********************************************************************** 


# ********************************************************************** 
# THE NEXT CURVE IS the curve 0 = f(x,y) = sin (x^2) - cos (y^2).
#    BUT we do the TAYLOR EXPANSION to the third term:
#	f(x,y)  =  x^2 - x^6/6 + x^10/120 - (1 - y^4/2 + y^8/24)
#    But our parser accepts only integer coefficients, so we multiply by 120:
#
# NOTE:  Our Core 2 Design Paper used these images
# ********************************************************************** 
eg10:  $(TARGETS)
	./cxy$(SUFFIX) "120 x^2 - 20 x^6 + x^10 - (120 - 60 y^4 + 5 y^8)" \
		 -2 -2 2 2 1000 0.001 0 1
eg11:  $(TARGETS)
	./cxy$(SUFFIX) "120 x^2 - 20 x^6 + x^10 - (120 - 60 y^4 + 5 y^8)" \
		 -2 -2 2 2 0.02 0.001 0 0
# eg12: it simply ignores all the divisions in the coefficients,
# 	so computes a completely different curve.
eg12:  $(TARGETS)
	./cxy$(SUFFIX) "x^2 - x^6/6 + x^10/120 - (1 - y^4/2 + y^8/24)" \
		 -2 -2 2 2 0.01 0.001 0.8 1
# ********************************************************************** 

# ********************************************************************** 
# Example from Krawcyzk test for intersecting two curves
eg20:	$(TARGETS)
	./cxy$(SUFFIX) "(x^3 - x)(x^2 y - 7)" \
		 -2 -2 10 10 0.01 0.001 0 1
eg21:	$(TARGETS)
	./cxy$(SUFFIX) "x^2 y = 7" \
		 -2 -2 10 10 0.01 0.001 0 1
eg22:	$(TARGETS)
	./cxy$(SUFFIX) "x^3 - x = 0" \
		 -2 -2 10 10 0.01 0.001 0 1

# ********************************************************************** 

# ********************************************************************** 
# Example FP2.2 from Paper of Duracz and Konecny (actually, they credit it to
# 	the thesis of Vu (Ref.[15]).  From discussion of Chee and Luke Ong.
# 	This example has two underlying curves: a quartic curve
#	   (x^2 + y^2 +12x + 9)^2 - 4 (2 x + 3)^3 = 0
#	and a circle
#	   x^2+y^2 - 2 = 0
#
# 	Eg31 and 32 are correspond to FP2.2, but Eg30 is a partial version (where
# 	only the quartic curve is shown).
#
eg30:	$(TARGETS)
	./cxy$(SUFFIX) "(x^2 + y^2 +12x + 9)^2 = 4 (2 x + 3)^3" \
		 -2 -2 2 2 0.02 0.001 0 1
# NOTES on eg31 and eg32:
# 	The difference between these 2 examples is that the last argument
# 	(the 9-th argument, "draw_box" boolean flag)
# 	is 1 in eg31, and 0 in eg32. 
#	Using the re-factored version of Long/Shuxing code,
#	we run out of memory on eg31, but eg32 runs for 23 minutes and still did not
#	stop. This does not seem right, because its memory
#	remained stuck at 77M throughout most of its computation time.  
#	Does it mean that it keeps constructing the SAME boxes because Level 1
#	resolution is exhausted?   Only way to find out is to use Level 2. 
#	Eventually, we fixed the code, and we could run these examples quite reasonably:
#	eg31 takes 13723 ms.   A newer implementation by Narayan improves this to 805 ms
#	(17 times faster).
eg31:	$(TARGETS)
	./cxy$(SUFFIX) "((x^2 + y^2 +12x + 9)^2 - 4 (2 x + 3)^3)(x^2+y^2 -2)" \
		 -2 -2 2 2 0.03 0.001 0 1
eg32:	$(TARGETS)
	./cxy$(SUFFIX) "((x^2 + y^2 +12x + 9)^2 - 4 (2 x + 3)^3)(x^2+y^2 -2)" \
		 -2 -2 2 2 0.03 0.001 0 0
#
# Example FP2.3 from Paper of Duracz and Konecny (actually, they credit it to
# 	the thesis of Vu (Ref.[15]).
# 	This example has three curves:
#		x^3 + y^3 - 3xy = 0
#		x^2 + y^2 - 0.1 = 0
#		(x^2 + y^2)(y^2 + x(x+1)) - 4xy^2 = 0
#	On the cxy-new, eg33 takes 6183 ms.
eg33: $(TARGETS)
	./cxy$(SUFFIX) "(x^3 + y^3 - 3xy)(x^2 + y^2 - 0.1)((x^2 + y^2)(y^2 + x(x+1)) - 4xy^2)" \
		 -2 -2 2 2 0.03 0.001 0 1

# ********************************************************************** 

p: $(p).o $(DEPEND)
	${CXX} $(LDFLAGS)  $< $(CORE_LIB) -o ${p}


# Compile with different number types

pC cxy: cxy.o

new cxy-new: cxy-new.o

cxy: box.o display.o
	${CXX} $(LDFLAGS) -DCORE_LEVEL=${LEV} \
	   box.o display.o cxy.o $(CORE_LIB) -o ${p}

#=================================================
# Rules for CORE_LEV 1, 2, and 3
#=================================================
cxy1: box_1.o display_1.o cxy_1

cxy2: box_2.o display_2.o cxy_2

cxy3: box_3.o display_3.o cxy_3

all: 
	make cxy1
	make cxy2
	make cxy3

CXY_DEP_lev1= box_1.o display_1.o
CXY_DEP_lev2= box_2.o display_2.o
CXY_DEP_lev3= box_3.o display_3.o

OPT_CXXFLAGS=$(CXXFLAGS)
# Include this flag if you want to run gcc with the
# highest level of optimization. This makes the compile
# slightly slower, but the code 2x or 3x faster
# OPT_CXXFLAGS=-O3 $(CXXFLAGS)

%_1.o: %.cpp
	${CXX} -c -DCORE_LEVEL=1 $(OPT_CXXFLAGS) $(CORE_INC) $< -o $@

%_2.o: %.cpp
	${CXX} -c -DCORE_LEVEL=2 $(OPT_CXXFLAGS) $(CORE_INC) $< -o $@

%_3.o: %.cpp
	${CXX} -c -DCORE_LEVEL=3 $(OPT_CXXFLAGS) $(CORE_INC) $< -o $@

%_1: %_1.o $(CXY_DEP_1)
	${CXX} $(LDFLAGS) $? $(CXY_DEP_lev1) \
	    $(CORE_LIB) $(COREX_LIB_LEVEL1) -o $@

%_2: %_2.o $(CXY_DEP_2)
	${CXX} $(LDFLAGS) $? $(CXY_DEP_lev2) \
	    $(CORE_LIB) $(COREX_LIB_LEVEL1) -o $@

%_3: %_3.o $(CXY_DEP_3)
	${CXX} $(LDFLAGS) $? $(CXY_DEP_lev3) \
	    $(CORE_LIB) $(COREX_LIB_LEVEL3) -o $@

#=================================================
# Rules
#=================================================
%: %.o $(DEPEND)
	${CXX} $(LDFLAGS) $< $(CORE_LIB) -o $@

.cpp.o:
	${CXX} -c $(OPT_CXXFLAGS) -DCORE_LEVEL=${LEV} \
	   $(CORE_INC) $< -o $@


#=================================================
# Clean object files
#=================================================
clean:
	-@test -z "*.o" || rm -f *.o

#=================================================
# Remove executable files
#=================================================
ALL=$(TARGETS) $(MORE_TARGETS)
EXEPROGS=$(ALL:=$(EXETYPE))

veryclean: clean
	-@test -z "$(EXEPROGS)" || rm -f $(EXEPROGS)
	-@rm -f cxy${EXETYPE} cxy_1 cxy_2 cxy_3

#=================================================
# Housekeeping
#=================================================

tar:
	-@tar cvf curves.tar \
		*cpp Makefile README

save:
	-@ci -l -m"make save" *.cpp *.tcc *.h Makefile README Notes

