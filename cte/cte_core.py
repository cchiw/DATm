import sys
import re
import os
import random


#top-level
from input import  *

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_field import *
from obj_counter import *
from obj_frame import *
from base_write import *
from base_var_ty import *
from base_observed import observed

#specific nc programs
from nc_compare import compare
from nc_continue import check
from nc_createField import sortField

# specific cte programs
from cte_writeDiderot import writeDiderot
from cte_eval import eval

pde_test=false# test pdes in femprime branche

# results from testing
def analyze(name_file, name_ty, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, branch):
    (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) =  rtn
    #print "X", x
    x = "\n-"+name_file+" "+name_describe+"| "+name_ty+"| "+rtn_1
    writeall(x)
    print  (x)
    
    # collect results
    counter.inc_locals(cnt, rtn)
    #writeCumulative(cnt)
    # check results
    if (rst_check_1==7):
        rst_check(fname_file, x, name_describe, branch, observed_data, correct_data)
    elif (rst_terrible_1==1):
        rst_terrible(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)

    elif (rst_NA_1==9):
         rst_NA(name_file, x, name_describe,  branch)
             #elif (rst_good_1==1 or rst_eh_1==1):
    #elif(rst_good_1==1):
    #raise Exception ("stop")
    #rst_good(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
    return

##################################################################################################
##################################################################################################

# already created app object
def cte_core(app, coeffs, dimF, names, testing_frame, cnt):
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
    g_space = frame.get_space(testing_frame)
    # transform from global variables
    t_isNrrd = frame.transform_isNrrd(testing_frame)
    t_nrrdbranch = frame.transform_nrrdpath(testing_frame)
    t_runtimepath = frame.transform_runtimepath(testing_frame)
    
    fnames = apply.get_all_FieldTys(app)
    x = "_"+fnames +" |"+names
    writetys(x)
    name_describe = app.name
    # testing positions
    positions = get_positions(dimF, g_lpos, g_upos, g_num_pos)
    
    #create synthetic field data with diderot
    flds = apply.get_all_Fields(app)
    (PARAMS,all50,all51,all52,all53,all54,all55) = sortField(flds, g_samples, coeffs, t_nrrdbranch, g_space)
    #create diderot program with operator
   

    print (name_describe+x)
    (isCompile, isRun, startall) = writeDiderot(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd, startall)
    if(isRun == None):
  
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
            return 1
        else:
            counter.inc_run(cnt)
            rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
            return 2
    else:
        observed_data = observed(app, g_output)
        if(check(app, observed_data)):
            correct_data = eval(app , positions)
            ex_otype = fty.get_tensorType(app.oty)
            rtn = compare(app.oty, app.name, observed_data, correct_data)
            analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)

            return 3
        else:
            
            return None
