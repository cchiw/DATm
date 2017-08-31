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


def get_fieldinfo(app):
    exps = apply.get_all_Fields(app)
    print "exps:",exps
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
    print "init_name:",init_name,
    print "num_fields:", num_fields
    return (init_name, num_fields, exp_fields)

def translate_ty(dim, exp_name, field_name):
    element = ty_toElement()
    k_order = ty_toK()
    mesh  = ty_toMesh(dim)
    foo = "\nmesh = "+mesh
    foo = foo+"\nV= FunctionSpace(mesh,\""+element+"\",degree="+k_order+")"
    foo = foo+"\n"+field_name+" = Function(V).interpolate(Expression("+exp_name+"))"
    return foo

def translate_exp(exp):
    return "\"x[0]\""

def get_exp_set(dim, field_name, exp):
    exp_name = "exp"+field_name
    foo = "\n"+exp_name+" = " +translate_exp(exp)
    return  foo+ translate_ty(dim, exp_name,field_name)

def get_exp(dim, field_name):
    exp_name = "exp"+field_name
    foo = "\n"+exp_name+" = \"x[0]\""
    return  foo+ translate_ty(dim, exp_name,field_name)

def write_fldExp(num_fields, exp_fields):

    foo = "\nname = \"cat\""
    foo = foo+"\ntarget =\"ex1\""
    foo = foo+"\nnamenrrd = name+'.nrrd'"
#    i = 0
#    names = ""
#    for exp in exp_fields:
#        name = "f"+str(i)
#        foo=foo+get_exp_set(dim, name, exp)
#        i=i+1
#        names = names+name+","
#
#    foo = foo+"\ninit"+str(num_fields)+"(namenrrd, "+names+" target)"
#    return foo 

    if(num_fields==1):
        foo = foo+ get_exp(dim, "f")
        foo = foo+"\ninit1(namenrrd, f,target)"
    elif(num_fields==2):
        foo = foo+ get_exp(dim, "f")+get_exp(dim, "g")
        foo =foo+"\ninit2(namenrrd, f, g,target)"
    elif(num_fields==3):
        foo = foo+ get_exp(dim, "f")+get_exp(dim, "g")+get_exp(dim, "h")
        foo =foo+"\ninit3(namenrrd, f, g,h,target)"
    elif(num_fields==4):
        foo = foo+ get_exp(dim, "f")+get_exp(dim, "g")+get_exp(dim, "h")+get_exp(dim, "i")
        foo =foo+"\ninit4(namenrrd, f, g, h, i, target)"
    elif(num_fields==5):
        foo = foo+ get_exp(dim, "f")+get_exp(dim, "g")+get_exp(dim, "h")+get_exp(dim, "i")+get_exp(dim, "j")
        foo =foo+"\ninit5(namenrrd, f, g, h, i, j, target)"
    elif(num_fields==6):
        foo = foo+ get_exp(dim, "f")+get_exp(dim, "g")+get_exp(dim, "h")+get_exp(dim, "i")+get_exp(dim, "j")+get_exp(dim, "k")
        foo =foo+"\ninit5(namenrrd, f, g, h, i, j, k, target)"
    return foo


# write fem
def writeFem(p_out, target, num_fields, dim, exp_fields):
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
            foo = write_fldExp(num_fields, exp_fields)
            f.write(foo.encode('utf8'))
            continue
        else:
            f.write(line)

    ftemplate.close()
    f.close()
    print p_out+".py"
    #raise Exception ("stop here")
