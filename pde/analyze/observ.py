
import sys
from firedrake import *
from os.path import abspath, dirname
import pytest
import os
from os import path
cwd = abspath(dirname(__file__))
sys.path.insert(0, '../../fem/')

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
    init_file = "/home/teodoro/gitcode/DATm/analyze" + target+'_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot_ex1.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p)
    result = _call.callDiderot_ex1(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p))
    return(result)

def init1Sample(name, f,target,res, stepSize, limit):
    init_file = "/home/teodoro/gitcode/DATm/pde/analyze/" + target+'_init.so'
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
expf0 = "0+(-3*1)+(3*x[1])+(-5*x[0]*x[1])+(-2*x[0])"
V= FunctionSpace(UnitSquareMesh(4,4),"Lagrange",degree=4)

f0 = Function(V).interpolate(Expression(expf0))
f11=interpolate(Expression("((-1.03753132461 * 1.0 + -0.866063439545 * (x[1]) + -0.728512075224 * (x[1] * x[1]) + -1.4487617379 * (x[1] * x[1] * x[1]) + -0.754282003383 * (x[1] * x[1] * x[1] * x[1]) + -1.01564563012 * (x[1] * x[1] * x[1] * x[1] * x[1])) * 1.0 + (-0.827567773027 * 1.0 + -0.530406327283 * (x[1]) + -1.43345574287 * (x[1] * x[1]) + -0.737048303181 * (x[1] * x[1] * x[1]) + -1.25816659804 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0]) + (-0.614878733798 * 1.0 + -0.612418695238 * (x[1]) + -0.270042507301 * (x[1] * x[1]) + -1.39594913416 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0]) + (-0.853453655863 * 1.0 + -0.610059618444 * (x[1]) + -1.43680723329 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0]) + (-0.878199850454 * 1.0 + -0.4606151854 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0] * x[0]) + (-1.09559627317 * 1.0 + 0.0 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0] * x[0] * x[0]))"),V)

bexpf1 = Expression("((0.898834130408 * 1.0 + 0.569697445748 * (x[1]) + 1.03362972091 * (x[1] * x[1]) + 1.16706510255 * (x[1] * x[1] * x[1])) * 1.0 + (0.468239799992 * 1.0 + 0.928363490473 * (x[1]) + 1.24516506124 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1])) * (x[0]) + (1.44058303639 * 1.0 + 1.37748719541 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1])) * (x[0] * x[0]) + (0.205420163205 * 1.0 + 0.0 * (x[1]) + 0.0 * (x[1] * x[1]) + 0.0 * (x[1] * x[1] * x[1])) * (x[0] * x[0] * x[0]))")
f21=9.33448514632
limit = f21

def L(q):
	a = 0.712199547962*q.dx(0)+4.62503594086*q.dx(0).dx(0)+1.87094539568*q.dx(0).dx(1)+0.502249940616*q.dx(1)+1.87094539568*q.dx(1).dx(0)+3.82417337049*q.dx(1).dx(1)
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


A = assemble(a,bcs=[bc])
# Define linear form
L = f*v*dx
b = assemble(L)
                
f1=Function(V)
solve(a == L, f1, bc)

#r =  0.712199547962*f1.dx(0)+4.62503594086*f1.dx(0).dx(0)+1.87094539568*f1.dx(0).dx(1)+0.502249940616*f1.dx(1)+1.87094539568*f1.dx(1).dx(0)+3.82417337049*f1.dx(1).dx(1)


#print("The data is {0}".format(f1.dat.data))
#q = project(r,V)
#outfile = File("output.pvd")
#outfile.write(q)





import numpy as np
def test_fp(A,u,bc):
    M = A.M.values
    uarray = u.dat.data
    s = u.dat.data.shape[0]
    ln = np.array(list(range(0,s)),dtype=int)
    bcn  = bc.nodes
    bs = bcn.shape[0]
    nbc = np.zeros((s-bs,),dtype=int)
    i = 0
    for x in ln:
        if x in bcn:
            continue
        else:
            nbc[i]=x
            i+=1
        
    
    Kb = np.zeros((s-bs,bs),dtype="float64")
    Ko = np.zeros((s-bs,s-bs),dtype="float64")
    ub = np.zeros((bs,),dtype="float64")
    uo = np.zeros((s-bs,),dtype="float64")
    Ko = M[np.ix_(nbc,nbc)]
    Kb = M[np.ix_(nbc,bcn)]
    ub = uarray[(bcn)]
    uo = uarray[(nbc)]

    Koinv = np.linalg.inv(Ko)
    m1 = Koinv >= 0
    m2 = (-1)*Koinv.dot(Kb) >= 0
    temp = (-1)*Koinv.dot(Kb)
    e = np.ones((bs),dtype="float64")
    m3 = temp.dot(e) <= 1
    t = m1.all() and m2.all() and m3.all()
    return(t)
t = test_fp(A,f1,bc)
if(not(t)):
    exit(25)


init1Sample(namenrrd, f1, target, res, stepSize ,limit)
