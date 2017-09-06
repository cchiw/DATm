import sys
import re
import os
import random

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')


#top-level
from frame import  *

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_field import *
from obj_counter import *
from obj_frame import *
from base_observed import observed
from base_write import *
from base_var_ty import *

# specific vis ver programs
from vis_createField import createField
from vis_writeDiderot import writeDiderot
from vis_eval import eval_sample
from vis_sample import run_sample,mk_vis_files
                                  

pde_test=false# test pdes in femprime branche

# results from testing
def vis_analyze(opr_name, name_file, name_ty, name_describe, cnt, rtn, observed_data, observed_sphere, arg_positions, PARAMS, branch):
    (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) =  rtn
    (rst_lbl,  rst_all) = rtn_1
    test_header_0 = name_file+"\n\t"+name_describe+"| "+name_ty+"| "+rst_lbl
    test_header_1 =  test_header_0+rst_all
    
    
    writeall(test_header_0)
    print test_header_0
    
    counter.inc_locals(cnt, rtn)
    # write to file
    correct_data = observed_sphere
    positions = arg_positions

    print "x:",test_header_0
    if (rst_terrible_1==1):
        rst_terrible(name_file, test_header_0, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
    else:
        rst_good(name_file, test_header_0, name_describe, branch, observed_data, correct_data,  positions, PARAMS)

##################################################################################################
##################################################################################################

# make choice if we should continue
def mk_choice_range(testing_frame, cnt):
    random_range  = frame.get_random_range(testing_frame)
    return (not random.randint(0, random_range))

def cleanup(g_p_Observ):
    filenames =["observ", "vis_sample_out", "vis_color",g_p_Observ]
    for n in filenames:
        rmFiles(n, "")



# already created app object
def core2(app, coeffs, dimF, names, testing_frame, cnt):
    print "############################################inside central############################################"
    writetys("\n\t-"+apply.get_all_FieldTys(app)+"|"+  names)
    
    # get global variables from testing framework
    g_lpos = frame.get_lpos(testing_frame)
    g_upos = frame.get_upos(testing_frame)
    g_num_pos = frame.get_num_pos(testing_frame)
    g_p_Observ = frame.get_p_Observ(testing_frame)
    g_output = frame.get_output(testing_frame)
    g_samples = frame.get_samples(testing_frame)
    g_branch = frame.get_branch(testing_frame)
    g_space = frame.get_space(testing_frame)
    g_template = frame.get_template(testing_frame)
    # transform from global variables
    t_isNrrd = frame.transform_isNrrd(testing_frame)
    t_nrrdbranch = frame.transform_nrrdpath(testing_frame)
    t_runtimepath = frame.transform_runtimepath(testing_frame)
    t_size = frame.transform_template_size(testing_frame)
    t_file = frame.transform_template_file(testing_frame)
    ##print "*******************************************"
    print "clean up files"
    #cleanup(g_p_Observ)
    fnames = apply.get_all_FieldTys(app)
    x = "_"+fnames +" |"+names
    name_describe = app.name

    # testing positions
    positions = get_positions(dimF, g_lpos, g_upos, g_num_pos)
    # samples
    #create synthetic field data with diderot

    PARAMS = createField(app, g_samples, coeffs, t_nrrdbranch, g_space)
    #create diderot program with operator
    print "\n ******************************   pre write date "
    (isCompile, isRun) = writeDiderot(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd,t_size*t_size,t_file)
    if(isRun == None):
        # did not run
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
            return 1
        else:
            counter.inc_run(cnt)
            rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
            return 2
    else:
        # read observed data
        print "---------------  pre read  observed data ----------------------"
        observed_data = observed(app, g_output)
        print "observed_data ",observed_data 
        # center of spehere
        arg_center = (t_size/2)
        # number of testing points
        arg_positions  = 20 #30
        # increment testing points
        arg_inc=arg_center/ arg_positions
        arg_perline = 9 # output of mip program
        # take samples of output
        
        print "---------------  pre read diderot ----------------------"
        # sampling diderot file
        os.system("cp rst/data/observ  rst/data/observ.nrrd")
        mk_vis_files(app, positions, arg_inc, arg_positions)
        os.system("cp rst/data/observ  rst/data/observ.nrrd")
        #print "--------------- pre run sample-----------------------"
        observed_sphere =  run_sample(t_runtimepath, arg_center, arg_inc,arg_positions)
        #print "observed_eval",observed_sphere
        rtn  = eval_sample(observed_sphere)
        #print "--------------- pre color-----------------------"

        #run_color(t_runtimepath, arg_center, arg_positions, arg_inc)
        

        # collect results
        vis_analyze(app.opr.name+"_", names, fnames, name_describe, cnt, rtn, observed_data, observed_sphere, arg_positions, PARAMS, g_branch)
        return 0
        #else:
        #return None

# is the input type okay for mip template
def input_ty1(e):
    #print "input type: ",e.name
    #print "e.id=",e.id
    #print "ty_vec3F_d3.id:",ty_vec3F_d3.id
    #print "ty_scalarF_d3.id:",ty_scalarF_d3.id
    if( (e.id==ty_scalarF_d3.id)):
        return True
    elif( (e.id==ty_vec3F_d3.id)):
        return True
    else:
        return False

def input_ty2(e):
    if(not (e.lhs==None)):
        #print "e.lhs", e.lhs
        #print "e.lhs.fldty",e.lhs.fldty
        #print "e.lhs.fldty.name",e.lhs.fldty.name
        #print "e.lhs.fldty.id",e.lhs.fldty.id
        
        if(input_ty1(e.lhs.fldty)):
            if(not (e.rhs==None)):
                #print "check rhs"
                return input_ty1(e.rhs.fldty)
            else:
                return True
        else:
            return False
    else:
        return False

def core(app, coeffs, dimF, names, testing_frame, cnt):
    #print "\n ****************************** vis   a"
    #writetys("\n\t***"+app.name)
    #writetys("\n\t-"+apply.get_all_FieldTys(app)+"|"+  names)
    #counter.inc_cnt(cnt)
    #counter.inc_cumulative(cnt)

    if(not(app.oty.id==ty_scalarF_d3.id)):
        #print "app.oty:",app.oty," name:",app.oty.name
        return
    if( not (input_ty2(app.lhs))):
    #    #print "does not pass"
    #    return
    # layer 1
    #if( not (input_ty2(app))):
        #print "does not pass"
        return
    
    if(not (app.rhs==None)):
        if(not (input_ty1(app.rhs.fldty))):
            #print "does not pass"
            return
    #print "passes"
    if(mk_choice_range(testing_frame, cnt)):
        counter.inc_cumulative(cnt)
        #return
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
        os.system(" rm symb_* ")
    else:
        return



##################################################################################################
##################################################################################################


##################################################################################################
# functions create app objects
# get example from list of examples
def create_single_app(opr_inner, t_num, testing_frame, cnt):
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_rst_ty = frame.get_rst_ty(testing_frame)
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
    ##print "single specific ex"
    def oprToEx(opr_inner, testing_frame, cnt):
        #get global variables
        g_in_tys  = frame.get_in_tys(testing_frame)
        g_rst_ty = frame.get_rst_ty(testing_frame)
        #using s variables get global variables
        tys = transform_tys(g_in_tys)  # use global var to get list of types
        #(l_all_T, l_all_F, l_all) = tys
        ex = oprToEx_a(opr_inner, g_rst_ty, tys)
        return ex
    
    opr = opr_inner
    ex = oprToEx(opr_inner, testing_frame, cnt)
    (name,ishape)= get_single_exampleEx(ex, t_num)
    # get k value of tshape from kernels
    ishape = set_ks(g_krn, ishape)
    ##print "calling tshape"
    (tf1, tshape1) = get_tshape(opr_inner,ishape,pde_test)
    if(not tf1):
        write_terrible("\n apply blocked from attempting: "+"b__"+name+str(opr_inner.id)+"_"+str(t_num))
        return None
    ##print "after calling tshape"
    #create app object

    (app, coeffs) = mkApply_fld(name, opr, ishape, g_inputfile, tshape1, g_coeff_style, g_ucoeff, g_krn, g_template )
    dimF = tshape1.dim
    names= "s_"+str(opr_inner.id)+"__"+"n_"+str(t_num)+"_"
    core(app, coeffs, dimF, names, testing_frame, cnt)
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
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
    (app, coeffs) = mkApply_twice(opr_inner,opr_outer, ishape, g_inputfile, tshape1, tshape2, g_coeff_style, g_ucoeff, g_krn,g_template)
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
def get_tshape3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt):
    [opr_inner, opr_outer1, opr_outer2] = oprs
    [_, _, t_ty3] = tys
    ##print "****************************************  get_tshape3 ************************************"
    # third layer operator, and second type it is applied to (incase it is a binary)
    tmpshape = []
    s = ""
    if(opr_outer2.arity==2):
        ty3 = get_all_extra(testing_frame)
        tmpshape = [ty3[t_ty3]]
        s = "_t"+str(t_ty3)
    
    counter.inc_total(cnt)
    # add new shape argment
    ishape_outer2 = [tshape2] + tmpshape
    ishape_all = ishape + tmpshape
    ishape_all = convert_fields(ishape_all, testing_frame)
    
    # ok now back to regular programming
    (tf3, tshape3) = get_tshape(opr_outer2, ishape_outer2)
    if(tf3==true):#
        writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        appname = opr_outer2.name+"("+opr_outer1.name+"("+opr_inner.name+")"+")"
        #print "appname :",appname
        title =  generate_name(oprs, tys, "_l3")
        create_apply3_then_core(ishape_all, appname, opr_outer2, tshape3, app, coeffs, title, testing_frame, cnt)


#iterate over extra possible type
def iter_ty3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt):
    [opr_inner, opr_outer1, opr_outer2] = oprs
    def f(t_ty3):
         get_tshape3(app, coeffs, ishape, tshape2, oprs, tys+[t_ty3], testing_frame, cnt)
    if(opr_outer2.arity==1):
        f(None)
    else:
        ty3 = get_all_extra(testing_frame)
        for t_ty3 in range(len(ty3)):  #extra type
            f(t_ty3)
    return

# iterating over third operator
def get_tshape3_iterop3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt):
    for opr_outer2 in op_all:
        # next function will type check it and get type
        iter_ty3(app, coeffs, ishape, tshape2, oprs+[opr_outer2], tys, testing_frame, cnt)
    return


# checks to see if specific ex works
def get_tshape2(tshape1, ishape, fty,  oprs, tys, testing_frame, cnt):
    # adjusting to accept 2|3 layers of operators
    
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    ##print "****************************************  get_tshape2 ************************************"
    # get value of k from kernels
    ishape = convert_fields(ishape, testing_frame)
    #second layer, adds second field type
    (tf2, tshape2) = get_tshape(opr_outer,[tshape1]+fty,pde_test)
    ##print "in get tshape 2 tys",tys
    if(tf2==true):# if it works continue
        #create app object
        (app, coeffs) = create_apply2(ishape, tshape1, tshape2, opr_inner, opr_outer,  testing_frame)
        # how many layers do we have here?
        # refer to testing frame
        layer = frame.get_layer(testing_frame)
        if(layer==2):
            dimF = tshape2.dim
            # done creating app. continute to main part
            title =  generate_name(oprs, tys, "_l2")
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



