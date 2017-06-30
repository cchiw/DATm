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
def simple_apply(c_layer, app):
    arity = apply.get_arity(app)
    oty = apply.get_oty (app)
    if (arity ==1):
        b = unary(app)
        #rtn = probeField(app.oty, pos, b)
        #print "after applying: ",app.opr.name," rtn:", rtn
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
    return simple_apply(None, app_tmp)


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
    def embed(c_layer, app_tmp):
        arity = apply.get_arity(app_tmp)
        gfnc = get_gfnc(c_layer)
        # get arguments
        [app_inner, rhs, third] = apply.getArgs(app_tmp)
        # apply 1st and second layer
        (_, oexp_inner) = gfnc(c_layer-1, app_inner)
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
        return embed(1, e)
    else:
        c_layer =  getLayers(e)
        return embed(c_layer, e) #multipler layers

# ***************************  main  ***************************
# evaluate an applicaiton at positions. returns the resulting expression.
def eval(app, pos):
    #"about to sort"
    (otyp1, ortn) = sort(app, pos) #apply operations to expressions
    rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
    return rtn
