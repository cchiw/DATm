from firedrake import *
import ctypes
from os.path import abspath, dirname
import os
from os import path
cwd = abspath(dirname(__file__))
from ctypes import POINTER, c_int, c_double, c_void_p, c_float
import numpy
import numpy.ctypeslib as npct
import time



float_type = "float64" #float or double
ctypes_float_type =  ctypes.c_double
        


#from pyop2
def as_ctypes(dtype):
    """Convert a numpy dtype like object to a ctypes type."""
    return {"bool": ctypes.c_bool,
            "int": ctypes.c_int,
            "int8": ctypes.c_char,
            "int16": ctypes.c_int16,
            "int32": ctypes.c_int32,
            "int64": ctypes.c_int64,
            "uint8": ctypes.c_ubyte,
            "uint16": ctypes.c_uint16,
            "uint32": ctypes.c_uint32,
            "uint64": ctypes.c_uint64,
            "float32": ctypes.c_float,
            "float64": ctypes.c_double}[numpy.dtype(dtype).name]


def mk_2d_array(x,t):
    return(ctypes.c_void_p(x.ctypes.data))



class _CFunction(ctypes.Structure):
    """C struct collecting data that we need"""
    _fields_ = [ ("dim",c_int),
                 ("Gdim", c_int),
                ("Sdim", c_int),
                ("NumCells", c_int),
                 ("GetTracker", c_void_p),
                ("CellToNode",c_void_p),
                ("NodeToCoords", c_void_p),
                ("NodeToPoint", c_void_p),
                 ("Coords", POINTER(ctypes_float_type)),
                 ("Nbrs",c_void_p)] 


def organizeData(f):
    func = f
    space = f.function_space()
    mesh = space.mesh()

    cellToNode = mesh.coordinates.cell_node_map().values
    nodeToPoint = mesh.coordinates.dat.data
    nodeToCoords = space.cell_node_map().values
    coords = numpy.asfarray(f.dat.data,dtype=float_type)
    gdim = len(cellToNode[0]) 
    sdim = len(nodeToCoords[0])
    nc = len(cellToNode)
    r = range(nc)
    import sets
    

    ###we need to speed this up.
    opt3 = numpy.ones((nc,nc),dtype="int32")
    opt = True
    if opt:
        setNodes = map(set,cellToNode)
        for x in r:
            s = 0
            e = nc - 1
            for y in r:
                if x== y:
                    opt3[x][s]=y
                    s+=1
                else:
                    test = setNodes[x].isdisjoint(setNodes[y]) #make lazy as symmetric
                    if test:
                        opt3[x][e] = y
                        e-=1
                    else:
                        opt3[x][s] = y
                        s+=1
    grumble = opt3.flatten().tolist()
    opt3 = numpy.array(grumble,dtype="int32")

    
    #might want to reoganizesome data
    c_data = _CFunction()
    c_data.dim = len(space.mesh().coordinates.dat.data[0])#erm... get this somewhere?
    c_data.Gdim = gdim
    c_data.Sdim  = sdim
    c_data.NumCells = nc

    
    q = numpy.array([0])
    c_data.GetTracker = ctypes.cast(mk_2d_array(q.astype("int32"),c_int),c_void_p) #mk_2d_array(numpy.asfarray(numpy.array([2]),dtype="int32"),c_int)
    c_data.CellToNode = mk_2d_array(cellToNode,c_int)
    c_data.NodeToCoords =  mk_2d_array(nodeToCoords,c_int) #nodeToPoint.ctypes.data_as(POINTER(POINTER(as_ctypes(c_int))))
    c_data.NodeToPoint = mk_2d_array(numpy.asfarray(nodeToPoint,dtype=float_type),c_int) 
    c_data.Coords =  coords.ctypes.data_as(POINTER(ctypes_float_type))
    c_data.Nbrs = ctypes.cast((ctypes.c_int32 * (nc*nc))(*opt3),c_void_p) #This change prevented many a segfault.
    #mk_2d_array(opt3,1) #ctypes.c_void_p(opt2.ctypes.data) #mk_2d_array(opt,c_int)

    return(c_data) #pass this back
