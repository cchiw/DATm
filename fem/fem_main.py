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

#######
# enable inside check
# enable conditional
# fnspace description part of field type
# limit to only scalar fields (2-d, and 3-d) case
# change position range
###########




# write firedrake program
def writeFem():
    mesh = UnitSquareMesh(2,2)
    V= FunctionSpace(mesh,"Lagrange",degree=2)
    f = Function(V).interpolate(Expression(exp))

    cut_step(name, f, res)


# make program
def makeProgram(p_out):
    s0 = "cp fem/observ_init.c observ_init.c"
    s1 = "cp fem/Makefile Makefile"
    s2 = "make clean"
    s3 = "make "+p_out+".o"
    s4 = "make "+p_out+"_init.o"
    s5 = "make "+p_out+"_init.so"
    s6 = "py.test -v "+p_out+".py"
    es = [s0, s1, s2, s3, s4, s5, s6]
    for i in es:
        os.system(i)

# read output of firedrake program




################################ write annd run test program ################################
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall):
    # write new diderot program
    readDiderot(p_out, app, pos)
    makeProgram(p_out)
    return (None, None, startall)