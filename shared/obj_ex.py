# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from obj_ty import *
from obj_operator import *
from base_var_ty import *
from base_constants import *
class example:
    def __init__(self, opr, tys):
        self.opr=opr
        self.tys=tys
    def toStr(self, i):
        name = self.opr.name+" ( "
        curty = self.tys[i]
        for j in curty:
            name+=j.name+","
        name+=" )"
        return name
    def get_oprname(self):
        return self.opr.name
    def get_opr(self):
        return self.opr
    def get_ty(self, i):
        if (i >= len(self.tys)):
            raise Exception("unsupported type("+str(i)+") for "+ self.opr.name)
        return self.tys[i]


InvR = flag_vis_test
#--------------  put list in parameter form  ----------------------
# make list of unary args
def get_unu(fall):
    rtn = []
    # binary operator
    for f in fall:
        rtn.append([f])
        #print ("["+f.name+"]")
    return rtn

#is type represented in list of fields
def outsupported(f, bshape):
    if (len(bshape)>4):
        return False
    dim = f.dim
    (tf, _) = shapeToTyhelper(bshape, dim)
    return tf

# types for multiplication
#one has to be a scalar, and one has to a be a field
def get_mul(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            if (fty.is_Field(e1)):
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif(fldresult and (not fty.is_Field(e2))):
                continue
            # one arg needs to be a scalar
            if (fty.is_Scalar(e1) or fty.is_Scalar(e2)):
                rtn.append([e1,e2])
    return rtn

# types for division
#one has to be a scalar, and one has to a be a field
def get_division(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            #print "e1", e1.name
            #print "e2", e2.name
            if (fty.is_Field(e1)):
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif(fldresult and (not fty.is_Field(e2))):
                continue
            # one arg needs to be a scalar
            if (fty.is_Scalar(e2)):
                rtn.append([e1, e2])
    return rtn

# types for addition, subtraction, modulate
# one has to be a field in list nonscalarsflds
# must have same type.
def get_add(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
    #rtn.append([e1, e2])
            if (fty.is_Field(e1)):
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif(fldresult and (not fty.is_Field(e2))):
                continue
            # needs to have same type
            if (fty.get_shape(e1) == fty.get_shape(e2)):
                rtn.append([e1, e2])
    return rtn

def get_modulate(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            if( fty.is_Scalar(e1)  or  fty.is_Scalar(e2)):
                continue
            if (fty.is_Field(e1)):
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif(fldresult and (not fty.is_Field(e2))):
                continue
            # needs to have same type
            if (fty.get_shape(e1) == fty.get_shape(e2)):
                rtn.append([e1, e2])
    return rtn

def get_doubledot(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            ashape = fty.get_shape(e1)
            bshape = fty.get_shape(e2)
            if(len(ashape) <2):
                continue
            if (fty.is_Field(e1)):
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif(fldresult and (not fty.is_Field(e2))):
                continue
            # needs to have same type
            if (fty.get_shape(e1) == fty.get_shape(e2)):
                rtn.append([e1, e2])
    return rtn

def get_concat2(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:

            if ((not fty.is_Field(e1)) or (not fty.is_Field(e2))):
                continue
            if(not (e1.dim==e2.dim)):
                continue
            # needs to have same type
            if (fty.get_shape(e1) == fty.get_shape(e2)):
                rtn.append([e1, e2])

    return rtn

def get_concat3(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            for e3 in es:
                if ((not fty.is_Field(e1)) or (not fty.is_Field(e2))or (not fty.is_Field(e3))):
                    continue
                if(not (e1.dim==e2.dim) or (not e1.dim==e3.dim)):
                    continue
                # needs to have same type
                if ((fty.get_shape(e1) == fty.get_shape(e2)) and (fty.get_shape(e1) == fty.get_shape(e3))):
                    rtn.append([e1, e2, e3])
    return rtn

def get_compose(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            if ((not fty.is_Field(e1)) or (not fty.is_Field(e2))):
                continue
            if(not (e1.dim==e2.dim)):
                continue
            # needs to have same type
            if (e1.dim==1 and fty.is_Scalar(e2)):
                rtn.append([e1, e2])
            elif(fty.get_shape(e2)== [e1.dim]):
                rtn.append([e1, e2])

    return rtn

def get_max(es, fldresult):
    rtn = []
    # binary operator
    for e1 in es:
        for e2 in es:
            if ((not fty.is_Field(e1)) or (not fty.is_Field(e2))):
                continue
            if(not (e1.dim==e2.dim)):
                continue
            if (fty.is_Scalar(e1) and fty.is_Scalar(e2)):
                rtn.append([e1, e2])
    return rtn


#binary operators between flds fld (limited in some way)
# and higher order tensor/tensor field
def get_inner(es, fldresult):
    rtn = []
    for e1 in es:
        for e2 in es:
            if( fty.is_Scalar(e1)  or  fty.is_Scalar(e2)):
                continue
            shape1 = fty.drop_first(e1)
            shape2 = fty.drop_last(e2)
            bshape = shape1+shape2
            if (fty.is_Field(e1)):
                if(not  outsupported(e1, bshape)):
                    continue
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif( (not fty.is_Field(e2)) and fldresult):
                continue
            if(not  outsupported(e2, bshape)):
                continue
            if((fty.get_last_ix(e1)==fty.get_first_ix(e2))):
                rtn.append([e1,e2])
    return rtn


#binary operators between flds fld (limited in some way)
# and higher order tensor/tensor field
def get_outer(es, fldresult):
    rtn = []
    for e1 in es:
        for e2 in es:
            if( fty.is_Scalar(e1)  or  fty.is_Scalar(e2)):
                continue
            
            bshape = fty.get_shape(e1)+fty.get_shape(e2)
            if (fty.is_Field(e1)):
                if(not  outsupported(e1, bshape)):
                    continue
                if(fty.is_Field(e2) and (not check_dim(e1, e2))):
                    continue
            elif( (not fty.is_Field(e2)) and fldresult):
                continue
            if(not  outsupported(e2, bshape)):
                continue
            rtn.append([e1,e2])
    return rtn

#binary operators between flds fld (limited in some way)
# and higher order tensor/tensor field
def get_cross(es, fldresult):
    rtn = []
    for e1 in es:
        for e2 in es:
            if((not (fty.is_Vector(e1)))  or  (not (fty.is_Vector(e2)))):
                continue
            # vectors have to have same length
            [n] = fty.get_shape(e1)
            [m] = fty.get_shape(e2)
            if(not (m==n)):
                continue
            bshape = [n]
            if (fty.is_Field(e1)):
                if(not  outsupported(e1, bshape)):
                    continue
                if(fty.is_Field(e2)):
                    if(not check_dim(e1, e2)):
                        continue
                    if(not (e2.dim==n)):
                        continue
                if(not (e1.dim==n)):
                    continue
            elif(fty.is_Field(e2)):
                if(not  outsupported(e2, bshape)):
                    continue
                if(not (e2.dim==n)):
                    continue
            elif(fldresult):
                continue
            rtn.append([e1,e2])
    return rtn


#-------------- examples with operators and types  ----------------------
# returns example object
def oprToArgs(op1, tys):
    # sets possible input types
    (l_all_T, l_all_F, l_all) = tys
    def rtnArgs_all(f):
        # #1 list to iterate over
        # #1 does the result have to be a field?
        ps_T = f(l_all_T, False)
        ps_F = f(l_all_F, True)
        ps_TFF = f(l_all, True)
        ps_TF = f(l_all, False)
        return [ps_T, ps_F,  ps_TFF, ps_TF]
    def get_k(f):
        g1 = f(l_all_T)
        t1 = get_unu(g1)
        g2 = f(l_all_F)
        t2 = get_unu(g2)
        g4 = f(l_all)
        t4 = get_unu(g4)
        return [t1, t2, t2, t4]

    #operator that only works on fields
    def get_k_noT(f):
        t1 = get_unu([])
        g2 = f(l_all_F)
        t2 = get_unu(g2)
        return [t1, t2, t2, t2]
    # unary args
    def same(e):
        #for i in e:
            #print "same", i.name
        return e
    # ps_..  list of unary args   [[a],[b],..]
    ### scalar argument
    ps_unu_sk =                 get_k_noT(get_scaF)
    ### all type arguments
    ps_unu_all  =               get_k(same)


    if(op1.arity==1):
        if((op1.id==op_negation.id) or  (op1.id==op_copy.id) or  (op1.id==op_none.id)):
            return (ps_unu_all)
        elif((op1.id==op_norm.id) or (op1.id==op_normalize.id)):
            return  ps_unu_all                # probe
        elif((op1.id==op_trace.id) or (op1.id==op_transpose.id)):
            return get_k(get_mat_symmal)                # trace, transpose,det
        elif(op1.id==op_det.id):
            return get_k(get_mat_symmal)                # trace, transpose,det
        elif(op1.id==op_inverse.id and InvR):
            return get_k(get_mat_symmalR)
        elif(op1.id==op_inverse.id):
            return get_k(get_mat_symmal)
            # symmetric matrices
        elif((op1.id==op_slicev0.id) or (op1.id==op_slicev1.id)) :
            return get_k(get_vecF)                  # slice vector
           # all vector arguments
        elif((op1.id==op_slicem0.id) or (op1.id==op_slicem1.id)):
            return  get_k(get_matF)
            # all matrices
            # slice matrix
        elif((op1.id==op_slicet0.id) or (op1.id==op_slicet1.id)):
            return  get_k(get_Ten3)  ### third order tensor type
            # slice third order tensor
        elif((op1.id==op_sine.id) or (op1.id==op_asine.id)):
            return ps_unu_sk
        elif((op1.id==op_cosine.id) or (op1.id==op_acosine.id)):
            return ps_unu_sk
        elif((op1.id== op_tangent.id) or (op1.id== op_atangent.id)):
            return ps_unu_sk
        elif(op1.id== op_sqrt.id):
            return get_k(get_scaF)
        elif(op1.id==op_gradient.id):
            return get_k_noT(get_scaF) # differentiation only for scalar fields
        elif(op1.id==op_hessian.id):
            return get_k_noT(get_scaF) # differentiation only for scalar fields
        elif((op1.id==op_divergence.id) or (op1.id==op_curl.id)):
            return  get_k_noT(get_vecF_samedim)
        elif(op1.id==op_jacob.id):
            return  get_k_noT(get_vecF_matF)
            # vector arguments where [dim]=shape
            # divergence, curl, jacobian
        elif(op1.id== op_zeros_add22.id):
            return get_k(get_mat_symmal_22)
        elif(op1.id== op_zeros_scale3.id):
            return get_k(get_scaF)
        elif(op1.id==op_zeros_outer2.id):
            return  get_k(get_vecF)
        elif(op1.id == op_crossT3.id):
            return  get_k(get_vec_3)
        else:
            raise Exception("no built in example of operator"+op1.name)
    elif(op1.arity==2):
        def get_eval():
            if((op1.id==op_add.id) or (op1.id==op_subtract.id)):
                return (get_add)                   # addition
            elif(op1.id==op_cross.id):
                return (get_cross)             # cross product
            elif(op1.id==op_outer.id):
                return ( get_outer)            # outer product
            elif(op1.id==op_inner.id):
                return  (get_inner)            # inner product
            elif(op1.id==op_scale.id):
                return  (get_mul)            # scaling
            elif(op1.id==op_division.id):
                return (get_division)           # division
            elif(op1.id==op_modulate.id):
                return  (get_modulate)                # modulate
            elif(op1.id==op_doubledot.id) :
                return (get_doubledot)                 # doubledot
            elif(op1.id==op_concat2.id):
                return (get_concat2)
            elif(op1.id==op_comp.id):
                return (get_compose)
            elif(op1.id==op_max.id or op1.id ==op_min.id):
                return (get_max)
            else:
                raise Exception("no built in example of operator"+op1.name)
        return rtnArgs_all(get_eval())
    elif(op1.arity==3):
        def get_eval():
            if(op1.id==op_concat3.id):
                return (get_concat3)
            else:
                raise Exception("no built in example of operator"+op1.name)
        return rtnArgs_all(get_eval())
    else:
        raise Exception("no built in example of operator"+op1.name)
# returns example object
def oprToEx_a(op1, rst_ty, tys):
    mm = oprToArgs(op1, tys)
    args = getArgs(mm, rst_ty)
    return example(op1, args)
# gets a single examples
def get_single_example(opr, ty_num, args_types):
    ex = oprToEx(opr, args_types)
    #print "current operator "+opr.name+ "("+str(opr.id)+ ") # "+str(ty_num)+"|"+str(len(ex.tys)-1)
    i = 0
    for t in ex.tys:
        x=""
        if(i==ty_num):
            x+="->"
        x += str(i)+". "
        for j in t:
            x+= j.name+","
        i+=1
    #print x
    name = example.toStr(ex, ty_num)
    ty = example.get_ty(ex, ty_num)
    return (name, opr,ty)
# gets a single examples
def get_single_exampleEx(ex, ty_num):
    i = 0
    for t in ex.tys:
        x=""
        if(i==ty_num):
            x+="->"
        x += str(i)+". "
        for j in t:
            x+= j.name+","
        i+=1
        #print x
    name = example.toStr(ex, ty_num)
    ty = example.get_ty(ex, ty_num)
    return (name, ty)
