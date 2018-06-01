import sys
import re
import os
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_constants import *
from input import s_field

#apply inverse of reals
InvReal = False #FIXME

# check application of operator to types
# organized by arity of operator

# isShapeOk()  is the shape ok? Is it supported?
def isShapeOk(a,b):
    #return shapeToTyhelper(a,b)#check if nrrd output for vis ver
    return shapeToTyhelper2(a,b)
#type of field after operation is applied
# note need to generalize for field and tensor operators 
# note need to check if field for correct
def applyUnaryOp(op1,ityps):
    ##print "inside unary op"
    ityp1=ityps[0]
    k = ityp1.k
    dim = ityp1.dim
    ashape = ityp1.shape
    name =  "op1 "+op1.name+"("+ityp1.name+")"
    ##print "apply unary op", name, ashape
    space = None
    if(fty.is_OField(ityp1)):
        space = ityp1.space
    def same():
        return (true, ityp1)
    def err():
        return (false, name)
    def mkTyp(shape):
        (tf, rty1) = isShapeOk(shape, dim)
        if(tf):
            rtn1 = fty.convertTySpace(rty1, k, space)
            return (true, rtn1)
        else:
            return err()
    # differentiation was used, k has a limit
    def mkTyp_deductk(k_limit, shape):
        ##print "inside mktyp deduct k "
        if(k<k_limit or len(shape)>3):
             return err()
        else:
            (tf, rty1) = isShapeOk(shape, dim)
            if(tf):
                rtn1 = fty.convertTySpace(rty1, k-k_limit, space)
                return (true, rtn1)
            else:
                return err()
    if(op_probe==op1):
        return (true, fty.convertToTensor(ityp1))
    elif ((op_copy==op1) or (op_none==op1) or (op_negation==op1) or (op1==op_negationT)):
        return same() #type unaffected by operation
    elif (op_normalize==op1):
        ###print "made it to normalize"
        if(fty.is_Scalar(ityp1)):
            return err()
        else:
            return same() #type unaffected by operation
    elif(op_norm==op1):            # apply op_norm
        return mkTyp([])
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
        if(op_sqrt==op1 or op_abs==op1):
            return same()
        elif(op_cosine==op1) or (op_sine==op1)or (op_tangent==op1) or (op_acosine==op1) or (op_asine==op1)or (op_atangent==op1):
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
            ##print "hessian mark"
            if(not fty.is_Field(ityp1)):
                return err()
            if (dim==1):
                # should actually  be gradient of gradient
                return err()
            else:
                #print "in here"
                return mkTyp_deductk(2, [dim, dim])
        elif(op_inverse==op1 and InvReal):            # apply op_inverse_d2
            return same()
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

    ###print "---------------------  applyBinaryOp ---------"

##print "---------------------  applyBinaryOp ---------"

    name =  "op1 "+op1.name
    ityp1 = ityps[0]
    ityp2 = ityps[1]
    ashape = fty.get_shape(ityp1)
    bshape = fty.get_shape(ityp2)

    ###print "type name", name
    (tf, fldty) = find_field(ityp1,ityp2) # assures same dimension for both fields
    if(not tf):
        return (false, "not the same dimension")
    k = fldty.k
    if (fty.is_Field(ityp1) and fty.is_Field(ityp2)):
        k = min(ityp1.k, ityp2.k)
    space = None
    if (fty.is_OField(ityp1)):
        space = ityp1.space
    elif (fty.is_OField(ityp2)):
        space = ityp2.space
    
    dim = fldty.dim
    def err():
        # type not supported
        return (false, name)
    def mkTyp(shape):
        if (len(shape)>3):
            return err()
        else:
            (tf, rty1) = isShapeOk(shape, dim)
            ##print tf, rty1
            if(tf):
                rtn1 = fty.convertTySpace(rty1, k, space)

                return (true, rtn1)
            else:
                return err()
    def sameshape(ty3):
        if(ashape==bshape):
            return (true, ty3) #type unaffected by operation
        else:
            return err()
    if (op_add==op1) or (op_subtract==op1):
        return sameshape(fldty)
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
                ##print "found a field"
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
        if((not fty.is_Field(ityp1)) or (not fty.is_Field(ityp2))):
            return err()
        else:
            ashape = ityp1.shape
            bshape = ityp2.shape
            if(ashape==bshape):
                return mkTyp ([2]+ashape)
            else:
                return err()
    elif(op_comp==op1):
        if((not fty.is_Field(ityp1)) or (not fty.is_Field(ityp2))):
            return err()
        else:
            if(ityp1.dim==1):
                return err()
            elif((ityp1.dim==1) and (fty.get_shape(ityp2)== [])):
                return mkTyp (ityp1.shape)
            elif(fty.get_shape(ityp2)==[ityp1.dim]):
                return  mkTyp (ityp1.shape)
            else:
                return err()
    else:
        # rest of operators are non scalar
        if(fty.is_Scalar(ityp1) or fty.is_Scalar(ityp2)):
            if(op_scale==op1):
                return mkTyp(ashape+bshape)
            elif(op_max.id==op1.id or op_min.id==op1.id):

                if(fty.is_ScalarField(ityp1) and fty.is_ScalarField(ityp2)):
                    return mkTyp ([])
                else:
                    return err()
            else:
                return err()
        else:
            # these operators don't apply to scalars
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
                        return mkTyp([])
                    else:
                        return err()
                else:
                    return err()
            elif(op_inner==op1):
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
    ###print "---------------------  applyBinaryOp ---------"
    name =  "op1 "+op1.name
    ###print name
    ityp1 = ityps[0]
    ityp2 = ityps[1]
    ityp3 = ityps[2]
    ashape = fty.get_shape(ityp1)
    bshape = fty.get_shape(ityp2)
    name += "("+ityp1.name+","+ityp2.name+","+ityp3.name+")"
    ###print "type name", name
    (tf, fldty) = find_field(ityp1,ityp2) # assures same dimension for both fields
    if(not tf):
        return (false, "not the same dimension")
    (tf, fldty) = find_field(fldty,ityp3)
    if(not tf):
        return (false, "not the same dimension")
    k = fldty.k
    dim = fldty.dim
    space = None
    if (fty.is_OField(ityp1)):
        space = ityp1.space
    elif (fty.is_OField(ityp2)):
        space = ityp2.space

    ###print "---------------------  continue ---------"
    def err():
        # type not supported
        return (false, name)
    def mkTyp(shape):
        ###print "mkTyp ", shape.name
        if (len(shape)>3):
            return err()
        else:
            ###print "shape",shape, "dim",dim
            (tf, rty1) = isShapeOk(shape, dim)
            ###print "mark d "
            if(tf):
                rtn1 = fty.convertTySpace(rty1, k,space)
                return (true, rtn1)
            else:
                return err()
    if(op_concat3==op1):
        ###print "concat 3 ********  here "
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
#############################################################################################
# apply unary and binary operator
def get_tshape(opr1, ishape):
    arity = opr1.arity
    if(arity==0):
        return (true, ty_mat3x3F_d3)
    elif(arity==1):
        (a,b) =  applyUnaryOp(opr1, ishape)
        return (a,b)
    elif(arity==2):
        (m,n) = applyBinaryOp(opr1, ishape)
        return (m,n)
    elif(arity==3):
        return applyThirdOp(opr1, ishape)
