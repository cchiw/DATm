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


from input import  s_field


def mkstatment(f, ty, lhs, rhs):
    foo = ty+lhs+" = " + rhs+";\n"
    f.write(foo)

# sets tmp variables for F0,F1,,.. placeholders
def cfe_defineField(f,args, app, dim):
    i=0
    for arg in args:
        lhs = fieldName(i)
        type =arg.fldty
        outTensor(f, lhs, type)
        i+=1
#Make CFE wrapper
def cfe_makeCFE(f,args,fldty,lhs,G):
    FLDNames = ""
    i=0
    for arg in args:
        FLDNames += ","+fieldName(i)
        i+=1
    exp = "cfexp("+G+FLDNames+")"
    ty = "field#"+str(fldty.k)+"("+str(dim)+")"+str(fldty.shape)
    mkstatment(f, ty, lhs, exp)

#witten inside update method
#conditionals are commented out
def cfe_update_method(f, args, pos, app):
    oty = app.oty
    if(fty.is_Field(oty)):
        dim = oty.dim
        # index field at random positions
        base_index_field_at_positions(f, pos, dim)
        foo  = ""
        if(dim==1):
            foo ="\n\t\treal x = pos;\n"
        elif(dim==2):
            foo ="\n\t\treal x  = pos[0]; \n\t\t real y = pos[1];\n"
        elif(dim==3):
            foo ="\n\t\treal x  = pos[0]; \n\t\t real y = pos[1]; \n\t\t real z = pos[2]\n"
        f.write(foo)
        FLDNames = ""
        i=0
        for arg in args:
            lhs = fieldName(i)+"T"
            FLDNames += ","+lhs
            rhs = str(arg.data)
            fldty = arg.fldty
            ty = "tensor "+str(fldty.shape)
            mkstatment(f, ty,lhs, rhs)
            i+=1
        foo = "\n\t\t out = inst("+const_probeG_cfe+FLDNames+");"
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
    oty = app.oty
    dim = oty.dim
    args = apply.get_all_Fields(app)
    #output type
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_in, line)
        if a0:
            #replace field input line
            cfe_defineField(f,args, app, dim)
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
            cfe_makeCFE(f,args,oty,const_probeG_cfe,const_probeG_conv)
            continue
        # index field at position
        d0 = re.search(foo_probe,line)
        if d0:
            #print "update_method"
            cfe_update_method(f, args, pos, app)
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