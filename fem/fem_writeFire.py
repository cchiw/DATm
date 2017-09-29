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

# fem specific programs
from fem_writeDiderot import readDiderot
from fem_helper import *

foo_femfields = "foo_femfield"
foo_femGen = "foo_femGen"



def translate_ty(field, exp_name, field_name):
    fldty = field.fldty
    fspace = fldty.space
    fnspace = space.ty_fnSpace_forFire(fspace)
    foo = "\nV= "+fnspace 
    foo = foo+"\n"+field_name+" = Function(V).interpolate(Expression("+exp_name+"))"
    k = fspace.k_order
    if(k>5):
        namedata = ""+space.ty_Json(fspace,fldty.dim) #name of json file
        foo = foo+"\nmakejson(V, \""+namedata+"\")"
    return foo

def translate_coeff(a, xyz):
    if(a==0):
        return ""
    else:
        return "+("+str(a)+"*"+xyz+")"
#######################################################################
#translate coeffs to firedrake expression
def translate_expSingle(coeffs):
    [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p] = coeffs
    x="x[0]"
    y="x[1]"
    
    yy = y+"*"+y
    yyy = yy+"*"+y
    xy = x+"*"+y
    xyy = yy+"*"+x
    xyyy = yyy+"*"+x
    xx = x+"*"+x
    xxy = xx+"*"+y
    xxyy = xx+"*"+yy
    xxyyy = xx+"*"+yyy
    xxx = xx+"*"+x
    xxxy = xxx+"*"+y
    xxxyy = xxx+"*"+yy
    xxxyyy = xxx+"*"+yyy
    
    #tA = a + b*y + c*x*y+ d*x;
    tA = [(a,"1"), (b,y), (c,xy), (d,x)]
    #tB = ((e+f*x+g*(x*x))*y*y) + (h*(x*x)*y);
    tB =  [(e,yy), (f,xyy), (g,xxyy), (h,xxy)]
    #tC = i*(x*x) + (j+k*x+l*(x*x))*y*y*y;
    tC =  [(i,xx), (j,yyy), (k,xyyy), (l,xxyyy)]
    #tD = (x*x*x)*((m*y*y*y)+(n*y*y)+(o*y)+p);
    tD =  [(m,xxxyyy), (n,xxxyy), (o,xxxy), (p,xxx)]
    return tA+ tB+ tC+ tD

#######################################################################
def get_CoeffExp_d2(coeff):
    ss="0"
    tE = translate_expSingle(coeff)
    for (var_n, var_c) in tE:
        ss=ss+translate_coeff(var_n, var_c)
    return "\""+ss+"\""

def cvtVector_d2(coeffs):
    ss0 = "("+get_CoeffExp_d2(coeffs[0])
    last = coeffs[1:]
    for c in last:
        ss0 = ss0+","+get_CoeffExp_d2(c)
    return ss0+")"

def get_CoeffExp_d3(coeffs):
    [coeff0, coeff1, coeff2] = coeffs
    ss="0"
    tE = translate_expSingle(coeff0)
    for (var_n, var_c) in tE:
        ss=ss+translate_coeff(var_n, var_c)
    tE = translate_expSingle(coeff1)
    z="x[2]"
    for (var_n, var_c) in tE:
        ss=ss+translate_coeff(var_n, var_c+"*"+z)
    tE = translate_expSingle(coeff2)
    zz = z+"*"+z
    for (var_n, var_c) in tE:
        ss=ss+translate_coeff(var_n, var_c+"*"+zz)
    return "\""+ss+"\""

def cvtVector_d3(coeffs):
    ss0 = "("+get_CoeffExp_d3(coeffs[0])
    last = coeffs[1:]
    for c in last:
        ss0 = ss0+","+get_CoeffExp_d3(c)
    return ss0+")"
#######################################################################

#translate field expression to something written in firedrake program
def translate_exp(field):
    fldty = field.fldty
    dim = fldty.dim
    coeffs = field.coeff
    #print "coeffs", len(coeffs)
    if(dim==1):
        raise Exception ("missing dim")
    elif(fldty.id == ty_scalarF_d2.id):
        return get_CoeffExp_d2(coeffs)
    elif(fldty.id == ty_scalarF_d3.id):
        return  get_CoeffExp_d3(coeffs)
    elif(fty.is_Vector(fldty)):
        if(dim==2):
            return cvtVector_d2(coeffs)
        elif(dim==3):
            return cvtVector_d3(coeffs)
    elif(fldty.id == ty_mat2x2F_d2.id):
        # Need to check when matrix field is implemented
        [coeffA, coeffB] = coeffs
        [coeff0, coeff1] = coeffA
        ss0A= get_CoeffExp_d2(coeff0)
        ss1A = get_CoeffExp_d2(coeff1)
        [coeff0, coeff1] = coeffB
        ss0B = get_CoeffExp_d2(coeff0)
        ss1B =get_CoeffExp_d2(coeff1)
        return "(("+ss0A+","+ss1A+")"+","+"("+ss0B+","+ss1B+"))"
    elif(fldty.id == ty_mat3x3F_d2.id):
        # Need to check when matrix field is implemented
        [coeffA, coeffB, coeffC] = coeffs
        [coeff0, coeff1, coeff2] = coeffA
        ss0A= get_CoeffExp_d2(coeff0)
        ss1A = get_CoeffExp_d2(coeff1)
        ss2A = get_CoeffExp_d2(coeff2)
        [coeff0, coeff1, coeff2] = coeffB
        ss0B = get_CoeffExp_d2(coeff0)
        ss1B = get_CoeffExp_d2(coeff1)
        ss2B = get_CoeffExp_d2(coeff2)
        [coeff0, coeff1, coeff2] = coeffC
        ss0C = get_CoeffExp_d2(coeff0)
        ss1C = get_CoeffExp_d2(coeff1)
        ss2C = get_CoeffExp_d2(coeff2)
        return "(("+ss0A+","+ss1A+","+ss2A+")"+","+"("+ss0B+","+ss1B+","+ss2B+")"+","+"("+ss0C+","+ss1C+","+ss2C+"))"
        #return "(("+ss0A+","+ss0B+","+ss0C+")"+","+"("+ss0A+","+ss1B+","+ss1C+")"+","+"("+ss2A+","+ss2B+","+ss2C+"))"
    elif(fldty.id == ty_mat2x2F_d3.id):
        # works
        # Need to check when matrix field is implemented
        [coeffA, coeffB] = coeffs
        [coeff0, coeff1] = coeffA
        ss0A= get_CoeffExp_d3(coeff0)
        ss1A = get_CoeffExp_d3(coeff1)
        [coeff0, coeff1] = coeffB
        ss0B = get_CoeffExp_d3(coeff0)
        ss1B =get_CoeffExp_d3(coeff1)
        return "(("+ss0A+","+ss1A+")"+","+"("+ss0B+","+ss1B+"))"
    elif(fldty.id == ty_mat3x3F_d3.id):
        # Need to check when matrix field is implemented
        [coeffA, coeffB, coeffC] = coeffs
        [coeff0, coeff1, coeff2] = coeffA
        ss0A = get_CoeffExp_d3(coeff0)
        ss1A = get_CoeffExp_d3(coeff1)
        ss2A = get_CoeffExp_d3(coeff2)
        [coeff0, coeff1, coeff2] = coeffB
        ss0B = get_CoeffExp_d3(coeff0)
        ss1B = get_CoeffExp_d3(coeff1)
        ss2B = get_CoeffExp_d3(coeff2)
        [coeff0, coeff1, coeff2] = coeffC
        ss0C = get_CoeffExp_d3(coeff0)
        ss1C = get_CoeffExp_d3(coeff1)
        ss2C = get_CoeffExp_d3(coeff2)
        return "(("+ss0A+","+ss1A+","+ss2A+")"+","+"("+ss0B+","+ss1B+","+ss2B+")"+","+"("+ss0C+","+ss1C+","+ss2C+"))"


    else:
        raise Exception ("not supported")

#######################################################################
def get_exp(field, field_name):
    exp_name = "exp"+field_name
    foo = "\n"+exp_name+" = "+translate_exp(field)
    return  foo+translate_ty(field, exp_name, field_name)

# write fem
def writeFem(p_out, target, num_fields, dim, fields, initPyname,test_new,res):
    #read firedrake template
    template = "fem/fire"+c_version+".foo"
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write firedrake program
    f = open(p_out+".py", 'w+')
    lbl = str(num_fields)+"_d"+str(dim)
    #output type
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_femfields, line)
        if a0:
            # should inline these pieces
            foo = "\nname = \"cat\""
            foo = foo+"\ntarget =\"ex1\""
            foo = foo+"\nnamenrrd = name+'.nrrd'"
            
            names = ""
            i = 0
            fields = fields[::-1]
            for field in fields:
                field_name = "f"+str(i)
                names = names+field_name+", "
                foo = foo+ get_exp(field,  field_name)
                i +=1
            if(test_new):
                foo =foo+"\n"+initPyname+"(namenrrd, "+names+" target, res, stepSize ,limit)"
            else:
                foo =foo+"\n"+initPyname+"(namenrrd, "+names+" target)"
            f.write(foo)
            continue
        b0 = re.search(foo_femGen, line)
        if b0:
            if(test_new):
                foo = "\nres = "+str(res)+" \nstepSize = 1.0/res \nlimit = 5"
                f.write(foo)
            continue
        else:
            f.write(line)

    ftemplate.close()
    f.close()
