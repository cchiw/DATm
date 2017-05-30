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

# specific cte programs
from cte_createField import createField,sortField
from cte_writeDiderot import writeDiderot
from cte_eval import eval
from cte_continue import *


#creating a test program
from obj_prog import *
from prog_writeDiderot import prog_writeDiderot
from prog_eval import prog_eval

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
    (isCompile, isRun, _) = prog_writeDiderot(g_p_Observ, program, fields, positions, g_output, t_runtimepath, t_isNrrd)
    if(isRun == None):
        raise Exception( "failed")
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
            return 1
        else:
            counter.inc_run(cnt)
            rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
            return 2
    else:
        observed_data = base_observed(program.oty, g_output)
        #if(check(app, observed_data)):
        correct_data = prog_eval(program, positions)
        rtn = compare(app, observed_data, correct_data)
        analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)
        #return 3
        # else:
        #return None