# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import re
import os
import random


#top-level
from frame import  *

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_field import *
from obj_counter import *
from obj_frame import *
from base_write import *
from base_var_ty import *
from base_observed import observed


def ty_toMesh(fldty):
    dim =  fldty.dim
    if(fldty.dim == 2):
        return "UnitSquareMesh(2,2)"
    elif(fldty.dim== 3):
        return "UnitCubeMesh(2,2,2)"
    else:
        raise Exception ("unsupported mesh")

def ty_toK():
    k_order = "2"
    return k_order

def ty_toElement():
    return "Lagrange"


def ty_fnSpaceParts(fldty):
    dim =  fldty.dim
    mesh = ty_toMesh(fldty)
    element = ty_toElement()
    k_order = ty_toK()
    return (mesh, element, k_order)

def ty_fnSpace(fldty, exp, isDiderot):
    if(fty.is_Scalar(fldty)):
        return "FunctionSpace("+exp+")"
    elif(fty.is_Vector(fldty)):
        n = fty.get_vecLength(fldty)
        if(isDiderot):
            return "TensorFunctionSpace("+exp+",{"+str(n)+"})"
        else:
            return "VectorFunctionSpace("+exp+", dim="+str(n)+")"

def ty_fnSpace_forFire(fldty):
    (mesh, element, k_order) = ty_fnSpaceParts(fldty)
    exp = mesh+",\""+element+"\",degree="+k_order
    space = ty_fnSpace(fldty, exp,false)
    return (space)

def ty_toSpace_forDiderot(fldty):
    (mesh, element, k_order) = ty_fnSpaceParts(fldty)
    exp = mesh+", "+element+"(), "+k_order
    space = ty_fnSpace(fldty, exp, true)
    return space