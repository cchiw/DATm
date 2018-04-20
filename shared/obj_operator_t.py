# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from base_constants import *
adj = (opr_adj)

import sys
import re
import os
import time

class operator:
    def __init__(self, keep, id, name, arity, symb, placement, limit, fieldop):
        self.keep = keep
        self.id=id
        self.name=name
        self.arity=arity
        self.symb=symb
        self.placement=placement
        self.limit = limit
        self.fieldop =fieldop
    def toStr(self):
        self.name+"("+str(arity)+")"
    def get_name(self):
        return self.name
    def isEq_id(a,b):
        return (a.id==b.id)
    def isEq_idNum(a,b):
        return (a.id==b)
    def toStr(self,s):
        if(self.arity==1):
            return self.name+"("+s+"0"+")"
        elif(self.arity==2):
            return self.name+"("+s+"0,"+s+ "1"+")"

#------------------------------ constants -----------------------------------------------------
#----------------- placement -----------------
# id, name, arity, symbol
# placement of the operator in respect to the arguments
place_left = "left"
place_right = "right"
place_middle = "middle"
place_split = "split"
#----------------- limitations -----------------
# add limit to arguments
limit_none = None
limit_trig = "trig1"# |0.1* x| <= 1
limit_small = "small"# |x2|>0.01 , second argument in arity=2
limit_det = "det"# |det(x)|>0.01
limit_nonzero = "positive" # |x|>0

#------------------------------ operators -----------------------------------------------------
#----------------- algebra -----------------
id=0
#op_none= operator(True,id,"none", 1,"", place_left, limit_none, False)
op_none= operator(True,id,"none", 1,"", place_right, limit_none, False)
op_negation = operator(True,id+1,"neg", 1,"-", place_left, limit_none, False)
op_copy= operator(True,id+2,"copy", 1,"", place_left, limit_none, False)
op_norm = operator(True,id+3,"norm", 1, (u'|',u'|'), place_split, limit_none, False)
op_normalize = operator(True,id+4,"normalize", 1, u'normalize', place_left, limit_none, False)
op_transpose = operator(True, id+5,"transpose", 1, u'transpose', place_left, limit_none, False)


op_trace = operator(False,-1,"trace", 1, u'trace', place_left, limit_none, False)
op_det = operator(False,-1,"det", 1, u'det', place_left, limit_none, False)
op_inverse = operator(False,-1, "inverse", 1, u'inv', place_left, limit_det, False)
op_reg = [op_none, op_negation, op_copy, op_norm, op_normalize,op_transpose]
id=id+len(op_reg)
#----------------- binary -----------------
op_add = operator(True,id,"addition", 2,"+", place_middle, limit_none, False)
op_subtract = operator(True,id+1,"subtraction", 2, "-", place_middle, limit_none, False)
op_scale = operator(True,id+2,"multiplication", 2, u'*', place_middle, limit_none, False)
op_division = operator(True,id+3,"division", 2, u'/', place_middle, limit_small, False)
op_cross = operator(True,id+4,"cross_product", 2, u'×', place_middle, limit_none, False)
op_modulate = operator(True,id+5,"modulate", 2, "modulate",  place_left, limit_none, False)

op_doubledot= operator(False,-1,"op_doubledot", 2, u':', place_middle, limit_none, False)
op_outer = operator(False,-7,"outer_product", 2, u'⊗', place_middle, limit_none, False)
op_inner = operator(False,-8,"inner_product", 2, u'•', place_middle, limit_none, False)
op_binary = [op_add, op_subtract,op_scale, op_division, op_cross, op_modulate]
#, op_doubledot,op_outer,op_inner ]
id=id+len(op_binary)
#----------------- trig -----------------
op_cosine = operator(True,id, "cosine", 1, u'cos', place_left, limit_none, True)
op_sine = operator(True,id+1, "sine", 1, u'sin', place_left, limit_none, True)
# limit- x must be between -1 and 1 for acos|asine and positive for sqrt.
# to avoid getting a bunch of (inf, or NAN)
# operator arguments are augmented here and in test_eval
op_acosine = operator(True,id+2, "arccosine", 1,  (u'acos(0.01*', u')'), place_split, limit_trig, True)
op_asine = operator(True,id+3, "arcsine", 1,  (u'asin(0.01*', u')'), place_split, limit_trig, True)
#note sqrt is 'sqrt' in each branch
#op_sqrt = operator(True,id+4, "sqrt", 1, (u'sqrt(|', u'|)'), place_split, limit_nonzero, False)
op_sqrt = operator(True,id+4, "sqrt", 1, (u'sqrt(', u')'), place_split, limit_nonzero, False)
op_atangent = operator(True,id+5, "arctangent", 1, u'atan', place_left, limit_none, True)
op_tangent = operator(True,id+6, "tangent", 1, u'tan', place_left, limit_none, True)
op_trig=[ op_cosine, op_sine, op_acosine, op_asine, op_sqrt]#,op_atangent, op_tangent]
id=id+len(op_trig)

#----------------- differentiation -----------------
#differentiation
op_gradient = operator(True,id, "grad", 1, u'∇', place_left, limit_none, True)
op_hessian = operator(True,id+1, "hessian", 1, u'∇⊗∇', place_left, limit_none, True)
op_diff =[op_gradient, op_hessian]
id=id+len(op_diff)

#----------------- new features that work on branch -----------------
op_zeros_add22 = operator(True,id, "zeros_add", 1, (u'(zeros[2, 2]+', u')'), place_split, limit_none, False)
op_zeros_scale3 = operator(True,id+1, "zeros_scale", 1, (u'(', u'*zeros[3, 3])'), place_split, limit_none, False)
op_max = operator(True,id+2,"max", 2,"maxF", place_left, limit_none, True)
op_min = operator(True,id+3,"min", 2,"minF", place_left, limit_none, True)
op_concat2 = operator(True,id+4,"concat2", 2,"concat", place_left, limit_none, True)
op_zeros_outer2 = operator(False,-5, "zeros_outer", 1, (u'(zeros[2]⊗', u')'), place_split, limit_none, False)
op_new1 = [op_zeros_add22, op_zeros_scale3,op_max, op_min, op_concat2]#, op_zeros_outer2]
id=id+len(op_new1)


#----------------- slicing -----------------
op_slicem0 = operator(False,-1,"slicem0", 1, u'[1,:]', place_right, limit_none, False)
op_slicem1 = operator(False,-1,"slicem1", 1, u'[:,0]', place_right, limit_none, False)
op_slicev0 = operator(False,-2,"slicev0", 1, u'[0]', place_right, limit_none, False)
op_slicev1 = operator(False,-3,"slicev1", 1, u'[1]', place_right, limit_none, False)
op_slicet0 = operator(False,-4,"slicet0", 1, u'[:,1,:]', place_right, limit_none, False)
op_slicet1 = operator(False,-5,"slicet1", 1, u'[1,0,:]', place_right, limit_none, False)
op_slice = []#[op_slicem0, op_slicem1, op_slicev0, op_slicev1, op_slicet0, op_slicet1]
id=id+len(op_slice)


### features not fully supported on fem. expected errors
op_jacob= operator(True,id, "jacob", 1, u'∇⊗', place_left, limit_none, True)
op_comp = operator(True,id+1,"compose", 2,(u'compose(', u'*'+str(adj)+')'), place_split, limit_none, True)
op_divergence = operator(False,-2, "div", 1, u'∇•', place_left, limit_none, True)
op_curl= operator(False,-3, "curl", 1, u'∇×',place_left, limit_none, True)
op_new2 = [op_jacob,op_comp]#,op_divergence,op_curl]
id=id+len(op_new2)


#----------------- list of all operators -----------------
# all the operators
#op_all = op_reg+op_binary+op_trig+op_diff+op_new1
op_all = op_reg+op_binary+op_trig+op_diff+op_new1+op_slice+op_new2




if(not pde_test):
    op_all=op_all+op_slice+op_new2


#------------------------------ operators not included -----------------------------------------------------

#----------------- embedded  operators -----------------
#### more than one operator or unsupported operation
op_probe= operator(True,-1,"probe", 1,"(pos)", place_right, limit_none, True)
op_crossT3 = operator(True,-1,"cross product twice", 1, (u'([9, 7, 8] ×', u')'), place_split, limit_none, False)
op_concat3 = operator(True,-3,"concat3", 3,"concat", place_left, limit_none, True)
op_negationT = operator(True,-1,"negT", 1,"-", place_left, limit_none, False)
#------------------------------ helpers -----------------------------------------------------
# print all the ops names and ids
def pnt_ops():
    e=""
    i=0
    for op1 in op_all:
        x= "\n-"+op1.name+"("+str(op1.id)+","+str(op1.keep)+") "
        print (x)
        e =e+x
        # see if id matches placement in list
        if(not (op1.id==i)):
            raise Exception(x+" does not match placement "+str(i))
        i+=1
    f = open("rst/stash/results_final.txt", 'a+')
    f.write(e)
    f.close()

# get operator from id
def id_toOpr(n):
    opr = op_all[n]
    if(opr.id ==n):
        return opr
    else:
        return "no match"
#name of operator from id
def idToStr(id):
    opr = id_toOpr(id)
    return opr.name
# number of operators
def getN():
    return len(op_all)
# do we need to create an extra field type
def needextratype(ex_outer):
    return (ex_outer.arity==2)
pnt_ops()
