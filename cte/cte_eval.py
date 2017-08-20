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
    lhs_tmp = field(true, "tmp", oty_inner, "", oexp_inner, "")
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
def getMax(lhs, rhs):
    rtn = []
    for (l,r) in zip(lhs, rhs):
        if(l< r):
            rtn.append(r)
        else:
            rtn.append(l)
    return rtn

def getMin(lhs, rhs):
    print "inside get min"
    print "\n\t **** result from probing field: \n\tlhs: ",lhs, "\n\trhs:",rhs
    rtn = []
    for (l,r) in zip(lhs, rhs):
        if(l> r):
            rtn.append(r)
        else:
            rtn.append(l)
    return rtn

#specifically applying the gradient
def getGradMax(app, pos, lhs, rhs, e3,e4):
    print "\n\t **** result from probing field: \n\tlhs: ",lhs, "\n\trhs:",rhs

    def applyProbe(exp):
        appL = apply("tmp", app.opr, exp, app.rhs, app.third, app.oty, true, true)
        (otyp1L, ortnL) = simple_apply(0, appL, pos)
        rtnL = probeField(otyp1L, pos, ortnL)
        print "rtnL: ", rtnL
        return rtnL
        
    rtnL = applyProbe(e3)
    rtnR = applyProbe(e4)
    rtn = []
    for (l,r, al, ar) in zip(lhs, rhs, rtnL, rtnR):
        print "comparing l:", l, "r:",r
        if(l< r):
            print "adding to list: ar ", ar
            rtn.append(ar)
        else:
            print "adding to list al: ", al
            rtn.append(al)
    print "rtn:", rtn
    return rtn


#specifically applying the gradient
def getGradMin(app, pos, lhs, rhs, e3,e4):
    print "\n\t **** result from probing field: \n\tlhs: ",lhs, "\n\trhs:",rhs
    
    def applyProbe(exp):
        appL = apply("tmp", app.opr, exp, app.rhs, app.third, app.oty, true, true)
        (otyp1L, ortnL) = simple_apply(0, appL, pos)
        rtnL = probeField(otyp1L, pos, ortnL)
        print "rtnL: ", rtnL
        return rtnL
    
    rtnL = applyProbe(e3)
    rtnR = applyProbe(e4)
    rtn = []
    # get max between lhs and rhs (which are values)
    # maximum determines which expression to use (rtnL, rtnR)
    # then apply operator to expression
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



#specifically applying the gradient
def getMaxMax(op1,op2,e0, e1, e2):
    rtn = []
    for (a0, a1, a2) in zip(e0, e1, e2):

        rtn.append(op2(a0,op1(a1, a2)))

    return rtn

def getOp(app):
    if(app.opr.id == op_max.id):
        return max
    else:
        return min

# ***************************  main  ***************************
# evaluate an applicaiton at positions. returns the resulting expression.
def eval(app, pos):
    if(app.isrootlhs):
        if (app.opr.id == op_max.id):
            oty = app.oty
            lhs = probeField(app.oty, pos, app.lhs.data)
            rhs = probeField(app.oty, pos, app.rhs.data)
            return getMax(lhs, rhs)
        elif (app.opr.id == op_min.id):
            oty = app.oty
            lhs = probeField(app.oty, pos, app.lhs.data)
            rhs = probeField(app.oty, pos, app.rhs.data)
            ortn = getMin(lhs, rhs)
            print "\nortn:",ortn
            return ortn
        else:
            (otyp1, ortn) = simple_apply(0, app, pos)
            rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
            return rtn
    else:
        if((app.lhs.opr.id == op_max.id) or (app.lhs.opr.id == op_min.id)):
            shift = app.lhs
            oty = shift.oty
            e3 = shift.lhs
            e4 = shift.rhs
            e1 = probeField(oty, pos, e3.data)
            e2 = probeField(oty, pos, e4.data)
            if((app.opr.id == op_max.id) or (app.opr.id == op_min.id)):
                op2 = getOp(shift)
                op1 = getOp(app)
                e0 = probeField(app.oty, pos, app.rhs.data)
                rtn = getMaxMax(op2, op1, e0, e1, e2)
                return rtn
            elif(app.lhs.opr.id == op_max.id):
                # need to check inside first
                # chooses based on inside result
                rtn = getGradMax(app, pos, e1,e2, e3, e4)
                return rtn
            elif(app.lhs.opr.id == op_min.id):
                rtn = getGradMin(app, pos, e1,e2, e3, e4)
                return rtn
        else:
            (otyp1, ortn) = sort(app, pos) #apply operations to expressions
            rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
            return rtn
