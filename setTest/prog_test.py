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
from cte_createField import createField,sortField
from cte_writeDiderot import writeDiderot
from cte_eval import eval
from cte_continue import *
from cte_core import *

#creating a test program
from obj_prog import *


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



# first argument
def set_first(id,  c_ity, c_opr, c_otype, testing_frame):
    (F1, _, coeff1) = set_fld(id, c_ity, testing_frame)


# internal typechecker
def isValid(outname, c_opr, c_arg):
    ishape = [c_arg.ty]
    (tf, tshape) = get_tshape(c_opr, ishape)
    #find if it is a valid test
    if(not tf):
        raise Exception( "\n apply blocked")
    # create output variable
    c_var = varname(outname, tshape)
    #create line of operator applied to arguement
    c_line = line(c_var, c_opr, c_arg, None)
    return c_line

# changing the core to write a test from a program.
def core3(program, fields, coeffs, dimF, testing_frame, cnt):
    # get global variables from testing framework
    g_lpos = frame.get_lpos(testing_frame)
    g_upos = frame.get_upos(testing_frame)
    g_num_pos = frame.get_num_pos(testing_frame)
    g_p_Observ = frame.get_p_Observ(testing_frame)
    g_output = frame.get_output(testing_frame)
    g_samples = frame.get_samples(testing_frame)
    g_branch = frame.get_branch(testing_frame)
    g_space = frame.get_space(testing_frame)
    # transform from global variables
    t_isNrrd = frame.transform_isNrrd(testing_frame)
    t_nrrdbranch = frame.transform_nrrdpath(testing_frame)
    t_runtimepath = frame.transform_runtimepath(testing_frame)

    # testing positions
    positions = get_positions(dimF, g_lpos, g_upos, g_num_pos)
    # samples
    #create synthetic field data with diderot
    PARAMS = sortField(fields, g_samples, coeffs, t_nrrdbranch, g_space)
    #create diderot program with operator
    (isCompile, isRun) = writeDiderot(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd)



#setting variable
def attempt(testing_frame, cnt):
    # create only field varoable
    c_ity = ty_scalarF_d3
    c_name = "F"
    var_F = varname(c_name, c_ity)
    (F1, _, coeff1) = set_fld(c_name, c_ity, testing_frame)
    coeffs = [coeff1]
    dimF = c_ity.dim
    
    # create lines of program
    l1 = isValid("gF", op_gradient, var_F)
    l2 = isValid("g", op_negation, l1.var)
    l3 = isValid("norm", op_normalize, l1.var)
    #create program
    lines  = [l1, l2, l3]
    p1 = prog("curvature", lines)
    core3(prog, [F1], coeffs, dimF, testing_frame, cnt)
     

    #core(app, coeffs, tshape1.dim, "t", testing_frame, cnt)
    return
