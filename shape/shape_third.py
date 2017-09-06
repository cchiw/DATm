

import re
import os
import time


from obj_field import *
from obj_counter import *
from obj_frame import  *

from core import *
from test_write import *
from var_ty import *
from frame import  *
from shape_helper import *
from shape_helper_current import *
from shape_backwards import *

pde_test = false # test pdes in femprime branch

##################################################################################################
# #print types on list
def pes(pre, es):
    n = len(es)
    l = pre+" length: "+str(n)+" : "
    for i in es:
        if(i==None):
            l+=" None,"
        else:
            l+=(i.name)+","
    #print l



##################################################################################################
##################################################################################################
# shape1 : shapes (ty_vecT, ty_matT) not a type
# ty1 : types with specific shapes (ty_vecFT, ty_vecF_d1..)
# exp1: specific types on ty1s list ^

def core_ops(exps, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    # can apply (shape1*shape2)* shape3 ->tshape2
    # assuming shape_to_fty() is ordered by dimension
    counter.inc_total(cnt)
    #convert_fields(exps, testing_frame)
    
    x = counter.writeCumulativeS(cnt)
    writeall(x)
    
    
    layer = frame.get_layer(testing_frame)
    if(layer==2):
        create_apply2_then_core(exps, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt)
    elif(layer==3):
        get_tshape3(exps, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt)
    #print "done core-ops"
    return



# inner operation is binary
# outer operation is unary
def core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    ##print "\n--------------------------- core_binary_unary  ---------------------------"
    exps =  [exp1,  exp2]
    if(exp1==None or exp2==None):
        return
    core_ops(exps, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
    return


##################################################################################################
##################################################################################################

# all of the type choosing split into multiple function
# iterate over third type
def pick_ty_to_exp3(exps, dim, ty3s, tshape1, tshape2_shape, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    # terating over tyes that are possible
    #print "\n---------------------------pick_third_type ---------------------------"

    
    # can apply (shape1*shape2)* shape3 ->tshape2
    # assuming shape_to_fty() is ordered by dimension
    [t3, f3d1, f3d2, f3d3] = ty3s
    # now get exp3
    #print "cat-a"
    def instance(exp3, dim):
        #print "instance instance"
        if(exp3 == None):
            return
        else:

            #print "exp3: ",exp3.name, " dim: ", dim, "k:", exp3.k
            exp_t =exps+[exp3]
            convert_fields(exp_t, testing_frame)
            exp3 = exp_t[len(exps)]
    
            #print "input to check2_tshape: tshape1:", tshape1.name,"k",tshape1.k ,"tshape2_shape:",tshape2_shape.name
            tshape2 = check2_tshape(opr_outer1, tshape1, exp3, tshape2_shape, dim)
            #print "tshape2:", tshape2
            if(not(tshape2 == None)):
                #print "inside if"
                # both operations are binary so there are three expressions
                core_ops(exp_t, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
                return
        
    if(dim==0):
        # tensors for exp1,exp2
        for exp3 in ty3s:
            instance(exp3, dim)
            dim+=1
    else:
        # choose a field as first|second argument so the rest of the choices must have same dimension
        #print "cat-b"
        exp3s = [t3, ty3s[dim]]
        for exp3 in exp3s:
            #print "cat-c----"
          
            instance(exp3, dim)
        return


#opr_inner arity == 2,  opr_outer1.arity == _
def pick_ty_to_exp2(exp1, dim, ty2s, ty3s, tshape1_shape, tshape2_shape, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    # terating over tyes that are possible
    #writeCumulative(cnt)
    ##print "\n---------------------------pick_second_type ---------------------------"
    #m = title + "Types: ("+exp1.name+", _)"
    #writenow(m)
    title = ""

    # can apply (shape1*shape2)* shape3 ->tshape2
    # assuming shape_to_fty() is ordered by dimension
    [t2, f2d1, f2d2, f2d3] = ty2s
   
   # run single instance
    def instance(exp1, exp2, dim):
        if(exp2 == None):
            return
        else:
            # current dim: dimension should be based on exp1*exp2
            ##print "  mark: convert_rst_binary"
            exps = [exp1, exp2]
            # conver k to correct kernel
            convert_fields(exps, testing_frame)
            exp1 = exps[0]
            exp2 = exps[1]
            tshape1 = check2_tshape(opr_inner, exp1, exp2, tshape1_shape, dim)
            if(not (tshape1==None)):
                 # then we iterate over tys3s
                if (opr_outer1.arity == 2):
                     # opr_outer1.arity == 2, opr_inner arity == 2
                     
                    # so then we do iterate over tys3s
                    exps = [exp1, exp2]
                    #print "pick_ty_to_exp2- tshape1: ", tshape1.name, " k:",tshape1.k
                    #print "exp1:", exp1.name," k:", exp1.k
                    #print "exp2:", exp2.name," k:", exp2.k
                    pick_ty_to_exp3(exps, dim, ty3s, tshape1, tshape2_shape, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
                else:
                # opr_outer1.arity == 1,opr_inner arity == 2
                
                 # third type not needed
                 ## need to check actual expression
                 ##print "  mark: check1_tshape"
                 ##print "pre",tshape1,"op1",opr_outer1.name
                # converts shape to type (tshape2_shape)
                # check to see if it is expression (tshape1) is a  differentiable field (if needed)
                    tshape2 = check1_tshape(opr_outer1,  tshape1, tshape2_shape, dim)
                    if(not(tshape2 == None)):
                    ##print "can not be differentiated"
                    # go straigh to core
                    ##print "dim", dim, "post",tshape1.name
                        core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
            else:
                return
    # run multiple instance
    def iter(exp1, exp2s, dim):
        # [tensor, field,_]
        for exp2 in exp2s:
            instance(exp1, exp2, dim)
    # choose t1 as first argument
    if(dim==0):
        # [tensor,_, _]
        # [tensor, tensor,_]
        exp2 = t2
        instance(exp1,exp2, dim)
        # [tensor, field,_]
        # create second field type
        for d in range(3):
            d+=1
            exp2 = ty2s[d]
            instance(exp1, exp2, d)
    else:
        #[field, _,_]
        exp2s = [t2, ty2s[dim]]
        iter(exp1, exp2s, dim)


##################################################################################################
# iterate over third type
def backwards_ty_to_exp2(exp1, dim, ty2s, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt):
    # terating over tyes that are possible
    #writeCumulative(cnt)
    ##print "\n---------------------------pick_second_type ---------------------------"
    #m = title + "Types: ("+exp1.name+", _)"
    #writenow("Types: ("+exp1.name+", _)")
    title = ""
    # can apply (shape1*shape2)* shape3 ->tshape2
    # assuming shape_to_fty() is ordered by dimension
    [t2, f2d1, f2d2, f2d3] = ty2s
    ##print "t2:",t2, "f2d1",f2d1
    # run single instance
    def instance(exp2, dim):
        if(exp2 == None):
            return
        else:
            ##print "\n\t exp2"+exp2.name
            core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
            return

    # run multiple instance
    def iter(exp2s, dim):
        # [tensor, field,_]
        for exp2 in exp2s:
            ##print "\n\t exp2-attempt"
            instance(exp2, dim)
    # choose t1 as first argument
    if(dim==0):
        ##print "dim=0"
        # [tensor,_, _]
        # [tensor, tensor,_]
        exp2 = t2
        instance(exp2, dim)
        # [tensor, field,_]
        # create second field type
        for d in range(3):
            d+=1
            exp2 = ty2s[d]
            instance(exp2, d)
    else:
        #[field, _,_]
        ##print "dimmorethan 0"
        exp2s = [t2, ty2s[dim]]
        iter(exp2s, dim)

def backwards_ty_to_exp1(ty1s, dim, exp2, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt):
    # terating over tyes that are possible
    #writeCumulative(cnt)
    ##print "\n---------------------------pick_second_type ---------------------------"
    #m = title + "Types: ("+exp1.name+", _)"
    #writenow(m)
    title = ""
    # can apply (shape1*shape2)* shape3 ->tshape2
    # assuming shape_to_fty() is ordered by dimension
    [t2, f2d1, f2d2, f2d3] = ty1s
    
    # run single instance
    def instance(exp1, dim):
        if(exp1 == None):
            return
        else:
            core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
            return

    # run multiple instance
    def iter(exp1s, dim):
        # [tensor, field,_]
        for exp1 in exp1s:
            instance(exp1, dim)
        # choose t1 as first argument
    if(dim==0):
        # [tensor,_, _]
        # [tensor, tensor,_]
        exp1 = t2
        instance(exp1, dim)
        # [tensor, field,_]
        # create second field type
        for d in range(3):
            d+=1
            exp2 = ty1s[d]
            instance(exp1, d)
    else:
        #[field, _,_]
        exp1s = [t2, ty1s[dim]]
        iter(exp1s, dim)



##################################################################################################
# iterate over third type
def pick_ty_to_exp1(ty1s, ty2s, ty3s, tshape1_shape, tshape2_shape, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    # terating over tyes that are possible
    #writeCumulative(cnt)
    ##print "\n---------------------------pick_first_type ---------------------------"
    # can apply (shape1*shape2)* shape3 ->tshape2
    # assuming shape_to_fty() is ordered by dimension
    dim = 0
    for exp1 in ty1s:
         #[t1, f1d1, f1d2, f1d3] = ty1s
        if(not(exp1 == None)):
            # expressions must be created
            pick_ty_to_exp2(exp1, dim, ty2s, ty3s, tshape1_shape, tshape2_shape, opr_inner, opr_outer1,opr_outer2, title, testing_frame, cnt)
            dim+=1
##################################################################################################
##################################################################################################
# shape1 : shapes (ty_vecT)
# ty1 : types with specific shapes (ty_vecFT, ty_vecF_d1..)
# exp1: specific types on ty1s list ^

# apply second operation
def pick_get_ty3s(ty1s, ty2s, rtn3s, tshape1_shape, opr_inner, opr_outer1, title, testing_frame, cnt):
    # can apply (shape1*shape2)* shape3 ->tshape2
    titlec ="\n\t"
    k_init = 2
    for (shape3, tshape2_shape) in rtn3s:
        if (limit_in(shape3)):
            ##print "-------------"
            tmp = ""
            tmp = title+ " * "+shape3.name+")"
            #writenow("\n\t---Shape3:("+tmp)
            #writenow("\n shape3: "+shape3.name+"  tshape2_shape: "+tshape2_shape.name)
            # convert shape to type
            ty3s = shape_to_fty(shape3, k_init)
            #pes("ty3s", ty3s)
            #make sure non-tmpty third types
            if (len(ty3s)>3):
                pick_ty_to_exp1(ty1s, ty2s, ty3s, tshape1_shape, tshape2_shape, opr_inner, opr_outer1, opr_outer2,  titlec, testing_frame, cnt)
            else:
                # no shapes make this combination of operations possible
                continue



# main function
def pick_get_ty2s(ty1s, rtn2s, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    # #print " --------------second  time---------------"
    # #print  "opr_inner:", opr_inner.name, "opr_outer1:", opr_outer1.name
    titlec ="\n\t"
    n = len(op_all)
    k_init = 2
    for (shape2, tshape1_shape) in rtn2s:
        # limits arguments to certain shapes
        if(limit_in(shape2)):
        
            ##print "------------------------------"
            # convert shape to type
            ty2s = shape_to_fty(shape2, k_init)
            # pes("ty2s", ty2s)
            tmp = title+ " * "+shape2.name+")"
            #writenow("\n\t--Shape2:("+tmp)
            # Do we need  a third type?
            def sort(opr_outer1):
                if (opr_outer1.arity == 2):
                    # yes if outer operation is binary
                    rtn3s = op2_to_shape(opr_outer1, tshape1_shape)
                    if (len(rtn3s)>0):
                        pick_get_ty3s(ty1s, ty2s, rtn3s, tshape1_shape, opr_inner, opr_outer1, tmp, testing_frame, cnt)
                else:
                    # outer operation is a unary
                    tshape2_shape = op1_to_shape(opr_outer1, tshape1_shape)
                    if(not (tshape2_shape == None)):
                        ty3s = None
                        pick_ty_to_exp1(ty1s, ty2s, ty3s, tshape1_shape, tshape2_shape, opr_inner, opr_outer1, opr_outer2, titlec, testing_frame, cnt)
    
    
            if(opr_outer1==None):
                n = len(op_all)
                # for loop
                #for t_outer in range(n):
                t_outer = 0
                startyy = time.time()
                opr_outer1 = id_toOpr(t_outer)
                counter.zero_locals(cnt)
                counter.zero_total(cnt)
                writeTitle_outer(opr_inner, opr_outer1)
                sort(opr_outer1)
                endyy = time.time()
                tty = "  time-outer:"+str(endyy - startyy)
                writeall(tty)
                #print (tty)
                writeCumulative(cnt)
            else:
                sort(opr_outer1)
    return

  #(opr_outer1.arity == 1 and opr_inner.arity == 1)
def iter_inner_unary(ty1s, shape1, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt):
    def iter_unary_unary(opr_outer1):
        tshape1_shape = op1_to_shape(opr_inner, shape1)
        #print "------------------------------------------------------"
        #print "opr_outer1.arity == 1 and opr_inner.arity == 1"
        #print "inner", opr_inner.name, "outer", opr_outer1.name
        #print "\n apply inner operator", opr_inner.name, "on shape:", shape1.name, tshape1_shape
        if( tshape1_shape==None):
            #print "tshape1_shape=None"
            return
        for exp1 in ty1s:
            if(not (exp1==None)):
                #print "-------------------        ----"
                #print "exp1:", exp1.name
                tshape1 = check1_tshape(opr_inner, exp1, tshape1_shape, exp1.dim)
      
                if(not (tshape1 == None)):
                    #print "tshape1: ", tshape1.name
                    dim = tshape1.dim
                    tshape1_shape = tshape1.tensorType
                    #print "\n apply outer operator", opr_outer1.name, "on shape:", tshape1_shape.name
                    tshape2_shape = op1_to_shape(opr_outer1, tshape1_shape)
                    if(not (tshape2_shape == None)):
                        #print "\n checking outer op->"+tshape2_shape.name
                        tshape2 = check1_tshape(opr_outer1, tshape1,  tshape2_shape, dim)
                        #print "\n checking outer op tshape1:", tshape1.name,"tshape2-shape:",tshape2_shape.name, "dim",dim, "tshape2:", tshape2
                        if(not (tshape2 == None)):
                            #print "tshape2: ", tshape2.name
                            exps = [exp1]
                            
                            core_ops(exps, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)


    def iter_binary_unary(opr_outer1):
        #(opr_outer1.arity == 2 and opr_inner.arity == 1)
        # apply unary
        #pes("ty1s",ty1s)
        ##print " shape1: ", shape1.name
        #print "------------------------------------------------------"
        tshape1_shape = op1_to_shape(opr_inner, shape1)
        
        #print " opr_inner: ", opr_inner.name, "shape1: ", shape1.name, "tshape1_shape: ", tshape1_shape
        k_init = 2
        #print "----  mark A"
        if(not (tshape1_shape == None)):
            #print "op2_to_shape","opr_outer1: ",opr_outer1.name," tshape1_shape: ", tshape1_shape.name
            #print " top tshape1_shape.id: ", tshape1_shape.id,"ty_noneT.id: ", ty_noneT.id
            #print (tshape1_shape.id ==  ty_noneT.id)
            #apply binary
            if(not(tshape1_shape.id ==  ty_noneT.id)):
                # field type
                # need to run through check tshape
                #print "tshape1_shape ==  ty_noneT", opr_outer1.name, tshape1_shape.name," tshape1_shape", tshape1_shape.shape,"ty_noneT", ty_noneT.name,"ty_noneT.shape", ty_noneT.shape
                #print "AB"
                #print "tshape1_shape.id: ", tshape1_shape.id,"ty_noneT.id: ", ty_noneT.id
                rtn3s = op2_to_shape(opr_outer1, tshape1_shape)
                #print "----  mark B"
                #print "rtn3s:",len(rtn3s)
                for (shape3, tshape2_shape) in rtn3s:
                     if(limit_in(shape3)):
                        # convert shape to type
                        #print "----  mark C"
                        #print  "shape3: ",shape3.name," tshape2_shape: ", tshape2_shape.name," shape: ", tshape2_shape.shape
                        #print "shape3-name: " , shape3.name, "shape3-id:",shape3.id, "shape3-shape:",shape3.shape, "k_init: ", k_init
                        ty3s = shape_to_fty(shape3, k_init)
                        #print "post getting ty3s"
                        pes("ty3s",ty3s)
                        # single argument
                        if ((len(ty3s)>0) and  (len(ty1s)>0)):
                            #print "----  mark D"
                            for exp1 in ty1s:
                                #print "----  mark E"
                                #print "exp1: ", exp1
                                if(not (exp1==None)):
                                    #print "----  mark F"
                                    #print "exp1: ", exp1.name
                                    dim = exp1.dim
                                    #print "dim: ", dim
                                    #print "tshape1_shape: ",tshape1_shape.name
                                    exps = [exp1]
                                    
                                    convert_fields(exps, testing_frame)
                                    exp1 = exps[0]
                                    exps = [exp1]
                    
                                    tshape1 = check1_tshape(opr_inner,  exp1, tshape1_shape, dim)
                                    if(not (tshape1 == None)):
                                        #print "----  mark G"
                                        #core_ops(exps, dim, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt)
                                        #print "tshape1:", tshape1.name
                                        #print "tshape2_shape:", tshape2_shape.name
                                        pes("ty3s",ty3s)
                                        #print "inner;", opr_inner.name, "outer:",opr_outer1.name
                                        
                                        #print "iter_binary_unary- tshape1: ", tshape1.name, " k:",tshape1.k
                                        #print "exp1:", exp1.name," k:", exp1.k
                           
                                                        
                                        pick_ty_to_exp3(exps, dim, ty3s, tshape1, tshape2_shape, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
            else:
                for exp1 in ty1s:
                    #print "----  marker a"
                    #print "exp1: ", exp1
                    if(not (exp1==None)):
                        #print "----  marker b"
                        #print "exp1: ", exp1.name
                        dim = exp1.dim
                        #print "dim: ", dim
                        #print "tshape1_shape: ",tshape1_shape.name
                        exps = [exp1]
                        convert_fields(exps, testing_frame)
                        exp1 = exps[0]
                        exps = [exp1]
                    
                        #print "check1_tshape:","exp1:",exp1.name, " k:",exp1.k
                        tshape1 = check1_tshape(opr_inner,  exp1, tshape1_shape, dim)
                        if(not (tshape1 == None)):
                            #print "----  marker c "
                            #core_ops(exps, dim, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt)
                            #print "tshape1:", tshape1.name


                            #print "inner;", opr_inner.name, "outer:",opr_outer1.name,"tshape1_shape: ",tshape1_shape.name,"tshape1_shape-shape: ",tshape1_shape.shape
                            #print "opr_outer1", opr_outer1.name
                            #print "tshape1: ", tshape1
                            #print "tshape1.name: ",tshape1.name
                            #print "op2_to_shape---"
                            tshape1_shape = tshape1.tensorType
                            rtn3s = op2_to_shape(opr_outer1, tshape1_shape)
                            for (shape3, tshape2_shape) in rtn3s:
                                if(limit_in(shape3)):
                                    # convert shape to type
                                    #print "----  marker d "
                                    ##print  "shape3: ",shape3.name," tshape2_shape: ", tshape2_shape.name," shape: ", tshape2_shape.shape
                                    # #print "shape3-name: " , shape3.name, "shape3-id:",shape3.id, "shape3-shape:",shape3.shape, "k_init: ", k_init
                                    ty3s = shape_to_fty(shape3, k_init)
                                    #print "post getting ty3s"
                                    pes("ty3s",ty3s)
                            
                                    #print "iter_binary_unary-else- tshape1: ", tshape1.name, " k:",tshape1.k
                                    #print "exp1:", exp1.name," k:", exp1.k
     
                                    
                                    pick_ty_to_exp3(exps, dim, ty3s, tshape1, tshape2_shape, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)




    def sort(opr_outer1):
        if(opr_inner.arity == 1 and opr_outer1.arity == 1): # arity is 1
            iter_unary_unary(opr_outer1)
        elif(opr_outer1.arity == 2 and opr_inner.arity == 1):
            iter_binary_unary(opr_outer1)
    # need to iterate over outer operator
    if(opr_outer1==None):
        n = len(op_all)
        for  t_outer in range(n):
            startouter = time.time()
            opr_outer1 = id_toOpr(t_outer)
            counter.zero_locals(cnt)
            counter.zero_total(cnt)
            writeTitle_outer(opr_inner, opr_outer1)
            sort(opr_outer1)
            endouter = time.time()
            ttouter ="shape-> inner->outer"+opr_inner.name+"_"+opr_outer1.name+"  time: "+str(endouter - startouter)
            writeall(ttouter)
            #print (ttouter)
    else:
        sort(opr_outer1)

# main function
def pick_get_ty1s(ty1s, shape1, opr_inner, opr_outer1, opr_outer2, testing_frame, cnt):
    # apply operation a first time
    ##print " --------------first time---------------"
    ##print  "\t\topr_inner:", opr_inner.name, opr_inner.arity,"\n\topr_outer1:", opr_outer1.name,opr_outer1.arity
    title = "("+shape1.name
    #writenow("\n-Shape1:"+title+" * _)")

    #pes("ty1s",ty1s)
    ##print "attempt:"+opr_inner.name+"shape1", shape1.name
    if(opr_inner.arity == 1): # arity is 1
        # meaning this one is fine
        iter_inner_unary(ty1s, shape1, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
    else:
        rtn2s = op2_to_shape(opr_inner, shape1)
        if (len(rtn2s)>0):
            n = len(op_all)
                #for t_outer in range(n):
                #opr_outer1 = id_toOpr(t_outer)
            pick_get_ty2s(ty1s, rtn2s, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
        else:
            return
    return
##################################################################################################

# go backwards
# assume outer is op1
# assumes inner is op2
def go_backwards(opr_outer1, opr_inner, testing_frame, cnt):
    k_init = 2
    #print "opr_outer1: ",opr_outer1.name, " opr_inner: ",opr_inner.name
    rst2  =  backward_op1(opr_outer1,  k_init)
    # assumes binary outer
    # assume unary inner
    title =""
    #print "rst2:", len(rst2)
    for  (tshape1, tshape2) in rst2:
   
        if((tshape1 ==None) or (tshape2 == None)):
            continue
        # (_,_)-> tshape
        #print "opr_outer1: ",opr_outer1.name, " opr_inner: ",opr_inner.name
        #print " tshape1: ", tshape1
        #print " tshape2 : ", tshape2
        dim = tshape2.dim
        # set one of the expressions to be a field
        ty1s = d_tofield(dim)
         # (exp1, _)-> tshapes
        #print "##############################"
        #print "dim: ", dim, "tshape1:",tshape1.name, "tshape2:",tshape2.name
        # arity is 2
        for exp  in ty1s:
            # needs to find 2nd argument
            #print "#############"
            #print "dim: ", dim, "tshape1:",tshape1.name, "tshape1:",tshape1.name
            #print "exp:",exp.name
            exp1 = exp
            #(exp1 * shape2) ==> tshape1
            #print "(exp1 * shape2) ==> tshape1"
            shape2 = backwards_op2_arg1(opr_inner, tshape1, exp1)

            if(not(shape2==None)):
                #print "rst2:##########################",opr_outer1.name,"(",tshape1.name,") ->",tshape2.name
                #print "rst2:","(",exp1.name,opr_inner.name,shape2.name,") ->",tshape1.name
                #print "rst2:",opr_outer1.name,"(",exp1.name,opr_inner.name,shape2.name,") ->",tshape2.name
                
                #tt ="\t\tex.(exp1:"+exp1.name+", shape2:"+shape2.name+")-> "+tshape2.name
                ##print(tt)
                ##print "dim: ", dim, "tshape1:",tshape1.name, "tshape2:",tshape2.name
                ##print "outer: ", opr_outer1.name,"tshape1:",tshape1.name,"-->tshape2:",tshape2.name
                ##print "inner: ", opr_inner.name, "(exp1: "+exp1.name+ ", shape2: "+shape2.name +  " )-->tshape1:",tshape1.name
                #print "shape2",shape2
                # convert shape to type
                k_init  = tshape1.k
                ##print "before rt2s"
                ty2s = shape_to_fty(shape2, k_init)
                ##print "len:", len(ty2s)
                #(exp1 * shape2) ==> tshape1
                if(fty.is_Field(tshape1) and (not (fty.is_Field(exp1)))):
                    # then exp2 must be a field
                    #print "mark -a"
                    exp2= ty2s[tshape1.dim]
                    core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
                ##print "inner: ", opr_inner.name, "(exp1: "+exp1.name+ ", ty2s[tshape1.dim]: "+ty2s[tshape1.dim].name +  " )-->tshape1:",tshape1.name
                elif(fty.is_Tensor(tshape1)):
                
                    # then exp2 must be  a tensor
                    exp2= ty2s[0]
                    ##print "inner: ", opr_inner.name, "(exp1: "+exp1.name+ ", ty2s[0]: "+ty2s[0].name +  " )-->tshape1:",tshape1.name
                    #print"mark-b"
                    if((exp1==None) or  (exp2==None) or (tshape1==None) or (tshape2==None)):
                        core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)
                    else:
                        continue
                else:
                            # then exp2 can by anything
                    ##print "inner: ", opr_inner.name, "(exp1: "+exp1.name+ ", ty2s-: ",len(ty2s),  " )-->tshape1:",tshape1.name
                    #print "mark-c"
                    backwards_ty_to_exp2(exp1, dim, ty2s, tshape1, tshape2, opr_inner, opr_outer1, title, testing_frame, cnt)
        
                #(shape1 * exp2) ==> tshape1
            #print "(shape1 * exp2) ==> tshape1"
            exp2 = exp
            shape1 = backwards_op2_arg2(opr_inner, tshape1, exp2)
            if(not (shape1==None)):
                t = "\t\tex.(shape1:"+shape1.name+", exp2:"+exp2.name+")-> "+tshape2.name
                #print(t)
                # convert shape to type
                exp1 = shape_to_tensor(shape1)
                writeall("mark-d")
                core_binary_unary(exp1, exp2, dim, tshape1, tshape2, opr_inner, opr_outer1, opr_outer2, title, testing_frame, cnt)



##################################################################################################
##################################################################################################
# main does everything fowards
# shape -> inner-> outer
# not operatot inputs
def pick_shape(testing_frame, cnt):
    #writeTitle_outer(opr_inner, opr_outer1)
    # iterate over shapes for first terms
    #shapes = tvs+tms#+tt2+tt3+tt4
    shapes = tvs+tms_sym
    n = len(op_all)
    startall = time.time()
    opr_outer1 = None
    opr_outer2 = None
    writeCumulative(cnt)
    for shape1 in shapes:
        # is shape a permitted size?
        if(limit_in(shape1)):
            startshape = time.time()
            writeall ("shape:"+shape1.name)
            ##print "shape1 ", shape1
            k_init = 2
            ty1s = shape_to_fty(shape1, k_init)
            writeall("shape1:"+shape1.name)
            writeall("ty1s:"+str(len(ty1s)))
            # iterating over inner operator
            for t_inner in range(n):
                # get operator from id
                opr_inner = id_toOpr(t_inner)
                # zero counters
                counter.zero_locals(cnt)
                counter.zero_total(cnt)
                # iterate over shape1
                pick_get_ty1s(ty1s, shape1, opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
                # results
                write_results("done all inner for a shape "+shape1.name, testing_frame, cnt)

    # timing and results
    writeCumulative(cnt)
    endall = time.time()
    ttall = " shape->.. time:"+ str(endall - startall)
    writeall(ttall)
    #print (ttall)
    write_results("done everything ", testing_frame, cnt)
    writeCumulative(cnt)
    return


# t_inner already chosen
def pick_shape_op1(t_inner, testing_frame, cnt):
    #writeTitle_outer(opr_inner, opr_outer1)
    # iterate over shapes for first terms
    #shapes = tvs+tms#+tt2+tt3+tt4
    shapes = tvs+tms_sym
    n = len(op_all)
    startall = time.time()
    opr_outer1 = None
    opr_outer2 = None
    writeCumulative(cnt)
    for shape1 in shapes:
        # is shape a permitted size?
        if(limit_in(shape1)):
            startshape = time.time()
            writeall ("shape:"+shape1.name)
            ##print "shape1 ", shape1
            k_init = 2
            ty1s = shape_to_fty(shape1, k_init)
            writeall("shape1:"+shape1.name)
            writeall("ty1s:"+str(len(ty1s)))
            
            # get operator from id
            opr_inner = id_toOpr(t_inner)
            # zero counters
            counter.zero_locals(cnt)
            counter.zero_total(cnt)
            # iterate over shape1
            pick_get_ty1s(ty1s, shape1, opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
            # results
            write_results("done all inner for a shape "+shape1.name, testing_frame, cnt)
    # timing and results
    writeCumulative(cnt)
    endall = time.time()
    ttall = " shape->.. time:"+ str(endall - startall)
    writeall(ttall)
    #print (ttall)
    write_results("done everything ", testing_frame, cnt)
    writeCumulative(cnt)
    return

# t_inner, t_outer1 already chosen
def pick_shape_op1(t_inner, t_outer1, testing_frame, cnt):
    #writeTitle_outer(opr_inner, opr_outer1)
  
    shapes = tvs+tms_sym
    n = len(op_all)
    startall = time.time()

    opr_outer2 = None
    writeCumulative(cnt)
    for shape1 in shapes:
        # is shape a permitted size?
        if(limit_in(shape1)):
            startshape = time.time()
            writeall ("shape:"+shape1.name)
            ##print "shape1 ", shape1
            k_init = 2
            ty1s = shape_to_fty(shape1, k_init)
            writeall("shape1:"+shape1.name)
            writeall("ty1s:"+str(len(ty1s)))
            
            # get operator from id
            opr_inner = id_toOpr(t_inner)
            opr_outer1 = id_toOpr(t_outer1)
            # zero counters
            counter.zero_locals(cnt)
            counter.zero_total(cnt)
            # iterate over shape1
            pick_get_ty1s(ty1s, shape1, opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
            # results
            write_results("done all inner for a shape "+shape1.name, testing_frame, cnt)
    # timing and results
    writeCumulative(cnt)
    endall = time.time()
    ttall = " shape->.. time:"+ str(endall - startall)
    writeall(ttall)
    #print (ttall)
    write_results("done everything ", testing_frame, cnt)
    writeCumulative(cnt)
    return
