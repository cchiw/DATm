
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
    init_file =  target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p))
    return(result)

def init1Sample(name, f,target,res, stepSize, limit):
    init_file =  target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_int,ctypes.c_float,ctypes.c_float)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p), res, stepSize, limit)
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
#general declarations

res = 10 
stepSize = 1.0/res 
limit = 5#init field
# call to init

name = "cat"
target ="ex1"
namenrrd = name+'.nrrd'
expf0 = "0+(4*1)+(5*x[1])+(3*x[0]*x[1])+(-1*x[0])"
V= FunctionSpace(UnitSquareMesh(4,4),"Lagrange",degree=2)

f0 = Function(V).interpolate(Expression(expf0))
f11=interpolate(Expression("((-0.0782965028281 * 1.0 + -1.16470424387 * (x[1]) + -0.92378191186 * (x[1] * x[1]) + -0.717925050484 * (x[1] * x[1] * x[1]) + -1.16000781672 * (x[1] * x[1] * x[1] * x[1]) + -1.27761220219 * (x[1] * x[1] * x[1] * x[1] * x[1]) + -0.902727332554 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * 1.0 + (-0.494122317348 * 1.0 + -0.76639796164 * (x[1]) + -1.30059899445 * (x[1] * x[1]) + -0.0963500538738 * (x[1] * x[1] * x[1]) + -0.259012224732 * (x[1] * x[1] * x[1] * x[1]) + -1.13192215524 * (x[1] * x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0]) + (-1.17315378887 * 1.0 + -1.29395771044 * (x[1]) + -1.30427929652 * (x[1] * x[1]) + -1.2565654441 * (x[1] * x[1] * x[1]) + -1.20321325999 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0]) + (-0.638394839753 * 1.0 + -0.693452332423 * (x[1]) + -1.31698947559 * (x[1] * x[1]) + -0.86074122147 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0]) + (-1.11836592992 * 1.0 + -0.618485848502 * (x[1]) + -0.946826448059 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0] * x[0]) + (-0.191315493092 * 1.0 + -1.08924506939 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0] * x[0] * x[0]) + (-1.47494090341 * 1.0 + 0.0 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0] * x[0] * x[0] * x[0]))"),V)

bexpf1 = Expression("((0.0740054089421 * 1.0 + 0.612182199682 * (x[1]) + 1.28836131248 * (x[1] * x[1]) + 0.293717672332 * (x[1] * x[1] * x[1])) * 1.0 + (1.35324922097 * 1.0 + 0.0142790149938 * (x[1]) + 0.28292596941 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1])) * (x[0]) + (1.02505639192 * 1.0 + 0.0891340002635 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1])) * (x[0] * x[0]) + (1.40737347964 * 1.0 + 0.0 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0]))")
f21=6.44028467063
limit = f21

def L(q):
	a = 0.926279142165*q.dx(0)+7.95222491756*q.dx(0).dx(0)+4.29475417509*q.dx(0).dx(1)+0.79560853275*q.dx(1)+4.29475417509*q.dx(1).dx(0)+4.20400837443*q.dx(1).dx(1)
	return(a)
# Define Dirichlet boundary
def inside(x, on_boundary):
    return on_boundary


# Define boundary condition
u01 = interpolate(bexpf1,V)
bc = DirichletBC(V, u01, (1,2,3,4))

# Define trial and test functions
u = TrialFunction(V)
v = TestFunction(V)

# Define normal component, mesh size and right-hand side
h = CellSize(V.mesh())
h_avg = (h('+') + h('-'))/2.0
n = FacetNormal(V.mesh())
x = SpatialCoordinate(V.mesh())
f = (f11) 

# Penalty parameter that must be played around with
alpha = Constant(32.0) #dependent on the mesh, I think???

# Define bilinear form
a = inner(L(u), L(v))*dx   - inner(avg(L(u)), jump(grad(v), n))*dS   - inner(jump(grad(u), n), avg(L(v)))*dS   + alpha/h_avg*inner(jump(grad(u),n), jump(grad(v),n))*dS



# Define linear form
L = f*v*dx
b = assemble(L)
                
f1=Function(V)
solve(a == L, f1, bc)
init1Sample(namenrrd, f1, target, res, stepSize ,limit)