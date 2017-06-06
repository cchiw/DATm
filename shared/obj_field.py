# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sympy
from sympy import *
#symbols
x,y,z =symbols('x y z')
import sys
import re
import os
from base_constants import *
from obj_ty import *
from obj_coeff import mk_exp, mk_exp_debug1, mk_exp_debug2
class kernel:
    def __init__(self, str, continuity, order):
        # str: string used in diderot program for kernel
        self.name = "kernel_"+str
        self.str = str
        self.continuity = continuity
        self.order = order

#kernel(name, str, continuity, order)
#c4hexic-cubic
#ctmr-quad
#bspln3-linear
krn_hex = kernel("c4hexic", 3, 3)
krn_bs3 = kernel("bspln5", 4, 1)
krn_tent = kernel("tent", 0, 1)
krn_ctmr = kernel("ctmr", 1, 2)
                 
# transform kernel from input global to kernel variable
def transform_krn(krn, id):
    if(krn == h_bs3):
        return krn_bs3
    elif(krn == h_bs5):
        return krn_bs3
    elif(krn == h_hex):
        return krn_hex
    elif(krn == h_tent):
        return krn_tent
    elif(krn == h_ctmr):
        return krn_ctmr
    elif(krn == h_mixcbc):
        if(id == 0):
            return krn_hex
        elif(id == 1):
            return krn_bs3
        elif(id == 2):
            return krn_hex
    elif(krn == h_mixcbt):
        if(id == 0):
            return krn_hex
        elif(id == 1):
            return krn_bs3
        elif(id == 2):
            return krn_tent

    else:
        raise Exception ("unsupported kernel type:", krn)

# transform kernel from input global to kernel variable
def krn_to_k(krn):
    return krn.continuity
def set_k(g_krn, id, ty1):
    c_krn = transform_krn(g_krn, id)
    c_k = c_krn.continuity
    ty1.k = c_k
    #print "set_k- kernel id:", id," g_krn :", c_krn.name, "k: ",ty1.k
    return fty(ty1.id, ty1.name, ty1.dim, ty1.shape, ty1.tensorType, c_k)
    
#return ty1
def set_ks(g_krn, ishapes):
    id = 0
    rtn = []
    for i in ishapes:
        r = set_k(g_krn, id, i)
        #print "set_ks", id, "r:", r.name,"k", r.k
        rtn.append(r)
        #print "->k", rtn[id].k
        id+=1

    return rtn


#returns expression created with coefficients
class field:
    def __init__(self, isField, name, fldty, krn, data, inputfile):
        self.isField = isField
        self.name = name
        self.fldty = fldty
        self.krn = krn
        self.data = data
        self.inputfile = inputfile
    def toStr(self):
        if (self==None):
            return "field is none"
        else:
            return ("Field:"+fty.toStr(self.fldty)+" "+self.name+"="+str(self.data))
    #equal id to fty
    def isEq_id(a,b):
        return (a.fldty.ty.id== b.id)
        #  def get_ty(self):
        # return self.fldty.ty
    def get_dim(self):
        #print "inside get dim", self.name
        return self.fldty.dim
    def get_data(self):
        d = self.data
        #print "self get data", d
        return d
    def get_ty(self):
        return self.fldty
    def get_isField(self):
        return self.isField
    # is scalar field
    def is_ScalarField(ty0):
        shape = ty0.fldty.shape
        return  (ty0.isField and len(shape)==0)
    def is_Scalar(ty0):
        print "ty0", ty0.name
        shape = ty0.fldty.shape
        return  (len(shape)==0)
    # is vecor field
    def is_VectorField(ty0):
        shape = ty0.fldty.shape
        return  (ty0.isField and len(shape)==1)
    def is_Vector(ty0):
        shape = ty0.fldty.shape
        return  (len(shape)==1)
    def is_Matrix(ty0):
        shape = ty0.fldty.shape
        return  (len(shape)==2)
    def is_Ten3(ty0):
        shape = ty0.fldty.shape
        return  (len(shape)==3)




#  i_fty: field type
def mk_Field(index, i_fty, k, inputfile, dim, coeff_style, ucoeff, krn, t_template):
    #print "inside mk fields: "+str(index)
    tag = str(index)
    id="F"+tag
    # field type
    finfo1 = fty.convertTy(i_fty, k)
    # translate coefficients to expression
    # name of input file
    input1 = inputfile+tag
    def get_vec(n):
        if (n==2):
            (coeff1, exp1)= mk_exp(dim, coeff_style, ucoeff, t_template)
            (coeff2, exp2)= mk_exp(dim, coeff_style, ucoeff, t_template)
            coeffs= [ coeff1,coeff2]
            exps = [exp1,exp2]
   
            #print " inside get vec(): exp1", exp1
            #print " inside get vec(): exp2", exp2
            return (coeffs, exps)
        elif (n==3):
            (coeff1, exp1)= mk_exp(dim, coeff_style, ucoeff, t_template)
            (coeff2, exp2)= mk_exp(dim, coeff_style, ucoeff, t_template)
            (coeff3, exp3)= mk_exp(dim, coeff_style, ucoeff, t_template)
            coeffs= [ coeff1,coeff2, coeff3]
            exps = [exp1, exp2, exp3]
            return (coeffs, exps)
        elif (n==4):
            (coeff1, exp1)= mk_exp(dim, coeff_style, ucoeff, t_template)
            (coeff2, exp2)= mk_exp(dim, coeff_style, ucoeff, t_template)
            (coeff3, exp3)= mk_exp(dim, coeff_style, ucoeff, t_template)
            (coeff4, exp4)= mk_exp(dim, coeff_style, ucoeff, t_template)
            coeffs= [ coeff1,coeff2, coeff3, coeff4]
            exps = [exp1, exp2, exp3, exp4]
            return (coeffs, exps)
        else:
            raise Exception ("unsupported length:"+str(n))
    def get_mat(n,m):
        exps=[]
        coeffs=[]
        #print "starting get_mat"
        for i in range(n):
            (c1,e1)= get_vec(m)
            exps.append(e1)
            coeffs.append(c1)
            # (c1,e1) = get_vec(m)

        #[a, b, c]=e1
        #e2 = [a*2,b*2,c*2]
        #e3 = [a*3,b*3,c*3]
        #exps = [e1, e1, e1] #each axis has fixed value
        #coeffs = [c1, c1, c1]
        #print "\n\n ********************** post get exp\n"
        #print "exps-e1",e1
        #print "coeffs-c1",c1
        #print " exps[0][0]", exps[0][0]
        #print " exps[0][1]", exps[0][1]
        #print " exps[1][0]", exps[1][0]
        #print "\n\n ---   \n"
        #print "coeffs",coeffs
        return (coeffs, exps)
    def get_ten3(n,m,o):
        exps=[]
        coeffs=[]
        for i in range(n):
            (c1,e1)= get_mat(m, o)
            exps.append(e1)
            coeffs.append(c1)
        return (coeffs, exps)

    if (fty.is_ScalarField(finfo1)):
        (coeff1, exp1)= mk_exp(dim, coeff_style, ucoeff,t_template)
        F = field(true, id, finfo1 , krn, exp1, input1)
        #print ("Fsca", field.toStr(F))
        return (F, finfo1, coeff1)
    elif(fty.is_VectorField(finfo1)): # input is a vector field
        n= fty.get_vecLength(finfo1)
        (coeffs, exps) = get_vec(n)
        F = field(true, id, finfo1 ,krn, exps, input1)
        #print ("Fvec", field.toStr(F))
        return (F, finfo1, coeffs)
    elif(fty.is_MatrixField(finfo1)): # input is a vector field
        [shape0, shape1] = fty.get_shape(finfo1)
        (coeffs, exps) =  get_mat(shape0, shape1)
        F = field(true, id, finfo1 ,krn, exps, input1)
        #print ("Fvec", field.toStr(F))
        return (F, finfo1, coeffs)
    
    elif(fty.get_dim(finfo1)==0): #tensor
        if(fty.is_Scalar(finfo1)):
            (coeff1, exp1)= mk_exp(dim, coeff_style, ucoeff,t_template)
            (coeffs, exps) = (coeff1, exp1)
            F = field(false, id, i_fty,"", exps, "")
            #print ("Ften", field.toStr(F))
            return (F, finfo1, coeff1)
        elif(fty.is_Vector(finfo1)):
            n= fty.get_vecLength(finfo1)
            (coeff1, exp1)= mk_exp(dim, coeff_style, ucoeff,t_template)
            (coeffs, exps) = get_vec(n)
            F = field(false, id, i_fty,"", exps, "")
            #print ("Ften", field.toStr(F))
            return (F, finfo1, coeff1)
        elif(fty.is_Matrix(finfo1)):
            [shape0, shape1] = fty.get_shape(finfo1)
            (coeffs, exps) =  get_mat(shape0, shape1)
            F = field(false, id, i_fty,"", exps, "")
            #print ("Ften", field.toStr(F))
            return (F, finfo1, coeffs)
        elif(fty.is_Ten3(finfo1)):
            [shape0, shape1, shape2] = fty.get_shape(finfo1)
            (coeffs, exps) = get_ten3(shape0, shape1, shape2)
            F = field(false, id, i_fty,"", exps, "")
            #print ("Ften", field.toStr(F))
            return (F, finfo1, coeffs)
        else:
            raise "unsupported field type"
    else:
        raise "unsupported field type"
