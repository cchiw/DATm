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
# cte operators
# possibly moved to another directory
from cte_eval import unary, binary

def handle(app):
    arity = app.opr.arity
    if (arity ==1):
        return unary(app)
    elif (arity ==2):
        return binary(app)
    else:
        raise Exception ("arity is not supported: ")


def simple_apply(c_exp, line):
    opr = line.opr
    oty = line.var.ty
    fldty = line.lhs.ty
    # create a field with data
    fld_tmp = field(true, "tmp", fldty, "", c_exp, "")
    #create new apply
    app = line.convertToAppWField(line, "tmp", fld_tmp)
    return (oty, handle(app))


def prog_eval(program, positions):
    lines = program.lines
    line1 = lines[0]
    app = line.convertToApp(line1, "firstline")
    return handle(app)