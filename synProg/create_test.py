#give users the ability to make their own test
# assumes unary operators
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

# specific cte programs
from cte_createField import createField
from cte_writeDiderot import writeDiderot
from cte_eval import eval
from cte_continue import *
from cte_core import *


pde_test = false # test pdes in fem branch
# create a field
def set_fld(id, c_ity, testing_frame):
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
   
    c_dim = fty.get_dim(c_ity)
    c_krn = transform_krn(g_krn,  id)  # get kernel
    c_continuity = c_krn.continuity
    
    return mk_Field(id, c_ity, c_continuity, g_inputfile, c_dim, g_coeff_style, g_ucoeff, c_krn, g_template)

#creating an application operator
def set_App(c_opr, lhs, rhs, otype1):
    return apply("opr", c_opr, lhs, rhs, otype1, true, true)

# base application
def set_BaseApp(c_opr, lhs, otype1):
    return apply("opr", c_opr, lhs, None, otype1, true, true)
# non base application
def set_UnaryApp(c_opr, lhs, otype1):
    return apply("opr", c_opr, lhs, None, otype1, false, true)


# first argument
def set_first(id,  c_ity, c_opr, c_otype, testing_frame):
    (F1, _, coeff1) = set_fld(id, c_ity, testing_frame)
    #assumes unary
    lhs = F1
    z = set_BaseApp(c_opr, lhs, c_otype)
    return (z, [coeff1])

# internal typechecker
def isValid(c_opr, ishape):
    (tf1, tshape1) = get_tshape(c_opr, ishape,pde_test)
    #find if it is a valid test
    if(not tf1):
        raise Exception( "\n apply blocked from attempting: "+"b__"+name+str(opc.id)+"_")
    return tshape1

#handle it
# assumes all unary operators
def all_unary(opn, ishapen, testing_frame, cnt):
    # get k value of tshape from kernels
    g_krn = frame.get_krn(testing_frame)
    ishape = set_ks(g_krn, ishapen)
    

    # apply first operator
    id = 0
    c_ity = ishape[id]
    c_opr = opn[id]
    c_otype = isValid(c_opr, ishape)
    (app, coeffs) =  set_first(id,  c_ity, c_opr, c_otype, testing_frame)
    
    # apply second operator
    id = 1
    lhs = app
    c_opr = opn[id]
    ishape = [c_otype]
    c_otype = isValid(c_opr, ishape)
    app = set_UnaryApp(c_opr, lhs, c_otype)
    
    # apply third operator
    id = 2
    lhs = app
    c_opr = opn[id]
    ishape = [c_otype]
    c_otype = isValid(c_opr, ishape)
    app = set_UnaryApp(c_opr, lhs, c_otype)

    # apply fourth operator
    id = 3
    lhs = app
    c_opr = opn[id]
    ishape = [c_otype]
    c_otype = isValid(c_opr, ishape)
    app = set_UnaryApp(c_opr, lhs, c_otype)

    return (app, coeffs, c_otype)

#setting variable
def user_sets_test(testing_frame, cnt):
    opn = [op_negation, op_gradient, op_norm, op_negation]
    ishapen = [ty_scalarF_d2]
    (app, coeffs, tshape1) = all_unary(opn, ishapen, testing_frame, cnt)
    core(app, coeffs, tshape1.dim, "t", testing_frame, cnt)
    return
