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
from obj_space import *
from base_write import * 
from base_writeDiderot import *
from base_constants import *

from nc_writeDiderot import nc_compileandRun, nc_setLength





#otherwise variables in diderot program
pde_test = true 
pde_Inside = c_pde_Inside

####### FIXME: need to create fem-inside/conditional
##################################### input tensor/field #####################################
# create space for field
def fem_fieldShape(f, fldty):
    #print "fldty: ",fldty
    pde_test = true
    foo = fty.toDiderot(fldty,pde_test)
    f.write(foo)


#field input line
#f: file to write to
#k:continuity
#itypes: types for input field
#inputlist: name for input data
def fem_inShape(f, core_fields):
    i=0
    for exp in core_fields:
        #print "current fld",field.toStr(exp)
        dim = field.get_dim(exp)
        if (field.get_isField(exp)):
            fi = fieldName(i)
            F = "F"+fi
            path = "path"+fi
            V = "V"+fi
            
            foo = "\n input "+fty.toFemDiderot(exp.fldty,sub=(-1))+ " "+F+";"
            foo = foo+ "\n //"+field.toStr(exp)
            fnspace = space.ty_toSpace_forDiderot(exp.fldty.space)
            foo = foo+"\n fnspace "+V+" = "+fnspace +";"
    
            foo = foo+"\n string "+path+" = \"fnspace_data/\";"
            #+exp.inputfile+"\";"
            foo = foo+"\n "+fty.toOFieldDiderot(exp.fldty,sub=(-1))+" "+fi+"0"+" = FEM("+F+","+V+","+ path+");\n"
            FF = exp.operator.replace("F",fi+"0")
            #foo = foo+"\n "+fty.toOFieldDiderot(exp.fldty,sub=(+2))+" "+fi+" = " + FF +";\n"
            foo = foo+"\n "+fty.toOFieldDiderot(exp.fldty)+" "+fi+" = " + FF +";\n"
            f.write(foo)
        else: #tensor type
            fem_fieldShape(f, exp.fldty)
            foo= fieldName(i)+" = "+str(field.get_data(exp))+";\n"
            f.write(foo)
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
    f.write(foo)


def posLast(f, dim):
    if(dim==2):
        foo = "initially [ f(i, j) | i in 0..res-1, j in 0..res-1];"
        f.write(foo)
    elif(dim==3):
        foo = "initially [ f(i, j, k) | i in 0..res-1, j in 0..res-1, k in 0..res-1]; "
        f.write(foo)

def posIn(f, dim):
    foo = "strand f("
    if(dim==2):
        foo = foo+ "int i, int j"
    elif(dim==3):
        foo = foo+"int i, int j, int k "
    foo =foo+"){"
    f.write(foo)

def fem_limits(f, dim,application): # look at base_writeDierot at 270 and getCond -> hand it set -> frame 
    foo = "\n"
    if(dim==2):
        foo = "tensor [2] pos = [i,j]*stepSize;"
    elif(dim==3):
        foo = "tensor [3] pos = [i,j,k]*stepSize;"
    foo =foo+ "\n\t\t tensor [] current = G(pos);"
    #foo = foo + "\n\t\tofield#3(2)[2,2] a = ∇⊗∇F00;\n\t\t print((a,pos),current);"
    foo = foo+"\n\t\t if(current > limit){out= 1;}"
    foo = foo+"\n\t\t else{out= 0;}"
    f.write(foo)

################################################################
#witten inside update method
#conditionals are commented out
def cte_update_method(f, pos, app):
    oty = app.oty
    if(fty.is_Field(oty)):
        dim = oty.dim
        base_index_field_at_positions(f, pos, dim)
        # check if position is inside
        if(c_pde_Inside):
            check_inside(f, opfieldname1, app, pde_test)
        else:
            foo= "\n\t\tout = G(pos);"
            f.write(foo)
    else:
        check_conditional(f,  foo_out, app)
################################ search Diderot template and replace foo variable name ################################
#itype: shape of fields
#otype: output tensor
#op1: unary operation involved
from sympy import diff
import sympy as sp
def readDiderot(p_out, app, pos, template,core_fields):
    #read diderot template
    # FIXME hardcode different fem limit here
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    f = open(p_out+".diderot", 'w+')
    oty = app.oty
    dim = oty.dim
    basis = "\ntensor[2] e1 = [1,0];\ntensor[2] e2 = [0,1];" if dim==2 else "\ntensor[3] e1 = [1,0,0];\ntensor[3] e2 = [0,1,0];\ntensor[3] e3 = [0,0,1];\n"

    #output type
    for line in ftemplate:
        # is it initial field line?
        z0 = re.search(foo_basis,line)
        if z0:
            f.write(basis)
            continue
        
        a0 = re.search(foo_in, line)
        if a0:
            #replace field input line
            fem_inShape(f,core_fields)
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
            fem_limits(f,dim,0)
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
