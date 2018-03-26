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
from fem_writeFire import writeFem

#core_fields: apply get all fields+space conversion
def get_fieldinfo(app,core_fields):
    init_name = "fem/"
    num_fields = 0
    n = len(core_fields)
    exp_fields = []
    tags = ""
    for e in (core_fields[::-1]):
        if(fty.is_Field(e.fldty)):
            tags = "f"+tags
            num_fields +=1
            exp_fields.append(e)
        elif(num_fields>0):
            tags= "t"+tags
    init_name =init_name +tags
    return (init_name, num_fields,exp_fields)


# create firedrake field
def useFem(p_out, shape, pos, output, target,dim, res, startall):
    os.system("python "+p_out+".py")
    endall = time.time()
    tall = str(endall - startall)
    writeTime("run python program", tall)
    startall=endall
    
    s13 = "cp "+p_out+".py" +output+".py"
    es = [s13]
    for i in es:
        os.system(i)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("copy python program", tall)
    startall=endall
    # convert to txt file
    product = 1
    for x in shape:
        product *= x
    m2 = len(pos)+1
    w_shape=" -s "+str(product)+" "+str(m2)
    os.system("unu reshape -i cat.nrrd "+w_shape+" | unu save -f text -o "+output+".txt")
    endall = time.time()
    tall = str(endall - startall)
    writeTime("cvt output", tall)


# make program
def makeProgram(p_out, output, target, init_name, startall):
    s0 = "cp "+init_name+"_init.c "+target+"_init.c"
    s1 = "cp observ.diderot "+target+".diderot"
    s2 = "cp fem/Makefile Makefile"
    s3 = "make clean"
    es = [s0, s1, s2, s3]
    for i in es:
        os.system(i)
        print (i)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("set up diderot programs", tall)
    startall=endall
    es = [".o", "_init.so"]
    for i in es:
        exp  = "make "+target+i
        os.system(exp)
        print(exp)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("make diderot program", tall)
    startall=endall
    es = [".diderot",".cxx","_init.c"]
    for i in es:
        exp = "cp "+target+i+" "+output+i
        os.system(exp)
        print(exp)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("copy relalated program", tall)
    startall=endall       
    # read output of firedrake program

################################ write annd run test program ################################
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall, core_fields):
    
    test_new  = False
    template = c_template
    shape = app.oty.shape
    res = 10
    target ="ex1"
    # write new diderot program
    readDiderot(p_out, app, pos,template,core_fields)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("read diderot", tall)
    startall=endall
    (init_name, num_fields, fields) = get_fieldinfo(app, core_fields)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("get field info", tall)
    startall=endall
    # output type
    oty = app.oty
    shape = oty.shape
    dim = oty.dim
    #write python firedrake program
    initPyname = "init"+str(num_fields)
    writeFem(p_out, target, num_fields, dim, fields, initPyname,res)
    endall = time.time()
    tall = str(endall - startall)
    writeTime("write fem", tall)
    startall=endall
    #run firedrake program and cvt to txt file
    makeProgram(p_out, output, target, init_name, startall)
    startall = time.time()
    # if we need to make k file first
    # check if the program was executed
    if(os.path.exists(target+".o") and os.path.exists(target+"_init.so")):
        useFem(p_out, shape, pos, output, target,dim, res, startall)
        if(os.path.exists(output+".txt")):
           return (1,1, startall)
        else:
           return (1, None, startall)
    else:
        # did not compile
        writeTime("hold", "0")
        writeTime("hold", "0")
        writeTime("hold", "0")
        return (None,None, startall)
