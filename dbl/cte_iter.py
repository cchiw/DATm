import sys
import re
import os
import time
import random

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'cte/')

#top-level
from frame import  *

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_field import *
from obj_counter import *
from obj_frame import  *
from base_observed import observed
from base_write import *
from base_var_ty import *

# specific cte programs
from cte_createField import createField
from cte_writeDiderot import writeDiderot
from cte_eval import eval
from cte_compare import compare
from cte_core import *

pde_test = false # test pdes in femprime branch

#    Iterate over defined types and operators
#create app object that represents that application of one or two operators on tensor and/or tensor field arguments.
#for a unary operator unary(e) we iterate over the single argu- ment (e) where e in tau.
#for two operators unary(binary(e1,e2)) we iterate over the two arguments e1 and e2 where e1 and e2 in tau.
#Internal type checking . slims down total iterations to only those that make mathematical sense before moving forward


##################################################################################################
# get example from list of examples
def single_specific_ex(opr_inner, t_num, testing_frame, cnt):
    # increment total
    counter.inc_total(cnt)
    # main
    rtn = create_single_app(opr_inner, t_num, testing_frame, cnt)

    return



##################################################################################################
##################################################################################################
##################################################################################################
# do we need to create an extra field type
def needextratype(ex_outer):
    return (ex_outer.arity>=2)


def get_extra(ex_ty2, testing_frame, cnt):
    g_rst_ty = frame.get_rst_ty(testing_frame)
    g_in_tys = frame.get_in_tys(testing_frame)
    l = get_all_types(g_rst_ty,g_in_tys)
    #print "get_all_types:"
    #j = 0
    #for i in l:
    #    if(j==ex_ty2):
    #        print "-->"+str(j)+"."+i.name+","
    #    else:
    #        print str(j)+"."+i.name+","
    #    j+=1
    return (len(l), l[ex_ty2])

def get_all_extra(testing_frame):
    g_rst_ty = frame.get_rst_ty(testing_frame)
    g_in_tys = frame.get_in_tys(testing_frame)
    l = get_all_types(g_rst_ty,g_in_tys)
    return l


# make choice if we should continue
def mk_choice_limit(testing_frame, cnt):
    random_limit = frame.get_random_limit(testing_frame)
    return (cnt.rst_cumulative < random_limit)
##################################################################################################
##################################################################################################

def embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt):
    # adjusting to accept 2|3 layers of operators
    #print "in embed_base_specific_ex, tys",tys
    opr_outer = oprs[1]
    t_ty2 = tys[1]
    #writeCumulative(cnt)
    def get_fty(ex_ty2):
        #print "-->get_fty  ex_ty2", ex_ty2
        if(needextratype(opr_outer)):
            #x = ex[ex_ty2]
            (_, x) = get_extra(ex_ty2, testing_frame, cnt)
            # convert new extra field
            id = len(ishape0)-1
            #print "gets extra type @", ex_ty2, x.name, "id:",id
            g_krn = frame.get_krn(testing_frame)
            x = set_k(g_krn, id, x)

            return (ishape0+[x], [x])
        return (ishape0,[])
    (ishape, fty) = get_fty(t_ty2)
    return get_tshape2(tshape1, ishape, fty, oprs, tys, testing_frame, cnt)

# concise verion of above code
# already given type for extra argument
# transforms that type to kernel specific type
def embed_giventy2_specific_ex(ex, tshape1, ishape0, oprs, tys, ty_ty2, testing_frame, cnt):
    fty=[]
    if(not (ty_ty2 == None)):
        g_krn = frame.get_krn(testing_frame)
        id = len(ishape0)-1
        fty= [set_k(g_krn, id, ty_ty2)]

    ishape = ishape0+fty
    return get_tshape2(tshape1, ishape, fty, oprs, tys, testing_frame, cnt)


################################################## more helpers  ###############################################

# current example
# get tshape of get_tshape
def pre_get_tshape1(ex, t_num, opr_inner, testing_frame):
    (name, ishape) = get_single_exampleEx(ex, t_num)
    g_krn = frame.get_krn(testing_frame)
    ishape0 = set_ks(g_krn, ishape)
    (tf1, tshape1) = get_tshape(opr_inner, ishape0,pde_test)
    return (name, tf1, tshape1, ishape0)


# operator, and testing framework -> built in example given
def oprToEx(opr_inner, testing_frame, cnt):
    #get global variables
    g_in_tys  = frame.get_in_tys(testing_frame)
    g_rst_ty = frame.get_rst_ty(testing_frame)
    #using s variables get global variables
    tys = transform_tys(g_in_tys)  # use global var to get list of types
    #(l_all_T, l_all_F, l_all) = tys
    ex = oprToEx_a(opr_inner, g_rst_ty, tys)
    return ex

################################################## iterating ###############################################

#iterates over extra type
#inter_num, and iter_ty2
def embed_base_iter_ty2(ex, oprs, testing_frame, cnt):
    # adjusting to accept 2|3 layers of operators
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    def f():
        #need third type
        tf = needextratype(opr_outer)
        if(tf):
            # use all field types as extra types
            # (n_ty2, _) = get_extra(0, testing_frame, cnt)
            ty2s = get_all_extra(testing_frame)
            n_ty2 = len(ty2s)
            return (tf, ty2s, n_ty2)
        else:
            return (tf, None, None)
    def call(t_num, t_ty2, ty_ty2):
        tys = [t_num, t_ty2]
        embed_giventy2_specific_ex(ex, tshape1, ishape0, oprs, tys, ty_ty2, testing_frame, cnt)
    # core
    n_num = len(ex.tys)
    (tf, ty2s, n_ty2) = f()
    for t_num  in range(n_num):
        # current example
        if(mk_choice_limit(testing_frame,cnt)):
            (name, tf1, tshape1, ishape0) = pre_get_tshape1(ex, t_num, opr_inner, testing_frame)
            if(tf1==true):
                if(tf):
                    for t_ty2 in range(n_ty2):  #extra type
                        if(mk_choice_limit(testing_frame, cnt)):
                            ty_ty2 = ty2s[t_ty2]
                            call(t_num, t_ty2,ty_ty2)
                else:# do not need extra type
                   call(t_num, None, None)
            else:
                # "tshape1 does not pass"
                continue
        else:
            # not chosen
            continue
    return

################################################## iterating ###############################################

#iterating ex_outer from 0...l
# iterate over outer operator and extra type
def embed_base_iter_outer2(ex, opr_inner, t_num, testing_frame, cnt):
    # set local counters to zero
    counter.zero_locals(cnt)
    # print "\nembed_base_iter_outer: ex_opr",ex_opr
    n_outer = getN()
    
    # current example
    (name, tf1, tshape1, ishape0) = pre_get_tshape1(ex, t_num, opr_inner, testing_frame)
    if(tf1==false):
        return
    else:
        #print "inside embed-outer2 tshape1:",tshape1.name, "k:",tshape1.k
        #have ex_opr iterating over ex_outer
        for  t_outer in range(n_outer):
            opr_outer = id_toOpr(t_outer)
            writeTitle_outer(opr_inner, opr_outer)
            oprs = [opr_inner, opr_outer]
            if(needextratype(opr_outer)):
                # use all field types as extra types
                (n_ty2, _) = get_extra(0, testing_frame, cnt)
                for t_ty2 in range(n_ty2):  #extra type
                    tys = [t_num, t_ty2]
                    embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
            else:
                tys = [t_num, None]
                embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
                writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
    return

# same as embed_base_iter_ty1, except already given extra type (t_ty2)
def embed_base_iter_ty2_wihty2(ex, oprs, tys, testing_frame, cnt):
    # adjusting to accept 2|3 layers of operators
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    t_num = tys[0]
    t_ty2 = tys[1]
    # print " embed_base_iter_ty2_wihty2 ts",tys
    # current example
    (name, tf1, tshape1, ishape0) = pre_get_tshape1(ex, t_num, opr_inner, testing_frame)
    # get built-in example
    if(tf1==false):
        return
    else:
        # print "inside embed_base_iter_ty2_wihty1 tshape1:",tshape1.name, "k:",tshape1.k
        ex_outer = oprToEx(opr_inner, testing_frame, cnt)
        if(needextratype(opr_outer)):
            # given extra type already
            (n_ty2, _) = get_extra(0, testing_frame, cnt)

     
            embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
        else:
            embed_base_specific_ex(ex, tshape1,  ishape0, oprs, tys, testing_frame, cnt)
        return


# same as embed_base_iter_ty2, except already given example number
def embed_base_iter_ty2_wihty1(ex, oprs, t_num, testing_frame, cnt):
    # adjusting to accept 2|3 layers of operators
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    
    # current example
    (name, tf1, tshape1, ishape0) = pre_get_tshape1(ex, t_num, opr_inner, testing_frame)
    # get built-in example
    if(tf1==false):
        return
    else:
        # print "inside embed_base_iter_ty2_wihty1 tshape1:",tshape1.name, "k:",tshape1.k
        ex_outer = oprToEx(opr_inner, testing_frame, cnt)
        if(needextratype(opr_outer)):
            # use all field types as extra types
            (n_ty2, _) = get_extra(0, testing_frame, cnt)
            for t_ty2 in range(n_ty2):  #extra type
                #print "as extra type using ", t_ty2,"|",n_ty2
                tys = [t_num, t_ty2]
                embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
        else:
            tys = [t_num, None]
            embed_base_specific_ex(ex, tshape1,  ishape0, oprs, tys, testing_frame, cnt)
        return

#iterating ex_outer from 0...length(potential outer_operators)
def embed_base_iter_outer(ex, opr_inner, testing_frame, cnt):
    writeTitle_inner(opr_inner)
    #have ex_opr iterating over ex_outer
    n_outer = getN()
    for  t_outer in range(n_outer):

        #zero counters
        counter.zero_locals(cnt)
        counter.zero_total(cnt)
        opr_outer = id_toOpr(t_outer)
        writeTitle_outer(opr_inner, opr_outer)
        oprs = [opr_inner, opr_outer]
        embed_base_iter_ty2(ex, oprs, testing_frame, cnt)
        writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
    return

#run all possible examples from 0...n
def embed2_iter_inner(testing_frame, cnt):
    n_opr = getN()
    for t_opr in range(n_opr):

        startx = time.time()
        opr_inner = (id_toOpr(t_opr))
        ex = oprToEx(opr_inner, testing_frame, cnt)
        embed_base_iter_outer(ex, opr_inner, testing_frame, cnt)

    return

#run all possible examples from 0...n
def embed2_iter_inner_setrange(t_start, t_range, testing_frame, cnt):
    n_opr = getN()
    for t_opr in range(t_range):
        t_opr+=t_start
        startx = time.time()
        opr_inner = (id_toOpr(t_opr))
        ex = oprToEx(opr_inner, testing_frame, cnt)
        embed_base_iter_outer(ex, opr_inner, testing_frame, cnt)
    
    return



#specify outer operator
def embed2_iter_inner_gotouter(opr_outer, testing_frame, cnt):
    counter.zero_total(cnt)  #zero counters
    n_opr = getN()
    
    #iterate over inner operator
    for t_opr in range(n_opr):
        #zero counters

        counter.zero_locals(cnt)
        counter.zero_total(cnt)
        opr_inner = id_toOpr(t_opr)
        writeTitle_outer(opr_inner, opr_outer)
        ex = oprToEx(opr_inner, testing_frame, cnt)
        oprs = [opr_inner, opr_outer]
        embed_base_iter_ty2(ex, oprs, testing_frame, cnt)
    return

#run all examples for a specific operator
def single_all_ops(opr_inner, testing_frame, cnt):
    # get built-in example
    ex = oprToEx(opr_inner, testing_frame, cnt)
    n_num = len(ex.tys)
    if (n_num==0):
        return
    writeTitle_inner(opr_inner)
    #zero counters
    counter.zero_locals(cnt)
    for t_num  in range(n_num):
        single_specific_ex(opr_inner, t_num, testing_frame, cnt)
    return
