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

from nc_writeDiderot import nc_compileandRun, nc_setLength

from fem_helper import *


#strings in diderot template
foo_in = "foo_in"
foo_outTen = "foo_outTen"
foo_op = "foo_op"
foo_probe = "foo_probe"
foo_length ="foo_length"
foo_limits = "foo_limits"
foo_posIn = "foo_posIn"
foo_posLast = "foo_posLast"

#otherwise variables in diderot program
foo_out = "out"
foo_pos = "pos"
const_out = "7.2"
pde_test = true 


####### FIXME: need to create fem-inside/conditional
##################################### input tensor/field #####################################
# create space for field
def ty_toSpace(V, fldty):
    dim =  fldty.dim
    element = ty_toElement()
    k_order = ty_toK()
    mesh = ty_toMesh(fldty)
    return "\n fnspace "+V+" = FunctionSpace("+ mesh+", "+element+"(), "+k_order +");"



def fem_fieldShape(f, fldty):
    #print "fldty: ",fldty
    pde_test = true
    foo = fty.toDiderot(fldty,pde_test)
    f.write(foo.encode('utf8'))


#field input line
#f: file to write to
#k:continuity
#itypes: types for input field
#inputlist: name for input data
def fem_inShape(f, appC):
    exps = apply.get_all_Fields(appC)
    #app = apply.get_root_app(appC)
    i=0
    for exp in exps:
        #print "current fld",field.toStr(exp)
        dim = field.get_dim(exp)
        if (field.get_isField(exp)):
            fi = fieldName(i)
            F = "F"+fi
            path = "path"+fi
            V = "V"+fi
            
            foo = "\n input "+fty.toFemDiderot(exp.fldty)+ " "+F+";"
            foo = foo+ "\n //"+field.toStr(exp)
            foo = foo+ty_toSpace(V, exp.fldty)
            foo = foo+"\n string "+path+" = \"fnspace_data/\";"
            #+exp.inputfile+"\";"
            foo = foo+"\n "+fty.toOFieldDiderot(exp.fldty)+" "+fi+" = convert("+F+","+V+","+ path+");\n"
            f.write(foo.encode('utf8'))
        else: #tensor type
            fem_fieldShape(f, exp.fldty)
            foo= fieldName(i)+" = "+str(field.get_data(exp))+";\n"
            f.write(foo.encode('utf8'))
        i+=1

################################################################
################################################################
# for new tests. sample whole field
def posIn(f, dim):
    foo = "strand f("
    if(dim==2):
        foo = foo+ "int i, int j"
    elif(dim==3):
        foo = foo+"int i, int j, int k "
    foo =foo+"){"
    f.write(foo.encode('utf8'))


def posLast(f, dim):
    if(dim==2):
        foo = "initially [ f(i, j) | i in 0..res-1, j in 0..res-1];"
        f.write(foo.encode('utf8'))
    elif(dim==3):
        foo = "initially [ f(i, j, k) | i in 0..res-1, j in 0..res-1, k in 0..res-1]; "
        f.write(foo.encode('utf8'))

def posIn(f, dim):
    foo = "strand f("
    if(dim==2):
        foo = foo+ "int i, int j"
    elif(dim==3):
        foo = foo+"int i, int j, int k "
    foo =foo+"){"
    f.write(foo.encode('utf8'))

def fem_limits(f, dim):
    foo = "\n"
    if(dim==2):
        foo = "tensor [2] pos = [i,j]*stepSize;"
    elif(dim==3):
        foo = "tensor [3] pos = [i,j,k]*stepSize;"
    foo =foo+ "\n\t\t tensor [] current = inst(G,pos);"
    foo = foo+"\n\t\t if(current > limit){out= 1;}"
    foo = foo+"\n\t\t else{out= 0;}"
    f.write(foo.encode('utf8'))

################################################################
#witten inside update method
#conditionals are commented out
def cte_update_method(f, pos, app):
    oty = app.oty
    if(fty.is_Field(oty)):
        dim = oty.dim
        base_index_field_at_positions(f, pos, dim)
        check_inside(f, opfieldname1, app, pde_test)
    #foo= "\n\t\tout = inst(G,pos);"
    #f.write(foo.encode('utf8'))
    else:
        check_conditional(f,  foo_out, app)
################################ search Diderot template and replace foo variable name ################################
#itype: shape of fields
#otype: output tensor
#op1: unary operation involved
def readDiderot(p_out, app, pos, template):
    #read diderot template
    # FIXME hardcode different fem limit here
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    f = open(p_out+".diderot", 'w+')
    oty = app.oty
    dim = oty.dim

    #output type
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_in, line)
        if a0:
            #replace field input line
            fem_inShape(f,app)
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
            
            continue
        # index field at position
        d0 = re.search(foo_probe,line)
        if d0:
            #print "update_method"
            cte_update_method(f, pos, app)
            continue
        # length number of positions
        e0 = re.search(foo_length, line)
        if e0:
            #print "Set length"
            nc_setLength(f,len(pos))
            continue
        f0 = re.search(foo_limits, line)
        if f0:
            fem_limits(f,dim)
            continue
        # nothing is being replaced
        g0 = re.search(foo_posIn, line)
        if g0:
            posIn(f, dim)
            continue
        
        g0 = re.search(foo_posLast, line)
        if g0:
            posLast(f, dim)
            continue

        else:
            f.write(line)

    ftemplate.close()
    f.close()
    #print "sptting out to:",p_out+".diderot"
