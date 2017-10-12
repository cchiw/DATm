
#include <math.h>
import sys
from base_constants import *

s_layer = 2

s_random_range =99
from obj_frame import *
cpath =  "/Users/chariseechiw/diderot/"
# note need to change path in fem/Makefile

# want to make your own testing frame?
# go for it!
# options are commented out


name = "currrent"
# branch information
#s_branch  = branch_vis15
#s_branch  = branch_ein16
s_branch  = branch_other
#s_branch = branch_chiw17

s_revision = "r current"
s_precision = precision_double  #precision_single
s_path = cpath # "--whatever the path to diderot is"

# order of coefficients
s_coeff_style = coeff_linear
#s_coeff_style = coeff_quadratic
#s_coeff_style = coeff_cubic


#s_element = elem_Lagrange
#s_element = elem_P
s_element = elem_random

s_length = 4
# kernel
#s_krn = h_bs5
s_krn = h_hex
#s_krn = h_bs3
#s_krn = h_tent
#s_krn = h_ctmr
#s_krn = h_mixcbc
# types
#ty_F ="all fields"
#ty_T ="all tensors"
#ty_All ="mix of tensors and fields"
# what type of arguments do we want to test?
s_in_tys  = ty_All
#s_in_tys  = ty_F # when doing PDE
#s_in_tys  = ty_T

# op1(t1) -> t2, what is the type of t2?

s_rst_ty  = ty_All  #ty_F #ty_T # when doing pDE
#s_rst_ty  =  ty_F #ty_T
#s_rst_ty  =  ty_T


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

#--------------------------------------------------------------------------------

def mk_default(name, s_coeff_style, krn):
    s_precision = precision_double
    #s_branch = branch_ein16
    s_branch = branch_vis15
    #s_branch = branch_other
    s_in_tys  = ty_All
    s_rst_ty  = ty_All
    s_samples = 70 #outSize
    s_num_pos = 7 # number of positions
    s_lpos =  -0.4
    s_upos = 0.4
    s_ucoeff_range = 5
    s_random_range = 0
    s_random_limit = 1000000
    s_path = cpath
    name = krn+"_"+s_coeff_style
    s_space = False
    s_layer = 2
    s_template = template_isPlain
    t_frame = frame(name, s_branch, "current", s_precision, s_path, s_coeff_style, s_in_tys, s_rst_ty, s_ucoeff_range, s_lpos, s_upos, s_num_pos, s_samples, krn, s_random_range,s_random_limit, s_space, s_layer,s_template,s_element,s_length)
    return t_frame

########## frames ######
t_new = frame(name, s_branch, s_revision, s_precision, s_path, s_coeff_style, s_in_tys, s_rst_ty, s_ucoeff_range, s_lpos, s_upos, s_num_pos, s_samples, s_krn,s_random_range,s_random_limit, s_space, s_layer,template_isPlain,s_element,s_length)


frames = [t_new]


def get_testing_frame(n_frame):
    if(len(frames)< n_frame):
        raise Exception ("frame outside range")
    else:
        return frames[n_frame]

# set template for initial frame
def set_template(template):
    t = template_isPlain
    if (template==1):
        t= template_isMipMax
    elif (template==2):
        t= template_isMipSum
    elif (template==3):
        t= template_isIso
    return frame(name, s_branch, s_revision, s_precision, s_path, s_coeff_style, s_in_tys, s_rst_ty, s_ucoeff_range, s_lpos, s_upos, s_num_pos, s_samples, s_krn,s_random_range,s_random_limit, s_space, s_layer,t,s_element,s_length)


# set template for initial frame
def set_templateLR(template, layer, random_range):
    t = template_isPlain
    if (template==1):
        t= template_isMipMax
    elif (template==2):
        t= template_isMipSum
    elif (template==3):
        t= template_isIso
    return frame(name, s_branch, s_revision, s_precision, s_path, s_coeff_style, s_in_tys, s_rst_ty, s_ucoeff_range, s_lpos, s_upos, s_num_pos, s_samples, s_krn,random_range,s_random_limit, s_space, layer,t,s_element,s_length)


