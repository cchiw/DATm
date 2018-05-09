import sys
import re
import os
import random


#top-level
from input import  *

# shared base programs
from obj_apply import *
from obj_counter import *
from obj_frame import *
from base_write import *
from base_observed import observed

#specific nc programs
from nc_compare import compare
from nc_continue import check
from cte_eval import eval

# specific cte programs
from cfe_writeDiderot import cfe_writeDiderot


##################################################################################################
##################################################################################################

# already created app object
def cfe_core(app, coeffs, dimF, names, testing_frame, cnt):
    endall = time.time()
    startall=time.time()
    # get global variables from testing framework
    g_lpos = frame.get_lpos(testing_frame)
    g_upos = frame.get_upos(testing_frame)
    g_num_pos = frame.get_num_pos(testing_frame)
    g_p_Observ = frame.get_p_Observ(testing_frame)
    g_output = frame.get_output(testing_frame)
    g_samples = frame.get_samples(testing_frame)
    g_branch = frame.get_branch(testing_frame)

    # transform from global variables
    t_isNrrd = frame.transform_isNrrd(testing_frame)
    t_nrrdbranch = frame.transform_nrrdpath(testing_frame)
    t_runtimepath = frame.transform_runtimepath(testing_frame)
    
    fnames = apply.get_all_FieldTys(app)
    x = "_"+fnames +" |"+names
    writetys(x)
    name_describe = app.name
    print (name_describe+x)
   
    
    # testing positions
    positions = get_positions(dimF, g_lpos, g_upos, g_num_pos)
    #create synthetic field data with diderot
    flds = apply.get_all_Fields(app)

    # field operations is used
    if(app.opr.fieldop or app.lhs.opr.fieldop):
        if(s_field == field_cfe_post):
            return 2
        elif(s_field == field_cfe_wrap and dimF>1):
            return 2
    (isCompile, isRun, startall) = cfe_writeDiderot(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd, startall)

    PARAMS = ""
    
    if(isRun == None):
  
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
            #raise Fail("does not compile")
            return 1
        else:
            counter.inc_run(cnt)
            rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
            #raise Fail("does not run")
            return 2
    else:
        observed_data = observed(app, g_output)
        #print("observed:",observed_data)
        if(check(app, observed_data)):
            correct_data = eval(app , positions)
            #print("correct:",correct_data)
            ex_otype = fty.get_tensorType(app.oty)
            rtn = compare(app.oty, app.name, observed_data, correct_data)
            analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)
            return 3
        else:
            
            return None
