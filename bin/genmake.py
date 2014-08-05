#! /usr/bin/env python

##################################################
# python script for generating Makefile
# author: Zilin Du (Mar 2006)
##################################################
# Description:
# Executing
#
#	> genmake.py
#
# will create an minimal Makefile for your
# CORE project in the current directory.
#
# To add additional targets in an existing Makefile 
# (which has been previously generated by genmake.py)
#
#	> genmake.py add prog1 [prog2 ...]
#
# To remove current targets in the Makefile, do:
#
#	> genmake.py remove prog1 [prog2 ...]
#
##################################################

import os.path, sys, string

empty_makefile="""# Makefile

# set the core library directory and include Make.config
include %s/Make.options

# define targets list
TARGETS=

# default target
all: ${TARGETS}

#@begin targets

#@end targets

#include standard rules from Make.rules
include %s/Make.rules
"""

# generate a makefile from template
def gen_empty_makefile(core_dir, make_fname="Makefile"):
  if os.path.isfile(make_fname):
    ans=raw_input("%s exists! Do you want to overwrite it? (y/n)" % make_fname)
    if ans != 'y' and ans != 'Y': return
  f = open(make_fname, 'w')
  f.write(empty_makefile % (core_dir, core_dir)) 

# add a target into makefile
def add_target(target_names, make_fname="Makefile"):
  print "Adding new target(s): %s ..." % ", ".join(target_names)
  tmp_fn = make_fname+'.bak'
  tmp_f = open(tmp_fn, "w")
  f = open(make_fname, "r")
  cont_line = False

  for line in f.readlines():
     #detect the start of continue line
    if line.startswith("TARGETS="):
      cont_line = True

    if cont_line and not line.endswith("\\\n"): #found end of continue line
      tmp_f.write(line[:-1])
      for t in target_names:
        tmp_f.write(" \\\n\t%s" % t)
      tmp_f.write("\n")
      cont_line = False
    elif line.startswith("#@end targets"):      #found the end of target rule
      for t in target_names:
        tmp_f.write("%s: %s.o\n\n" % (t, t))
      tmp_f.write(line)
    else:
      tmp_f.write(line)

  tmp_f.close()
  f.close()
  os.system("mv %s %s" % (tmp_fn, make_fname))
  print "Done."

# remove a target from makefile
def remove_target(target_names, make_fname="Makefile"):
  print "Removing target(s): %s ..." % ", ".join(target_names)
  tmp_fn = make_fname+'.bak'
  tmp_f = open(tmp_fn, "w")
  f = open(make_fname, "r")

  skip_next_line = False
  lines = f.readlines()
  
  for i in range(len(lines)):
    line = lines[i]
    if skip_next_line:
      skip_next_line = False
      continue
    skip_cur_line = False
    for t in target_names:
      target_rule = "%s: %s.o" % (t, t)
      target_name_1 = "%s\n" % t
      target_name_2 = "%s \\\n" % t
      if line.startswith(target_rule): # find the target rule, skip next line
        skip_next_line = True
        skip_cur_line = True
        break
      elif i<len(lines)-2 and lines[i+1].endswith(target_name_1):
        tmp_f.write(line[:-3])
        tmp_f.write("\n")
        skip_cur_line = True
        break
      elif (line.endswith(target_name_1) or line.endswith(target_name_2)):
        skip_cur_line = True
        break
    if not skip_cur_line:
      tmp_f.write(line)

  tmp_f.close()
  f.close()
  os.system("mv %s %s" % (tmp_fn, make_fname))
  print "Done."

# main function
if __name__ == '__main__':
  if len(sys.argv) >= 2:
    if sys.argv[1] == 'add':
      add_target(sys.argv[2:])
    elif sys.argv[1] == 'remove':
      remove_target(sys.argv[2:])
    else:
      gen_empty_makefile(sys.argv[1])
  else:
    gen_empty_makefile("..")
