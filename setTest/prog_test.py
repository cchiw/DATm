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
def isValid(outname, c_opr, c_arg1, c_arg2):
    ishape = [c_arg1.ty]
    (tf, tshape) = get_tshape(c_opr, ishape)
    #find if it is a valid test
    if(not tf):
        raise Exception( "\n apply blocked")
    # create output variable
    c_var = varname(outname, tshape, None)

    #create line of operator applied to arguement
    c_line = line(c_var, c_opr, c_arg1, c_arg2)

    return c_line
