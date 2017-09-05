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


