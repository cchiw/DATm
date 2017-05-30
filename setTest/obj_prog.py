import sys
import re
import os
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *

#variable name and type
class varname:
    def __init__(self, name, ty, field):
        self.name = name
        self.ty = ty
        self.field = field 

# line of program
# var = operators (argument) where argument is (lhs,rhs))
class line:
    def __init__(self, var, opr, lhs, rhs):
        self.var = var
        self.opr = opr
        self.lhs = lhs
        self.rhs = rhs

    def convertToApp(self, name):
        return apply("name", self.opr, self.lhs, self.rhs, self.var.ty, true, true)
    def convertToAppWField(self, name, fld):
        return apply(name, self.opr, fld, None, self.var.ty, true, true)

# build a program from a list of lines
class prog:
    def __init__(self, name, lines, oty):
        self.name = name
        self.lines = lines
        self.oty = oty
