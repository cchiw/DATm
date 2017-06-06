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
from base_observed import base_observed
#specific nc programs
from nc_compare import compare
from nc_createField import sortField

#creating a test program
from obj_prog import *
from prog_writeDiderot import prog_writeDiderot
from prog_eval import prog_eval

# results from testing
def analyze(name_file, name_ty, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, branch):
    (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) =  rtn
    #print "X", x
    x = "\n-"+name_file+" "+name_describe+"| "+name_ty+"| "+rtn_1
    writeall(x)
    print  x
    
    
    # collect results
    counter.inc_locals(cnt, rtn)
    writeCumulative(cnt)
    # check results
    if (rst_check_1==7):
        rst_check(fname_file, x, name_describe, branch, observed_data, correct_data)
    elif (rst_terrible_1==1):
        rst_terrible(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
    #raise Exception("terrible")
    elif (rst_NA_1==9):
        rst_NA(name_file, x, name_describe,  branch)
    return

# changing the core to write a test from a program.
def core3(program, dict, testing_frame, cnt):
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

    fields = program.fields
    coeffs = program.coeffs
    dimF = program.dim
    
    # testing positions
    positions = get_positions(dimF, g_lpos, g_upos, g_num_pos)
    # samples
    #create synthetic field data with diderot
    PARAMS = sortField(fields, g_samples, coeffs, t_nrrdbranch, g_space)
    print "**************** write program"
    name = program.name
    name_ty = fields[0].fldty.name
    (isCompile, isRun, _) = prog_writeDiderot(g_p_Observ, program, fields, positions, g_output, t_runtimepath, t_isNrrd)
    if(isRun == None):
       
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(name, name_ty, program.name, g_branch,  positions, PARAMS)
            return 1
        else:
            counter.inc_run(cnt)
            rst_execute(name, name_ty, program.name, g_branch,  positions, PARAMS)
            return 2
    else:
        print "*****************************read observed data"
        observed_data = base_observed(program.oty, g_output)
        #if(check(app, observed_data)):
        print "*****************************prog eval"
        correct_data = prog_eval(program, positions, dict)
        print "***************************** compare"
        rtn = compare(program.oty, program.name, observed_data, correct_data)
       
        analyze(program.name, name_ty, program.name, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)
        #return 3
        # else:
        #return None