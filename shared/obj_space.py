# -*- coding: utf-8 -*-

from __future__ import unicode_literals
nonefield_k= -1
nonefield_dim = 0
import random
from base_constants import *


class space:
    def __init__(self, mesh, element, k_order, fnspace, shape):
        self.id=id
        self.mesh =mesh
        self.element = element
        self.k_order = k_order
        self.fnspace = fnspace
        self.shape = shape
    
    def getParts(self):
        return (self.mesh, self.element, self.k_order, self.fnspace)

    def ty_fnSpace(self, exp, isDiderot):
        shape =  self.shape
        shapen = len(shape)
        fnspace = self.fnspace
        mesh = self.mesh
        center = ""
        if(shapen==0):
            fnspace = fnspace_sca
            center = exp
        elif(shapen==1):
            [n] = shape
            ns = str(n)
            if(isDiderot):
                fnspace = fnspace_ten
                center = exp+",{"+ns+"}"
            else:
                fnspace = fnspace_vec
                center =  exp+", dim="+ns
        elif(shapen==2):
            [n,m] = shape
            nms = str(n)+","+str(m)
            fnspace = fnspace_ten
            if(isDiderot):
                center = exp+",{"+nms+"}"
            else:

                center = exp+", shape =("+nms+")"
        return  fnspace+"("+center+")"

    def ty_fnSpace_forFire(self):
        mesh = self.mesh
        element = self.element
        k_order = 4 #if pde else self.k_order
        exp = mesh+",\""+element+"\",degree="+str(k_order)
        fnspace = space.ty_fnSpace(self, exp,False)+ "\n"
        return fnspace
    def ty_toSpace_forDiderot(self):
        mesh = self.mesh
        element = self.element
        k_order = self.k_order
        self.k_order = 4 #if pde else self.k_order #4# min(k_order,4)
        fnspace = self.fnspace
        exp = mesh+", "+element+"(), "+str(self.k_order)
        fnspace= space.ty_fnSpace(self, exp, True)
        return fnspace
    def ty_Json(self,dim):
        mesh =""
        if(dim==2):
            mesh = mesh_UnitSquareMesh
        elif(dim==3):
            mesh =mesh_UnitCubeMesh
        element = self.element
        k_order = self.k_order
        fnspace = self.fnspace
        
        exp = mesh+"_"+element+"_"+str(k_order)+".json"
        return exp

def dimToMesh(dim, length):
    n = str(length)
    if(dim == 2):
        return mesh_UnitSquareMesh+"("+n+","+n+")"
    elif(dim== 3):
        return mesh_UnitCubeMesh+"("+n+","+n+","+n+")"
    else:
        raise Exception ("unsupported mesh")
def shapeToSpace(shape):
    shapen = len(shape)
    if(shapen==0):
        return fnspace_sca
    elif(shapen==1):
        return fnspace_vec
    else:
        return fnspace_ten
def coeff_tok(g_coeff_style, dim):
    #return 4
    if(g_coeff_style==coeff_linear):
        return 1
    elif(g_coeff_style ==coeff_quadratic):
        return 2
    elif(g_coeff_style ==coeff_cubic):
        return 3


def getSpace(fldty,g_element, g_coeff_style, g_length):
    dim = fldty.dim
    mesh = dimToMesh(dim, g_length)
    # element indicated by frame
    element = g_element
    if(g_element==elem_random):
        elements = [elem_Lagrange, elem_P]
        element= elements[(random.randint(0,1))]
    k_order = coeff_tok(g_coeff_style, dim)*dim

    shape = fldty.shape
    fnspace = shapeToSpace(shape)
    return space(mesh, element, k_order, fnspace, shape)
