import sys
import re
import os
import random

sys.path.insert(0,'fem/')
sys.path.insert(0,'cte/')

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
from fem_core import  fem_core
from cte_core import  cte_core
from input import s_field

###################################################################################################
###################################################################################################
# different based on cte or fem
def convert_fields(ishape,testing_frame):
    if(s_field==field_pde):
        g_krn = frame.get_krn(testing_frame)
        x = set_ks_ofield(g_krn, ishape, space)
        return x

    elif(s_field==field_conv):
        g_krn = frame.get_krn(testing_frame)
        x = set_ks(g_krn, ishape)
        return x
    else:
        raise Fail ("convert fields issue")

def core_inside(app, coeffs, dimF, title, testing_frame, cnt):
    if(s_field==field_pde):
        return fem_core(app, coeffs, dimF, title, testing_frame, cnt)
    elif(s_field==field_conv):
        return  cte_core(app, coeffs, dimF, title, testing_frame, cnt)
    else:
        raise Fail ("core inside issue")

###################################################################################################
###################################################################################################
#
# make choice if we should continue
def mk_choice_range(testing_frame, cnt):
    random_range  = frame.get_random_range(testing_frame)
    return (not random.randint(0, random_range))

def core(app, coeffs, dimF, names, testing_frame, cnt):
    writetys("\n\t***"+app.name)
    writetys("\n\t-"+apply.get_all_FieldTys(app)+"|"+  names)
    counter.inc_cnt(cnt)
    if(mk_choice_range(testing_frame, cnt)):
        counter.inc_cumulative(cnt)
        
        rtn = core_inside(app, coeffs, dimF, names, testing_frame, cnt)
        if(rtn==None):
            fnames = apply.get_all_FieldTys(app)
            x = "_"+fnames +" |"+names
            name_describe = app.name
            g_branch = frame.get_branch(testing_frame)
            counter.inc_NA(cnt)
            rst_NA(names, x, name_describe, g_branch)

    else:
        return

###################################################################################################
###################################################################################################

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
    ishape = convert_fields(ishape,testing_frame)
    #print "calling tshape"
    #print opr_inner.name,ishape[0].name
    (tf1, tshape1) = get_tshape(opr_inner,ishape)
    #print "post get-tshape"
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


##################################################################################################
################### getTshape3 ####################
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
##ztwice, coeffstwice: result of application of second layer
def get_tshape3(app, coeffs, ishape, tshape2, oprs, tys, newtys, testing_frame, cnt):
    [opr_inner, opr_outer1, opr_outer2] = oprs
    #print "****************************************  get_tshape3 ************************************"
    # third layer operator, and second type it is applied to (incase it is a binary)
    tmpshape = []
    s = ""

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

    # ok now back to regular programming
    (tf3, tshape3) = get_tshape(opr_outer2, ishape_outer2)
    if(tf3==true):#
        writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        appname = opr_outer2.name+"("+opr_outer1.name+"("+opr_inner.name+")"+")"
        #print "appname :",appname
        tys =tys+newtys
        title =  generate_name(oprs, tys, "_l3")
        create_apply3_then_core(ishape_all, appname, opr_outer2, tshape3, app, coeffs, title, testing_frame, cnt)
#################### Two Tshape ####################
##iterate over extra possible type
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
## iterating over third operator
def get_tshape3_iterop3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt):

    for opr_outer2 in op_all:
        # next function will type check it and get type
        iter_ty3(app, coeffs, ishape, tshape2, oprs+[opr_outer2], tys, testing_frame, cnt)
    return


## checks to see if specific ex works
def core_get_tshape2(tshape1, ishape, fty,  oprs, tys, testing_frame, cnt):
    #writeTime(9)
    # adjusting to accept 2|3 layers of operators
    #print "in get-tshape print ishape"
    opr_inner = oprs[0]
    opr_outer = oprs[1]

    # get value of k from kernels
    ishape = convert_fields(ishape, testing_frame)
    #second layer, adds second field type
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
                    get_tshape3(app, coeffs, ishape, tshape2, oprs, tys,[], testing_frame, cnt)
                else:
                    # iterate over third argument
                    iter_ty3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt)
            else:
                # create third application by iterating over possible operators
                get_tshape3_iterop3(app, coeffs, ishape, tshape2, oprs, tys, testing_frame, cnt)
    else:
        return
#################### One operator ####################
def create_apply2(ishape, tshape1, tshape2, opr_inner, opr_outer,  testing_frame):
    #writeTime(11)
    # global variables needed from testing framework
    g_inputfile = frame.get_inputfile(testing_frame)
    g_ucoeff = frame.g_ucoeff(testing_frame)
    g_coeff_style = frame.get_coeff_style(testing_frame) # global variable from set
    g_krn = frame.get_krn(testing_frame)
    g_template = frame.get_template(testing_frame)
    (app, coeffs) = mkApply_twice(opr_inner,opr_outer, ishape, g_inputfile, tshape1, tshape2, g_coeff_style, g_ucoeff, g_krn, g_template )

    return (app, coeffs)

