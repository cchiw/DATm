import sympy
from sympy import *
#symbols
x,y,z =symbols('x y z')
import sys
import re
import math

# shared base programs
from obj_ty import *
from obj_apply import *
from obj_operator import *
from obj_field import *
#specific nc programs
from nc_eval import unary, binary, third, probeField

# ***************************  applying a single operator ***************************
  #a single application
def simple_apply(c_layer, app, pos):
    arity = apply.get_arity(app)
    oty = apply.get_oty (app)
    if (arity ==1):
        b = unary(app)
        rtn = probeField(app.oty, pos, b)
        #print "after applying: ",app.opr.name," rtn:", rtn
        #tmp = apply(app.name, op_norm, app.lhs, app.rhs, app.third, ty_scalarF_d3, app.isrootlhs, app.isrootrhs)
        # rtn = probeField(tmp.oty, pos, unary(tmp))
        #print "after applying: ",tmp.opr.name," rtn:", rtn
        #tmp = apply(app.name, op_copy, app.lhs, app.rhs, app.third, app.oty, app.isrootlhs, app.isrootrhs)
        #rtn = probeField(tmp.oty, pos, unary(tmp))
        #print "after applying: ",tmp.opr.name," rtn:", rtn
        
        return (oty, b)
    elif (arity ==2):
        b = binary(app)
        return (oty, b)
    elif (arity ==3):
        b = third(app)
        return (oty, b)
    else:
        raise Exception ("arity is not supported: "+str(app.opr.arity))
#create field and an apply instance
#then apply a single operator
def applyOnce(oexp_inner, app_inner, app_outer, rhs1, rhs2, pos, arity):
    oty_inner = apply.get_oty(app_inner)
    oty_outer = apply.get_oty(app_outer)
    opr_outer = app_outer.opr
    lhs_tmp = field(true, "tmp", oty_inner, "", oexp_inner, "", None)
    #create new apply
    app_tmp = apply("tmp", opr_outer, lhs_tmp, rhs1, rhs2, oty_outer, true, true)
    return simple_apply(None, app_tmp, pos)


# ***************************  sorting an apply object ***************************
# sort all applications
def sort(e, pos):
    def get_gfnc(c_layer):
        if (c_layer==1):
            #a single application
            return simple_apply
        else:
            # calls embed multiple times
            return embed
    def embed(c_layer, app_tmp, _):
        arity = apply.get_arity(app_tmp)
        gfnc = get_gfnc(c_layer)
        # get arguments
        [app_inner, rhs, third] = apply.getArgs(app_tmp)
        # apply 1st and second layer
        (_, oexp_inner) = gfnc(c_layer-1, app_inner, pos)
        # applies third layer
        (oty_outer, oexp_tmp) = applyOnce(oexp_inner, app_inner, app_tmp, rhs, third, pos, arity)
        return (oty_outer, oexp_tmp)
     
    # number of layers
    def getLayers(m):
        if(m.isrootlhs):
            return 0
        else:
            return 1+getLayers(m.lhs)
    if(e.isrootlhs): # is root
        return embed(1, e, pos)
    else:
        c_layer =  getLayers(e)
        return embed(c_layer, e, pos) #multipler layers


# ***************************  main  ***************************
# evaluate an applicaiton at positions. returns the resulting expression.
def eval(app, pos):
    if(app.isrootlhs):
        (otyp1, ortn) = simple_apply(0, app, pos)
        rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
        return rtn

##############################################################################
######################## get max or min
def getMaxOrMin(opr, lhs, rhs):
    print "\n\t **** result from probing field: \n\tlhs: ",lhs, "\n\trhs:",rhs
    rtn = []
    if(opr.id==op_max.id):
        for (l,r) in zip(lhs, rhs):
            if(l< r):
                rtn.append(r)
            else:
                rtn.append(l)
    elif(opr.id==op_min.id):
        for (l,r) in zip(lhs, rhs):
            if(l> r):
                rtn.append(r)
            else:
                rtn.append(l)
    return rtn
######################## get max or min of an inner operator
# create a new app (using exp as lhs)
# then probe at a position
def applyProbe(exp, app, pos):
    appL = apply("tmp", app.opr, exp, app.rhs, app.third, app.oty, true, true)
    (otyp1L, ortnL) = simple_apply(0, appL, pos)
    rtnL = probeField(otyp1L, pos, ortnL)
    #print "\n\n\nto apply operator:", app.opr.name, " on \n\t", exp.data, "\n\t",app.rhs.data,"\n\tresult:", ortnL, "\n\tprobed:", rtnL
    
    return rtnL

#applying max|min to another operator
def getGradMax(opr, app, pos, lhs, rhs, e3,e4):

    rtnL = applyProbe(e3, app, pos)
    rtnR = applyProbe(e4, app, pos)
    print "\n\t **** result from probing field: \n\tlhs: ",lhs, "\n\tlhs exp:",e3.data, "\n\t apply then probe", rtnL
    print "\n\t **** result from probing field: \n\trhs: ",rhs, "\n\trhs exp:",e4.data, "\n\t apply then probe", rtnR
    
    rtn = []
    if(opr.id==op_max.id):
        # get max between lhs and rhs (which are values)
        # maximum determines which expression to use (rtnL, rtnR)
        # then apply operator to expression
        for (l,r, al, ar) in zip(lhs, rhs, rtnL, rtnR):
            print "comparing l:", l, "r:",r
            if(l< r):
                print "adding to list: ar ", ar
                rtn.append(ar)
            else:
                print "adding to list al: ", al
                rtn.append(al)
    elif(opr.id==op_min.id):
        for (l,r, al, ar) in zip(lhs, rhs, rtnL, rtnR):
            print "comparing l:", l, "r:",r
            if(l>r):
                print "adding to list: ar ", ar
                rtn.append(ar)
            else:
                print "adding to list al: ", al
                rtn.append(al)
    print "rtn:", rtn
    return rtn


######################## max of a max
#specifically applying the gradient
def getMaxTwice(op1,op2,e0, e1, e2):
    def getOp(opr):
        if(opr.id == op_max.id):
            return max
        else:
            return min
    rtn = []
    for (a0, a1, a2) in zip(e0, e1, e2):
        rtn.append(getOp(op2)(a0,getOp(op1)(a1, a2)))

    return rtn

#probe lhs and rhs of app
def multipleProbe(app, pos):
    lhs = probeField(app.oty, pos, app.lhs.data)
    rhs = probeField(app.oty, pos, app.rhs.data)
    print "\n\nresult of multiple probe \n\t lhs exp:", app.lhs.data, "\n\tlhs:",lhs
    print "\n\nresult of multiple probe \n\t rhs:", app.rhs.data, "\n\trhs:",rhs
    return (lhs, rhs)
# ***************************  main  ***************************
# evaluate an applicaiton at positions. returns the resulting expression.
def eval(app, pos):
    # outer layer is max|min
    if((app.opr.id == op_max.id) or (app.opr.id == op_min.id)):
        if(app.isrootlhs):
            # layer is 1
            (lhs, rhs) = multipleProbe(app, pos)
            return getMaxOrMin(app.opr, lhs, rhs)
        elif((app.lhs.opr.id == op_max.id) or (app.lhs.opr.id == op_min.id)):
            # layer is 2- inner op is another max|min
            shift = app.lhs
            (e1, e2) = multipleProbe(shift, pos)
            e0 = probeField(app.oty, pos, app.rhs.data)
            rtn = getMaxTwice(shift.opr, app.opr, e0, e1, e2)
            return rtn
        else:
            # layer is 2 - inner op not another max|min
            # probe result of 2nd or 3rd app then compare it
            shift = app.lhs
            rtnL = applyProbe(shift.lhs, shift, pos)
            rhs = probeField(app.oty, pos, app.rhs.data)
            return getMaxOrMin(app.opr,rtnL, rhs)
    elif(app.isrootlhs):
        # layer is 1
        (otyp1, ortn) = simple_apply(0, app, pos)
        rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
        return rtn
    elif((app.lhs.isrootlhs) and ((app.lhs.opr.id == op_max.id) or (app.lhs.opr.id == op_min.id))):
        # layer is 2
        # inner layer is a max or min
            print "layer 2 with inner layer being max/min"
            shift = app.lhs
            (e1, e2) = multipleProbe(shift, pos)
            rtn = getGradMax(app.lhs.opr, app, pos, e1,e2, shift.lhs, shift.rhs)
            return rtn
    else:
        (otyp1, ortn) = sort(app, pos) #apply operations to expressions
        rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
        return rtn
