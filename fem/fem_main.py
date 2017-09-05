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


def get_fieldinfo(app):
    exps = apply.get_all_Fields(app)
    #print "exps:",exps
    #name of init file
    init_name = "fem/"
    num_fields = 0
    n = len(exps)
    exp_fields = []
    for e in (exps[:n-1]):
        if(fty.is_Field(e.fldty)):
            init_name = init_name+"f"
            num_fields +=1
            exp_fields.append(e)
        else:
            init_name =init_name+"t"
    last = exps[n-1]
    if(fty.is_Field(last.fldty)):
        init_name = init_name+"f"
        num_fields +=1
        exp_fields.append(last)
    #print "init_name:",init_name,
    #print "num_fields:", num_fields
    return (init_name, num_fields,exp_fields)


# create firedrake field
def useFem(p_out, shape, pos, output, target,dim, res, test_new):
    
    os.system("python "+p_out+".py")
    s13 = "cp "+p_out+".py" +output+".py"
    es = [s13]
    for i in es:
        os.system(i)
    
    # convert to txt file
    product = 1
    for x in shape:
        product *= x
    m2 = 0
    if(test_new):
        if(dim==2):
            m2 = res*res
        elif(dim==3):
            m2 = res*res*res
    else:
        m2 = len(pos)+1

    w_shape=" -s "+str(product)+" "+str(m2)
    print "w-shape:",w_shape
    os.system("unu reshape -i cat.nrrd "+w_shape+" | unu save -f text -o "+output+".txt")
    #raise Exception ("stop")
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
    s11 = "cp "+target+".cxx "+output+".cxx"
    s12 = "cp "+target+"_init.c "+output+"_init.c"
    
    print "init_name:", init_name
    #print "target:", target
    
    es = [s0, s1, s2, s3, s4, s5, s6,s10, s11, s12]
    for i in es:
        os.system(i)
    es = [s10, s11, s12]
    for i in es:
        os.system(i)
# read output of firedrake program



################################ write annd run test program ################################
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall, test_new):
    template = c_template     # default/main template
    # note here(creating different program)
    if(test_new):
        template =  "shared/template/foo_limit.ddro"
            
    res = 10
    target ="ex1"

    # write new diderot program
    readDiderot(p_out, app, pos,template)

    (init_name, num_fields, fields) = get_fieldinfo(app)
    # output type
    oty = app.oty
    shape = oty.shape
    dim = oty.dim
    #write python firedrake program
    initPyname = "init"+str(num_fields)
    if(test_new):
        initPyname = initPyname+"Sample"
        init_name = init_name+"Sample"
    writeFem(p_out, target, num_fields, dim, fields, initPyname,test_new,res)
    #run firedrake program and cvt to txt file
    makeProgram(p_out, output, target, init_name)

    # check if the program was executed
    if(os.path.exists(target+".o") and os.path.exists(target+"_init.so")):
        shape = app.oty.shape
  
        useFem(p_out, shape, pos, output, target,dim, res, test_new)
        print "pos:",pos
        if(os.path.exists(output+".txt")):
           return (1,1, startall)
        else:
           return (1, None, startall)
    else:
        # did not compile
        return (None,None, startall)