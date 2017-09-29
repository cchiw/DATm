from firedrake import *
import ctypes
from functools import reduce
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
    # y = numpy.empty(x.shape[0],dtype=object)
    # for i in range(0,len(x)):
    #     print(x[i])
    #     y[i] = x[i].ctypes.data_as(POINTER(as_ctypes(x.dtype)))
    # return(y.ctypes.data_as(POINTER(POINTER(as_ctypes(x.dtype)))))
    #return((ctypes.cast(ctypes.c_void_p(x.ctypes.data),POINTER(POINTER(as_ctypes(c_int))))))
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
        setNodes = list(map(set,cellToNode))
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

    # print(opt3[0])


                    #opt3 = np.array(np.where(opt3.flatten != 0 ),dtype=float_type)

        #float(len(setNodes[x].intersection(setNodes[y]))): this is more inefficient but could be use to enforce stricter locality

    # s = time.clock()
    # opt = 0-numpy.ones((nc,nc),dtype="int32")
    # r = range(nc)
    # #THIS IS MASSIVELY INEFFICIENT: I'm workon a better one
    # #Use sets -> different system -> cell by cell array
    # for x in r:
    #     #a  = (numpy.where(map(lambda y: numpy.intersect1d(cellToNode[x],y).size!=0,cellToNode))[0]).astype("int32")
    #     a  = (numpy.where(map(lambda y: numpy.intersect1d(cellToNode[x],y).size!=0,cellToNode))[0]).astype("int32")
    #     #This is really important
    #     #it needs to have a uniform type or everything goes to hell
        
    #     opt[x][0:a.shape[0]]= a
    #     #opt[x][a.shape[0]] = x -> a should include x
    # e = time.clock()
    # print("First loop time is {0}".format(e-s))
    # opt2 = numpy.empty((nc,nc),dtype=float_type)
    # for x in r:
    #     for y in r:
    #         opt2[x][y] = float(opt[x][y])


    
    
    
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

    
    functionDataCtype = reduce(lambda x,y : x*y, coords.shape, ctypes_float_type)
    functionDataSize = reduce(lambda x,y : x*y, coords.shape, 1)
    c = coords.flatten().copy()
    # print(coords.T[0][0])
    # print(coords.ctypes.shape)
    # print(c.flags)
    # print(len(c))
    c_data.Coords =  ctypes.cast((ctypes_float_type*functionDataSize)(*c),POINTER(ctypes_float_type)) #c.ctypes.data_as(POINTER(ctypes_float_type))

    c_data.Nbrs = ctypes.cast((ctypes.c_int32 * (nc*nc))(*opt3),c_void_p) #This change prevented many a segfault.
    #mk_2d_array(opt3,1) #ctypes.c_void_p(opt2.ctypes.data) #mk_2d_array(opt,c_int)

    return(c_data) #pass this back
    
    


# connect to diderot programs
def data_d2s(name, f, resU, resV, stepSize):
    p_cf = f._ctypes
    init_file = path.join(path.dirname(__file__), '../programs/data_d2s/data_d2s_init.o')
    diderot_file = path.join(path.dirname(__file__),'../programs/data_d2s/data_d2s.o')
    #call = make_c_evaluate(f, "callDiderot", ldargs=[init_file, diderot_file, "-lteem"])
    # the datafile
    return call(ctypes.c_char_p(name),p_cf, resU, resV, ctypes.c_float(stepSize))


def basic_d2s_sample(name,f, resU, resV, stepSize, type):
    p_cf = f._ctypes
    init_file = path.join(path.dirname(__file__), '../programs/basic_d2s_sample/basic_d2s_sample_init.o')
    diderot_file = path.join(path.dirname(__file__),'../programs/basic_d2s_sample/basic_d2s_sample.o')
    #call = make_c_evaluate(f, "callDiderot", ldargs=[init_file, diderot_file, "-lteem"])
    type = 0
    return call(ctypes.c_char_p(name),type,p_cf, resU, resV, ctypes.c_float(stepSize))


def mesh_d2s_single(name, f, res):
    #init_file = '/home/teodoro/gitcode/diderot_fem/programs/mesh_d2s_single/mesh_d2s_single_init.so'
    init_file = '/home/teodoro/gitcode/diderot_fem/programs/mesh_d2s_single/mesh_d2s_single_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)

    _call.callDiderot.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_float)
    result = _call.callDiderot(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p), res)
    return(result)

def single_mesh(name, f, res,init_file):
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_float)
    result = _call.callDiderot(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p), res)
    return(result)
def single_mesh_step(name, f, res,step,init_file):
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_int,ctypes.c_float)
   
    result = _call.callDiderot(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p), res,step)
   
    return(0)

def mesh_d2s_twofields(name, f, g, res):
    p_cf = f._ctypes
    p_cg = g._ctypes
    
    init_file = path.join(path.dirname(__file__), '../programs/mesh_d2s_twofields/mesh_d2s_twofields_init.o')
    diderot_file = path.join(path.dirname(__file__),'../programs/mesh_d2s_twofields/mesh_d2s_twofields.o')
    #call = make_c_evaluate(f, "callDiderot", ldargs=[init_file, diderot_file, "-lteem"])
    type = 1
    return call(ctypes.c_char_p(name), type, p_cf, p_cg, res)



def mesh_step(name, f, res, stepSize):
    init_file = '/Users/chariseechiw/fire/firedrake/src/firedrake/diderot_fem/programs/mesh_step/mesh_step_init.so'
    _call = ctypes.CDLL(init_file)
    type = 1
    data = organizeData(f)
    _call.callDiderot_mesh_step.argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_int,ctypes.c_float)
    result = _call.callDiderot_mesh_step(ctypes.c_char_p(name), type,ctypes.cast(ctypes.pointer(data),ctypes.c_void_p), res, stepSize)
    return(result)



#visualize images
def quantize(namenrrd,namepng):
    os.system('unu quantize -b 16 -i ' +namenrrd+ ' -o '+ namepng )
    os.system('open ' + namepng)



