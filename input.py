
#include <math.h>
import sys
from base_constants import *
from obj_frame import *



#--------------------- Testing envt parameters ------------------------------------------
#------ Different Field Definitions(choose one) -----------------
#s_field = field_conv # type of field
s_field = field_cfe
#s_field = field_pde
#-------------- ---------------Parameters -----------------------
# Number of operations in  a core computaiton
s_layer = 2
# probably of a single test being executed
s_random_range = 99

#--------------------- New user (look here) ---------------------
# note need to change path in fem/Makefile
s_path=  "/Users/chariseechiw/diderot/"
# "the path to diderot compilers^"
#-------------- Branch (choose one) ------------------------------
#s_branch  = branch_vis15
#s_branch  = branch_ein16
#s_branch  = branch_other
#s_branch = branch_chiw17
s_branch = branch_dev
#s_branch = branch_fem


#----------------------------------- Data details ---------------------------------
#-------------- Precision(choose one) ----------------------------
s_precision = precision_double
#s_precision = precision_single
#-------------- order of coefficients(choose one) ----------------
# order of coefficients
s_coeff_style = coeff_linear
#s_coeff_style = coeff_quadratic
#s_coeff_style = coeff_cubic
#-------------- Type of element(choose one) ----------------------
#s_element = elem_Lagrange
#s_element = elem_P
s_element = elem_random
#-------------- Length of Mesh ------- ---------------------------
s_length = 4
# kernel
#-------------- Convolution kernel (choose one)-------------------
#s_krn = h_bs5
s_krn = h_hex
#s_krn = h_bs3
#s_krn = h_tent
#s_krn = h_ctmr
#s_krn = h_mixcbc
#------------------- Type of inputs (choose one)-------------------
# what type of arguments do we want to test?
#s_in_tys  = ty_All
s_in_tys  = ty_F # when doing PDE
#s_in_tys  = ty_T
#------------------ Type of results (choose one)-------------------
# op1(t1) -> t2, what is the type of t2?
#s_rst_ty  = ty_All
s_rst_ty  =  ty_F
#s_rst_ty  =  ty_T
#------------------ Other -------------------
# other text that will get printed with results (optional)
name = "currrent"
s_revision = "r current"
#--------------------------------------------------------------------------------

def setTemplate(template):
    #-------------- randomize ----------------------
    #randomize angle and shear?
    s_space = False
    s_random_limit = 800000000
    #-------------- constants ----------------------
    #coeff bounds
    s_ucoeff_range = 5
    #position bounds
    s_lpos =  -0.4
    s_upos = 0.4
    # number of positions
    s_num_pos = 7 #10
    # number of samples
    s_samples = 70

    return frame(name, s_branch, s_revision, s_precision, s_path, s_coeff_style, s_in_tys, s_rst_ty, s_ucoeff_range, s_lpos, s_upos, s_num_pos, s_samples, s_krn,s_random_range,s_random_limit, s_space, s_layer,template,s_element,s_length)

#--------------------------------------------------------------------------------
########## frames ######
def get_testing_frame():
    return setTemplate(template_isPlain)

# set template for initial frame
def set_template(template):
    if (template==1):
        return setTemplate(template_isMipMax)
    elif (template==2):
        return setTemplate(template_isMipSum)
    elif (template==3):
        return setTemplate(template_isIso)
    return setTemplate(template_isPlain)
