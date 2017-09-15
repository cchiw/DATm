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