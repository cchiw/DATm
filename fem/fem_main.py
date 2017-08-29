# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re
import time
# shared base programs
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_write import * 
from base_writeDiderot import *
from base_constants import *

# fem specific programs
from fem_writeDiderot import readDiderot
from sd2 import connect1, connect2

#######
# enable inside check
# enable conditional
# fnspace description part of field type
# limit to only scalar fields (2-d, and 3-d) case
# change position range (set by branch). should be dependent on mesh testing
# need to translate exp in field type to exp for python
###########


target ="ex1" #name in Makefile

# create firedrake field
def writeFem(p_out, shape, pos, output):
    #convert exp to field
    # depends on number of args
    #connect1(p_out, "x[0]",target)
    connect2(p_out, "x[0]", "x[0]", target)
    
    # convert to txt file
    product = 1
    for x in shape:
        product *= x
    m2 = len(pos)+1
    w_shape=" -s "+str(product)+" "+str(m2)
    
    os.system("unu reshape -i "+p_out+".nrrd "+w_shape+" | unu save -f text -o "+output+".txt")

# make program
def makeProgram(p_out, output):
    name = "fem/sd2"  # for a specific shape
    name  = name+"_fg" # two field args to be init

    s0 = "cp "+name+"_init.c "+target+"_init.c"
    s1 = "cp observ.diderot "+target+".diderot"
    s2 = "cp fem/Makefile Makefile"
    s3 = "make clean"
    s4 = "make "+target+".o"
    s5 = "make "+target+"_init.o"
    s6 = "make "+target+"_init.so"
    
    
    s10 = "cp "+target+".diderot "+output+".diderot"
    es = [s0, s1, s2, s3, s4, s5, s6]
    for i in es:
        os.system(i)

# read output of firedrake program




################################ write annd run test program ################################
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall):
    # write new diderot program
    readDiderot(p_out, app, pos)
    os.system("rm *.*o")
    makeProgram(p_out, output)
    name = "ex1"
    if(os.path.exists(name+".o") and os.path.exists(name+"_init.so")):
        shape = app.oty.shape
        writeFem(p_out, shape, pos, output)
        if(os.path.exists(output+".txt")):
           return (1,1, startall)
        else:
           return (1, None, startall)
    else:
        # did not compile
        return (None,None, startall)