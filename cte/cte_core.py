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

#specific nc programs
from nc_compare import compare
from nc_continue import check
from nc_createField import sortField

# specific cte programs
from cte_writeDiderot import writeDiderot
from cte_eval import eval

# results from testing
def analyze(name_file, name_ty, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, branch):
    (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) =  rtn
    #print "X", x
    x = "\n-"+name_file+" "+name_describe+"| "+name_ty+"| "+rtn_1
    writeall(x)
    print  x

    
    # collect results
    counter.inc_locals(cnt, rtn)
    #writeCumulative(cnt)
    # check results
    if (rst_check_1==7):
        rst_check(fname_file, x, name_describe, branch, observed_data, correct_data)
    elif (rst_terrible_1==1):
        rst_terrible(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
        #raise Exception("terrible")
    elif (rst_NA_1==9):
         rst_NA(name_file, x, name_describe,  branch)
    return

##################################################################################################
##################################################################################################

# make choice if we should continue
def mk_choice_range(testing_frame, cnt):
    random_range  = frame.get_random_range(testing_frame)
    return (not random.randint(0, random_range))


# already created app object
def core2(app, coeffs, dimF, names, testing_frame, cnt):
    #writeTime(100,"\n\n\n\n")
    #startall = time.time()
    #writeTime(125, str(startall))
    print "############################################inside central############################################"

    
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
    
    #print "*******************************************"
    fnames = apply.get_all_FieldTys(app)
    x = "_"+fnames +" |"+names
    print (x)
    writetys(x)
    name_describe = app.name

    # testing positions
    #endall = time.time()
    #tall = str(endall - startall)
    #writeTime(21, tall)
    #startall=endall
    positions = get_positions(dimF, g_lpos, g_upos, g_num_pos)
    # samples
    #endall = time.time()
    #tall = str(endall - startall)
    #writeTime(22, tall)
    #startall=endall
    
    #create synthetic field data with diderot
    flds = apply.get_all_Fields(app)
    (PARAMS,all50,all51,all52,all53,all54,all55) = sortField(flds, g_samples, coeffs, t_nrrdbranch, g_space)
    #create diderot program with operator
   


    endall = time.time()
    #tall = endall - startall
    #writeTime(100,"n\n")
    #writeTime(50, str(all50))
    #writeTime(50, str(all51))
    #writeTime(50, str(all52))
    #writeTime(50, str(all53))
    #writeTime(50, str(all54))
    #writeTime(50, str(all55))
    #writeTime(50, str(tall-(all50+all51+all52+all53+all54+all55)))
    #writeTime(100,"n\n")
    startall=endall

    (isCompile, isRun, startall) = writeDiderot(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd, startall)
    #endall = time.time()
    #tall = str(endall - startall)
    #writeTime(27, tall)
    #startall=endall


    if(isRun == None):
  
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
           
            return 1
        else:
            counter.inc_run(cnt)
            rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
            raise Exception("stop after 1")
            return 2
    else:
        #print "read observed data"
        observed_data = observed(app, g_output)
        #endall = time.time()
        #tall = str(endall - startall)
        #writeTime(28, tall)
        #startall=endall
        #correct_data = eval(app , positions)
        if(check(app, observed_data)):
            correct_data = eval(app , positions)
            #endall = time.time()
            #tall = str(endall - startall)
            #writeTime(29, tall)
            #startall=endall
            #print "observed data:", observed_data
            #print "correct data:", correct_data
            ex_otype = fty.get_tensorType(app.oty)
            rtn = compare(app.oty, app.name, observed_data, correct_data)
            #endall = time.time()
            #tall = str(endall - startall)
            #writeTime(30, tall)
            #startall=endall
            analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)
            #endall = time.time()
            #tall = str(endall - startall)
            #writeTime(31, tall)
            #startall=endall
            return 3
        else:
            #writeTime(29, "0")
            #writeTime(30, "0")
            #writeTime(31, "0")
            
            return None


def core(app, coeffs, dimF, names, testing_frame, cnt):
    writetys("\n\t***"+app.name)
    writetys("\n\t-"+apply.get_all_FieldTys(app)+"|"+  names)
    counter.inc_cnt(cnt)
    #writeTime(13)
    if(mk_choice_range(testing_frame, cnt)):
        counter.inc_cumulative(cnt)
        
        rtn = core2(app, coeffs, dimF, names, testing_frame, cnt)
        if(rtn==None):
#            core2(app, coeffs, dimF, names, testing_frame, cnt)
#            if(rtn==None):
#                fnames = apply.get_all_FieldTys(app)
#                x = "_"+fnames +" |"+names
#                name_describe = app.name
#                g_branch = frame.get_branch(testing_frame)
#                counter.inc_NA(cnt)
#                rst_NA(names, x, name_describe, g_branch)
            fnames = apply.get_all_FieldTys(app)
            x = "_"+fnames +" |"+names
            name_describe = app.name
            g_branch = frame.get_branch(testing_frame)
            counter.inc_NA(cnt)
            rst_NA(names, x, name_describe, g_branch)

    else:
        return


##################################################################################################
##################################################################################################


##################################################################################################
# functions create app objects
# get example from list of examples
def create_single_app(ex, opr_inner, t_num, testing_frame, cnt):
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_rst_ty = frame.get_rst_ty(testing_frame)
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
    
    opr = opr_inner
    #ex = oprToEx(opr_inner, testing_frame, cnt)
    (name,ishape)= get_single_exampleEx(ex, t_num)
    # get k value of tshape from kernels
    ishape = set_ks(g_krn, ishape)
    #print "calling tshape"
    #print opr_inner.name,ishape[0].name
    (tf1, tshape1) = get_tshape(opr_inner,ishape)
    #print "post get-tshape"
    #print tf1, tshape1
    if(not tf1):
        write_terrible("\n apply blocked from attempting: "+"b__"+name+str(opr_inner.id)+"_"+str(t_num))
        return None
    #print "after calling tshape"
    #create app object

    (app, coeffs) = mkApply_fld(name, opr, ishape, g_inputfile, tshape1, g_coeff_style, g_ucoeff, g_krn,g_template)
    dimF = tshape1.dim
    names= "s_"+str(opr_inner.id)+"__"+"n_"+str(t_num)+"_"
    core(app, coeffs, dimF, names, testing_frame, cnt)
    return

def getdata(opr_inner, opr_outer, testing_frame, cnt):
    # break
    #y = Title_outer(opr_inner, opr_outer)
    #x = "\n -- shapes:"
    #for i in ishape:
    #x+=i.name+","
    #   writeall(y+x)
    #   counter.inc_cumulative(cnt)
    #   counter.inc_cnt(cnt)
    #   write_results(y, testing_frame, cnt)
    return



def convert_fields(ishape,testing_frame):
    g_krn = frame.get_krn(testing_frame)
    x = set_ks(g_krn, ishape)
    return x


def get_all_extra(testing_frame):
    g_rst_ty = frame.get_rst_ty(testing_frame)
    g_in_tys = frame.get_in_tys(testing_frame)
    l = get_all_types(g_rst_ty,g_in_tys)
    return l

# how test cases are labeled
def generate_name(oprs, tys, s):
    cnt = 0
    title = "p"
    for i in oprs:
        title+= "_o"+str(i.id)

    for i in tys:
        if(i==None):
            title+= "_tN"
        else:
            title+= "_t"+str(i)

    title =  title+"_"+(s)
    #print "title", title
    return title



########################################################################
def create_apply2(ishape, tshape1, tshape2, opr_inner, opr_outer,  testing_frame):
    #writeTime(11)
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
    (app, coeffs) = mkApply_twice(opr_inner,opr_outer, ishape, g_inputfile, tshape1, tshape2, g_coeff_style, g_ucoeff, g_krn, g_template )
    print "___________________", app.oty.name
    print "___________________", app.lhs.oty.name
    return (app, coeffs)


def create_apply3_then_core(ishape, appname, opr_outer2, tshape3, ztwice, coeffstwice, title, testing_frame, cnt):
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
    (app, coeffs) = mkApply_third(ztwice, coeffstwice, ishape, tshape3, appname, opr_outer2, g_inputfile, g_coeff_style, g_ucoeff, g_krn,g_template)
    dimF = tshape3.dim
    # main part
    core(app, coeffs, dimF, title, testing_frame, cnt)


 # generate third layer
#ztwice, coeffstwice: result of application of second layer
def get_tshape3(app, coeffs, ishape, tshape2, oprs, tys, newtys, testing_frame, cnt):
    [opr_inner, opr_outer1, opr_outer2] = oprs
    #print "****************************************  get_tshape3 ************************************"
    # third layer operator, and second type it is applied to (incase it is a binary)
    tmpshape = []
    s = ""
    print "opr_outer2", opr_outer2.name
    print "opr_outer1", opr_outer1.name
    print "opr_inner:", opr_inner.name
    print "tys", tys
    if(opr_outer2.arity==2):
        ty3 = get_all_extra(testing_frame)
        [i] = newtys
        t_ty3 = ty3[i]
        tmpshape = [t_ty3]
        s = s+ "_t"+str(t_ty3)
    elif(opr_outer2.arity==3):
        ty3 = get_all_extra(testing_frame)
        [i, j] = newtys
        t_ty3 = ty3[i]
        t_ty4 = ty3[j]
        tmpshape = [t_ty3, t_ty4]
        s = s+ "_t"+str(t_ty3)+ "_t"+str(t_ty4)

    counter.inc_total(cnt)
    # add new shape argment
    ishape_outer2 = [tshape2] + tmpshape
    ishape_all = ishape + tmpshape
    ishape_all = convert_fields(ishape_all, testing_frame)
    print "trying to match opr_outer2", opr_outer2.name ,"with ",tshape2.name
    for j in tmpshape:
        print "-- shape", j.name
    # ok now back to regular programming
    (tf3, tshape3) = get_tshape(opr_outer2, ishape_outer2)
    if(tf3==true):#
        writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        appname = opr_outer2.name+"("+opr_outer1.name+"("+opr_inner.name+")"+")"
        #print "appname :",appname
        tys =tys+newtys
        title =  generate_name(oprs, tys, "_l3")
        create_apply3_then_core(ishape_all, appname, opr_outer2, tshape3, app, coeffs, title, testing_frame, cnt)


#iterate over extra possible type
def iter_ty3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt):
    [opr_inner, opr_outer1, opr_outer2] = oprs
    def f(newtys):
        get_tshape3(app, coeffs, ishape, tshape2, oprs, tys, newtys, testing_frame, cnt)
    arity =opr_outer2.arity
    ty3 = get_all_extra(testing_frame)
    if(arity==1):
        f([])
    elif(arity==2):
        for t_ty3 in range(len(ty3)):  #extra type
            f([t_ty3])
    elif(arity==3):
        for t_ty3 in range(len(ty3)):
            for t_ty4 in range(len(ty3)):
                f([t_ty3, t_ty4])
    return

# iterating over third operator
def get_tshape3_iterop3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt):
    print "gettshap3-iterop3"
    for opr_outer2 in op_all:
        # next function will type check it and get type
        iter_ty3(app, coeffs, ishape, tshape2, oprs+[opr_outer2], tys, testing_frame, cnt)
    return


# checks to see if specific ex works
def get_tshape2(tshape1, ishape, fty,  oprs, tys, testing_frame, cnt):
    
    print "inside get_tshape 2"
    print "tys:", tys

    #writeTime(9)
    # adjusting to accept 2|3 layers of operators
    #print "in get-tshape print ishape"
    for j in ishape:
        print "-ishape -", j.name
    print "in get tshape1 ",tshape1.name
    opr_inner = oprs[0]
    opr_outer = oprs[1]

    # get value of k from kernels
    ishape = convert_fields(ishape, testing_frame)
    #second layer, adds second field type
    #print "tshape1", tshape1
    #print "fty", fty
    es = [tshape1]+fty
    xy = get_tshape(opr_outer,es)
  
    (tf2, tshape2) =xy
    #print "tshape2", tshape2
    #print "tf2", tf2

    if(tf2==true):# if it works continue
        #create app object
 
        #writeTime(10)
        (app, coeffs) = create_apply2(ishape, tshape1, tshape2, opr_inner, opr_outer,  testing_frame)

        # how many layers do we have here?
        # refer to testing frame
        layer = frame.get_layer(testing_frame)
        if(layer==2):
    
            dimF = tshape2.dim
            # done creating app. continute to main part
            title =  generate_name(oprs, tys, "_l2")
            #writeTime(12)
            return core(app, coeffs, dimF, title, testing_frame, cnt)
        elif(layer==3):
            # first did the user specify 3 operators in the command line?
            if(len(oprs)==3):
                # user specified 3 operators
                if(len(tys)==3):
                    #specific third argument
                    get_tshape3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt)
                else:
                    # iterate over third argument
                    iter_ty3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt)
            else:
                # create third application by iterating over possible operators
                get_tshape3_iterop3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt)
    else:
        return



