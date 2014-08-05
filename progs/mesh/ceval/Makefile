# Makefile for bareiss 
#
# (template Makefile for simple targets)
#
# Core Library, $Id: Makefile,v 1.5 2010/07/01 22:25:43 exact Exp $

CORE_PATH=../../..
include ../Make.options

#=================================================
# Define target files (put all your files here)
#=================================================
TARGETS = ceval

all: $(TARGETS)

test: $(TARGETS)
	./ceval

moretest: $(TARGETS)
# nothing to do

ceval: ceval.o algorithm.o predicates.o
	${CXX} $(LDFLAGS) ceval.o algorithm.o predicates.o $(CORE_LIB) -o $@


#=================================================
# Rules
#=================================================
%: %.o
	${CXX} $(LDFLAGS) $< $(CORE_LIB) -o $@

.cpp.o:
	${CXX} -c -O3 $(CXXFLAGS) $(CORE_INC) $< -o $@

#=================================================
# Clean object files
#=================================================
clean:
	-@test -z "*.o" || rm -f *.o

#=================================================
# Remove executable files
#=================================================
EXEPROGS=$(TARGETS:=$(EXETYPE))

veryclean: clean
	-@test -z "$(EXEPROGS)" || rm -f $(EXEPROGS)

