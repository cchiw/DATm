# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re

# shared base programs
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_constants import *
from input import s_field



adj = (opr_adj)
template="shared/template/foo.ddro"     # template

#strings in diderot template
foo_in="foo_in"
foo_outTen="foo_outTen"
foo_op ="foo_op"
foo_probe ="foo_probe"
foo_length="foo_length"
#otherwise variables in diderot program
foo_out="out"
foo_pos="pos"
const_out ="7.2"
opfieldname1="G"
eps = "0.01"

# constants from contants file
removeCond = False # FIXME flag_vis_test



def write(f,foo):
 f.write(foo)
##################################### field declaration helpers #####################################
def fieldName(i):
    return "F"+str(i)
# type of field
def fieldShape(f, fldty):
    #print "fldty: ",fldty
    foo = fty.toDiderot(fldty)
    f.write(foo)
# writing to a line
def write_shape(pre, f, typ, lhs, rhs):
    f.write(pre)
    # type of resulting field
    fieldShape(f, typ)
    # set expression equal to output field
    foo = lhs+" = "+rhs+";\n"
    # Write to file
    write(f, foo)
##################################### input tensor/field #####################################
#field input line
#f: file to write to
#k:continuity
#itypes: types for input field
#inputlist: name for input data
def inShape_base(f, exps):
    #app = apply.get_root_app(appC)
    i=0
    for exp in exps:
        #print "current fld",field.toStr(exp)
        dim = field.get_dim(exp)
        fieldShape(f, exp.fldty)
        if (field.get_isField(exp)):
            krnstr = exp.krn.str
            foo= fieldName(i)+" = "+krnstr+u'⊛'+"  image(\""+exp.inputfile+".nrrd\");\n"
            f.write(foo)
        else: #tensor type
            foo= fieldName(i)+" = "+str(field.get_data(exp))+";\n"
            f.write(foo)
        i+=1
#inputlist: name for input data
def inShape(f, appC):
    exps = apply.get_all_Fields(appC)
    inShape_base(f, exps)
##################################### output tensor/field #####################################
#instaniate output tensor
def outLineTF(type,s):
    otype= fty.get_tensorType(type)
    def mkMat(i, e):
        rtn = " ["+e
        for i in range(i-1):
            rtn +=","+e
        rtn+= "]"
        return rtn
    if (ty_scalarT==otype):
        return s
    elif(tty.isVec(otype)):
        [i] = otype.shape
        return mkMat(i,s)
    elif(tty.isMat(otype)):
        [j, i] = otype.shape
        return mkMat(j, mkMat(i,s))
    elif(tty.isTen3(otype)):
        [k, j, i] = otype.shape
        return mkMat(k, mkMat(j, mkMat(i,s)))
#instaniate output tensor
def outLineF(f, type):
    otype = fty.get_tensorType(type)
    foo="\toutput "
    foo+="tensor "+str(otype.shape)+" "+foo_out+" = "+outLineTF(type,"0.0")+";\n\t"
    f.write(foo)

##################################### field declaration helpers #####################################
# checks inside a field but not inside a tensor term
def getInside(exp, pos, name,):
    inside ="inside"
    if ((s_field==field_pde)):
        inside ="insideF"
    
    if (fty.is_Field(exp.fldty)):
        return "("+inside+"("+name+","+pos+")) && "
    else:
        return ""
# probes field at variable position
def makeProbe(exp, pos,cfenames):
    if (s_field==field_cfe):
        return "inst("+const_probeG_cfe+cfenames+")"
    else:
        return "("+exp+")("+pos+")"


def isProbe(cfenames,exp, fld):
    #print "\n\n***************************  exp", exp
    #print "fld.ty:",fld.name
    if(fty.is_Tensor(fld)):
        return "("+exp+")"
    else:
        return makeProbe(exp, "pos",cfenames)


##################################### print unary,binary,n-arity op #####################################
################## place operator symbol in args ##################
# print operator between arguments
# center is commas between args
def prntOpr(opr, center):
    if(opr.placement == place_split):
        (symb_lhs, symb_rhs)= opr.symb
        return symb_lhs+center+ symb_rhs
    elif(opr.placement == place_left):
        return (opr.symb)+center
    elif(opr.placement == place_right):
        return center+(opr.symb)
    else:
        raise Exception ("unsupported placement"+opr.placement)
# separated here by arity
def prntUnary(opr, e):
    center = "("+e+")"
    return prntOpr(opr, center)
def prntBinary(opr, e1, e2):
    center = "(("+e1+"),("+e2+"))"
    if(opr.placement == place_middle):
        return "("+e1+")"+(opr.symb)+"("+e2+")"
    elif(opr.placement == place_split):
        (symb_lhs, symb_rhs)= opr.symb
        return symb_lhs+e1+",("+e2+ symb_rhs+")"
    else:
        return prntOpr(opr, center)
def prntThird(opr, e1, e2, e3):
    center = "(("+e1+"),("+e2+"),("+e3+"))"
    return prntOpr(opr, center)
#op1: operator, i:argument index
def rtn_rhs(f, op1, typ_inner, e, i):
    arity = op1.arity
    # names of lhs variables
    # next arguments are [e, fi, fi+1]
    f1 = fieldName(i)
    f2 = fieldName(i+1)
    #print "op1:", op1.name, "typ-inner", typ_inner.name
    #print "e: ", e, " i:", i
    if (arity==1):
        #if(op1.placement==place_right):
        #    write_shape("\t", f, typ_inner, f1, e)
        #    return (prntUnary(op1, f1), i+1)
        #else:
        return (prntUnary(op1, e),i)
    elif(arity==2):
        return (prntBinary(op1, e, f1),i+1)
    elif(arity==3):
        return (prntThird(op1, e, f1, f2),i+2)
    else:
        raise Exception("unsupported arity")

def get_exp2(opr, lhs, i):
    exp1 = fieldName(i)
    exp2 = fieldName(i+1)
    arity = opr.arity
    if(arity==1):
        return (prntUnary(opr, lhs),i)
    elif(arity==2):
        return (prntBinary(opr, lhs, exp1),i+1)
    elif(arity==3):
        return (prntThird(opr, lhs, exp1, exp2),i+2)


################## apply 1 layer of operator ##################
#write operation between fields
#get output var name-lhs
def gotop1(f, app, pre, lhs):
    op1 = app.opr
    oty = app.oty
    f0 = fieldName(0)
    (rhs, _) = rtn_rhs(f, op1, oty, f0, 1)
    write_shape(pre, f, oty, lhs, rhs)
    return
################## apply 2 layers of operators ##################
#write operation between fields
def gotop2(f, app_outer, pre, lhs):

    opr_outer=app_outer.opr
    app_inner=apply.get_unary(app_outer)
    opr_inner=app_inner.opr
    # type of output of each app
    typ_outer = app_outer.oty
    typ_inner = app_inner.oty

    # names of lhs variables
    f0 = fieldName(0)
    #first operator
    (e1, n) = rtn_rhs(f, opr_inner, typ_inner, f0, 1)
    # second operator
    (line1,_) = rtn_rhs(f, opr_outer, typ_outer, e1, n)
    # writing to a line
    write_shape(pre, f, typ_outer, lhs, line1)
    return
################## apply 3 layers of operators ##################
#write operation between fields
def gotop3(f, app_outer2, pre, lhs):
    opr_outer2 = app_outer2.opr
    app_outer1 = apply.get_unary(app_outer2)
    opr_outer1 = app_outer1.opr
    app_inner=apply.get_unary(app_outer1)
    opr_inner=app_inner.opr
    # type of output of each app
    typ_outer2 = app_outer2.oty
    typ_outer1 = app_outer1.oty
    typ_inner = app_inner.oty
    
    # names of lhs variables
    f0 = fieldName(0)
    (e1, n) = rtn_rhs(f, opr_inner, typ_inner, f0, 1)
    (e2, n) = rtn_rhs(f, opr_outer1, typ_inner, e1, n)
    (line1,_) = rtn_rhs(f, opr_outer2, typ_outer1, e2, n)
    # writing to a line
    write_shape(pre, f, typ_outer2, lhs, line1)
################## write operator lines ##################
# write operator lines
# calls above functions
def iter(f, app, lhs, name):
    if(app.isrootlhs):
        return gotop1(f, app, lhs, name)
    elif((app.lhs).isrootlhs):
        #print "twice embedded"
        return gotop2(f ,app, lhs, name)
    else:
        #print "third layers"
        return gotop3(f, app, lhs, name)
#write operator stmts in field line
def replaceOp(f, app):
    if (fty.is_Field(app.oty)):
        #field type
        iter(f, app, "", opfieldname1)
    else:
        return
#write operator stmts in output tensor line
def outLine(f, app):
    type  = app.oty
    if (fty.is_Field(type)):
        outLineF(f, type)
    else:
        return iter(f, app, "\toutput ", foo_out)

##################################### conditionals and limits #####################################
# limitation on operator
def limit(e, opr):
    eps = "0.01"
    if(opr.limit==limit_small):
        return "((("+e+")>"+eps+") || (("+e+")< -"+eps+"))"
    elif(opr.limit==limit_det):
        return "((det("+e+")>"+eps+") || (det("+e+")< -"+eps+"))"
    elif(opr.limit ==limit_trig):
        return "(((0.1*("+e+"))<= 1.0) && (( 0.1*("+e+"))>=  -1.0))"
    elif(opr.limit == limit_nonzero):
        return "((("+e+")> 0.0) || (("+e+")< 0.0))"
    else:
        raise Exception(opr.name,"unknown limit:",opr.limit)
################## if else statements  ##################
#wrape expression inside an if statement
def wrap(exp, stmt, oty):
    return "\n\tif("+exp+"){\n\t\t"+stmt+"\n\t}\n\t else{"+foo_out+ " = "+ outLineTF(oty, const_out)+";}"
def ifelse(cond, set, oty):
    return"if("+cond+")\n\t\t\t{"+set+"}"+ "\n\t\telse{"+foo_out+" = "+outLineTF(oty, const_out)+";}"
################## get args  ##################
def get_exp1(opr, i):
    arity = opr.arity
    if(arity==1):
        return fieldName(i)
    elif(arity==2):
        return fieldName(i+1)
    elif(arity==3):
        return fieldName(i+2)
def innerL(app, lhs, i):
    opr = app.opr
    oty = app.oty
    (z, _) = get_exp2(opr, lhs , i)
    return isProbe(cfenames,z, oty)
def innerF(app, i):
    exp0 = fieldName(i)
    return  innerL(app, exp0, i+1)
def get_args2(app, app_inner, i):

    opr_inner =app_inner.opr
    exp0 = fieldName(i)
    exp1 = fieldName(i+1)
    if(opr_inner.limit==limit_small):
        i = i+1 #looking at denominator
        oty =  app_inner.rhs.fldty
        z= fieldName(i)
        if(not(app.lhs.isrootlhs)):
            third = app.lhs.lhs
            opr = third.opr
            z = get_exp1(opr, i)
        return isProbe(cfenames,z, oty)
    else:
        if(app.lhs.isrootlhs):
            oty  = app_inner.oty
            return isProbe(cfenames,exp0, oty)
        else:
            third = app.lhs.lhs
            return innerF(third, i)
def get_args3(app):
 
    if(app.opr.limit==limit_small):# op_division.id):
        if((app.lhs).isrootlhs):
            #2 layers
            app_outer = app
            app_inner = apply.get_unary(app_outer)
            opr_inner = app_inner.opr
            z = get_exp1(opr_inner,1)
            oty = app_outer.rhs.fldty
            return isProbe("FIXME",z, oty)
        else:
            # one layer
            z = app.rhs.name
            oty = app.rhs.fldty
            return isProbe(cfenames,z, oty)
    else:
        if((app.lhs).isrootlhs):
            # layer 2
            app_outer = app
            app_inner = apply.get_unary(app_outer)
            return innerF(app_inner, 0)
        else:
            # layer 3
            app_outer2 = app
            app_outer1 = apply.get_unary(app_outer2)
            app_inner = apply.get_unary(app_outer1)
            opr_inner = app_inner.opr
            exp0 = fieldName(0)
            (lhs,n) = get_exp2(opr_inner, exp0, 1)
            return innerL(app_outer1, lhs, n)

################## conditional function  ##################
# get restraint on argument to operators
# i.e. sqrt(x), so x must be positive
def getCond(app, set):
    if(removeCond):
        return set
    oty = app.oty
    app_outer = app
    opr_outer=app_outer.opr
    app_inner =apply.get_unary(app_outer)
    opr_inner =app_inner.opr
    # checks limitations in operators
    if((opr_inner.limit== None) and (opr_outer.limit== None)):
        # there is no limit
        return set
    elif(not (opr_inner.limit== None)):
        # there is a limit on inner operator
        texp = get_args2(app, app_inner, 0)
        cond = limit(texp, opr_inner)
        return ifelse(cond, set, oty)
    elif(not (opr_outer.limit== None)):
        texp = get_args3(app)
        cond = limit(texp, opr_outer)
        return  ifelse(cond, set, oty)
    else:
        return  set
##ff: field that is being probed or tensor variable inside if statement
def check_conditional(f, ff, app):
    # probes field at variable position
    oty = app.oty
    set = "\t"+foo_out+" = "+isProbe(cfenames,ff,oty)+";\n"
    foo = ""
    if(app.isrootlhs or oty.dim==1):
        foo = set
    else: #twice embedded
        # there might be a conditional restraint
        foo= getCond(app, set)
    f.write(foo)
    return
##ff: field that is being probed or tensor variable inside if statement
def check_conditional(f, ff, app):
    # probes field at variable position
    oty = app.oty
    set =  "\t"+foo_out+" = "+isProbe(cfenames,ff,oty)+";\n"
    foo =  ""
    if(app.isrootlhs or oty.dim==1):
        foo = set
    else: #twice embedded
        # there might be a conditional restraint
        foo= getCond(app, set)
    f.write(foo)
    return
##################################### inside field test  #####################################
#probes field at variable position
def check_inside(f, probeG, app,cfenames):

    oty = app.oty
    set =  "\t"+foo_out+" = "+isProbe(cfenames,probeG,oty)+";"
    exps = apply.get_all_Fields(app)
    foo = ""
    pos = "pos"
    i0 = getInside(exps[0],"F0", pos)
    adjs = str(adj)
    outerif = "true"     # create outer if
    ################## comp term ##################
    #number of fields we probe for composition inside test
    def insideExpFld0(i):
        return getInside(exps[i], fieldName(i) , pos)
    def insideExpFld1(i, j):
        prbe = makeProbe(fieldName(j), pos,cfenames)
        return getInside(exps[i], fieldName(i), prbe+"*"+adjs)
    def insideExpFld2(i, j, k):
        prbeI = makeProbe(fieldName(k), pos,cfenames)
        prbeO = makeProbe(fieldName(j), "("+prbeI+")*" +adjs,cfenames)
        return getInside(exps[i], fieldName(i) , prbeO+"*"+adjs)
    # inside expression for field in composition
    def i0():
        return insideExpFld0(0)
    def i1():
        return insideExpFld0(1)
    def i2():
        return insideExpFld0(2)
    def i3():
        return insideExpFld0(3)
    def i0C2():
        return insideExpFld1(0, 2)
    def i1C2():
        return insideExpFld1(1, 2)
    def i2C3():
        return insideExpFld1(2, 3)
    def i0C12():
        return insideExpFld2(0, 1, 2)
    def termA():
        # B(pos)+A(B(po))
        i0C1 = insideExpFld1(0, 1)
        return i1()+i0C1+"true"
    def termB():
        # C(pos)+B(pos)+A(B(pos))
        return i2()+termA()
    def termC():
        # C(pos)+B(C(pos))+A(C(pos))
        return i2()+i1C2()+i0C2()+"true"
    def termD():
        # D(pos)+C(D(pos))
        return i3()+i2C3()
    def termE():
        # D(pos)+C(pos)+B(pos)+A(B(pos))
        return  i3()+termB()
    def termG():
        # C(pos) + B(C(pos))+ A(B(C(pos)))
        return i2()+i1C2()+i0C12()+"true"
    def termH():
        #C(pos)+ B(C(pos))+A(B(C(pos)))
        return i2()+i1C2()+i0C12()+"true"
    def termI():
        #C(pos)+ D(pos) + B(C(pos))+A(C(pos))
        return i2()+i3()+i1C2()+i0C2()+"true"
    def termJ():
        # D(pos)+C(D(pos))+ B(C(D(pos)))+ A(C(D(pos)))
        i1C23 = insideExpFld2(1, 2, 3)
        i0C23 = insideExpFld2(0, 2, 3)
        return termD()+i1C23+i0C23+"true"
    def termK():
        # D(pos)+A(D(pos))+ B(D(pos))+ C(D(pos))
        i1C3 = insideExpFld1(1, 3)
        i0C3 = insideExpFld1(0, 3)
        return i3()+i0C3+i1C3+i2C3()+"true"
    ################## checks app for composition operator ##################
    #either comp inspired probing or regular probing
    if(app.opr==op_comp):
        if( (not app.isrootlhs)  and (app.lhs.opr == op_comp)):
            if(not app.lhs.isrootlhs):
                #3 layers
                arity = app.lhs.lhs.opr.arity
                if(arity==2):
                    outerif = termJ()
                else:
                    outerif = termG()
            else:
                # 2 layers
                outerif = termH()
        else:
            if((not app.isrootlhs) and (not app.lhs.isrootlhs)):
                arityO = app.lhs.opr.arity
                arityI = app.lhs.lhs.opr.arity
                if((arityI==2) and (arityO==2)):
                    outerif = termK()
                elif((arityO==2) or (arityI==2)):
                    outerif = termC()
                else:
                    outerif = termA()
            elif(not app.isrootlhs) :
                arity = app.lhs.opr.arity
                if(arity==1):
                    outerif = termA()
                elif(arity==2):
                    outerif = termC()
            else:
                #fix me
                outerif ="true"
    elif ((not app.isrootlhs) and  (app.lhs.opr==op_comp)):
        arityO = app.opr.arity
        if(not app.lhs.isrootlhs):
            arityI = app.lhs.lhs.opr.arity
            if((arityI==2) and (arityO==2)):
                outerif = termI()
            elif((arityO==2)):
                outerif = termB()
            elif((arityI==2)):
                outerif = termC()
            else:
                outerif = termA()
        else:
            if(arityO==1):
                outerif = termA()
            elif(arityO==2):
                outerif= termB()
    elif ((not app.isrootlhs) and (not app.lhs.isrootlhs) and (not app.lhs.lhs.isrootlhs) and app.lhs.lhs.opr==op_comp):
        arityO = app.opr.arity
        arityI = app.lhs.opr.arity
        if((arityO==2) and (arityI==2)):
            outerif= termE()
        elif((arityO==2) or (arityI==2)):
            outerif= termB()
        else:
            outerif = termA()
    else:
        #regular probing of expressions
        j= ""
        for i in range(len(exps)):
            j = j+ getInside(exps[i],"F"+str(i), pos)
        outerif = j+"true"
        # inside if
        # check none inside test
    if(app.isrootlhs):

        foo = wrap(outerif,set, oty)
        f.write(foo)
    else:
        t = ""
        if(removeCond):
            t = "out ="+makeProbe(probeG, "pos",cfenames)+";"
        else:
            t = getCond(app,set)
        foo = wrap(outerif, t, oty)
        write(f,foo)


##################################### probe field at positions #####################################
# set positions variables
# index field at position
def create_position(f,  dim):
   
    i=0
    foo="\t\t"
    if(dim==1):
        foo+="real  "+foo_pos+"=0;\n"
    elif(dim==2):
        foo+="tensor [2] "+foo_pos+"=[0,0];\n"
    elif(dim==3):
        foo+="tensor [3] "+foo_pos+"=[0,0,0];\n"
    f.write(foo)


def base_index_field_at_positions(f, pos, dim):

    i=0
    foo="\t\t"
    if(dim==1):
        foo+="real  "+foo_pos+"=0;\n"
    elif(dim==2):
        foo+="tensor [2] "+foo_pos+"=[0,0];\n"
    elif(dim==3):
        foo+="tensor [3] "+foo_pos+"=[0,0,0];\n"
    # does first position
    p=str(pos[0])
    foo += "\t\tif(i=="+str(i)+"){\n"
    # just sets poitions
    foo += "\t\t\t"+foo_pos+" = "+"("+p+");\n"
    # probes field at position
    foo += "\t\t}\n"
    i=i+1
    for p1 in pos:
        p=str(p1)
        foo += "\t\telse if(i=="+str(i)+"){\n"
        # just sets poitions
        foo += "\t\t\t"+foo_pos+" = "+"("+p+");\n"
        # probes field at current position
        foo += "\t\t}\n"
        i=i+1
    f.write(foo)

def index_field_at_positions(f, pos, app):
    oty = app.oty
    return base_index_field_at_positions(f, pos, oty)
