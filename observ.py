
import sys
from firedrake import *
from os.path import abspath, dirname
import pytest
import os
from os import path
cwd = abspath(dirname(__file__))
sys.path.insert(0, 'fem/')

from init import *
#from connect import *
#from makejson import *

import ctypes
from ctypes import POINTER, c_int, c_double, c_void_p, c_float
import numpy
import numpy.ctypeslib as npct





# init diderot program
# single field
def init1(name, f,target):
    init_file = target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p))
    return(result)

# two fields
def init2(name, f, g,target):
    init_file = target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    dataF = organizeData(f)
    dataG = organizeData(g)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(dataF),ctypes.c_void_p),ctypes.cast(ctypes.pointer(dataG),ctypes.c_void_p))
    return(result)

# three fields
def init3(name, f, g, h, target):
    init_file = target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    dataF = organizeData(f)
    dataG = organizeData(g)
    dataH = organizeData(h)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(dataF),ctypes.c_void_p), ctypes.cast(ctypes.pointer(dataG),ctypes.c_void_p),ctypes.cast(ctypes.pointer(dataH),ctypes.c_void_p))
    return(result)

# four fields
def init4(name, f, g, h, i, target):
    init_file = target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    dataF = organizeData(f)
    dataG = organizeData(g)
    dataH = organizeData(h)
    dataI = organizeData(i)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(dataF),ctypes.c_void_p), ctypes.cast(ctypes.pointer(dataG),ctypes.c_void_p),ctypes.cast(ctypes.pointer(dataH),ctypes.c_void_p),ctypes.cast(ctypes.pointer(dataI),ctypes.c_void_p))
    return(result)


##############################################

#init field

name = "cat"
target ="ex1"
namenrrd = name+'.nrrd'
expf0 = "0+(2*1)+(1*x[1])"
mesh = UnitSquareMesh(2,2)
V= FunctionSpace(mesh,"Lagrange",degree=2)
f0 = Function(V).interpolate(Expression(expf0))
init1(namenrrd, f0,  target)