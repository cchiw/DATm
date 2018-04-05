import sys
import re
import os
import time
import random

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'fem/')
sys.path.insert(0, 'nc/')
#top-level
from input import  *

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_field import *
from obj_counter import *
from obj_frame import  *
from base_observed import observed
from base_write import *
from base_var_ty import *

# specific fem programs
from fem_core import *


#    Iterate over defined types and operators
#create app object that represents that application of one or two operators on tensor and/or tensor field arguments.
#for a unary operator unary(e) we iterate over the single argu- ment (e) where e in tau.
#for two operators unary(binary(e1,e2)) we iterate over the two arguments e1 and e2 where e1 and e2 in tau.
#Internal type checking . slims down total iterations to only those that make mathematical sense before moving forward
##################################################################################################
# get example from list of examples
def single_specific_ex(ex, opr_inner, t_num, testing_frame, cnt):
    # increment total
    counter.inc_total(cnt)

    rtn = create_single_app(ex, opr_inner, t_num, testing_frame, cnt)
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
    # print "in embed_base_specific_ex, tys",tys
    opr_outer = oprs[1]

    #writeCumulative(cnt)
    def get_fty():
        #print "-->get_fty  ex_ty2", ex_ty2
        arity = opr_outer.arity
        g_krn = frame.get_krn(testing_frame)
        id = len(ishape0)-1
        if(arity==1):
            return (ishape0,[])
        elif(arity==2):
            t_ty2 = tys[1]
            #x = ex[ex_ty2]
            (_, x) = get_extra(t_ty2, testing_frame, cnt)
            # convert new extra field
            x = set_k(g_krn, id, x)
            return (ishape0+[x], [x])
        elif(arity==3):
            t_ty2 = tys[1]
            (_, x) = get_extra(t_ty2, testing_frame, cnt)
            # convert new extra field
            y = set_k(g_krn, id, x)
            z = set_k(g_krn, id+1, x)
            return (ishape0+[y,z], [y,z])
    (ishape, fty) = get_fty()
    return get_tshape2(tshape1, ishape, fty, oprs, tys, testing_frame, cnt)

# concise verion of above code
# already given type for extra argument
# transforms that type to kernel specific type
def embed_giventy2_specific_ex(ex, tshape1, ishape0, oprs, tys_num, tys_ty, testing_frame, cnt):

    #writeTime(8)
    fty=[]
    g_krn = frame.get_krn(testing_frame)
    id = len(ishape0)-1
    for ty_ty2 in tys_ty:
        fty= fty+[set_k(g_krn, id, ty_ty2)]
        id = id+1
                
    ishape = ishape0+fty
    return get_tshape2(tshape1, ishape, fty, oprs, tys_num, testing_frame, cnt)


################################################## more helpers  ###############################################
# current example
# get tshape of get_tshape
def pre_get_tshape1(name, ishape, opr_inner, testing_frame):
    g_krn = frame.get_krn(testing_frame)
    space =  "Unit"
    ishape0 = set_ks_ofield(g_krn, ishape, space)
    pde_test = True
    (tf1, tshape1) = get_tshape(opr_inner, ishape0, pde_test)
    return (name, tf1, tshape1, ishape0)


# operator, and testing framework -> built in example given
def oprToEx(opr_inner, testing_frame, cnt):
    #get global variables
    g_in_tys  = frame.get_in_tys(testing_frame)
    g_rst_ty = frame.get_rst_ty(testing_frame)
    #using s variables get global variables
    tys = transform_tys(g_in_tys)  # use global var to get list of types
    ex = oprToEx_a(opr_inner, g_rst_ty, tys)
    return ex

################################################## iterating ###############################################
#iterates over extra type
#inter_num, and iter_ty2
def embed_base_iter_ty2(ex, oprs, testing_frame, cnt):

    #writeTime(5)
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    # core
    n_num = len(ex.tys)
    for t_num  in range(n_num):
        # current example
        (name, ishape) = get_single_exampleEx(ex, t_num)
        (name, tf1, tshape1, ishape0) = pre_get_tshape1(name, ishape, opr_inner, testing_frame)
        #writeTime(7)
        if(tf1==true):
            arity = opr_outer.arity
            if(arity==1):
                tys_num = [t_num, None, None]
                tys_ty = []
                embed_giventy2_specific_ex(ex, tshape1, ishape0, oprs, tys_num, tys_ty, testing_frame, cnt)
            elif(arity==2):
                ty2s = get_all_extra(testing_frame)
                n_ty2 = len(ty2s)
                for t_ty2 in range(n_ty2):  #extra type
                    ty_ty2 = ty2s[t_ty2]
                    #call(t_num, t_ty2,ty_ty2)
                    tys_num = [t_num, t_ty2, None]
                    tys_ty = [ty_ty2]
                    embed_giventy2_specific_ex(ex, tshape1, ishape0, oprs, tys_num, tys_ty, testing_frame, cnt)
            elif(arity==3):
                ty2s = get_all_extra(testing_frame)
                n_ty2 = len(ty2s)
                for t_ty2 in range(n_ty2):
                    for t_ty3 in range(n_ty2):
                        ty_ty2 = ty2s[t_ty2]
                        ty_ty3 = ty2s[t_ty3]
                        tys_num = [t_num, t_ty2, t_ty3]
                        tys_ty = [ty_ty2, ty_ty3]
                        embed_giventy2_specific_ex(ex, tshape1, ishape0, oprs, tys_num, tys_ty, testing_frame, cnt)
    
        else:
            continue
    return

################################################## iterating ###############################################
#iterating ex_outer from 0...l
# iterate over outer operator and extra type
def embed_base_iter_outer2(ex, name, ishape, opr_inner, t_num, testing_frame, cnt):
    # set local counters to zero
    counter.zero_locals(cnt)
    n_outer = getN()
    # current example
    (name, tf1, tshape1, ishape0) = pre_get_tshape1(name, ishape, opr_inner, testing_frame)
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
                    tys = [t_num, t_ty2, None]
                    embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
            else:
                tys = [t_num, None, None]
                embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
                writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
    return

# same as embed_base_iter_ty1, except already given extra type (t_ty2)
def embed_base_iter_ty2_wihty2(ex, name, ishape, oprs, tys, testing_frame, cnt):
    #print "embed base-iter ty2-with2", tys
    # adjusting to accept 2|3 layers of operators
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    # current example
    (name, tf1, tshape1, ishape0) = pre_get_tshape1(name, ishape, opr_inner, testing_frame)
    # get built-in example
    if(tf1==false):
        return
    else:
        # #print "inside embed_base_iter_ty2_wihty1 tshape1:",tshape1.name, "k:",tshape1.k
        ex_outer = oprToEx(opr_inner, testing_frame, cnt)
            #if(needextratype(opr_outer)):
            # given extra type already
            #(n_ty2, _) = get_extra(0, testing_frame, cnt)
        embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
            #else:
            #embed_base_specific_ex(ex, tshape1,  ishape0, oprs, tys, testing_frame, cnt)
        return


# same as embed_base_iter_ty2, except already given example number
def embed_base_iter_ty2_wihty1(ex, oprs, name, ishape, t_num, testing_frame, cnt):
    # adjusting to accept 2|3 layers of operators
    opr_inner = oprs[0]
    opr_outer = oprs[1]
    # current example
    (name, tf1, tshape1, ishape0) = pre_get_tshape1(name, ishape, opr_inner, testing_frame)
    # get built-in example
    if(tf1==false):
        return
    else:
        ex_outer = oprToEx(opr_inner, testing_frame, cnt)
        if(needextratype(opr_outer)):
            # use all field types as extra types
            (n_ty2, _) = get_extra(0, testing_frame, cnt)
            for t_ty2 in range(n_ty2):  #extra type
                tys = [t_num, t_ty2]
                embed_base_specific_ex(ex, tshape1, ishape0, oprs, tys, testing_frame, cnt)
        else:
            tys = [t_num, None]
            embed_base_specific_ex(ex, tshape1,  ishape0, oprs, tys, testing_frame, cnt)
        return

#iterating ex_outer from 0...length(potential outer_operators)
def embed_base_iter_outerSingle(ex, opr_inner, testing_frame, cnt):
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

def embed_base_iter_outer(ex, opr_inner, testing_frame, cnt):
    writeTitle_inner(opr_inner)
    #have ex_opr iterating over ex_outer
    n_outer = getN()
    #writeTime(4)
    for  t_outer in range(n_outer):
        #zero counters
        counter.zero_locals(cnt)
        counter.zero_total(cnt)
        opr_outer = id_toOpr(t_outer)
        writeTitle_outer(opr_inner, opr_outer)
        oprs = [opr_inner, opr_outer]
        embed_base_iter_ty2(ex, oprs, testing_frame, cnt)
        writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
    #switch
#    writeall("\nswitch")
#    opr_outer=opr_inner
#    for  t_inner in range(n_outer):
#        #zero counters
#        counter.zero_locals(cnt)
#        counter.zero_total(cnt)
#        opr_inner = id_toOpr(t_inner)
#        ex = oprToEx(opr_inner, testing_frame, cnt)
#        writeTitle_outer(opr_inner, opr_outer)
#        oprs = [opr_inner, opr_outer]
#        embed_base_iter_ty2(ex, oprs, testing_frame, cnt)
#        writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
    return
#run all possible examples from 0...n
def embed2_iter_inner(testing_frame, cnt):
    n_opr = getN()
    for t_opr in range(n_opr):
        t_opr = t_opr
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
    #print "embed2_iter_inner_gotouter"
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
        single_specific_ex(ex, opr_inner, t_num, testing_frame, cnt)
    return



def embed2_iter_inner_setrange_layer1(t_start, t_range, testing_frame, cnt):
    n_opr = getN()
    for t_opr in range(t_range):
        t_opr+=t_start
        startx = time.time()
        opr_inner = (id_toOpr(t_opr))
        single_all_ops(opr_inner, testing_frame, cnt)

