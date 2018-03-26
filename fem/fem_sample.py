import sys
from firedrake import *
from os.path import abspath, dirname
import pytest
import os
from os import path
cwd = abspath(dirname(__file__))
from init import *


import ctypes
from ctypes import POINTER, c_int, c_double, c_void_p, c_float
import numpy
import numpy.ctypeslib as npct


# init diderot program
def ex1(name, f, res, stepSize):
    init_file = 'observ_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p,ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), ctypes.cast(ctypes.pointer(data),ctypes.c_void_p))
    return(result)

#progrm creates step size
def cut_step(name, f, res):
    stepSize = 1.0/res
    datafile = imgpath+name
    namenrrd = datafile +'.nrrd'
    ex1(namenrrd, f, res, stepSize)


