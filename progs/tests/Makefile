# Core Library, $Id: Makefile,v 1.14 2010/07/21 22:23:00 exact Exp $

CORE_PATH= ../..
include $(CORE_PATH)/progs/Make.options

#=================================================
# Define target files (put all your files here)
#=================================================
p= floorLg
p= zero
p= tExpr
p= tCin
p= tQueue

LEV= 3
TARGETS=tQueue
MORE_TARGETS= floor_ceil bench \
	tCin linn

test: $(TARGETS)
	./tQueue

moretest: $(MORE_TARGETS)
	./floor_ceil
	./bench

p ${p}: ${p}.cpp
	${CXX} -c $(CXXFLAGS) $(CORE_INC) ${p}.cpp -o ${p}.o
	${CXX} $(LDFLAGS) ${p}.o $(CORE_LIB) -o ${p}

floor_ceil: floor_ceil.o

floorLg: floorLg.o

length: length.o

invalid: invalid.o

bench: bench.o

linn: linn.o

jihun: jihun.o

conditions: conditions.o

bench1: bench1.o

tBigFloat: tBigFloat.o

tt: tt.o

stl: stl.o

itoa: itoa.o

tExpr: tExpr.o

tCin: tCin.o

tQueue: tQueue.o

triplyNested: triplyNested.o

cu: triplyNested
	triplyNested

1: 1.o

t: t.o

hw2_4:hw2_4.o

precision: precision.o

#=================================================
# Rules
#=================================================
#%: %.o
#	${CXX} $(LDFLAGS) $< -lcorex++$(VAR)_level${LEV} $(CORE_LIB) -o $@

#.cpp.o:
#	${CXX} -c $(CXXFLAGS) $(CORE_INC) -DCORE_LEVEL=${LEV} $< -o $@

include $(CORE_PATH)/progs/Make.rules
#=================================================
# END
#=================================================
