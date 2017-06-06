import sympy
from sympy import *
#symbols
x,y,z =symbols('x y z')
import sys
import re
import math

# shared base programs
from obj_ty import *
from obj_apply import *
from obj_operator import *
from obj_field import *
from obj_prog import *

#specific nc programs
from nc_eval import unary, binary, probeField


def handle(app):
    print "**************** handle"+app.opr.name
    arity = app.opr.arity
    if (arity ==1):
        #print "lhs:",app.lhs.data
        return unary(app)
    elif (arity ==2):
        return binary(app)
    else:
        raise Exception ("arity is not supported: ")



def handle2(app, positions, dim):
    print "**************** handle"+app.opr.name
    if (app.opr.id == op_probe.id):
        ty = app.oty
        oty = fty(ty.id, ty.name, dim, ty.shape, ty.tensorType, ty.k)
        #print "oty", oty.name
        #rtn = probeField(oty, positions, lastexp)
        #print "rtn about to probe field"
        exp = field.get_data(app.lhs)
        rtn = probeField(oty, positions, exp)
        #print "rtn from probe", rtn
        return rtn
    else:
        arity = app.opr.arity
        if (arity ==1):
            #print "lhs:",app.lhs.data
            return unary(app)
        elif (arity ==2):
            return binary(app)
        else:
            raise Exception ("arity is not supported: ")


def mk_field(linet, dict, rtn_exp):
    rtn_var = linet.var
    fldty = rtn_var.ty
    fldname = rtn_var.name
    # create a field with data
    fld_tmp = field(true, "tmp", fldty, "", rtn_exp, "")
    # place field in dictionary
    dict[fldname] = fld_tmp
    return dict


def simple_apply(linet, dict):
    # look up variable argument in dictionary

    rhs = None
 
    lhs = dict[linet.lhs.name]
    if(linet.rhs):
        rhs = dict[linet.rhs.name]
    # convert line to app
    #print "lhs",lhs
    #print "rhs", rhs
    app = line.convertToAppWField(linet, "tmp", lhs, rhs)
    #print "app", app
    return  app


def prog_eval(program, positions, dict):
    lines = program.lines1
    line0 = lines[0]

    app = simple_apply(line0, dict)
    exp = handle(app)
    lastexp = exp
    # next line
    prev = line0
    next = prev
    for i in range(len(lines)-1):
        # next line
        #print "***************** on current line", i
        dict = mk_field(prev, dict, exp)
        next = lines[i+1]
        prev = next
        app = simple_apply(next, dict)
        lastexp = exp
        exp = handle(app)
        #print "rtn exp", exp
        
    #print "post initial for loop"
    lines2 = program.lines2
    #print "post second line 2 ", lines2
    if(len(lines2)==0):
        print "nothing in lines2"
        # last step
        oty = app.oty
        #rtn = probeField(oty, positions, lastexp)
        #print "rtn about to probe field"
        rtn = probeField(oty, positions, exp) #evaluate expression at positions
        #print "rtn last", rtn
        return rtn
    for i in range(len(lines2)):
        # next line
        print "***************** on current lines2 line ", i
        dict = mk_field(prev, dict, exp)
        next = lines2[i]
        prev = next
        app = simple_apply(next, dict)
        lastexp = exp
        exp = handle2(app, positions, program.dim)
    #print "rtn exp", exp
    return exp