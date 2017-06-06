# - dek_ir(k_init, es): deduct continuity of types on list
# - d_tofield(dim): return list of type given dimension
# - backward_op1(op1, k_init): unary operator and initial k -> (input type, result type)
# possible argument to operator and output.


from obj_field import *
from obj_operator import *
from obj_ty import *
from shape import *

#########################################################################################################


# deduct continuity fields
def dek_ir(k_init, es):
    rtn = []
    for (ity1, rty1) in es:
        if(not(k_init==0)):
            tmp = (ity1, fty.convertTy(rty1, k_init-1))
            rtn.append(tmp)
    return rtn
#given a field of a particular dim, return all types with that dimension.
def d_tofield(dim):
    if(dim==1):
        return [ty_scalarF_d1, ty_vec2F_d1, ty_vec3F_d1, ty_vec4F_d1, ty_mat2x2F_d1, ty_mat3x3F_d1]
    elif(dim==2):
        return  [ty_scalarF_d2, ty_vec2F_d2, ty_vec3F_d2, ty_vec4F_d2, ty_mat2x2F_d2, ty_mat3x3F_d2]
    elif(dim==3):
        return  [ty_scalarF_d3, ty_vec2F_d3, ty_vec3F_d3, ty_vec4F_d3, ty_mat2x2F_d3, ty_mat3x3F_d3]
    else:
        return l_all1

# moving backwards
# given opr1(airty =1)
# what are possible inputs and possible outputs
def backward_op1(op1, k_init):
    # (op1) input type -> output type
    # dek diff field types by 1
    def same(es):
        rtn = []
        for i in es:
            rtn.append((i,i))
        return rtn
    
    if(op1 == op_gradient):
        d1 = [(ty_scalarF_d1, ty_scalarF_d1)]
        d2 = [(ty_scalarF_d2, ty_vec2F_d2)]
        d3 =[(ty_scalarF_d3, ty_vec3F_d3)]
        return dek_ir( k_init, d1+d2+d3)
    elif(op1 == op_divergence):
        d2 = [(ty_vec2F_d2, ty_scalarF_d2)]
        d3 =[(ty_vec3F_d3, ty_scalarF_d3)]
        return dek_ir(k_init, d2+d3)
    elif(op1 == op_curl):
        d2 = [(ty_vec2F_d2, ty_scalarF_d2)]
        d3 =[(ty_vec3F_d3, ty_vec3F_d3)]
        return dek_ir(k_init, d2+d3)
    elif(op1 == op_jacob):
        d2 = [(ty_vec2F_d2, ty_mat2x2F_d2),(ty_mat2x2F_d2, ty_ten2x2x2F_d2)]
        d3 =[(ty_vec3F_d3, ty_mat3x3F_d3), (ty_mat3x3F_d3, ty_ten3x3x3F_d3)]
        return dek_ir(k_init, d2+d3)
    elif(op1==op_normalize):
        m =[]
        for i in l_all1:
            if(not (fty.is_Scalar(i))):
                m.append((i, i))
        return m
    elif((op1 ==op_norm)):
        m =[]
        for i in l_all1:
            y =  convert_rst_unary(i, ty_scalarT, i.dim)
            x=(i, y)
            m.append(x)
        return m

    elif((op1 == op_negation) or (op1==op_copy)):
        m =[]
        for i in l_all1:
            m.append((i, i))
        return m
    elif(op1==op_transpose):
        rtn = []
        n = [2,3,4]
        for ni in n:
            for nj in n:
                mij = nToshape([ni, nj])
                mji = nToshape([nj, ni])
                print "-----------------"
                print "mij: " ,mij.name," mji: ",mji.name
                ty1 = shape_to_fty(mij, k_init)
                ty2 = shape_to_fty(mji, k_init)
                for (i, j) in zip(ty1, ty2):
                    #print "rtn from tys i: ", i, " j: ", j
                    if((not (i==None)) and (not(j==None))):
                        x =(i,j)
                        rtn.append(x)
                        print "transpose",i.name,"==>", j.name
        return rtn
    elif((op1==op_trace)):
        d0 = [(ty_mat2x2FT, ty_scalarFT), (ty_mat3x3FT, ty_scalarFT), (ty_mat4x4FT, ty_scalarFT)]
        d1 = [(ty_mat2x2F_d1, ty_scalarF_d1), (ty_mat3x3F_d1, ty_scalarF_d1), (ty_mat4x4F_d1, ty_scalarF_d1)]
        d2 = [(ty_mat2x2F_d2, ty_scalarF_d2), (ty_mat3x3F_d2, ty_scalarF_d2), (ty_mat4x4F_d2, ty_scalarF_d2)]
        d3 = [(ty_mat2x2F_d3, ty_scalarF_d3), (ty_mat3x3F_d3, ty_scalarF_d3), (ty_mat4x4F_d3, ty_scalarF_d3)]
        return d0+d1+d2+d3
    elif((op1==op_det)):
        d0 = [(ty_mat2x2FT, ty_scalarFT), (ty_mat3x3FT, ty_scalarFT)]
        d1 = [(ty_mat2x2F_d1, ty_scalarF_d1), (ty_mat3x3F_d1, ty_scalarF_d1)]
        d2 = [(ty_mat2x2F_d2, ty_scalarF_d2), (ty_mat3x3F_d2, ty_scalarF_d2)]
        d3 = [(ty_mat2x2F_d3, ty_scalarF_d3), (ty_mat3x3F_d3, ty_scalarF_d3)]
        return d0+d1+d2+d3
    elif((op1==op_slicem0)):
        rtn = []
        n = [2,3,4]
        for ni in n:
            for nj in n:
                mij = nToshape([ni, nj])
                vj = nToshape([nj])
                ty1 = shape_to_fty(mij, k_init)
                ty2 = shape_to_fty(vj, k_init)
                for (i, j) in zip(ty1, ty2):
                    x = (i,j)
                    rtn.append(x)
        return rtn
    elif((op1==op_slicem1)):
        rtn = []
        n = [2,3,4]
        for ni in n:
            for nj in n:
                mij = nToshape([ni, nj])
                vj = nToshape([ni])
                ty1 = shape_to_fty(mij, k_init)
                ty2 = shape_to_fty(vj, k_init)
                for (i, j) in zip(ty1, ty2):
                    x = (i,j)
                    rtn.append(x)
        return rtn
    elif((op1==op_slicev0) or (op1==op_slicev1)):
        rtn = []
        n = [2,3,4]
        for ni in n:
            vi = nToshape([ni])
            s = ty_scalarT
            ty1 = shape_to_fty(vi, k_init)
            ty2 = shape_to_fty(s, k_init)
            for (i, j) in zip(ty1, ty2):
                x = (i,j)
                rtn.append(x)
        return rtn
    elif(op1==op_slicet0):
        rtn = []
        n = [2,3,4]
        for ni in n:
            for nj in n:
                for nk in n:
                    tijk = nToshape([ni, nj, nk])
                    mik = nToshape([ni,nk])
                    ty1 = shape_to_fty(tijk, k_init)
                    ty2 = shape_to_fty(mik, k_init)
                    for (i, j) in zip(ty1, ty2):
                        x = (i,j)
                        rtn.append(x)
        return rtn
    elif(op1==op_slicet1):
        rtn = []
        n = [2,3,4]
        for ni in n:
            for nj in n:
                for nk in n:
                    tijk = nToshape([ni, nj, nk])
                    mik = nToshape([ni,nk])
                    ty1 = shape_to_fty(tijk, k_init)
                    ty2 = shape_to_fty(mik, k_init)
                    for (i, j) in zip(ty1, ty2):
                        x = (i,j)
                        rtn.append(x)
        return rtn
    elif(op1==op_inverse):
        es = [ty_mat2x2FT, ty_mat3x3FT,ty_mat2x2F_d1,ty_mat3x3F_d1,ty_mat2x2F_d2,ty_mat3x3F_d2,ty_mat2x2F_d3,ty_mat3x3F_d3]
        return same(es)
    elif((op1==op_cosine) or (op1==op_sine) or (op1==op_tangent) or (op1==op_sqrt)):
        es = [ty_scalarFT, ty_scalarF_d1, ty_scalarF_d2, ty_scalarF_d3]
        return same(es)
    elif((op1==op_acosine) or (op1==op_asine) or (op1==op_atangent)):
        es = [ty_scalarFT, ty_scalarF_d1, ty_scalarF_d2, ty_scalarF_d3]
        return same(es)

    else:
        raise Exception ("op1:"+op1.name)

#given tshape, and arg1, what is arg2 (shape)
def backwards_op2_arg1(op1, tshape, arg1):
    # inner product operation
    print "op1:",op1.name, "tshape:", tshape.name, "arg1:",arg1.name
    tshape_shape = fty.get_shape(tshape)
    arg1_shape = fty.get_shape(arg1)
    if((op1  == op_add) or  (op1  == op_subtract) or (op1==op_modulate)):
        if(tshape.id==arg1.id):
            return  tshape
        else:
            return None
    elif(op1 == op_scale):
        if(fty.is_Scalar(arg1)):
            return tshape
        else:
            return ty_scalarT
    elif(op1==op_division):
        return  tshape
    elif(op1 == op_cross):
        if(fty.is_Vector(tshape) and fty.is_Vector(arg1)):
            [u] = fty.get_shape(tshape)
            [v] = fty.get_shape(arg1)
            if(u==v and u==2):
                return ty_scalarT
            elif(u==v and u==3):
                return ty_vec3T
            else:
                return None
        else:
            return None
    elif(op1  == op_inner):
        #(arg1, _) -> tshape
        if(fty.is_Vector(arg1)):
            [u] =  arg1_shape
            #[u]*[u...]-> [...]
            if(fty.is_Ten3(tshape)):
                return None
            else:
                return nToshape([u]+tshape_shape)
        elif(fty.is_Matrix(arg1)):
            [u, v] =  arg1_shape
            #[u,v]*[v...]-> [u...]
            if(fty.is_Scalar(tshape)):
                return None
            else:
                tu = tshape_shape[0]
                if(not(u==tu)):
                    return None
                else:
                    return nToshape([v]+tshape_shape[1:])
        elif(fty.is_Ten3(arg1)):
            [u, v, w] =  arg1_shape
            #[u,v, w]*[w...]-> [u v ...]
            if(fty.is_Scalar(tshape) or fty.is_Vector(tshape)):
                return None
            else:
                tu = tshape_shape[0]
                tv = tshape_shape[1]
                if(not(u == tu) and (not(v == tv))):
                    return None
                else:
                    return nToshape([w]+tshape_shape[2:])
        else:
            return None
    elif(op1 ==op_outer):
        if(fty.is_Matrix(tshape) and (fty.is_Vector(arg1))):
            [a] = arg1_shape
            [d, e] = tshape_shape
            if(a==d):
                return nToshape([e])
            else:
                return None
        elif(fty.is_Ten3(tshape)):
            [d, e, f] = tshape_shape
            if(fty.is_Vector(arg1)):
                [a] = arg1_shape
                if(a==d):
                    return nToshape([e,f])
                else:
                    return None
            elif(fty.is_Matrix(arg1)):
                [a, b] = arg1_shape
                if((a==d) and (b==e)):
                    return nToshape([f])
                else:
                    return None
            else:
                return None
        else:
            return None

    elif(op1  == op_doubledot):
        #(arg1, _) -> tshape
        if(fty.is_Matrix(arg1)):
            [u, v] =  arg1_shape
            #[u,v]*[u,v...]-> [...]
            if(fty.is_Scalar(tshape)):
                return arg1
            elif(fty.is_Vector(tshape)):
                #[u,v]*[u,v,w]
                tw = tshape_shape[0]
                return nToshape([u,v,tw])
            else:
                return None
        elif(fty.is_Ten3(arg1)):
            [u, v, w] =  arg1_shape
            if(fty.is_Scalar(tshape)):
                return None
            elif(fty.is_Vector(tshape)):
                tu = tshape_shape[0]
                #[u,v, w]*[v,w]-> [u]
                if(not(u == tu)):
                    return None
                return nToshape([v,w])
            elif(fty.is_Ten3(tshape)):
                tu = tshape_shape[0]
                tx = tshape_shape[1]
                #[u,v, w]*[v,w,x]-> [u,x]
                if(not(u == tu)):
                    return nToshape([v,w,tx])
            else:
                return None
        else:
            return None
    else:
        #print "not rightoperator"
        raise Exception ("op1:"+op1.name)

#given tshape, and arg1, what is arg2 (shape)
def backwards_op2_arg2(op1, tshape, arg2):
    # inner product operation
    print "op1:",op1.name, "tshape:", tshape.name, "arg2:",arg2.name
    arg2_shape = fty.get_shape(arg2)
    tshape_shape = fty.get_shape(tshape)
    if((op1  == op_add) or  (op1  == op_subtract) or (op1 == op_modulate)):
        return backwards_op2_arg1(op1, tshape, arg2)
    elif((op1 == op_scale) or (op1==op_cross)):
        return backwards_op2_arg1(op1, tshape, arg2)
    elif(op1==op_division):
        return ty_scalarT
    elif(op1 ==op_outer):
        if(fty.is_Matrix(tshape) and (fty.is_Vector(arg2))):
            [a] = arg2_shape
            [d, e] = tshape_shape
            if(a==e):
                return nToshape([d])
            else:
                return None
        elif(fty.is_Ten3(tshape)):
            [d, e, f] = tshape_shape
            if(fty.is_Vector(arg2)):
                [a] = arg2_shape
                if(a==f):
                    return nToshape([d, e])
                else:
                    return None
            elif(fty.is_Matrix(arg2)):
                [a, b] = arg2_shape
                if((a==e) and (b==f)):
                    return nToshape([d])
                else:
                    return None
            else:
                return None
        else:
            return None
    elif(op1  == op_inner):
        #(_, arg2) -> tshape
        if(fty.is_Vector(arg2)):
            #[...u]*[u]-> [...]
            [u] =  arg2_shape
            if(fty.is_Ten3(tshape)):
                return None
            else:
                return nToshape(tshape_shape+arg2_shape)
        elif(fty.is_Matrix(arg2)):
            [u, v] =  arg2_shape
            #[...u]*[u,v]-> [...v]
            if(fty.is_Scalar(tshape)):
                return None
            else:
                n = len(tshape_shape)-1
                t = tshape_shape[n]
                if(not(v == t)):
                    return None
                else:
                    return nToshape(tshape_shape[0:(n-1)]+[u])
        elif(fty.is_Ten3(arg2)):
            [u, v, w] =  arg2_shape
            #[...., u]*[u,v,w]-> [...,v,w]
            if(fty.is_Scalar(tshape) or fty.is_Vector(tshape)):
                return None
            else:
                n = len(tshape_shape)-1
                tw = tshape_shape[n]
                tv = tshape_shape[n-1]
                if((not(w==tw)) and (not(v==tv))):
                    return None
                else:
                    return nToshape(tshape_shape[0:(n-2)]+[u])
        else:
            return None

    elif(op1  == op_doubledot):
        #(arg1, _) -> tshape
        if(fty.is_Matrix(arg2)):
            [u, v] =  arg2_shape
            #[...u,v]*[u,v]-> [...]
            if(fty.is_Scalar(tshape)):
                return arg2
            elif(fty.is_Vector(tshape)):
                #[tw,u,v]*[u,v]->[tw]
                tw = tshape_shape[0]
                return nToshape([tw,u,v])
            else:
                return None
        elif(fty.is_Ten3(arg2)):
            [u, v, w] =  arg2_shape
            if(fty.is_Scalar(tshape)):
                return None
            elif(fty.is_Vector(tshape)):
                tw = tshape_shape[0]
                #[..,v, w]*[u,v,w]-> [u]
                if(not(w == tw)):
                    return None
                return nToshape([u,v])
            elif(fty.is_Ten3(tshape)):
                ta = tshape_shape[0]
                tw = tshape_shape[1]
                #[-,u,v]*[u, v,w]-> [ta,tw]
                if(not(w == tw)):
                    return nToshape([ta,u,v])
            else:
                return None
        else:
            return None


    else:
        #print "not rightoperator"
        raise Exception ("op1:"+op1.name)