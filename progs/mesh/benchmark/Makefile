# Makefile for root isolation benchmarks.
#
# Core Library, $Id: Makefile,v 1.4 2010/08/16 17:20:14 exact Exp $

CORE_PATH=../../..
include ../Make.options

#=================================================
# Define target files (put all your files here)
#=================================================
TARGETS = main_ceval main_newt

all: $(TARGETS)

test: $(TARGETS)
	python ./run_tests.py

moretest: $(TARGETS)
# nothing to do

# The following is for visualization and interactive mode:
#
#  NOTE that you can zoom-in (i) or zoom-out (k), pan (w,a,s,d) to
#  view the display.
#
# eg1 (20 roots of unity)
eg1: main_ceval
	main_ceval --poly ./data/nroots20.pol --display --use_root_bounds

# eg2
#
eg2 : main_ceval
	main_ceval --poly ./data/somepoly6.pol --display --use_root_bounds

# 
# eg3 (laguerre20 polynomial) gives explicit bounding box to search for roots:
eg3 : main_ceval
	main_ceval --poly ./data/laguerre20.pol --display \
		--x_max 70 --x_min 0 --y_min -1 --y_max 1

# eg4 (laguerre20 polynomial) uses root bound calculations that
# ensure that all roots are found:
eg4 : main_ceval
	main_ceval --poly ./data/laguerre20.pol --display --use_root_bounds

# eg


main_ceval : main_ceval.o benchmark.o ../ceval/algorithm.o ../ceval/predicates.o ../ceval/tmp-display.o 
	${CXX} $(LDFLAGS) benchmark.o main_ceval.o ../ceval/algorithm.o ../ceval/predicates.o ../ceval/tmp-display.o $(CORE_LIB) -o $@
main_newt : main_newt.o benchmark.o ../krawczyk/tmp-display.o
	${CXX} $(LDFLAGS) benchmark.o main_newt.o ../krawczyk/tmp-display.o $(CORE_LIB) -lprofiler -o $@

#=================================================
# Rules
#=================================================
%: %.o
	${CXX} $(LDFLAGS) $< $(CORE_LIB) -o $@

.cpp.o:
	${CXX} -c $(CXXFLAGS) -O3 $(CORE_INC) $< -o $@

#=================================================
# Clean object files
#=================================================
clean:
	-@test -z "*.o" || rm -f *.o
	-@test -z "../ceval/*.o" || rm -f ../ceval/*.o
	-@test -z "../krawczyk/*.o" || rm -f ../krawczyk/*.o

#=================================================
# Remove executable files
#=================================================
EXEPROGS=$(TARGETS:=$(EXETYPE))

veryclean: clean
	-@test -z "$(EXEPROGS)" || rm -f $(EXEPROGS)

