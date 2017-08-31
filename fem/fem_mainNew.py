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
from fem_helper import *
from fem_writeFire import  *
foo_femexp = "foo_fireexp"


template = "fem/fire.foo"



def cleanup(output, p_out):
    os.system("rm ex1.o")
    os.system("rm ex1_init.o")
    os.system("rm ex1_init.so")
    os.system("rm ex1.cxx")
    os.system("rm ex1.diderot")
    os.system("rm *.c")
    os.system("rm *.h")
    os.system("rm *.txt")
    os.system("rm *.nrrd")
    os.system("rm observ.diderot")
    os.system("rm rst/data/*")
    os.system("rm ex1*.*")
    os.system("rm "+output+"*")
    os.system("rm -r __pycache__")
    os.system("rm cat.nrrd")
    os.system("rm  "+p_out+".nrrd")
    os.system("rm  "+output+".txt")
    os.system("rm  "+p_out+".txt")


#if(num_fields==1):
#connect1("cat", "x[0]",target)
#os.system("python fem/sd2.py")
#elif(num_fields==2):
#connect2("cat", "x[0]", "x[0]", target)
#os.system("python fem/sd2_two.py")

# create firedrake field
def useFem(p_out, shape, pos, output, target):
    print "pos:",pos
    #convert exp to field
    # depends on number of args : (attached to arity now)
    # run program
    os.system("python "+p_out+".py")
    # convert to txt file
    product = 1
    for x in shape:
        product *= x
    m2 = len(pos)+1
    w_shape=" -s "+str(product)+" "+str(m2)
    os.system("unu reshape -i cat.nrrd "+w_shape+" | unu save -f text -o "+output+".txt")

# make program
def makeProgram(p_out, output, target, init_name):
    
    s0 = "cp "+init_name+"_init.c "+target+"_init.c"
    s1 = "cp observ.diderot "+target+".diderot"
    s2 = "cp fem/Makefile Makefile"
    s3 = "make clean"
    s4 = "make "+target+".o"
    s5 = "make "+target+"_init.o"
    s6 = "make "+target+"_init.so"
    
    
    s10 = "cp "+target+".diderot "+output+".diderot"
    es = [s0, s1, s2, s3, s4, s5, s6, s10]
    for i in es:
        os.system(i)

# read output of firedrake program



################################ write annd run test program ################################
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall):
    cleanup(output, p_out)
    target ="ex1"#+str(app.opr.id)
    # write new diderot program
    print "p_out:",p_out
    readDiderot(p_out, app, pos)

    (init_name, num_fields, exp_fields) = get_fieldinfo(app)
    # output type
    oty = app.oty
    shape = oty.shape
    dim = oty.dim
    #write python firedrake program
    writeFem(p_out, target,num_fields, dim, exp_fields)
    #run firedrake program and cvt to txt file
    makeProgram(p_out, output, target, init_name)

    # check if the program was executed
    if(os.path.exists(target+".o") and os.path.exists(target+"_init.so")):
        shape = app.oty.shape  
        useFem(p_out, shape, pos, output, target)
        print "pos:",pos
        if(os.path.exists(output+".txt")):
           return (1,1, startall)
        else:
           return (1, None, startall)
    else:
        # did not compile
        return (None,None, startall)