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
from ex1 import *

#######
# enable inside check
# enable conditional
# fnspace description part of field type
# limit to only scalar fields (2-d, and 3-d) case
# change position range (set by branch). should be dependent on mesh testing
###########




# create firedrake field
def writeFem(p_out, shape, pos, output):
    vis_exp(p_out, "x[0]")
    # convert to txt file


    product = 1
    for x in shape:
        product *= x
    m2 = len(pos)+1
    w_shape=" -s "+str(product)+" "+str(m2)
    
    os.system("unu reshape -i "+p_out+".nrrd "+w_shape+" | unu save -f text -o "+output+".txt")

# make program
def makeProgram(p_out, output):
    s0 = "cp observ.diderot ex1.diderot"
    s1 = "cp fem/ex1_init.c ex1_init.c"
    s2 = "cp fem/Makefile Makefile"
    s3 = "make clean"
    s4 = "make ex1.o"
    s5 = "make ex1_init.o"
    s6 = "make ex1_init.so"
    s8 = "cp fem/ex1.py ex1.py"
    
    
    s10 = "cp ex1.diderot "+output+".diderot"
    es = [s0, s1, s2, s3, s4, s5, s6, s8]
    for i in es:
        os.system(i)

# read output of firedrake program




################################ write annd run test program ################################
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall):
    # write new diderot program
    readDiderot(p_out, app, pos)
    makeProgram(p_out, output)
    shape = app.oty.shape
    writeFem(p_out, shape, pos, output)
    return (1,1, startall)