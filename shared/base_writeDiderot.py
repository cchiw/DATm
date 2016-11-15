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

def fieldName(i):
    return "F"+str(i)


# type of field
def fieldShape(f, fldty):
    #print "fldty: ",fldty
    foo = fty.toDiderot(fldty)
    f.write(foo.encode('utf8'))

#field input line
#f: file to write to
#k:continuity
#itypes: types for input field
#inputlist: name for input data
def inShape(f,appC):
    #app = apply.get_root_app(appC)
    i=0
    #exps =  apply.get_exps(app)
    exps = apply.get_all_Fields(appC)
    for exp in exps:
        #print "current fld",field.toStr(exp)
        dim = field.get_dim(exp)
        #print ("exp:", field.toStr(exp))
        fieldShape(f, exp.fldty)
        if (field.get_isField(exp)):
            krnstr = exp.krn.str
            foo= fieldName(i)+" = "+krnstr+u'⊛'+"  image(\""+exp.inputfile+".nrrd\");\n"
            f.write(foo.encode('utf8'))
        else: #tensor type
            foo= fieldName(i)+" = "+str(field.get_data(exp))+";\n"
            f.write(foo.encode('utf8'))
        i+=1


#instaniate output tensor
def outLineTF(type,s):
    otype = fty.get_tensorType(type)
    v2 =  " ["+s+","+s+"]"
    v3 = " ["+s+","+s+","+s+"]"
    v4 = " ["+s+","+s+","+s+","+s+"]"
    def mkTen2(e):
        return "["+e+","+e+"]"
    def mkTen3(e):
        return "["+e+","+e+","+e+"]"
    def mkTen4(e):
        return "["+e+","+e+","+e+","+e+"]"
    
    m22 = mkTen2(v2)
    m23 = mkTen2(v3)
    m24 = mkTen2(v4)
    m32 = mkTen3(v2)
    m33 = mkTen3(v3)
    m34 = mkTen3(v4)
    m42 = mkTen4(v2)
    m43 = mkTen4(v3)
    m44 = mkTen4(v4)
    t222 = mkTen2(m22)
    t223 = mkTen2(m23)
    t224 = mkTen2(m24)
    t232 = mkTen2(m32)
    t233 = mkTen2(m33)
    t234 = mkTen2(m34)
    t242 = mkTen2(m42)
    t243 = mkTen2(m43)
    t244 = mkTen2(m44)
    t322 = mkTen3(m22)
    t323 = mkTen3(m23)
    t324 = mkTen3(m24)
    t332 = mkTen3(m32)
    t333 = mkTen3(m33)
    t334 = mkTen3(m34)
    t342 = mkTen3(m42)
    t343 = mkTen3(m43)
    t344 = mkTen3(m44)
    t422 = mkTen4(m22)
    t423 = mkTen4(m23)
    t424 = mkTen4(m24)
    t432 = mkTen4(m32)
    t433 = mkTen4(m33)
    t434 = mkTen4(m34)
    t442 = mkTen4(m42)
    t443 = mkTen4(m43)
    t444 = mkTen4(m44)
    if (ty_scalarT==otype):
        return s
    elif(ty_vec2T==otype):
        return v2
    elif(ty_vec3T==otype):
        return v3
    elif(ty_vec4T==otype):
        return v4
    elif(ty_mat2x2T==otype):
        return  m22
    elif(ty_mat2x3T==otype):
        return m23
    elif(ty_mat2x4T==otype):
        return m24
    elif(ty_mat3x2T==otype):
        return m32
    elif(ty_mat3x3T==otype):
        return m33
    elif(ty_mat3x4T==otype):
        return m34
    elif(ty_mat4x2T==otype):
        return m42
    elif(ty_mat4x3T==otype):
        return m43
    elif(ty_mat4x4T==otype):
        return m44
    elif(ty_ten2x2x2T==otype):
        return t222
    elif(ty_ten2x2x3T==otype):
        return t223
    elif(ty_ten2x2x4T==otype):
        return t224
    elif(ty_ten2x3x2T==otype):
        return t232
    elif(ty_ten2x3x3T==otype):
        return t233
    elif(ty_ten2x3x4T==otype):
        return t234
    elif(ty_ten2x4x2T==otype):
        return t242
    elif(ty_ten2x4x3T==otype):
        return t243
    elif(ty_ten2x4x4T==otype):
        return t244

    elif(ty_ten3x2x2T==otype):
        return t322
    elif(ty_ten3x2x3T==otype):
            return t323
    elif(ty_ten3x2x4T==otype):
        return t324
    elif(ty_ten3x3x2T==otype):
        return t332
    elif(ty_ten3x3x3T==otype):
        return t333
    elif(ty_ten3x3x4T==otype):
        return t334
    elif(ty_ten3x4x2T==otype):
        return t342
    elif(ty_ten3x4x3T==otype):
        return t343
    elif(ty_ten3x4x4T==otype):
        return t344
    
    elif(ty_ten4x2x2T==otype):
        return t422
    elif(ty_ten4x2x3T==otype):
        return t423
    elif(ty_ten4x2x4T==otype):
        return t424
    elif(ty_ten4x3x2T==otype):
        return t432
    elif(ty_ten4x3x3T==otype):
        return t433
    elif(ty_ten4x3x4T==otype):
        return t434
    elif(ty_ten4x4x2T==otype):
        return t442
    elif(ty_ten4x4x3T==otype):
        return t443
    elif(ty_ten4x4x4T==otype):
        return t444

    else:
        raise Exception("unsupported input type",otype.name)


#instaniate output tensor
def outLineF(f, type):
    otype = fty.get_tensorType(type)
    foo="\toutput "
    #print " otype", otype
    #print " otype", otype.name,otype.id," ty_scalarT",ty_scalarT.name,"id",ty_scalarT.id
    foo+="tensor "+str(otype.shape)+" "+foo_out+" = "+outLineTF(type,"0.0")+";\n\t"
    f.write(foo.encode('utf8'))




# print unary operator
def prntUnary(opr, e):
    if(opr.placement == place_split):
        (symb_lhs, symb_rhs)= opr.symb
        k = symb_lhs+"("+e+")"+ symb_rhs
        return k
    elif(opr.placement == place_left):
        k = (opr.symb)+"("+e+")"
        return k
    elif(opr.placement == place_right):
        k = "("+e+")"+(opr.symb)
        return k
    else:
        raise Exception ("unsupported placement")

def prntBinary(opr, e1, e2):
    #print "prntBinary",opr.name
    #print "symb,",opr.symb
    if(opr.placement == place_left):
        return  (opr.symb)+"(("+e1+"),("+e2+"))"
    elif(opr.placement == place_middle):
        return "("+e1+")"+(opr.symb)+"("+e2+")"
    elif(opr.placement == place_right):
        return  "(("+e1+"),("+e2+"))"+(opr.symb)
    else:
        raise Exception ("unhandled placement")

# writing to a line
def write_shape(pre, f, typ, lhs, rhs):
    f.write(pre.encode('utf8'))
    # type of resulting field
    fieldShape(f, typ)
    # set expression equal to output field
    foo = lhs+" = "+rhs+";\n"
    # Write to file
    f.write(foo.encode('utf8'))


#write operation between fields
#get output var name-lhs
def gotop1(f,app, pre, lhs):
    op1 = app.opr
    arity = op1.arity
    oty = app.oty
    # names of lhs variables
    f0 = fieldName(0)
    f1 = fieldName(1)
    def rtn_rhs():
        if (arity==1):
            return prntUnary(op1, f0)
        elif(arity==2):
            return prntBinary(op1, f0, f1)
        else:
            raise Exception("unsupported arity")
    rhs = rtn_rhs()
    write_shape(pre, f, oty, lhs, rhs)
    return


#write operation between fields
def gotop2(f, app_outer, pre, lhs):
    opr_outer=app_outer.opr
    app_inner=apply.get_unary(app_outer)
    opr_inner=app_inner.opr
    # arity of each app
    arity_inner= opr_inner.arity
    arity_outer= opr_outer.arity
    # type of output of each app
    typ_outer = app_outer.oty
    typ_inner = app_inner.oty
    
    # names of lhs variables
    f0 = fieldName(0)
    f1 = fieldName(1)
    f2 = fieldName(2)
    #s_inner = apply.toStr(app_inner,0)
    #s_outer = apply.toStr(app_outer,0)

    # writing to a line
    def write_inner(e):
        write_shape("\t", f, typ_inner, f2, e)
    def write_lastline(e):
        write_shape(pre, f, typ_outer, lhs, e)

    if (arity_inner==1):
        # inner placement
        e1 = prntUnary(opr_inner, f0)
        if(arity_outer==1):
            if(opr_outer.placement==place_right):
                # multiple lines
                write_inner(e1)
                line2 = f2+(opr_outer.symb)
                write_lastline(line2)
                return
            else:
                #single line
                line1= prntUnary(opr_outer, e1)
                write_lastline(line1)
                return
        elif(arity_outer==2):
            #assumes second arg is a field
            line1 = prntBinary(opr_outer, e1, f1)
            write_lastline(line1)
            return
        else:
            raise Exception("unsupported arity")
    elif(arity_inner==2):
        e1 = prntBinary(opr_inner, f0, f1)
        if(arity_outer==1):
            write_inner(e1)
            line2 = prntUnary(opr_outer, f2)
            write_lastline(line2)
            return
        elif(arity_outer==2):
            line1 = prntBinary(opr_outer, e1, f2)
            write_lastline(line1)
            return
        else:
            raise Exception("unsupported arity")
    else:
        raise Exception("unsupported arity")


#write operation between fields

def gotop3(f, app_outer2, pre, lhs):
    opr_outer2 = app_outer2.opr
    app_outer1 = apply.get_unary(app_outer2)
    opr_outer1 = app_outer1.opr
    app_inner=apply.get_unary(app_outer1)
    opr_inner=app_inner.opr
    # arity of each app
    arity_inner= opr_inner.arity
    arity_outer1= opr_outer1.arity
    arity_outer2= opr_outer2.arity
    # type of output of each app
    typ_outer2 = app_outer2.oty
    typ_outer1 = app_outer1.oty
    typ_inner = app_inner.oty
    
    # names of lhs variables
    f0 = fieldName(0)
    f1 = fieldName(1)
    f2 = fieldName(2)
    f3 = fieldName(3)
    f8 = fieldName(8)
    f9 = fieldName(9)
    #s_inner = apply.toStr(app_inner,0)
    #s_outer = apply.toStr(app_outer,0)
    
    # writing to a line
    def write_inner(fn, oty, e):
        write_shape("\t", f, oty, fn, e)
    def write_lastline(e):
        write_shape(pre, f, typ_outer2, lhs, e)

    if (arity_inner==1):
        # inner placement
        print "write diderot: inner =1"
        e1 = prntUnary(opr_inner, f0)
        if(arity_outer1==1):
            print "write diderot: outer1=1"
            if(opr_outer1.placement==place_right):
                # multiple lines
                write_inner(f8, typ_inner, e1)
                e2 = f8+(opr_outer1.symb)
                if(arity_outer2==1):
                    print "write diderot: outer2 =1"
                    if(opr_outer2.placement==place_right):
                        write_inner(f9, typ_outer1, e2)
                        line3= prntUnary(opr_outer2, f9)
                        write_lastline(line3)
                        return
                
                    else:
                        line2= prntUnary(opr_outer2, e2)
                        write_lastline(line2)
                        return
                elif(arity_outer2==2):
                    print "write diderot: outer2=2"
                    line2 = prntBinary(opr_outer2, e2, f1)
                    write_lastline(line2)
                    return
            else:
                e2 = prntUnary(opr_outer1, e1)
                if(arity_outer2==1):
                    if(opr_outer2.placement==place_right):
                        write_inner(f8, typ_outer1, e2)
                        line1= prntUnary(opr_outer2, f8)
                        write_lastline(line1)
                        return
                    else:
                        #single line
                        line1= prntUnary(opr_outer2, e2)
                        write_lastline(line1)
                        return
                elif(arity_outer2==2):
                    line2 = prntBinary(opr_outer2, e2, f1)
                    write_lastline(line2)
                    return
                return
        elif(arity_outer1==2):
            print "write diderot: outer1=2"
            #assumes second arg is a field
            e2 = prntBinary(opr_outer1, e1, f1)
            if(arity_outer2==1):
                if(opr_outer2.placement==place_right):
                    write_inner(f8, typ_outer1, e2)
                    line1 = prntUnary(opr_outer2, f8)
                    write_lastline(line1)
                    return
                else:
                    line1= prntUnary(opr_outer2, e2)
                    write_lastline(line1)
                    return
            elif(arity_outer2==2):
                 line1 = prntBinary(opr_outer2, e2, f2)
                 write_lastline(line1)
                 return
        else:
            raise Exception("unsupported arity")
    elif(arity_inner==2):
        e1 = prntBinary(opr_inner, f0, f1)
        if(arity_outer1==1):
            if(opr_outer1.placement==place_right):
                write_inner(f8, typ_inner, e1)
                e2 = prntUnary(opr_outer1, f8)
                if(arity_outer2==1):
                    if(opr_outer2.placement==place_right):
                        write_inner(f9, typ_outer2, e2)
                        e3 = prntUnary(opr_outer2, f9)
                        write_lastline(e3)
                    else:
                        e3 = prntUnary(opr_outer2, e2)
                        write_lastline(e3)
                elif(arity_outer2==2):
                    line1 = prntBinary(opr_outer2, e2, f2)
                    write_lastline(line1)
            else:
                e2 = prntUnary(opr_outer1, e1)
                if(arity_outer2 == 1):
                    if(opr_outer2.placement==place_right):
                        write_inner(f8, typ_outer1, e2)
                        e3 = prntUnary(opr_outer2, f8)
                        write_lastline(e3)
                    else:
                        line1=  prntUnary(opr_outer2, e2)
                        write_lastline(line1)
                elif(arity_outer2 == 2):
                    line1 = prntBinary(opr_outer2, e2, f2)
                    write_lastline(line1)
            return
        elif(arity_outer1==2):
            e2 = prntBinary(opr_outer1, e1, f2)
            if(arity_outer2==1):
                if(opr_outer2.placement==place_right):
                    write_inner(f8, typ_outer1, e2)
                    line1 = prntUnary(opr_outer2, f8)
                    write_lastline(line1)
                else:
                    line1 = prntUnary(opr_outer2, e2)
                    write_lastline(line1)
            elif(arity_outer2==2):
                line1 = prntBinary(opr_outer2, e2, f3)
                write_lastline(line1)
            return
        else:
            raise Exception("unsupported arity")
    else:
        raise Exception("unsupported arity")


                          

def replaceOp(f,app):
    if (fty.is_Field(app.oty)):
        #field type
        # one or two operators?
        if(app.isrootlhs):
            #print "going to 1"
            return gotop1(f,app, "",opfieldname1)
        else: #twice embedded
            #print "goint to 2"
            if((app.lhs).isrootlhs):
                return gotop2(f,app, "", opfieldname1)
            else:
                # third layers
                return gotop3(f, app, "", opfieldname1)
    else:
        return


# probes field at variable position
def isProbe(exp, fld):
    if(fty.is_Field(fld)):
        return "("+exp+")(pos)"
    else:
        return "("+exp+")"

# get restraint on argument to operators
# i.e. sqrt(x), so x must be positive
def getCond(app, set):
    oty = app.oty
    app_outer = app
    opr_outer=app_outer.opr
    app_inner =apply.get_unary(app_outer)
    opr_inner =app_inner.opr
    exp0 = "F0"
    exp1 = "F1"
    exp2 = "F2"
    foo = ""
    eps = "0.01"
    def limit(e, opr):
        if(opr.limit==limit_small):
            return "((("+e+")>"+eps+") || (("+e+")< -"+eps+"))"
        elif(opr.limit==limit_det):
            return "((det("+e+")>"+eps+") || (det("+e+")< -"+eps+"))"
        elif(opr.limit ==limit_trig):
            return "(((0.1("+e+"))<= 1.0) && (( 0.1*("+e+"))>=  -1.0))"
        elif(opr.limit == limit_nonzero):
            return "((("+e+")> 0.0) || (("+e+")< 0.0))"
        else:
            raise Exception(opr.name,"unknown limit:",opr.limit)
    def ifelse(cond):
        k= "\n\tif("+cond+"){\n\t"+set+"\t}\n\t"
        k+="\n\telse{\n\t\t"+foo_out+" = "+outLineTF(oty, const_out)+";\n\t}"
        return k
    if((opr_inner.limit== None) and (opr_outer.limit== None)):
        # there is no limit

        foo += set
    elif(not (opr_inner.limit== None)):

        # there is a limit on inner operator
        def get_args():
            if(opr_inner.limit==limit_small):
                #if(opr_inner.id==op_division.id):
                return isProbe(exp1,app_inner.rhs.fldty)
            else:
                return isProbe(exp0,app_inner.oty)
        texp = get_args()
        cond = limit(texp, opr_inner)
        foo+= ifelse(cond)
    elif(not (opr_outer.limit== None)):

        # check outer operator
        def get_exp1(opr):
            if(opr.arity==2):
                return exp2
            else:
                return exp1
        def get_exp2(opr, lhs):
            if(opr.arity==2):
                return prntBinary(opr, lhs, exp1)
            else:
                return prntUnary(opr, lhs)
        def get_args(app):
            oty = app.oty
            app_outer = app
            opr_outer=app_outer.opr
            app_inner =apply.get_unary(app_outer)
            opr_inner =app_inner.opr
            if(opr_outer.limit==limit_small):# op_division.id):
               
                if((app.lhs).isrootlhs):
                    #print "2 layers"
                    pexp = get_exp1(opr_inner)
                    return isProbe(pexp, app_outer.rhs.fldty)
                else:
                    pexp = app.rhs.name
                    return isProbe(pexp, app.rhs.fldty)
        
            else:

                if((app.lhs).isrootlhs):
                    #print "2 layers"
                    # layer 2
                    pexp = get_exp2(opr_inner, exp0)
                    return isProbe(pexp, app_inner.oty)
                else:
                    #print "3 layers"
                    # layer 3
                    app_outer2 = app
                    app_outer1 = apply.get_unary(app_outer2)
                    app_inner = apply.get_unary(app_outer1)
                    opr_outer1 = app_outer1.opr
                    opr_inner = app_inner.opr
                    
                    lhs = get_exp2(opr_inner, exp0)
                    pexp = get_exp2(opr_outer1, lhs)
                    return isProbe(pexp, app_outer1.oty)

        texp = get_args(app)
        cond = limit(texp, opr_outer)
        foo+= ifelse(cond)
    else:

        foo = set
    return foo

##ff: field that is being probed or tensor variable inside if statement
def check_conditional(f, ff, app):
    # probes field at variable position
    oty = app.oty
    set =  "\t"+foo_out+" = "+isProbe(ff,oty)+";\n"
    foo =  ""
    if(app.isrootlhs or oty.dim==1):
        foo = set
    else: #twice embedded
        # there might be a conditional restraint
        foo= getCond(app, set)
    f.write(foo.encode('utf8'))
    return

def check_inside(f, ff, app):
    # probes field at variable position
    oty = app.oty
    set =  "\t"+foo_out+" = "+isProbe(ff,oty)+";\n"
    
    exps = apply.get_all_Fields(app)
    i=0
    j=[]
    foo= ""
    for exp in exps:
        if (field.get_isField(exp)):
            s="inside(pos, F"+str(i)+")"
            j.append(s)
        i+=1
    if(len(j)==1):
        foo =  ""
        if(app.isrootlhs):
            foo += set
        else: #twice embedded
            # there might be a conditional restraint
            foo += getCond(app, set)
            foo+="\t}\n\telse {"+foo_out+ " = "+ outLineTF(oty, const_out)+";}"
        f.write(foo.encode('utf8'))
        return

    elif(len(j)==2):
        foo =  "\tif("+j[0]+" && "+j[1]+"){\n\t"
    elif(len(j)==3):
        foo =  "\tif("+j[0]+" && "+j[1]+" && "+j[2]+"){\n\t"
    if(app.isrootlhs):
        foo += set
    else: #twice embedded
        # there might be a conditional restraint
        foo += getCond(app, set)
    foo+="\t}\n\telse {"+foo_out+ " = "+ outLineTF(oty, const_out)+";}"
    f.write(foo.encode('utf8'))
    return




# set positions variables
# index field at position
def index_field_at_positions(f, pos, app):
    oty = app.oty
    i=0
    foo="\t\t"
    dim=oty.dim
    if(dim==1):
        foo+="real  "+foo_pos+"=0;\n"
    elif(dim==2):
        foo+="tensor [2] "+foo_pos+"=[0,0];\n"
    elif(dim==3):
        foo+="tensor [3] "+foo_pos+"=[0,0,0];\n"
    # does first position
    #pos.insert(0,pos[0])
    p=str(pos[0])
    foo += "\t\tif(i=="+str(i)+"){\n"
    # just sets poitions
    foo += "\t\t\t"+foo_pos+" = "+"("+p+");\n"
    # probes field at position
    # foo += "\t\t\t"+foo_out+" = "+opfieldname1+"("+p+");\n"
    foo += "\t\t}\n"
    i=i+1
    for p1 in pos:
        p=str(p1)
        foo += "\t\telse if(i=="+str(i)+"){\n"
        # just sets poitions
        foo += "\t\t\t"+foo_pos+" = "+"("+p+");\n"
        # probes field at current position
        #foo += "\t\t\t"+foo_out+" = "+opfieldname1+"("+p+");\n"
        foo += "\t\t}\n"
        i=i+1
    f.write(foo.encode('utf8'))



def outLine(f, app):
    type  = app.oty
    #print "\n outline-","type: ",type.name," app: ",app.name
    if (fty.is_Field(type)):
        #print "isfld-layer 1"
        outLineF(f, type)
    else:
        if(app.isrootlhs):
            return gotop1(f,app, "\toutput ", foo_out)
        elif((app.lhs).isrootlhs):
            #print "twice embedded"
            return gotop2(f,app, "\toutput ", foo_out)
        else:
            #print "third layers"
            return gotop3(f, app, "\toutput ", foo_out)

