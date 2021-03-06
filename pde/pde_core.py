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
from nc_compare import compare,compare_zero
from nc_continue import check
from nc_createField import sortField

# specific fem programs
from pde_main import writeTestPrograms



#from fem_eval import eval
sys.path.insert(0, 'cte/')
from cte_eval import eval

pde_test=true # test pdes in femprime branche
test_new = true # new type of test

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
#pde data = sol degree, boundary degree, type, coefficient matrix, vector
def analyze(name_file, name_ty, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, branch,t="d",pde_data=None):
    (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) =  rtn
    #print "X", x
    x = "\n-"+name_file+" "+name_describe+"| "+name_ty+"| " + "stored additional data in rst2/" + t +" | " + rtn_1 
    writeall(x)
    print  (x)
    if pde_data != None:
        f = pde_data[-1][0]
        bp = f.pde_boundary.sympy_exp
        sp = f.pde_ground_state.sympy_exp
        x1 = "\n-"+name_file+" "+name_describe+"| "+name_ty+"| " + "-\n The degree of the solution poly is {0} and the poly is {1}".format(pde_data[1],sp)
        x1 += "- The degree of the boundary poly is {0} and the poly is {1} \n" .format(pde_data[0],bp)
        #x1 += "- The pde is biharmonic" if pde == 0 else "The pde is biellipticial\n"
        x1 += """The pde vector is two applications of: {0}        """.format(f.aoperator)
        writeall(x1)
        print(x1)

    
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
    #else:
    #print "made it here"
    #rst_good(cnt.rst_t_good, name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
    return

##################################################################################################
##################################################################################################

# make choice if we should continue
def mk_choice_range(testing_frame, cnt):
    random_range  = frame.get_random_range(testing_frame)
    return (not random.randint(0, random_range))



    # from obj_operator import op_gradient
    # from obj_apply import *
    # from itertools import repeat
    #grad_otype = list(repeat(app.oty,dimSave))
    #g_otype = isValid(op_gradient,grad_otype)
    #newapp = set_UnaryApp(op_gradient,app,list(repeat(app.oty,dimSave)))
    #newapp = apply("opr",op_gradient,app,None,None,grad_otype,False,True)
    #print(newapp.toStr(0))

def core_test(core_fields,app, coeffs, dimF, names, testing_frame, cnt,bpd=6,spd=10,pde=2):
    backup_lab = "d"+str(time.time())
    
    print ("############################################inside central############################################")
    # making a test program
    counter.inc_cumulative(cnt)
    
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
    
    

    #print "*******************************************"
    fnames = apply.get_all_FieldTys(app)
    x = "_"+fnames +" |"+names
    #print (x)
    writetys(x)
    name_describe = app.name

    # testing positions
    # note here should set positions based on space
    l_lpos = 0.0
    l_rpos = 1.0
    positions = get_positions(dimF, l_lpos, l_rpos, g_num_pos)
    #a = eval(newapp,positions)
    #print(a)
    #exit(0)
    # samples
    #create synthetic field data with diderot
    (PARAMS,all50,all51,all52,all53,all54,all55) = sortField(core_fields, g_samples, coeffs, t_nrrdbranch, g_space)
    #create diderot program with operator
    endall = time.time()
    startall=endall
    cleanup(g_output, g_p_Observ)
    (isCompile, isRun, startall,fp) = writeTestPrograms(g_p_Observ, app, positions, g_output, t_runtimepath, t_isNrrd, startall,test_new,core_fields,t=backup_lab,tt=(bpd,spd,pde))
    if(isRun == None):
        if(isCompile == None):
            counter.inc_compile(cnt)
            rst_compile(names, x, name_describe, g_branch,  positions, PARAMS)
            #raise Exception("stop")
            
            return
        else:
            if (fp == 1):
                counter.inc_fp(cnt)
                rst_fp(names, x, name_describe, g_branch,  positions, PARAMS)
                return
            else:
                counter.inc_run(cnt)
                rst_execute(names, x, name_describe, g_branch,  positions, PARAMS)
                return

    else:
        #print "read observed data"
        observed_data = observed(app, g_output)
        print ("observed", observed_data)
        if(check(app, observed_data)):

            if(test_new):
                correct_data = 0 #expects zero everywhere
                rtn = compare_zero(app.oty, app.name, observed_data)
                analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch,t=backup_lab,pde_data=(bpd,spd,pde, core_fields))
            else:
                correct_data = eval(app, positions)
                print ("correct_data",correct_data)
                rtn = compare(app.oty, app.name, observed_data, correct_data)
                analyze(names, fnames, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, g_branch)
            return
        else:
            # NA
            fnames = apply.gvet_all_FieldTys(app)
            x = "_"+fnames +" |"+names
            name_describe = app.name
            g_branch = frame.get_branch(testing_frame)
            counter.inc_NA(cnt)
            #rst_NA(names, x, name_describe, g_branch)
            return



# already created app object
def core_checktys(app, coeffs, dimF, names, testing_frame, cnt,bpd=6,spd=10,pde=2):
    backup_lab = "d"+str(time.time())
    
    print ("############################################inside central############################################")
    
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
    
    core_fieldsOrig = apply.get_all_Fields(app) #Orig -> collection of all fields and kaking lists
    core_fields = []
    # limit core fields by the ones we can rep.
    if(not (fty.is_Field(app.oty))):
        return None

    for e in core_fieldsOrig: #go through fields and pick the kosher ones #1
        ty = e.fldty
        #print "ty name:",ty.name,ty.space
        dim =ty.dim
        
        shapen = len(ty.shape)
        
        if(dim != 2):
            return None
        elif(shapen>1):
            return None
        f= field.addSpace(e, g_element,g_coeff_style, g_length,pde_test=test_new,bpd=bpd,spd=spd,pde=pde )
        if(not(f.fldty.is_ScalarField())):
            return None
        
        core_fields.append(f) #add to list of core fields -> add space -> add relevant everything relevat to what we want-> Lagrange, P, random -> vary elements and


    for e in core_fields:
        ty = e.fldty
        e.set_pde()
        print ("ty name:",ty.name,ty.space)

    # if we made it this far then the types are okay
    reps = 2
    bdp = 6
    spd = 10
    pde = 2
    total = reps*pde*bpd*spd
    for x in range(reps):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Starting new reptition {0} out of {1}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(x,reps))
        for bpds in range(1,bdp+1):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Starting new Round of BPD type {0} out of {1}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(bpds,bpd+1))
            for spds in range(1,spd+1):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Starting new Round of SPD type {0} out of {1}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(spds,spd+1))
                for pdes in range(1,pde+1):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Starting new Round of PDE type {0} out of {1}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(pdes,pde+1))
                    core_test(core_fields, app, coeffs, dimF, names, testing_frame, cnt,bpd=bpds,spd=spds,pde=pdes)


def core(app, coeffs, dimF, names, testing_frame, cnt):
    #print "**** at core ***"
    writetys("\n\t***"+app.name)
    writetys("\n\t-"+apply.get_all_FieldTys(app)+"|"+  names)
    #counter.inc_cnt(cnt)
    if(mk_choice_range(testing_frame, cnt)):
        rtn = core_checktys(app, coeffs, dimF, names, testing_frame, cnt)
    
    else:
        return


##################################################################################################
##################################################################################################

space = "Unit"
##################################################################################################
# functions create app objects
# get example from list of examples
def create_single_app(ex, opr_inner, t_num, testing_frame, cnt):
    #print "################## creating single app##################"
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

    ishape = set_ks_ofield(g_krn, ishape, space)


    #print opr_inner.name,ishape[0].name
    (tf1, tshape1) = get_tshape(opr_inner,ishape,pde_test)

    if(not tf1):
        #write_terrible("\n apply blocked from attempting: "+"b__"+name+str(opr_inner.id)+"_"+str(t_num))
        return None
    #print tf1, tshape1.name, tshape1.space
    #print " mark C"
    (app, coeffs) = mkApply_fld(name, opr, ishape, g_inputfile, tshape1, g_coeff_style, g_ucoeff, g_krn,g_template)
    #print " mark D"
    dimF = tshape1.dim
    names= "s_"+str(opr_inner.id)+"__"+"n_"+str(t_num)+"_"
    core(app, coeffs, dimF, names, testing_frame, cnt)
    return




def convert_fields(ishape,testing_frame):
    #print "inside convert fields"

    g_krn = frame.get_krn(testing_frame)
    x = set_ks_ofield(g_krn, ishape, space)
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
    #print "___________________", app.oty.name
    #print "___________________", app.lhs.oty.name
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
    #print "opr_outer2", opr_outer2.name
    #print "opr_outer1", opr_outer1.name
    #print "opr_inner:", opr_inner.name
    #print "tys", tys
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
    #print "trying to match opr_outer2", opr_outer2.name ,"with ",tshape2.name
    #for j in tmpshape:
    #print "-- shape", j.name
    # ok now back to regular programming
    (tf3, tshape3) = get_tshape(opr_outer2, ishape_outer2,pde_test)
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

    for opr_outer2 in op_all:
        # next function will type check it and get type
        iter_ty3(app, coeffs, ishape, tshape2, oprs+[opr_outer2], tys, testing_frame, cnt)
    return


# checks to see if specific ex works
def get_tshape2(tshape1, ishape, fty,  oprs, tys, testing_frame, cnt):

    #writeTime(9)
    # adjusting to accept 2|3 layers of operators

    opr_inner = oprs[0]
    opr_outer = oprs[1]

    # get value of k from kernels
    ishape = convert_fields(ishape, testing_frame)
    #second layer, adds second field type
    #print "tshape1", tshape1.name,"tshape1-space",tshape1.space
    #print "fty", fty
    es = [tshape1]+fty
    xy = get_tshape(opr_outer,es,pde_test)
  
    (tf2, tshape2) =xy
    #print "tf2:", tf2, " tshape2:", tshape2
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



