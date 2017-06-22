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
from nc_eval import unary, binary, probeField

def applyUnaryOnce(oexp_inner,app_inner,app_outer, pos):
    ##print "applyUnaryOnce",app_inner.opr.name,"-",app_outer.opr.name
    #apply.toStr(app_inner)
    oty_inner = apply.get_oty(app_inner)
    oty_outer = apply.get_oty(app_outer)
    opr_outer = app_outer.opr
    ##print "oexp_inner",oexp_inner,"opr_outer",opr_outer.name
    lhs_tmp = field(true, "tmp", oty_inner, "", oexp_inner, "")
    #create new apply
    app_tmp = apply("tmp", opr_outer, lhs_tmp, None, oty_outer, true, true)
    oexp_tmp = unary(app_tmp)
    print "after applying: ",app_tmp.opr.name
    print " oexp_tmp", oexp_tmp
    rtn = probeField(app_tmp.oty, pos, oexp_tmp)
    print "after applying: ",app_tmp.opr.name," rtn:", rtn
    return (oty_outer, oexp_tmp)

def applyBinaryOnce(oexp_inner,app_inner,app_outer,rhs, pos):
    oty_inner = apply.get_oty(app_inner)
    oty_outer = apply.get_oty(app_outer)
    opr_outer = app_outer.opr
    
    lhs_tmp = field(true, "tmp", oty_inner, "", oexp_inner, "")
    
    app_tmp = apply("tmp", opr_outer, lhs_tmp, rhs, oty_outer, true,true)
    oexp_tmp = binary(app_tmp)
    
    print " before applying: ",app_tmp.opr.name
    print " lhs_tmp", oexp_inner
    print "rhs tmp", rhs.data

    print "after applying: ",app_tmp.opr.name
    print " oexp_tmp", oexp_tmp
    rtn = probeField(app_tmp.oty, pos, oexp_tmp)
    print "after applying: ",app_tmp.opr.name," rtn:", rtn
    return (oty_outer, oexp_tmp)



# sort all applications
def sort(e, pos):
    #a ssingle application
    def simple_apply(c_layer, app):
        arity = apply.get_arity(app)
        oty = apply.get_oty (app)
        if (arity ==1):
            b = unary(app)
            rtn = probeField(app.oty, pos, b)
            print "after applying: ",app.opr.name," rtn:", rtn
            return (oty, b)
        elif (arity ==2):
            print " before applying: ",app.opr.name
            print " lhs_tmp",  probeField(app.lhs.fldty, pos, app.lhs.data)
            print "rhs tmp",  probeField(app.rhs.fldty, pos, app.rhs.data)
            
            
            b = binary(app)
            otyp1 = ty_vec3F_d3
            print "after applying: ",app.opr.name
            print " oexp_tmp", otyp1
            rtn = probeField(app.oty, pos, b)
            print "after applying: ",app.opr.name," rtn:", rtn
            return (oty, b)
        else:
            raise Exception ("arity is not supported: "+str(arity_outer))
    #  multiple applications
    def get_gfnc(c_layer):
        if (c_layer==1):
            return simple_apply
        else:
            # calls embed multiple times
            return embed
    def embed(c_layer, app_tmp):
        ##print "embed",c_layer,app_tmp
        ##print app_tmp.opr.name
        arity = apply.get_arity(app_tmp)
        gfnc = get_gfnc(c_layer)
        if(arity==1):
            app_inner = apply.get_unary(app_tmp)
            (_, oexp_inner) = gfnc(c_layer-1, app_inner)
            (oty_outer, oexp_tmp) =  applyUnaryOnce(oexp_inner, app_inner, app_tmp, pos)
            rtn = probeField(oty_outer, pos, oexp_tmp)
            #print "rtn:", rtn
            return (oty_outer, oexp_tmp)
        elif(arity==2):
            (app_outer1, rhs) =  apply.get_binary(app_tmp)
            # apply 1st and second layer
            (_, oexp_tmp) = gfnc(c_layer-1, app_outer1)
            # applies third layer
            (oty_outer, oexp_tmp) = applyBinaryOnce(oexp_tmp, app_outer1, app_tmp, rhs, pos)
       
            rtn = probeField(oty_outer, pos, oexp_tmp)
            #print "rtn:", rtn
            return (oty_outer, oexp_tmp)
        else:
            raise Exception("arity is not supported:"+str(arity))

    def getLayers(m):
        if(m.isrootlhs):
            return 0
        else:
            return 1+getLayers(m.lhs)
    c_layer =  getLayers(e)
    if(e.isrootlhs): # is root
        # 1 layer
        #c_layer = 1
        return embed(1, e)
    else:
        # 3 layers
        #print "layers", c_layer
        return embed(c_layer, e)

# ***************************  main  ***************************

# operators with scalar field and vector field
def eval(app, pos):
    #print "evalname",app.name
    ##print apply.toStr(app,3)
    #print "about to sort"
    (otyp1, ortn) = sort(app, pos) #apply operations to expressions
    # #print "ortn|:", ortn
    #print "about probe"
    rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
    ##print "rtn", rtn
    return rtn
