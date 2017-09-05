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
    os.system("rm "+output+"*")
    os.system("rm cat.nrrd")
    os.system("rm  "+p_out+".nrrd")
    os.system("rm  "+output+".txt")
    os.system("rm  "+p_out+".txt")


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
#    elif(fldty.id == ty_mat3x3F_d3.id):
#        [coeffA, coeffB, coeffC] = field.coeff
#        [coeff0, coeff1, coeff2] = coeffA
#        ss="0"
#        tE = translate_expSingle(coeff0)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss0A= "\""+ss+"\""
#        
#        tE = translate_expSingle(coeff1)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss1A = "\""+ss+"\""
#    
#        tE = translate_expSingle(coeff2)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss2A = "\""+ss+"\""
#        [coeff0, coeff1, coeff2] = coeffB
#        ss="0"
#        tE = translate_expSingle(coeff0)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss0B= "\""+ss+"\""
#        
#        tE = translate_expSingle(coeff1)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss1B = "\""+ss+"\""
#
#        tE = translate_expSingle(coeff2)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss2B = "\""+ss+"\""
#        [coeff0, coeff1, coeff2] = coeffC
#        ss="0"
#        tE = translate_expSingle(coeff0)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss0C= "\""+ss+"\""
#        
#        tE = translate_expSingle(coeff1)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss1C = "\""+ss+"\""
#        
#        tE = translate_expSingle(coeff2)
#        for (var_n, var_c) in tE:
#            ss=ss+translate_coeff(var_n, var_c)
#        ss2C = "\""+ss+"\""
#        return "(("+ss0A+","+ss1A+","+ss2A+"),("+ss0B+","+ss1B+","+ss2B+"),("+ss0C+","+ss1C+","+ss2C+"))"
    else:
        raise Exception ("not supported")


def get_exp(field, field_name):
    exp_name = "exp"+field_name
    foo = "\n"+exp_name+" = "+translate_exp(field)
    return  foo+translate_ty(field, exp_name, field_name)

# write fem
def writeFem(p_out, target, num_fields, dim, fields):
    #read diderot template
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    f = open(p_out+".py", 'w+')
    lbl = str(num_fields)+"_d"+str(dim)
    #output type
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_femexp, line)
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
            foo =foo+"\ninit"+str(num_fields)+"(namenrrd, "+names+" target)"
            f.write(foo.encode('utf8'))
            continue
        else:
            f.write(line)

    ftemplate.close()
    f.close()
    #print p_out+".py"
    #raise Exception ("stop here")

#if(num_fields==1):
#connect1("cat", "x[0]",target)
#os.system("python fem/sd2.py")
#elif(num_fields==2):
#connect2("cat", "x[0]", "x[0]", target)
#os.system("python fem/sd2_two.py")

# create firedrake field
def useFem(p_out, shape, pos, output, target):
    
    os.system("python "+p_out+".py")
    s13 = "cp "+p_out+".py" +output+".py"
    es = [s13]
    for i in es:
        os.system(i)
    
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
def writeTestPrograms(p_out, app, pos, output, runtimepath, isNrrd, startall):
    cleanup(output, p_out)
    target ="ex1"

    # write new diderot program
    readDiderot(p_out, app, pos)

    (init_name, num_fields, fields) = get_fieldinfo(app)
    # output type
    oty = app.oty
    shape = oty.shape
    dim = oty.dim
    #write python firedrake program
    writeFem(p_out, target, num_fields, dim, fields)
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