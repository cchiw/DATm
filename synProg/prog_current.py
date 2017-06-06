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



def setProg(name, lines, lines2, fields, dimF, coeffs):

    
    if(len(lines2)==0):
        #make the last line G.
        n = len(lines)-1
        linef = lines[0:n]
        linen = lines[n]
        oty = linen.var.ty
        oname = "G"
        ovar = varname(oname, oty, None)
        oline = line(ovar, linen.opr, linen.lhs, linen.rhs)
        return prog(name, linef+[oline], lines2, oty, fields, dimF, coeffs)
    n = len(lines2)-1
    linef = lines2[0:n]
    linen = lines2[n]
    oty = linen.var.ty
    oname = "out"
    ovar = varname(oname, oty, None)
    oline = line(ovar, linen.opr, linen.lhs, linen.rhs)
    return prog(name, lines, linef+[oline], oty, fields, dimF, coeffs)

#setting variable
#Expects input field to be F0
#Expects last line,output to be G
def getProgram_curv(testing_frame):
    # create only field varoable
    c_ity = ty_scalarF_d3
    c_name = "F0"
    (F1, _, coeff1) = set_fld(c_name, c_ity, testing_frame)
    var_F = varname(c_name, c_ity, F1)
    dimF = c_ity.dim
    coeffs = [coeff1]
    # get constant identity matrix. Initialize with k value
    fixed_id3F = getConst_id3(1, true)
    fixed_n2 = getConst_n2(1)
    #dictionary from variable to fields
    dict = {}
    dict[var_F.name] = var_F.field
    dict[fixed_id3.name] = fixed_id3.field
    dict[fixed_n2.name] = fixed_n2.field
    id=0
    # create lines of program
    l0 = isValid(id,"del", op_gradient, var_F, None)
    l1 = isValid(id+1,"grad", op_negation, l0.var, None)
    l2 = isValid(id+2,"norm", op_normalize, l1.var, None)
    l3 = isValid(id+3,"hessian", op_hessian, var_F, None)
    l4 = isValid(id+4,"outer", op_outer, l2.var, l2.var)
    
    l5 = isValid(id+5,"P", op_subtract, fixed_id3F, l4.var)
    l6 = isValid(id+6,"PH", op_inner, l5.var, l3.var)
    l7 = isValid(id+7,"PHP", op_inner, l6.var, l5.var)
    l8 = isValid(id+8,"nPHP", op_negation, l7.var, None)
    l9 = isValid(id+9,"normgrad", op_norm, l1.var, None)
    l10 = isValid(id+10,"GG", op_division, l8.var, l9.var)
    l11 = isValid(id+11,"Gnorm", op_norm, l10.var, None)
    l12 = isValid(id+12,"GnormSq", op_scale, l11.var, l11.var)
    l13 = isValid(id+13,"scale2", op_scale, fixed_n2, l12.var)
    l14 = isValid(id+14,"traceG", op_trace, l10.var, None)
    l15 = isValid(id+15,"traceGSq", op_scale, l14.var, l14.var)
    l16 = isValid(id+16,"discsubt", op_subtract, l13.var, l15.var)
    l17 = isValid(id+17,"disc", op_sqrt, l16.var, None)
    l18 = isValid(id+18,"discAdd", op_add, l14.var, l17.var)
    l19 = isValid(id+19,"k1", op_division, l18.var, fixed_n2)
    l20 = isValid(id+20,"discSubt", op_subtract, l14.var, l17.var)
    l21 = isValid(id+21,"k2",op_division, l20.var, fixed_n2)
    #create program
    lines1 = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16,l17,l18,l19,l20, l21]
    lines2 = []
    p1 = setProg("curvature", lines1, lines2, [F1], dimF, coeffs)
    return (p1, dict)


def getProgram_crest(testing_frame):
    # create only field varoable
    c_ity = ty_scalarF_d3
    c_name = "F0"
    (F1, _, coeff1) = set_fld(c_name, c_ity, testing_frame)
    c_ity = F1.fldty
    var_F = varname(c_name, c_ity, F1)
    dimF = c_ity.dim
    coeffs = [coeff1]
    # get constant identity matrix. Initialize with k value
    fixed_id3F = getConst_id3(3, true)
    fixed_id3T = getConst_id3(3, false)
    
    fixed_n2 = getConst_n2(3)
    #dictionary from variable to fields
    dict = {}
    dict[var_F.name] = var_F.field
    dict[fixed_id3F.name] = fixed_id3F.field
    dict[fixed_n2.name] = fixed_n2.field
    
    # create lines of program for curvature
    id= 0
    l0 = isValid(id,"del", op_gradient, var_F, None)
    l1 = isValid(id+1,"grad", op_negation, l0.var, None)
    l2 = isValid(id+2, "norm", op_normalize, l1.var, None)
    l3 = isValid(id+3,"hessian", op_hessian, var_F, None)
    l4 = isValid(id+4,"outer", op_outer, l2.var, l2.var)
    l5 = isValid(id+5,"P", op_subtract, fixed_id3F, l4.var)
    l6 = isValid(id+6,"PH", op_inner, l5.var, l3.var)
    l7 = isValid(id+7,"PHP", op_inner, l6.var, l5.var)
    l8 = isValid(id+8,"nPHP", op_negation, l7.var, None)
    l9 = isValid(id+9,"normgrad", op_norm, l1.var, None)
    l10 = isValid(id+10,"GG", op_division, l8.var, l9.var)
    l11 = isValid(id+11,"Gnorm", op_norm, l10.var, None)
    l12 = isValid(id+12,"GnormSq", op_scale, l11.var, l11.var)
    l13 = isValid(id+13,"scale2", op_scale, fixed_n2, l12.var)
    l14 = isValid(id+14,"traceG", op_trace, l10.var, None)
    l15 = isValid(id+15,"traceGSq", op_scale, l14.var, l14.var)
    l16 = isValid(id+16,"discsubt", op_subtract, l13.var, l15.var)
    l17 = isValid(id+17,"disc", op_sqrt, l16.var, None)
    l18 = isValid(id+18,"discAdd", op_add, l14.var, l17.var)
    l19 = isValid(id+19,"k1", op_division, l18.var, fixed_n2)
    l20 = isValid(id+20,"discSubt", op_subtract, l14.var, l17.var)
    l21 = isValid(id+21,"k2",op_division, l20.var, fixed_n2)
    ######################################### crest line  #########################################
    # attempting to probe
#    id = id+21
#    lk1 = isValid(id+1, "k1tensor", op_probe, l19.var, None)
#    lk2 = isValid(id+2, "k2tensor", op_probe, l21.var, None)
#    lGG = isValid(id+3, "Gtensor", op_probe, l10.var, None)
#    id=id+3
#    var_k1 = lk1.var
#    var_k2 = lk2.var
#    var_g = lGG.var
#    id3 = fixed_id3T
    ######################################### all fields #########################################
    #### all field setting
    var_k1 = l19.var
    var_k2 = l21.var
    id3 = fixed_id3F
    var_g = l10.var
    
    #create lines of program for crest program
    l22 = isValid(id+1,"E1a", op_scale, id3, var_k2)
    l23 = isValid(id+2,"E2a", op_scale, id3, var_k1)
    l24 = isValid(id+3,"E1b", op_subtract, var_g, l22.var)
    l25 = isValid(id+4,"E2b", op_subtract, var_g, l23.var)
    l26 = isValid(id+5,"E1c", op_normalize, l24.var, None)
    l27 = isValid(id+6,"E2c", op_normalize, l25.var, None)
    # handle E1 side
    l28 = isValid(id+28,"delk1", op_gradient, l19.var, None)
    l29 = isValid(id+29,"gk1", op_inner, l26.var, l28.var)
    l30 = isValid(id+30,"fdd1", op_norm, l29.var, None)
    l31 = isValid(id+31,"dir", op_normalize, l29.var, None)
    l32 = isValid(id+32,"sdd1a", op_hessian, l19.var, None)
    l33 = isValid(id+33,"sdd1b", op_inner, l31.var, l32.var)
    l34 = isValid(id+34,"sdd1c", op_inner, l33.var, l31.var)
    
    #create program
    lines1 = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16,l17,l18,l19,l20, l21]
    linesk = [l22,l23,l24,l25,l26,l27, l28, l29, l30, l31,l32, l33, l34]
    lines2 = []#[lk1, lk2, lGG]+linesk
    p1 = setProg("crest lines", lines1+linesk, lines2, [F1], dimF, coeffs)
    return (p1, dict)

def buildProgram(testing_frame, cnt):
    (p1, dict) = getProgram_crest(testing_frame)
    lines1 = p1.lines1
    lines2 = p1.lines2
    linesT= []
    for i in range(len(lines1)):
        l = lines1[i]
        linesT=linesT+[l]
        p2 = setProg("curvature_"+str(i), linesT, lines2, p1.fields, p1.dim, p1.coeffs)
        core3(p2, dict, testing_frame, cnt)
    return


def fullProgram(testing_frame, cnt):
    (p1, dict) = getProgram_crest(testing_frame)
    core3(p1, dict, testing_frame, cnt)
    return



setting = 2
def attempt(testing_frame, cnt):
    if(setting==1):
        fullProgram(testing_frame, cnt)
    elif(setting==2):
        buildProgram(testing_frame, cnt)