# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re
import time

from nc_writeDiderot import nc_compileandRun, nc_setLength


# shared base programs
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_write import * 
from base_writeDiderot import *
from base_constants import *
template=c_template     # template

# define field  as tensors
def cfe_defineField(f, app):
    exps = apply.get_all_Fields(app)
    i=0
    foo = "\nreal x= 11.1;\nreal y= 22.2;\nreal z= 33.3;\n"
    f.write(foo)
    for exp in exps:
        if (field.get_isField(exp)):
            type = (exp.fldty)
            shape =(type.shape)
            #outLineTF(type,"0.0")
            print("\n exp-data:",str(exp.data))
            print("\n exp-cfe:",str(exp.cfes))
            foo="tensor "+str(shape)+" "+fieldName(i)+" = "+str(exp.data)+";\n\t"
            f.write(foo)
        else: #tensor type
            fieldShape(f, exp.fldty)
            foo= fieldName(i)+" = "+str(field.get_data(exp))+";\n"
            f.write(foo)
        i+=1

def  getField(app):
    exps = apply.get_all_Fields(app)
    flds = []
    i = 0
    f_vars = []
    for exp in exps:
        if (field.get_isField(exp)):
            f_vars+=[(fieldName(i),exp)]
        i+=1
    return f_vars

# last line to make cse
def cfe_makeCFE(f,app):
    fldty = app.oty
    dim =fldty.dim
    shape = fldty.shape
    f_str =""
    if(dim==1):
        f_str = "x"
    elif(dim==2):
        f_str = "x,y"
    elif(dim==3):
        f_str = "x,y,z"
    foo = "ofield#3("+str(dim)+")"+str(shape)+const_probeG_cfe+" = " + "cfexp(G,"+f_str+");\n"
    f.write(foo)

def  cfe_defineXYZ(f,dim):
    foo  = ""
    if(dim==1):
        foo =",pos"
    elif(dim==2):
        foo =",pos[0],pos[1]"
    elif(dim==3):
        foo =",pos[0], pos[1] , pos[2]"
    return foo

#witten inside update method
#conditionals are commented out
def cfe_update_method(f, pos, app):
    oty = app.oty
    if(fty.is_Field(oty)):
        # index field at random positions
        dim = oty.dim
        base_index_field_at_positions(f, pos, dim)
        XYZ = cfe_defineXYZ(f,dim)
        # check_inside(f, const_probeG_cfe, app,XYZ)
        foo = "\n\t\t out = inst("+const_probeG_cfe+XYZ+");"
        f.write(foo)
    else:
        # get conditional for tensor argument
        check_conditional(f,  foo_out, app)

################################ search Diderot template and replace foo variable name ################################
#itype: shape of fields
#otype: output tensor
#op1: unary operation involved
def cfe_readDiderot(p_out, app, pos):
    #read diderot template
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    f = open(p_out+".diderot", 'w+')
    
    #output type
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_in, line)
        if a0:
            #replace field input line
            cfe_defineField(f,app)
            # put each argument s
            continue
        # is it output tensor line?
        b0 = re.search(foo_outTen, line)
        if b0:
            #print "outline"
            outLine(f, app)
            continue
        # operation on field
        c0 = re.search(foo_op,line)
        if c0:
            #print "replace op"
            replaceOp(f, app)
            cfe_makeCFE(f,app)
            continue
        # index field at position
        d0 = re.search(foo_probe,line)
        if d0:
            #print "update_method"
            cfe_update_method(f, pos, app)
            continue
        # length number of positions
        e0=re.search(foo_length, line)
        if e0:
            #print "Set length"
            nc_setLength(f,len(pos))
            continue
        # nothing is being replaced
        else:
            f.write(line)

    ftemplate.close()
    f.close()

################################ write annd run main function ################################
# write, compile, and execute new diderot program
def cfe_writeDiderot(p_out, app, pos, output, runtimepath, isNrrd, startall):
    print ("mark A")
    # write new diderot program
    cfe_readDiderot(p_out, app, pos)
    endall = time.time()
    tall = str(endall - startall)
    writeTime(24, tall)
    startall=endall
    shape = app.oty.shape
    return nc_compileandRun(p_out, shape, pos, output, runtimepath, isNrrd, startall)