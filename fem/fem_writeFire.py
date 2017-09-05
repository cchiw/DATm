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

foo_femfields = "foo_femfield"
foo_femGen = "foo_femGen"



def translate_ty(field, exp_name, field_name):
    element = ty_toElement()
    k_order = ty_toK()
    fldty = field.fldty
    mesh  = ty_toMesh(field.fldty)
    foo = "\nmesh = "+mesh

    foo = foo+"\nV= FunctionSpace(mesh,\""+element+"\",degree="+k_order
    
    if(fty.is_ScalarField(fldty)):
        foo=foo+")"
    elif(fty.is_VectorField(fldty)):
        n = fty.get_vecLength(fldty)
        foo=foo+", dim = "+str(n)+")"
    foo = foo+"\n"+field_name+" = Function(V).interpolate(Expression("+exp_name+"))"
    return foo

def translate_coeff(a, xyz):
    if(a==0):
        return ""
    else:
        return "+("+str(a)+"*"+xyz+")"

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

#translate field expression to something written in firedrake program
def translate_exp(field):

    fldty = field.fldty
    dim = fldty.dim
    
    if(dim==1):
        raise Exception ("missing dim")
    elif(fldty.id == ty_scalarF_d2.id):
        coeffs= field.coeff
        ss="0"
        tE = translate_expSingle(coeffs)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        return "\""+ss+"\""
    elif(fldty.id == ty_scalarF_d3.id):
        [coeff0, coeff1, coeff2] = field.coeff
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
    elif(fldty.id == ty_vec2F_d2.id):
        [coeff0, coeff1] = field.coeff
        ss="0"
        tE = translate_expSingle(coeff0)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss0= "\""+ss+"\""

        tE = translate_expSingle(coeff1)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss1 = "\""+ss+"\""
        return "("+ss0+","+ss1+")"
    elif(fldty.id == ty_vec3F_d2.id):
        [coeff0, coeff1, coeff2] = field.coeff
        ss="0"
        tE = translate_expSingle(coeff0)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss0= "\""+ss+"\""
        
        tE = translate_expSingle(coeff1)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss1 = "\""+ss+"\""

        tE = translate_expSingle(coeff2)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss2 = "\""+ss+"\""
        return "("+ss0+","+ss1+","+ss2+")"

    elif(fldty.id == ty_mat2x2F_d2.id):
        [coeffA, coeffB] = field.coeff
                    
        [coeff0, coeff1] = coeffA
        ss="0"
        tE = translate_expSingle(coeff0)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss0A= "\""+ss+"\""

        tE = translate_expSingle(coeff1)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss1A = "\""+ss+"\""

        [coeff0, coeff1] = coeffB
        ss="0"
        tE = translate_expSingle(coeff0)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss0B= "\""+ss+"\""
        
        tE = translate_expSingle(coeff1)
        for (var_n, var_c) in tE:
            ss=ss+translate_coeff(var_n, var_c)
        ss1B = "\""+ss+"\""
        return "(("+ss0A+","+ss1A+")"+","+"("+ss0B+","+ss1B+"))"
    else:
        raise Exception ("not supported")


def get_exp(field, field_name):
    exp_name = "exp"+field_name
    foo = "\n"+exp_name+" = "+translate_exp(field)
    return  foo+translate_ty(field, exp_name, field_name)

# write fem
def writeFem(p_out, target, num_fields, dim, fields, initPyname,test_new,res):
    #read firedrake template
    template = "fem/fire.foo"
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
            for field in fields:
                field_name = "f"+str(i)
                names = names+field_name+", "
                foo = foo+ get_exp(field,  field_name)
                i +=1
            foo =foo+"\n"+initPyname+"(namenrrd, "+names+" target, res, stepSize ,limit)"
            f.write(foo.encode('utf8'))
            continue
        b0 = re.search(foo_femGen, line)
        if b0:
            if(test_new):
                foo = "\nres = "+str(res)+" \nstepSize = 1.0/res \nlimit = 5"
                f.write(foo.encode('utf8'))
            continue
        else:
            f.write(line)

    ftemplate.close()
    f.close()