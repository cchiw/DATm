import sys
import re
import os
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from obj_typechecker import *
class apply:
    def __init__(self, name, opr, lhs, rhs, third, oty, isrootlhs, isrootrhs):
        self.name=name
        self.opr=opr
        self.lhs=lhs
        self.rhs=rhs
        self.third = third
        self.oty=oty
        self.isrootlhs=isrootlhs
        self.isrootrhs=isrootrhs
    def oprToStr(self):
        out=self.opr.name
        def g(t):
            if(t):
                return "x"
            else:
                op1 = self.lhs.opr
                return "_"+operator.toStr(op1,"x")
        out+=g(self.isrootlhs)+g(self.isrootrhs)
        return out
    def get_all_FieldTys(self):
        flds = ""
        lhs = self.lhs
        rhs = self.rhs
        if (lhs!=None):
            if (self.isrootlhs):
                flds+=lhs.fldty.name
            else :
                flds += apply.get_all_FieldTys(lhs)
        if (rhs!=None):
            if (self.isrootrhs):
                flds+= ","+rhs.fldty.name
            else :
                flds += apply.get_all_FieldTys(rhs)
        return flds
    def toStr(self, layer):
        if (self==None):
            return "None"
        s = str(layer)+"\t"+self.opr.name
        lhs = self.lhs
        rhs= self.rhs
        def l(n):
            if(n==0):
                return ""
            else:
                return "\t"+l(n-1)
            
        if(self.isrootlhs):
            if(lhs!=None):
                s+="\n"+str( layer)+"\tlhs(arg):"+ field.toStr(lhs)
        else:
            #s+= "\n"+l(layer)+str( layer)+"lhs(app)"
            if (lhs!=None):
                s+=" lhsapp: "+apply.toStr(lhs, layer-1)
            else:
                s+="None"
        if (self.isrootrhs):
            if(rhs!=None):
                s+="\n"+str( layer)+"\trhs(arg):"+field.toStr(rhs)
        else:
            #s+= "\n"+l(layer)+str( layer)+"rhs(app)"
            if(rhs!=None):
                s+=" rhsapp: "+apply.toStr(rhs, layer-1)
            else:
                s+="None"
        return s
    def checkDim(self):
        if (self.isroot):
            d1=self.lhs.fldty.ty.dim
            d2=self.rhs.fldty.ty.dim
            if (d1==d2):
                return d1
            else :
                raise "dimension is not the same"
        else :
            raise "not a root app"
    def get_arity(self):
        return self.opr.arity
    def getArgs(self):
        # return three arguments exactly
        # None for null argument 
        arity = self.opr.arity
        if(arity==1):
            return [self.lhs, None, None]
        elif(arity==2):
            return [self.lhs, self.rhs, None]
        elif(arity==3):
            return [self.lhs, self.rhs, self.third]
    
    def get_unary(self):
        return self.lhs
    def get_binary(self):
        f=self.lhs
        g=self.rhs
        return (f,g)
    def get_types(self):
        #if (self.isroot):
        rtn=[]
        if(self.lhs!=None):
            rtn.append(self.lhs.fldty)
        if(self.rhs!=None):
            rtn.append(self.rhs.fldty)
        return rtn
            #else :
            #raise "not a root app"
    # single list
    def get_exps(self):
        rtn=[]
        if(self.lhs!=None):
            rtn.append(self.lhs)
        if(self.rhs!=None):
            rtn.append(self.rhs)
        return rtn

    def get_root_types(self):
        rtn=[]
        if (self.isroot):
            for i in [self.lhs, self.rhs]:
                rtn.append(i.fldty)
            return rtn
        else :
            for i in [self.lhs, self.rhs]:
                rtn=rtn+(apply.get_root_types(i))
            return rtn
    def get_root_app(self):
        if (self.isrootlhs):
            return self
        else :
            if(self.rhs== None):
                return (apply.get_root_app(self.lhs))
            else:
                raise "more expressions in root"
    def get_all_Fields(self):
        flds = []
        lhs = self.lhs
        rhs = self.rhs
        if (lhs!=None):
            if (self.isrootlhs):
                flds.append(lhs)
            else :
                flds = flds + apply.get_all_Fields(lhs)
        if (rhs!=None):
            if (self.isrootrhs):
                flds.append(rhs)
            else :
                flds = flds + apply.get_all_Fields(rhs)
        if(self.third!=None):
            flds.append(self.third)
        return flds

    def get_oty(self):
        return self.oty


#------------------------------ helpers -----------------------------------------------------
#field dimension is the same as vector length
def checkNd(ityp1):
    if(fty.is_Vector(ityp1)):
        n1 = fty.get_vecLength(ityp1)
        dim1 = fty.get_dim(ityp1)
        return (n1==dim1)
    else:
        return (false,"needs vector")
def isDifferentiable(ityp):
    return (ityp.k>0)
##################################################################################################
# create apply, operator and field objects
# from an example opr number, type number, and input file
#Apply to two field expressions
def mkApply_fld(name, opr, ishape, inputfile, otype1, i_coeff_style, i_ucoeff, g_krn,t_template):
    ##print "t_template:",t_template
    # arity
    arity = opr.arity
    def set_App(lhs, rhs):
        return apply(name, opr, lhs, rhs, None, otype1, true, true)
    def set_fld(id):
        c_ity = ishape[id]
        c_dim = fty.get_dim(c_ity)
        # get kernel
        c_krn = transform_krn(g_krn,  id)
        c_continuity = c_krn.continuity
        ##print "t_template:",t_template
        return mk_Field(id, c_ity, c_continuity, inputfile, c_dim, i_coeff_style, i_ucoeff, c_krn,t_template)
    # first argument
    index1 = 0
    if (arity==1): # unary operator
        (F1, finfo1, coeff1) = set_fld(index1)
        z = set_App(F1, None)
        return (z, [coeff1])
    elif (arity==2): # binary operator
        (F1, finfo1, coeff1) = set_fld(index1)
        index2 = 1 # second argument
        (F2, finfo2, coeff2) = set_fld(index2)
        z = set_App(F1, F2)
        return (z, [coeff1, coeff2])
    elif (arity==3): # n- ary operator
        (F1, finfo1, coeff1) = set_fld(index1)
        index2 = 1 # second argument
        (F2, finfo2, coeff2) = set_fld(index2)
        index3 = 2 # third argument
        (F3, finfo3, coeff3) = set_fld(index3)
        z = apply(name, opr, F1, F2, F3, otype1, true, true)
        return (z, [coeff1, coeff2, coeff3])
    else:
        raise Exception ("arity is not supported: "+str(arity))
# otype1 = tshape1
def mkApply_twice(opr_inner, opr_outer, ishape, inputfile, otype1, tshape2, coeff_style, ucoeff, g_krn,t_template):
    name = opr_outer.name+"("+opr_inner.name+")"
    outer_arity = opr_outer.arity
    inner_arity = opr_inner.arity
    ##print "otype1:", otype1.name
    ##print "tshape2:", tshape2.name
    def set_innerApp(shape):
        return mkApply_fld(name, opr_inner, shape, inputfile, otype1, coeff_style, ucoeff, g_krn,t_template)
    def set_outerApp(lhs, rhs):
        return apply(name, opr_outer,lhs, rhs, None, tshape2, false, true)
    def set_outerApp3(lhs, rhs, third):
        return apply(name, opr_outer,lhs, rhs, third, tshape2, false, true)
    def set_field(id):
        # get kernel
        c_krn = transform_krn(g_krn, id)
        c_k =  c_krn.continuity
        c_fty = ishape[id]
        c_dim = fty.get_dim( c_fty)
        return mk_Field(id, c_fty, c_k, inputfile, c_dim, coeff_style, ucoeff, c_krn,t_template)
    if (outer_arity==1):
        ##print "outer arity=1"
        (z1, coeffs) =  set_innerApp(ishape)
        z2 = set_outerApp(z1, None)#[otype1]
        return (z2, coeffs)
    elif (outer_arity==2 and inner_arity==1): # one is a unary operator
        # apply inner operator to first arg
        ishape1 = [ishape[0]]
        (z1, coeffs) =  set_innerApp(ishape1)
        ##print "create another argument (tensor/field)"
        id2 = 1
        (F2, finfo2, coeff2) = set_field(id2)
        # apply outer operator to otype and second arg
        ishape3 =  [otype1, ishape[1]]
        z2 = set_outerApp(z1, F2)#, ishape3
        coeffs = coeffs+[coeff2]
        return (z2, coeffs)
    elif (outer_arity==2 and inner_arity==2): # binary operators
        # apply inner operator to first arg
        (z1, coeff1) = set_innerApp(ishape)
         # create third field
        id2 = 2
        (F2, finfo2, coeff2) = set_field(id2)
        ishape3 =[otype1, finfo2]
        z2 = set_outerApp(z1, F2)#ishape3
        coeffs = coeff1+[coeff2]
        return (z2, coeffs)
    elif (outer_arity==2 and inner_arity==3): # binary and third-arity operators
        # apply inner operator to first arg
        (z1, coeff1) = set_innerApp(ishape)
        # create third field
        id2 = 2
        (F2, finfo2, coeff2) = set_field(id2)
        id3 = 3
        (F3, finfo3, coeff3) = set_field(id3)
        ishape3 =[otype1, finfo2, finfo3]
        z2 = set_outerApp3(z1, F2 ,F3)
        coeffs = coeff1+[coeff2, coeff3]
        return (z2, coeffs)
    elif (outer_arity==3): #  third-arity operators
        # apply inner operator to first arg
        (z1, coeff1) = set_innerApp(ishape)
        # create third field
        id2 = 2
        (F2, finfo2, coeff2) = set_field(id2)
        id3 = 3
        (F3, finfo3, coeff3) = set_field(id3)
        ishape3 =[otype1, finfo2, finfo3]
        z2 = set_outerApp3(z1, F2 ,F3)
        coeffs = coeff1+[coeff2, coeff3]
        return (z2, coeffs)
    else:
        raise Exception ("arity is not supported: "+str(outer_arity))
# create application for third layer of operation
# (ztwice, coeffstwice) is the resulting second layer
def mkApply_third(ztwice, coeffstwice, ishape, tshape3, name, opr_outer2, inputfile, coeff_style, ucoeff, g_krn,t_template):
    outer2_arity = opr_outer2.arity
    cnt = 0
    def set_outer2App(lhs, rhs):
        ##print "set_outer2App, tshape3: ", tshape3.name
        return apply(name, opr_outer2, lhs, rhs, None, tshape3, false, true)
    def set_field(id):
        # get kernel
        c_krn = transform_krn(g_krn, id)
        c_k =  c_krn.continuity
        c_fty = ishape[id]
        c_dim = fty.get_dim(c_fty)
        return mk_Field(id, c_fty, c_k, inputfile, c_dim, coeff_style, ucoeff, c_krn,t_template)
    def set_outerApp(lhs, rhs):
        return apply(name, opr_outer2,lhs, rhs, None, tshape3, false, true)
    def set_outerApp3(lhs, rhs, third):
        return apply(name, opr_outer2,lhs, rhs, third, tshape3, false, true)
    if(outer2_arity==1):
        # just place in 2nd layer app in  left hand side
        z2 = set_outer2App(ztwice, None)
        return (z2, coeffstwice)
    elif(outer2_arity==2):
        # create another argument (tensor/field)
        # get last shape added (assuming ishape was built correctly)
        id2 = len(ishape)-1
        (F2, finfo2, coeff2) = set_field(id2)
        z2 = set_outerApp(ztwice, F2)#ishape3
        # add to existing coeffients
        coeffs = coeffstwice+[coeff2]
        return (z2, coeffs)
    elif(outer2_arity==3):
        # create another argument (tensor/field)
        # get last shape added (assuming ishape was built correctly)
        id2 = len(ishape)-2
        (F2, finfo2, coeff2) = set_field(id2)
        id3 = id2+1
        (F3, finfo3, coeff3) = set_field(id3)
        z2 = set_outerApp3(ztwice, F2, F3)#ishape3
        # add to existing coeffients
        coeffs = coeffstwice+[coeff2, coeff3]
        return (z2, coeffs)
    else:
        raise Exception ("arity is not supported: "+str(outer2_arity))
