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
from nc_compare import compare,compare_zero
from nc_continue import check
from nc_createField import sortField

# specific fem programs
from fem_main import writeTestPrograms


#from fem_eval import eval
sys.path.insert(0, 'cte/')
from cte_eval import eval

pde_test=true # test pdes in femprime branche
test_new = false # new type of test

def cleanup(output, p_out):
    os.system("rm ex1.o")
    os.system("rm ex1_init.o")
    os.system("rm ex1_init.so")
    os.system("rm ex1.cxx")
    os.system("rm ex1.diderot")
    os.system("rm *.c")
    os.system("rm *.h")
    os.system("rm *.txt")
    os.system("rm *.nrrd")
    os.system("rm observ.diderot")
    os.system("rm "+output+"*")
    os.system("rm cat.nrrd")
    os.system("rm  "+p_out+".nrrd")
    os.system("rm  "+output+".txt")
    os.system("rm  "+p_out+".txt")

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
             #elif (rst_good_1==1):
             #rst_good(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
    return

##################################################################################################
##################################################################################################

# already created app object
def fem_core(app, coeffs, dimF, names, testing_frame, cnt):
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
    g_element = frame.get_element(testing_frame)
    g_length = frame.get_length(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame)
    # transform from global variables
    t_isNrrd = frame.transform_isNrrd(testing_frame)
    t_nrrdbranch = frame.transform_nrrdpath(testing_frame)
    t_runtimepath = frame.transform_runtimepath(testing_frame)
    
    fem_core_fieldsOrig = apply.get_all_Fields(app)
    fem_core_fields = []
    # limit fem_core fields by the ones we can rep.
    if(not (fty.is_Field(app.oty))):
        return
    
    for e in fem_core_fieldsOrig:
        ty = e.fldty
        #print "ty name:",ty.name,ty.space
        dim =ty.dim
        shapen = len(ty.shape)
        if(dim==1):
            return
        elif(shapen>2):
            return
        fem_core_fields.append(field.addSpace(e, g_element,g_coeff_style, g_length ))
        
    for e in fem_core_fields:
        ty = e.fldty
        #print "ty name:",ty.name,ty.space

    counter.inc_cumulative(cnt)
    fnames = apply.get_all_FieldTys(app)
    x = "_"+fnames +" |"+names
    print (x)
    writetys(x)
    #print "*******************************************"
    # testing positions
    # note here should set positions based on space
    l_lpos = 0.0
    l_rpos = 1.0
    positions = get_positions(dimF, l_lpos, l_rpos, g_num_pos)

    writetys(x)
    name_describe = app.name
    # samples
    #create synthetic field data with diderot
    ##PARAMS,all50,all51,all52,all53,all54,all55) = sortField(fem_core_fields, g_samples, coeffs, t_nrrdbranch, g_space)
    PARAMS =""
    #create diderot program with operator
    cleanup(g_output, g_p_Observ)
    (isCompile, isRun, startall) = writeTestPrograms(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd, startall, fem_core_fields)
    if(isRun == None):
        writeTime("hold", "0")
        writeTime("hold", "0")
        writeTime("hold", "0") 
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
            return 
        else:
            counter.inc_run(cnt)
            rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
            return
        
    else:
        observed_data = observed(app, g_output)

        if(check(app, observed_data)):
            correct_data = eval(app, positions)
            rtn = compare(app.oty, app.name, observed_data, correct_data)
            analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)
                          
            return 
        else:
            counter.inc_NA(cnt)
            writeTime("hold", "0")
            writeTime("hold", "0")
            writeTime("hold", "0")
            return 

