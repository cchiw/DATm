import sys
import re
import os
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *

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
        s = str(layer)+"\t"+self.opr.name#+" isrootlhs: "+str(self.isrootlhs)+" isrootrhs: "+str(self.isrootrhs)+" oty: "+str(self.oty.name))
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


# isShapeOk()  is the shape ok? Is it supported?
def isShapeOk(a,b):
    #return shapeToTyhelper(a,b)#check if nrrd output for vis ver
    return shapeToTyhelper2(a,b)


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
    ##print "isDifferentiabl-ityp",ityp
    dim = fty.get_dim(ityp)
    k=ityp.k
    return (k>0)

#type of field after operation is applied
# note need to generalize for field and tensor operators 
# note need to check if field for correct
def applyUnaryOp(op1,ityps):
    #print "inside unary op"
    ityp1=ityps[0]
    ##print "itype1", ityp1.name
    k = ityp1.k
    dim = ityp1.dim
    ashape = ityp1.shape
    
    name =  "op1 "+op1.name+"("+ityp1.name+")"
    #print "apply unary op", name, ashape
    def same():
        return (true, ityp1)
    def err():
        return (false, name)
    def mkTyp(shape):
        ##print "mark-a"
        (tf, rty1) = isShapeOk(shape, dim)
        if(tf):
            ##print "mark-b"
            rtn1 = fty.convertTy(rty1, k)
            return (true, rtn1)
        else:
            return err()
    # differentiation was used, k has a limit
    def mkTyp_deductk(k_limit, shape):
        #print "inside mktyp dedcut k "
        if(k<k_limit or len(shape)>3):
             return err()
        else:
            (tf, rty1) = isShapeOk(shape, dim)
            if(tf):
                rtn1 = fty.convertTy(rty1, k-k_limit)
                return (true, rtn1)
            else:
                return err()
    if(op_probe==op1):
        return (true, fty.convertToTensor(ityp1))
    elif ((op_copy==op1) or (op_negation==op1)):
        return same() #type unaffected by operation
    elif (op_normalize==op1):
        ##print "made it to normalize"
        if(fty.is_Scalar(ityp1)):
            return err()
        else:
            return same() #type unaffected by operation
    elif(op_norm==op1):            # apply op_norm
        return mkTyp([])
    elif (op_negationT==op1):
        return same() #type unaffected by operation
    elif(op_jacob==op1):            # apply op_jacob
        if(not fty.is_Field(ityp1)):
            return err()
        if(fty.is_Vector(ityp1)):
            [n1] = ashape
            if(n1==2 and dim==2):
                return mkTyp_deductk(1, [2,2])
            elif(n1==3 and dim==3):
                return mkTyp_deductk(1, [3,3])
            else:
                return err()
        elif(fty.is_Matrix(ityp1)):
            [n1,n2] = ashape
            if(n1==n2 and n2==dim):
                if(dim==2):
                    return mkTyp_deductk(1, [2,2,2])
                elif(dim==3):
                    return mkTyp_deductk(1, [3,3,3])
                else:
                    return err()
            else:
                return err()
        else:
            return err()
    elif(fty.is_Scalar(ityp1)):
        ##print "tshape-scalar"
        if(op_sqrt==op1):
            return same()
        elif(op_cosine==op1) or (op_sine==op1)or (op_tangent==op1) or (op_acosine==op1) or (op_asine==op1)or (op_atangent==op1):
            ##print "found trig"
            if(fty.is_Field(ityp1)):
                return same()
            else:
                return err()
        elif(op_zeros_scale3==op1):
            return mkTyp([3, 3])
        elif (op_gradient==op1):
            if(not fty.is_Field(ityp1)):
                return err()
            if (dim==1):
                return mkTyp_deductk(1, [])
            else:
                return mkTyp_deductk(1, [dim])
        elif (op_hessian==op1):
            #print "inside here"
            if(not fty.is_Field(ityp1)):
                return err()
            if (dim==1):
                #print "dim 1 "
                # should actually  be gradient of gradient
                return err()
            else:
                return mkTyp_deductk(2, [dim, dim])
        else:
            return err()
    elif(fty.is_Vector(ityp1)):
      
        [n1] = ashape
        if((op_slicev0==op1) or(op_slicev1 ==op1)):            # apply op_slice
            return mkTyp([])
        elif(not (n1==dim)):
            # since the rest are differentiation operators
            return err()
        elif(op_curl==op1):            # apply curl
            if(not fty.is_Field(ityp1)):
                return err()
            if((n1==2) and (dim==2)):
                return mkTyp_deductk(1, [])
            elif((n1==3) and (dim==3)):
                return mkTyp_deductk(1, [3])
            else:
                return err()
        #elif(op_jacob==op1):            # apply op_jacob
        #   if(not fty.is_Field(ityp1)):
        #        return err()
        #if(n1==2 and dim==2):
        #               return mkTyp_deductk(1, [2,2])
        #           elif(n1==3 and dim==3):
        #               return mkTyp_deductk(1, [3,3])
        #           else:
        #               return err()
        elif(op_divergence==op1):
            if(not fty.is_Field(ityp1)):
                return err()
            return mkTyp_deductk(1, [])
        elif(op_zeros_outer2==op1):
            return  mkTyp([2,n1])
        elif(op_crossT3==op1):
            if(fty.is_Field(ityp1)):
                if((dim==3) and (n1==3)):
                    return mkTyp ([3])
                else:
                    return err()
            elif(n1==3):
                return mkTyp ([3])
            else:
                return err()
        else:
            return err()
    elif(fty.is_Matrix(ityp1)):
        [n, m] = ashape
        if(op_slicem1 ==op1):            # apply op_slice [:,0]
            return mkTyp([n])
        elif(op_slicem0==op1):            # apply op_slice [1,:]
            return mkTyp([m])
        elif(n!=m):
            return err()
        elif(op_transpose==op1):            # apply op_tranpose
            return mkTyp([m, n])
        elif((op_trace==op1) or (op_det==op1)):
            if(n==m and (n==2 or n==3)):
                return mkTyp([])
            else:
                return err()
        elif(op_inverse==op1):            # apply op_inverse_d2
            if(n==m and (n==2 or n==3)):
                return same()
            else:
                return err()
        elif(op_zeros_add22 ==op1):
            if(n==m and n==2):
                return mkTyp([n, m])
            else:
                return err()
        else:
            return err()
    elif(fty.is_Ten3(ityp1)):
        if(op_slicet0==op1):            # apply op_slice [:,1,:]
            [a, _, c] = ashape
            return mkTyp([a,c])
        elif(op_slicet1 ==op1):            # apply op_slice [1,0,:]
            [_,_,c] = ashape
            return mkTyp([c])
        else:
            return err()
    else:
        return err()

#type of field after operation is applied
def applyBinaryOp(op1,ityps):
    ##print "---------------------  applyBinaryOp ---------"
    name =  "op1 "+op1.name
    ##print name
    ityp1 = ityps[0]
    ityp2 = ityps[1]
    ##print "ityps:",ityps
    ##print "ityp1 :",ityp1
    ##print ityp1.name
    ashape = fty.get_shape(ityp1)
    bshape = fty.get_shape(ityp2)
    name += "("+ityp1.name+","+ityp2.name+")"
    ##print "type name", name
    (tf, fldty) = find_field(ityp1,ityp2) # assures same dimension for both fields
    if(not tf):
        return (false, "not the same dimension")
    k = fldty.k
    if (fty.is_Field(ityp1) and fty.is_Field(ityp2)):
        k = min(ityp1.k, ityp2.k)
    dim = fldty.dim
    ##print "---------------------  continue ---------"
    def err():
        # type not supported
        return (false, name)
    def mkTyp(shape):
        if (len(shape)>3):
            return err()
        else:
            ##print "in mk type"
            ##print shape, dim
            #NTS if we are creating visver
            (tf, rty1) = isShapeOk(shape, dim)
            ##print tf, rty1
            if(tf):
                rtn1 = fty.convertTy(rty1, k)
                return (true, rtn1)
            else:
                return err()
    def sameshape(ty3):
        ##print "---------------------  same shape ---------"
        if(ashape==bshape):
            return (true, ty3) #type unaffected by operation
        else:
            return err()
    ##print "ityp1: ", ityp1.name, " K: ", ityp1.k
    ##print "ityp2: ", ityp2.name, " K: ", ityp2.k
    # K is not the same
    #if (fty.is_Field(ityp1) and fty.is_Field(ityp2) and (not (ityp1.k==ityp2.k))):
        ##print "k is not the same"
        #return err()
    if (op_add==op1) or (op_subtract==op1):
        ##print "current addition "
        ##print ityp1.name, "-",ityp2.name
        ##print "fldty", fldty.name
        x = sameshape(fldty)
        ##print x
        return x
    elif(op_division==op1):
        if(fty.is_Scalar(ityp2)):
            return mkTyp(ashape)
        else:
            return err()
    elif(op_cross==op1):
        if(fty.is_Vector(ityp1) and fty.is_Vector(ityp2)):
            n1 = fty.get_vecLength(ityp1)
            n2 = fty.get_vecLength(ityp2)
            if(not (n1==n2)):
                return err()
            if(fty.is_Field(fldty)):
                if ((dim==2) and (n1==2)):
                    return mkTyp([])
                elif((dim==3) and (n1==3)):
                    return mkTyp([3])
                else:
                    return err()
            else:
                if(n1==2):
                    return mkTyp([])
                elif((n1==3)):
                    return mkTyp([3])
                else:
                    return err()
        else:
            return err()
    elif(op_concat2==op1):
        ##print "concat 2 ********  here "
        if((not fty.is_Field(ityp1)) or (not fty.is_Field(ityp2))):
            return err()
        else:
            ashape = ityp1.shape
            bshape = ityp2.shape
            ##print "ashape",ashape
            if(ashape==bshape):
                ##print "here"
                x= mkTyp ([2]+ashape)
                ##print "x",x
                return x
            else:
                return err()
    elif(op_comp==op1):
        ##print "checking composition", ityp1.name, ityp2.name
        if((not fty.is_Field(ityp1)) or (not fty.is_Field(ityp2))):
            return err()
        else:
            if(ityp1.dim==1):
                return err()
            elif((ityp1.dim==1) and (fty.get_shape(ityp2)== [])):
                x= mkTyp (ityp1.shape)
                ##print "x",x
                return x
            elif(fty.get_shape(ityp2)==[ityp1.dim]):
                x= mkTyp (ityp1.shape)
                ##print "x",x
                return x
            else:
                return err()
    else:
        # rest of operators are non scalar
        if(fty.is_Scalar(ityp1) or fty.is_Scalar(ityp2)):
            if(op_scale==op1):
                return mkTyp(ashape+bshape)
            else:
                return err()
        else:
            if((op_modulate==op1)):
                n = len(ashape)
                if(n==1):
                    return sameshape(fldty)
                else:
                    return err()
            elif(op_outer==op1):
                return mkTyp(ashape+bshape)
            elif(op_doubledot==op1):
                n = len(ashape)
                if(n==2):
                    if (fty.is_Field(ityp1) and fty.is_Field(ityp2) and (ityp1.k != ityp2.k)):
                        return err()
                    elif(ashape==bshape):
                        ##print "same shape"
                        return mkTyp([])
                    else:
                        ##print "not the same shape"
                        return err()
                else:
                    return err()
            elif(op_inner==op1):
                ##print "here"
                n1 = fty.get_last_ix(ityp1)
                n2 = fty.get_first_ix(ityp2)
                if(n1!=n2): #must have equal vector lengths
                    return err()
                shape1 = fty.drop_first(ityp1)
                shape2 = fty.drop_last(ityp2)
                return mkTyp(shape1+shape2)
            else:
                return err()


#type of field after operation is applied
def applyThirdOp(op1,ityps):
    ##print "---------------------  applyBinaryOp ---------"
    name =  "op1 "+op1.name
    ##print name
    ityp1 = ityps[0]
    ityp2 = ityps[1]
    ityp3 = ityps[2]
    ashape = fty.get_shape(ityp1)
    bshape = fty.get_shape(ityp2)
    name += "("+ityp1.name+","+ityp2.name+","+ityp3.name+")"
    ##print "type name", name
    (tf, fldty) = find_field(ityp1,ityp2) # assures same dimension for both fields
    if(not tf):
        return (false, "not the same dimension")
    k = fldty.k
    dim = fldty.dim
    ##print "---------------------  continue ---------"
    def err():
        # type not supported
        return (false, name)
    def mkTyp(shape):
        ##print "mkTyp ", shape.name
        if (len(shape)>3):
            return err()
        else:
            ##print "shape",shape, "dim",dim
            (tf, rty1) = isShapeOk(shape, dim)
            ##print "mark d "
            if(tf):
                rtn1 = fty.convertTy(rty1, k)
                return (true, rtn1)
            else:
                return err()
    if(op_concat3==op1):
        ##print "concat 3 ********  here "
        if((not fty.is_Field(ityp1)) or (not fty.is_Field(ityp2)) or (not fty.is_Field(ityp3))):
            return err()
        else:
            ashape = ityp1.shape
            bshape = ityp2.shape
            cshape = ityp3.shape
            if(ashape==bshape and ashape ==cshape):
                return mkTyp ([3]+ashape)
            else:
                return err()
    else:
        return err()
##################################################################################################
# apply unary and binary operator
def get_tshape(opr1, ishape):
    #print "inside getshape", opr1.name
    arity = opr1.arity
    if(arity==0):
        #print "arity 0"
        return (true, ty_mat3x3F_d3)
    elif(arity==1):
        #print "artity 1"
        x = applyUnaryOp(opr1, ishape)
        #print "retn from get unary", x
        return x
    elif(arity==2):
        #print "getting tshape of-applyBinaryOp", opr1.name,"arg=", ishape[0].name,",", ishape[1].name
        x = applyBinaryOp(opr1, ishape)
        #print "rtn from get binary", x
        return x
    elif(arity==3):
        return applyThirdOp(opr1, ishape)

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
    
    else:
        raise Exception ("arity is not supported: "+str(outer_arity))

# create application for third layer of operation
# (ztwice, coeffstwice) is the resulting second layer
def mkApply_third(ztwice, coeffstwice, ishape, tshape3, name, opr_outer2, inputfile, coeff_style, ucoeff, g_krn,t_template):
    outer2_arity = opr_outer2.arity
    cnt = 0
    for i in ishape:
        ##print cnt,":",i.name, len(ishape)
        cnt+=1
    
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
    if(outer2_arity==1):
        # just place in 2nd layer app in  left hand side
        z2 = set_outer2App(ztwice, None)
        ##print "z2-oty:", z2.oty
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
    else:
        raise Exception ("arity is not supported: "+str(outer2_arity))

