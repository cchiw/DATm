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

# specific prog programs
from obj_prog import *
from prog_test import *
from prog_core import *


#setting variable
def attempt(testing_frame, cnt):
    # create only field varoable
    c_ity = ty_scalarF_d3
    #Expects input field to be F0
    c_name = "F0"
    
    (F1, _, coeff1) = set_fld(c_name, c_ity, testing_frame)
    var_F = varname(c_name, c_ity, F1)
    coeffs = [coeff1]
    dimF = c_ity.dim
    
    #Expects last line,output to be G
    
    # create lines of program
    l1 = isValid("grad", op_gradient, var_F, None)
    l2 = isValid("neg", op_negation, l1.var, None)
    l3 = isValid("G", op_normalize, l1.var, None)
    #l4 = isValid("G", op_hessian, var_F, None)
    #l5 = isValid("G", op_outer, l3.var, l3.var)
    #create program
    lines  = [l1, l2, l3]
    p1 = prog("curvature", lines, l3.var.ty)
    core3(p1, [F1], coeffs, dimF, testing_frame, cnt)
     

    #core(app, coeffs, tshape1.dim, "t", testing_frame, cnt)
    return
