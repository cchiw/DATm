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
    def convertToAppWField(self, name, fld, rhs):
        return apply(name, self.opr, fld, rhs, self.var.ty, true, true)

# build a program from a list of lines
class prog:
    def __init__(self, name, lines1,lines2, oty, fields, dim, coeffs):
        self.name = name
        self.lines1 = lines1
        self.lines2= lines2
        self.oty = oty
        self.fields = fields
        self.dim = dim
        self.coeffs = coeffs

# creating constant values that can be used as arguments
def setConstF(ty1, k1, ty_tensor, opr_symb, name, data):
    ty2 = fty(ty1.id, ty1.name, ty1.dim, ty1.shape, ty1.tensorType, k1)
    F2 = field (False, name, ty_tensor, None, data, None)
    fixed = varname(opr_symb, ty2, F2)
    return fixed

def setConstT(ty1, k1, ty_tensor, opr_symb, name, data):
    data = [[1,0,0],[0,1,0],[0,0,1]]
          
    ty2 = fty(ty1.id, ty1.name, nonefield_dim, ty1.shape, ty1.tensorType, None)
    F2 = field (False, name, ty_tensor, None, data, None)
    fixed = varname(opr_symb, ty2, F2)
    return fixed

def getConst_id3 (k1, isField):
    opr_symb ="identity[3]"
    ty1 = ty_mat3x3F_d3
    ty_tensor = ty_mat3x3FT
    data = [[1,0,0],[0,1,0],[0,0,1]]
    if(isField):
        return setConstF(ty1, k1, ty_tensor, opr_symb, "id3", data)
    else:
        return setConstT(ty1, k1, ty_tensor, opr_symb, "id3", data)
def getConst_n2 (k1):
    opr_symb = "2"
    ty1 = ty_scalarF_d3
    ty_tensor = ty_scalarFT
    data = 2
    return setConstF(ty1, k1, ty_tensor, opr_symb, "double", data)