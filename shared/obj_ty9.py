# -*- coding: utf-8 -*-

from __future__ import unicode_literals
#from set import *
# constants
nonefield_k =  -1
nonefield_dim =  0
k_init = 2 #null k

#tensor types
class tty:
    def __init__(self, id, name, shape):
        self.id = id
        self.name = "ttt"+name
        self.shape = shape
    def toStr(self):
        return ("tensor"+str(self.name))
    def isEq_id(a,b):
        return (a.id == b.id)
    def psize(self):
        p =  1
        for i in self.shape:
            p =  p*i
        print self.name+"psize", p 
        return p
    def isSca(self):
        s =  self.shape
        n =  len(s)
        if(n == 0):
            return True
        else:
            return False
    def isVec(self):
        s =  self.shape
        n =  len(s)
        if(n == 1):
            return True
        else:
            return False
    def isMat(self):
        s =  self.shape
        n =  len(s)
        if(n == 2):
            return True
        else:
            return False
    def isTen3(self):
        s =  self.shape
        n =  len(s)
        if(n == 3):
            return True
        else:
            return False
    def tyToStr(self):
        s =  self.shape
        n =  len(s)
        if(n == 0):
            return "s"
        elif(n == 1):
            [v] =  s
            return "v"+str(v)
        elif(n == 2):
            [v,m] =  s
            return "m"+str(v)+"x"+str(m)
        elif(n == 3):
            [v,m,l] =  s
            return "t"+str(v)+"x"+str(m)+"x"+str(l)
        return "t"


# field types
class fty:
    def __init__(self, id, name, dim, shape, tensorType, k):
        self.id = id
        self.name = name#+"_k"+str(k)
        self.dim = dim
        self.shape = shape
        self.tensorType = tensorType # if we probed a field with this field type
        self.k = k
    def toStr(self):
        if(self.dim == nonefield_dim):
            return "tensor "
        else:
            return ("field #"+str(self.k)+"("+str(self.dim)+")"+str(self.shape))
    def get_tensorType(self):
        return self.tensorType
    def get_dim(self):
        return self.dim
    # get vector length
    def get_shape(ty0):
        return  ty0.shape
    def get_vecLength(ty0):
        shape =  ty0.shape
        if  (len(shape) == 1):
            return shape[0] # vector length
        else:
            raise "unsupported get_vecLength types"
    def is_Field(self):
        return  (not (self.dim == nonefield_dim))
    def is_Tensor(self):
        return  (self.dim == nonefield_dim)
    def is_ScalarField(self):
        return  ((len(self.shape) == 0) and fty.is_Field(self))
    def is_VectorField(self):
        return  ((len(self.shape) == 1) and fty.is_Field(self))
    def is_MatrixField(self):
        return  ((len(self.shape) == 2) and fty.is_Field(self))
    def is_Scalar(self):
        return  (len(self.shape) == 0)
    def is_Vector(self):
        return  (len(self.shape) == 1)
    def is_Matrix(self):
        return  (len(self.shape) == 2)
    def is_Ten3(self):
        return  (len(self.shape) == 3)
    def get_first_ix(self):
        return  self.shape[0]
    def get_last_ix(self):
        return  self.shape[len(self.shape)-1]
    def drop_first(self):
        rtn =  []
        for i in range(len(self.shape)-1):
            rtn.append(self.shape[i])
        return rtn
    def drop_last(self):
        rtn =  []
        for i in range(len(self.shape)-1):
            rtn.append(self.shape[i+1])
        return rtn
    #compares finfo with fty constant
    def isEq_id(a,b):
        return (a.id == b.id)
    #string for diderot program
    def toDiderot(self):
        if(self.dim == 0):
            return "tensor "+str(self.shape)
        else:
            return "field#"+str(self.k)+"("+str(self.dim)+")"+str(self.shape)
    #creates ty object
    def convertTy(const,k):
        return  fty(const.id,const.name, const.dim, const.shape, const.tensorType, k)
    def convertToTensor(self):
        return fty(200, "T", nonefield_dim, self.shape, self.tensorType, None)
#------------------------------ make tty function  -----------------------------------------------------
# shorthand used to refer to different types
# the helper functions match shorthand to other properties and creates ty object
def shapeToStr(s):
    n =  len(s)
    if(n == 0):
        return "s"
    elif(n == 1):
        [v] =  s
        return "v"+str(v)
    elif(n == 2):
        [v,m] =  s
        return "m"+str(v)+"x"+str(m)
    elif(n == 3):
        [v,m,l] =  s
        return "t"+str(v)+"x"+str(m)+"x"+str(l)
    return "t"
def mkTensor(id, shape):
    name =  "t_"+shapeToStr(shape)
    return tty(id, name, shape)
#----------------- initializes mkTensor() and creates tty -----------------
# define possible tensor types
#[ty_scalarT, ty_vec2T, ty_vec3T, ty_vec4T]
# vector types
def mkVecT(id):
    ty_scalarT =  mkTensor(id, [])
    ty_vec2T =  mkTensor(id+1, [2])
    ty_vec3T =  mkTensor(id+2, [3])
    ty_vec4T =  mkTensor(id+3, [4])
    return [ty_scalarT, ty_vec2T, ty_vec3T, ty_vec4T]
#matrices
#[ty_mat2x2T,ty_mat2x3T,ty_mat2x4T,ty_mat3x2T,ty_mat3x3T,ty_mat3x4T,ty_mat4x2T,ty_mat4x3T,ty_mat4x4T]
def mkMatT():
    rtn =  []
    for i in range(3):
        for j in range(3):
            i =  i+2
            j =  j+2
            id =  i*10+j
            rtn.append(mkTensor(id, [i,j]))
    return rtn
# second-order tensor types leading with n
def mkTenT(n):
    rtn =  []
    for i in range(3):
        for j in range(3):
            i =  i+2
            j =  j+2
            id =  n*100+i*10+j
            rtn.append(mkTensor(id, [n,i,j]))
    return rtn
#tensors
id = 0
tvs =  mkVecT(id)
tms =  mkMatT()
tt2 =  mkTenT(2)
tt3 =  mkTenT(3)
tt4 =  mkTenT(4)
[ty_scalarT, ty_vec2T, ty_vec3T, ty_vec4T] =  tvs
[ty_mat2x2T, ty_mat2x3T,ty_mat2x4T,ty_mat3x2T,ty_mat3x3T,ty_mat3x4T,ty_mat4x2T,ty_mat4x3T,ty_mat4x4T] =  tms
[ty_ten2x2x2T, ty_ten2x2x3T,ty_ten2x2x4T, ty_ten2x3x2T,ty_ten2x3x3T, ty_ten2x3x4T,ty_ten2x4x2T,ty_ten2x4x3T,ty_ten2x4x4T] =  tt2
[ty_ten3x2x2T, ty_ten3x2x3T,ty_ten3x2x4T, ty_ten3x3x2T,ty_ten3x3x3T, ty_ten3x3x4T,ty_ten3x4x2T,ty_ten3x4x3T,ty_ten3x4x4T] = tt3
[ty_ten4x2x2T, ty_ten4x2x3T,ty_ten4x2x4T, ty_ten4x3x2T,ty_ten4x3x3T, ty_ten4x3x4T,ty_ten4x4x2T,ty_ten4x4x3T,ty_ten4x4x4T] = tt4
tms_sym = [ty_mat2x2T, ty_mat3x3T,ty_mat4x4T]
standard_tyT =  tvs+ tms
#------------------------------ make fldty function  -----------------------------------------------------
#----------------- field helper functions -----------------
# distinctive features of lifted tensors or NoneFields
# are dim = 0 and k = -1
def mkNoneField(id, _, outputtensor):
    shape =  outputtensor.shape
    name =  "T_"+shapeToStr(shape)
    return fty(id, name,nonefield_dim, shape, outputtensor, nonefield_k)
#fields:  #id,name, dim, shape in string form,probe field type returns tensor type
def mkField(id, dim, outputtensor):
    #print "id",str(id)
    name =  "F_"+shapeToStr(outputtensor.shape)+"_d"+str(dim)
    return fty(id, name, dim, outputtensor.shape, outputtensor, k_init)
# define possible tensor types
# vector types
def mkVecF(f, id, dim):
    ty_scalarF =  f(id, dim, ty_scalarT)
    ty_vec2F =  f(id+1, dim, ty_vec2T)
    ty_vec3F =  f(id+2, dim, ty_vec3T)
    ty_vec4F =  f(id+3, dim, ty_vec4T)
    return [ty_scalarF, ty_vec2F, ty_vec3F, ty_vec4F]
# matrix types
def mkMatF(f, id, dim):
    id +=  10
    ty_mat2x2F =  f(id, dim, ty_mat2x2T)
    ty_mat2x3F =  f(id+1, dim, ty_mat2x3T)
    ty_mat2x4F =  f(id+2, dim, ty_mat2x4T)
    ty_mat3x2F =  f(id+3, dim, ty_mat3x2T)
    ty_mat3x3F =  f(id+4, dim, ty_mat3x3T)
    ty_mat3x4F =  f(id+5, dim, ty_mat3x4T)
    ty_mat4x2F =  f(id+6, dim, ty_mat4x2T)
    ty_mat4x3F =  f(id+7, dim, ty_mat4x3T)
    ty_mat4x4F =  f(id+8, dim, ty_mat4x4T)
    return [ty_mat2x2F,ty_mat2x3F,ty_mat2x4F,ty_mat3x2F,ty_mat3x3F,ty_mat3x4F,ty_mat4x2F,ty_mat4x3F,ty_mat4x4F]
# second-order tensor types leading 2
def mkTen2F(f, id, dim):
    id +=  25
    ty_ten2x2x2F =  f(id, dim, ty_ten2x2x2T)
    ty_ten2x2x3F =  f(id+1, dim, ty_ten2x2x3T)
    ty_ten2x2x4F =  f(id+2, dim, ty_ten2x2x4T)
    ty_ten2x3x2F =  f(id+3, dim, ty_ten2x3x2T)
    ty_ten2x3x3F =  f(id+4, dim, ty_ten2x3x3T)
    ty_ten2x3x4F =  f(id+5, dim, ty_ten2x3x4T)
    ty_ten2x4x2F =  f(id+6, dim, ty_ten2x4x2T)
    ty_ten2x4x3F =  f(id+7, dim, ty_ten2x4x3T)
    ty_ten2x4x4F =  f(id+8, dim, ty_ten2x4x4T)
    return [ty_ten2x2x2F, ty_ten2x2x3F, ty_ten2x2x4F,  ty_ten2x3x2F, ty_ten2x3x3F,  ty_ten2x3x4F, ty_ten2x4x2F, ty_ten2x4x3F, ty_ten2x4x4F]
# second-order tensor types leading 3
def mkTen3F(f, id, dim):
    id +=  50
    ty_ten3x2x2F =  f(id, dim, ty_ten3x2x2T)
    ty_ten3x2x3F =  f(id+1, dim, ty_ten3x2x3T)
    ty_ten3x2x4F =  f(id+2, dim, ty_ten3x2x4T)
    ty_ten3x3x2F =  f(id+3, dim, ty_ten3x3x2T)
    ty_ten3x3x3F =  f(id+4, dim, ty_ten3x3x3T)
    ty_ten3x3x4F =  f(id+5, dim, ty_ten3x3x4T)
    ty_ten3x4x2F =  f(id+6, dim, ty_ten3x4x2T)
    ty_ten3x4x3F =  f(id+7, dim, ty_ten3x4x3T)
    ty_ten3x4x4F =  f(id+8, dim, ty_ten3x4x4T)
    return [ty_ten3x2x2F, ty_ten3x2x3F, ty_ten3x2x4F,  ty_ten3x3x2F, ty_ten3x3x3F,  ty_ten3x3x4F, ty_ten3x4x2F, ty_ten3x4x3F, ty_ten3x4x4F]
# second-order tensor types leading 4
def mkTen4F(f, id, dim):
    id += 75
    ty_ten4x2x2F =  f(id, dim, ty_ten4x2x2T)
    ty_ten4x2x3F =  f(id+1, dim, ty_ten4x2x3T)
    ty_ten4x2x4F =  f(id+2, dim, ty_ten4x2x4T)
    ty_ten4x3x2F =  f(id+3, dim, ty_ten4x3x2T)
    ty_ten4x3x3F =  f(id+4, dim, ty_ten4x3x3T)
    ty_ten4x3x4F =  f(id+5, dim, ty_ten4x3x4T)
    ty_ten4x4x2F =  f(id+6, dim, ty_ten4x4x2T)
    ty_ten4x4x3F =  f(id+7, dim, ty_ten4x4x3T)
    ty_ten4x4x4F =  f(id+8, dim, ty_ten4x4x4T)
    return [ty_ten4x2x2F, ty_ten4x2x3F, ty_ten4x2x4F,  ty_ten4x3x2F, ty_ten4x3x3F,  ty_ten4x3x4F, ty_ten4x4x2F, ty_ten4x4x3F, ty_ten4x4x4F]

#----------------- constant field types -----------------
#lift tensor to field level
id =  0
dim =  0
vecFT =   mkVecF(mkNoneField, id, dim)
matFT =  mkMatF(mkNoneField, id, dim)
ten2FT =  mkTen2F(mkNoneField, id, dim)
ten3FT =  mkTen3F(mkNoneField, id, dim)
ten4FT =  mkTen4F(mkNoneField, id, dim)
[ty_scalarFT, ty_vec2FT, ty_vec3FT, ty_vec4FT] =  vecFT
[ty_mat2x2FT, ty_mat2x3FT,ty_mat2x4FT,ty_mat3x2FT,ty_mat3x3FT,ty_mat3x4FT,ty_mat4x2FT,ty_mat4x3FT,ty_mat4x4FT] =  matFT
[ty_ten2x2x2FT,  ty_ten2x2x3FT, ty_ten2x2x4FT,  ty_ten2x3x2FT, ty_ten2x3x3FT,  ty_ten2x3x4FT, ty_ten2x4x2FT, ty_ten2x4x3FT, ty_ten2x4x4FT] =  ten2FT
[ty_ten3x2x2FT,  ty_ten3x2x3FT, ty_ten3x2x4FT,  ty_ten3x3x2FT, ty_ten3x3x3FT,  ty_ten3x3x4FT, ty_ten3x4x2FT, ty_ten3x4x3FT, ty_ten3x4x4FT] =  ten3FT
[ty_ten4x2x2FT,  ty_ten4x2x3FT, ty_ten4x2x4FT,  ty_ten4x3x2FT, ty_ten4x3x3FT,  ty_ten4x3x4FT, ty_ten4x4x2FT, ty_ten4x4x3FT, ty_ten4x4x4FT] =  ten4FT
#dimension 1
id =  100
dim =  1
vecd1 =   mkVecF(mkField, id, dim)
matd1 =  mkMatF( mkField, id, dim)
ten2d1 =  mkTen2F(mkField, id, dim)
ten3d1 =  mkTen3F(mkField, id, dim)
ten4d1 =  mkTen4F(mkField, id, dim)
fld1 =  vecd1+matd1+ten2d1+ten3d1+ten4d1
[ty_scalarF_d1, ty_vec2F_d1, ty_vec3F_d1, ty_vec4F_d1] =   vecd1
[ty_mat2x2F_d1, ty_mat2x3F_d1,ty_mat2x4F_d1,ty_mat3x2F_d1,ty_mat3x3F_d1,ty_mat3x4F_d1,ty_mat4x2F_d1,ty_mat4x3F_d1,ty_mat4x4F_d1] =  matd1
[ty_ten2x2x2F_d1,  ty_ten2x2x3F_d1, ty_ten2x2x4F_d1,  ty_ten2x3x2F_d1, ty_ten2x3x3F_d1,  ty_ten2x3x4F_d1, ty_ten2x4x2F_d1, ty_ten2x4x3F_d1, ty_ten2x4x4F_d1] =  ten2d1
[ty_ten3x2x2F_d1,  ty_ten3x2x3F_d1, ty_ten3x2x4F_d1,  ty_ten3x3x2F_d1, ty_ten3x3x3F_d1,  ty_ten3x3x4F_d1, ty_ten3x4x2F_d1, ty_ten3x4x3F_d1, ty_ten3x4x4F_d1] =  ten3d1
[ty_ten4x2x2F_d1,  ty_ten4x2x3F_d1, ty_ten4x2x4F_d1,  ty_ten4x3x2F_d1, ty_ten4x3x3F_d1,  ty_ten4x3x4F_d1, ty_ten4x4x2F_d1, ty_ten4x4x3F_d1, ty_ten4x4x4F_d1] =  ten4d1
#dimension 2
id =  200
dim =  2
vecd2 =   mkVecF(mkField, id, dim)
matd2 =  mkMatF( mkField, id, dim)
ten2d2 =  mkTen2F(mkField, id, dim)
ten3d2 =  mkTen3F(mkField, id, dim)
ten4d2 =  mkTen4F(mkField, id, dim)
[ty_scalarF_d2, ty_vec2F_d2, ty_vec3F_d2, ty_vec4F_d2] =  vecd2
[ty_mat2x2F_d2, ty_mat2x3F_d2,ty_mat2x4F_d2,ty_mat3x2F_d2,ty_mat3x3F_d2,ty_mat3x4F_d2,ty_mat4x2F_d2,ty_mat4x3F_d2,ty_mat4x4F_d2] =  matd2
[ty_ten2x2x2F_d2,  ty_ten2x2x3F_d2, ty_ten2x2x4F_d2,  ty_ten2x3x2F_d2, ty_ten2x3x3F_d2,  ty_ten2x3x4F_d2, ty_ten2x4x2F_d2, ty_ten2x4x3F_d2, ty_ten2x4x4F_d2] =  ten2d2
[ty_ten3x2x2F_d2,  ty_ten3x2x3F_d2, ty_ten3x2x4F_d2,  ty_ten3x3x2F_d2, ty_ten3x3x3F_d2,  ty_ten3x3x4F_d2, ty_ten3x4x2F_d2, ty_ten3x4x3F_d2, ty_ten3x4x4F_d2] =  ten3d2
[ty_ten4x2x2F_d2,  ty_ten4x2x3F_d2, ty_ten4x2x4F_d2,  ty_ten4x3x2F_d2, ty_ten4x3x3F_d2,  ty_ten4x3x4F_d2, ty_ten4x4x2F_d2, ty_ten4x4x3F_d2, ty_ten4x4x4F_d2] =  ten4d2
fld2 =  vecd2+matd2+ten2d2+ten3d2+ten4d2
#dimension 3
id =  300
dim =  3
[ty_scalarF_d3, ty_vec2F_d3, ty_vec3F_d3, ty_vec4F_d3] =   mkVecF(mkField, id, dim)
(ty_mat2x2F_d3, ty_mat2x3F_d3,ty_mat2x4F_d3,ty_mat3x2F_d3,ty_mat3x3F_d3,ty_mat3x4F_d3,ty_mat4x2F_d3,ty_mat4x3F_d3,ty_mat4x4F_d3) =  mkMatF( mkField, id, dim)
[ty_ten2x2x2F_d3,  ty_ten2x2x3F_d3, ty_ten2x2x4F_d3,  ty_ten2x3x2F_d3, ty_ten2x3x3F_d3,  ty_ten2x3x4F_d3, ty_ten2x4x2F_d3, ty_ten2x4x3F_d3, ty_ten2x4x4F_d3] =  mkTen2F(mkField, id, dim)
[ty_ten3x2x2F_d3,  ty_ten3x2x3F_d3, ty_ten3x2x4F_d3,  ty_ten3x3x2F_d3, ty_ten3x3x3F_d3,  ty_ten3x3x4F_d3, ty_ten3x4x2F_d3, ty_ten3x4x3F_d3, ty_ten3x4x4F_d3] =  mkTen3F(mkField, id, dim)
[ty_ten4x2x2F_d3,  ty_ten4x2x3F_d3, ty_ten4x2x4F_d3,  ty_ten4x3x2F_d3, ty_ten4x3x3F_d3,  ty_ten4x3x4F_d3, ty_ten4x4x2F_d3, ty_ten4x4x3F_d3, ty_ten4x4x4F_d3] =  mkTen4F(mkField, id, dim)

# fields that can be synthesized with template
l_all_d1F =  [ty_scalarF_d1, ty_vec2F_d1, ty_vec3F_d1, ty_vec4F_d1, ty_mat2x2F_d1, ty_mat3x3F_d1]
l_all_d2F =  [ty_scalarF_d2, ty_vec2F_d2, ty_vec3F_d2, ty_vec4F_d2, ty_mat2x2F_d2, ty_mat3x3F_d2]
l_all_d3F =  [ty_scalarF_d3, ty_vec2F_d3, ty_vec3F_d3, ty_vec4F_d3, ty_mat2x2F_d3, ty_mat3x3F_d3]
l_all_F1 =   l_all_d1F +l_all_d2F +l_all_d3F
#tensors that can be created
l_all_T1 =  vecFT+matFT+ten2FT+ten3FT+ten4FT
# currentl adjusted for specific types 
l_all_T1 =  vecFT+[ty_mat2x2FT,ty_mat3x3FT]
#l_all_F1 =   [ty_vec2F_d1, ty_mat2x2F_d1,ty_vec2F_d2, ty_mat2x2F_d2, ty_vec2F_d3, ty_mat2x2F_d3]
l_all1 =   l_all_T1+l_all_F1
#print " l_all_T1: ",len(l_all_T1)," l_all_F1: ",len(l_all_F1)," l_all1: ",len(l_all1)


#---------------------- gets types in the list of a certain type  ----------------------
#used mostly by examples object
def get_scaF(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Scalar(f)):
            rtn.append(f)
    return rtn
#list of vector fields
def get_vecF(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Vector(f)):
            rtn.append(f)
    return rtn
#list of vector fields
def get_vec_3(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Vector(f)):
            [n] =f.shape
            if(n==3):
                rtn.append(f)
    return rtn
#list of vector fields (d)=n.
def get_vecF_samedim(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Vector(f)):
            [n] =f.shape
            if(f.dim== n):
                rtn.append(f)
    return rtn
#list of vector fields (d)=n.
def get_vecF_matF(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Vector(f) or fty.is_Matrix(f)):
            rtn.append(f)
    return rtn
#list of matrix fields
def get_matF(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Matrix(f)):
            rtn.append(f)
    #print "ty", f.name
    return rtn
#list of matrix fields
def get_mat_symmal(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Matrix(f)):
            [n, m] = f.shape
            if(n==m):
                rtn.append(f)
    return rtn
#list of matrix fields
def get_mat_symmal_22(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Matrix(f)):
            [n, m] = f.shape
            if(n==2 and m==2):
                rtn.append(f)
    return rtn
#list of matrix fields
def get_Ten3(es):
    rtn = []
    # binary operator
    for f in es:
        if(fty.is_Ten3(f)):
            rtn.append(f)
    return rtn
#---------------------- checks dimensions  ----------------------
# check equal dim
def check_dim(fld,b):
    if(fty.is_Field(b)):
        return (fld.dim==b.dim)
    return true
#binary operator so two args
def find_field(ty1, ty2):
    dim1=ty1.dim
    dim2=ty2.dim
    if (dim1==0): # tensors
        return (True , ty2)
    elif(dim2==0):# tensors
        return  (True , ty1)
    elif(dim1==dim2):
        return  (True , ty1)
    else :
        return (False, None)
#---------------------- match shape to tty type----------------------
def err():
    raise Exception( ("unsupported shapeout "+ str(shapeout)))
def nToshape(shapeout):
    n = len(shapeout)
    def check(i):
        if((i<2) or (i>4)):
            err()
        return
    if (n==0):
        return ( ty_scalarT)
    elif(n==1):
        [i] =shapeout
        check(i)
        return mkTensor(i, shapeout)
    elif(n==2):
        [i, j] =shapeout
        check(i)
        check(j)
        id = i*10+j
        return  mkTensor(id, shapeout)
    elif(n==3):
        [i, j,k] =shapeout
        check(i)
        check(j)
        check(k)
        id = i*100+j*10+k
        return  mkTensor(id, shapeout)
    else:
        return err()

#shape to type
#shape to type
def shapeToTyhelper2(shapeout, dim):
    #print "got dim",dim
    if (dim==nonefield_dim):
        if (shapeout==[]):
            return (True, ty_scalarFT)
        elif (shapeout==[2]):
            return  (True,  ty_vec2FT)
        elif (shapeout==[3]):
            return  (True,  ty_vec3FT)
        elif (shapeout==[4]):
            return  (True,  ty_vec4FT)
        elif(shapeout==[2,2]):
            return (True, ty_mat2x2FT)
        elif(shapeout==[2,3]):
            return (True, ty_mat2x3FT)
        elif(shapeout==[2,4]):
            return (True, ty_mat2x4FT)
        elif(shapeout==[3,2]):
            return (True, ty_mat3x2FT)
        elif(shapeout==[3,3]):
            return (True, ty_mat3x3FT)
        elif(shapeout==[3,4]):
            return (True, ty_mat3x4FT)
        elif(shapeout==[4,2]):
            return (True, ty_mat4x2FT)
        elif(shapeout==[4,3]):
            return (True, ty_mat4x3FT)
        elif(shapeout==[4,4]):
            return (True, ty_mat4x4FT)
        elif (shapeout==[2, 2,2]):
            return (True, ty_ten2x2x2FT)
        elif(shapeout==[2, 2, 3]):
            return (True, ty_ten2x2x3FT)
        elif(shapeout==[2, 2, 4]):
            return (True, ty_ten2x2x4FT)
        elif (shapeout==[2, 3,2]):
            return (True, ty_ten2x3x2FT)
        elif(shapeout==[2, 3, 3]):
            return (True, ty_ten2x3x3FT)
        elif(shapeout==[2, 3, 4]):
            return (True, ty_ten2x3x4FT)
        elif (shapeout==[2, 4,2]):
            return (True, ty_ten2x4x2FT)
        elif(shapeout==[2, 4, 3]):
            return (True, ty_ten2x4x3FT)
        elif(shapeout==[2, 4, 4]):
            return (True, ty_ten2x4x4FT)
        elif (shapeout==[3, 2,2]):
            return (True, ty_ten3x2x2FT)
        elif(shapeout==[3, 2, 3]):
            return (True, ty_ten3x2x3FT)
        elif(shapeout==[3, 2, 4]):
            return (True, ty_ten3x2x4FT)
        elif (shapeout==[3, 3,2]):
            return (True, ty_ten3x3x2FT)
        elif(shapeout==[3, 3, 3]):
            return (True, ty_ten3x3x3FT)
        elif(shapeout==[3, 3, 4]):
            return (True, ty_ten3x3x4FT)
        elif (shapeout==[3, 4,2]):
            return (True, ty_ten3x4x2FT)
        elif(shapeout==[3, 4, 3]):
            return (True, ty_ten3x4x3FT)
        elif(shapeout==[3, 4, 4]):
            return (True, ty_ten3x4x4FT)
        elif (shapeout==[4, 2,2]):
            return (True, ty_ten4x2x2FT)
        elif(shapeout==[4, 2, 3]):
            return (True, ty_ten4x2x3FT)
        elif(shapeout==[4, 2, 4]):
            return (True, ty_ten4x2x4FT)
        elif (shapeout==[4, 3,2]):
            return (True, ty_ten4x3x2FT)
        elif(shapeout==[4, 3, 3]):
            return (True, ty_ten4x3x3FT)
        elif(shapeout==[4, 3, 4]):
            return (True, ty_ten4x3x4FT)
        elif (shapeout==[4, 4,2]):
            return (True, ty_ten4x4x2FT)
        elif(shapeout==[4, 4, 3]):
            return (True, ty_ten4x4x3FT)
        elif(shapeout==[4, 4, 4]):
            return (True, ty_ten4x4x4FT)
        else:
            #print "shapeout",shapeout,"dim", dim
            return (False, ("unsupported shapeout dim-1 "+ str(shapeout)))
    elif (dim==1):
        if (shapeout==[]):
            return (True, ty_scalarF_d1)
        elif (shapeout==[2]):
            return  (True,  ty_vec2F_d1)
        elif (shapeout==[3]):
            return  (True,  ty_vec3F_d1)
        elif (shapeout==[4]):
            return  (True,  ty_vec4F_d1)
        elif(shapeout==[2,2]):
            return (True, ty_mat2x2F_d1)
        elif(shapeout==[2,3]):
            return (True, ty_mat2x3F_d1)
        elif(shapeout==[2,4]):
            return (True, ty_mat2x4F_d1)
        elif(shapeout==[3,2]):
            return (True, ty_mat3x2F_d1)
        elif(shapeout==[3,3]):
            return (True, ty_mat3x3F_d1)
        elif(shapeout==[3,4]):
            return (True, ty_mat3x4F_d1)
        elif(shapeout==[4,2]):
            return (True, ty_mat4x2F_d1)
        elif(shapeout==[4,3]):
            return (True, ty_mat4x3F_d1)
        elif(shapeout==[4,4]):
            return (True, ty_mat4x4F_d1)
        elif (shapeout==[2, 2,2]):
            return (True, ty_ten2x2x2F_d1)
        elif(shapeout==[2, 2, 3]):
            return (True, ty_ten2x2x3F_d1)
        elif(shapeout==[2, 2, 4]):
            return (True, ty_ten2x2x4F_d1)
        elif (shapeout==[2, 3,2]):
            return (True, ty_ten2x3x2F_d1)
        elif(shapeout==[2, 3, 3]):
            return (True, ty_ten2x3x3F_d1)
        elif(shapeout==[2, 3, 4]):
            return (True, ty_ten2x3x4F_d1)
        elif (shapeout==[2, 4,2]):
            return (True, ty_ten2x4x2F_d1)
        elif(shapeout==[2, 4, 3]):
            return (True, ty_ten2x4x3F_d1)
        elif(shapeout==[2, 4, 4]):
            return (True, ty_ten2x4x4F_d1)
        elif (shapeout==[3, 2,2]):
            return (True, ty_ten3x2x2F_d1)
        elif(shapeout==[3, 2, 3]):
            return (True, ty_ten3x2x3F_d1)
        elif(shapeout==[3, 2, 4]):
            return (True, ty_ten3x2x4F_d1)
        elif (shapeout==[3, 3,2]):
            return (True, ty_ten3x3x2F_d1)
        elif(shapeout==[3, 3, 3]):
            return (True, ty_ten3x3x3F_d1)
        elif(shapeout==[3, 3, 4]):
            return (True, ty_ten3x3x4F_d1)
        elif (shapeout==[3, 4,2]):
            return (True, ty_ten3x4x2F_d1)
        elif(shapeout==[3, 4, 3]):
            return (True, ty_ten3x4x3F_d1)
        elif(shapeout==[3, 4, 4]):
            return (True, ty_ten3x4x4F_d1)
        elif (shapeout==[4, 2,2]):
            return (True, ty_ten4x2x2F_d1)
        elif(shapeout==[4, 2, 3]):
            return (True, ty_ten4x2x3F_d1)
        elif(shapeout==[4, 2, 4]):
            return (True, ty_ten4x2x4F_d1)
        elif (shapeout==[4, 3,2]):
            return (True, ty_ten4x3x2F_d1)
        elif(shapeout==[4, 3, 3]):
            return (True, ty_ten4x3x3F_d1)
        elif(shapeout==[4, 3, 4]):
            return (True, ty_ten4x3x4F_d1)
        elif (shapeout==[4, 4,2]):
            return (True, ty_ten4x4x2F_d1)
        elif(shapeout==[4, 4, 3]):
            return (True, ty_ten4x4x3F_d1)
        elif(shapeout==[4, 4, 4]):
            return (True, ty_ten4x4x4F_d1)
        else:
            #print "shapeout",shapeout,"dim", dim
            return (False, ("unsupported shapeout dim-1 "+ str(shapeout)))
    elif (dim==2):
        if (shapeout==[]):
            return (True, ty_scalarF_d2)
        elif (shapeout==[2]):
            return  (True,  ty_vec2F_d2)
        elif (shapeout==[3]):
            return  (True,  ty_vec3F_d2)
        elif (shapeout==[4]):
            return  (True,  ty_vec4F_d2)
        elif(shapeout==[2,2]):
            return (True, ty_mat2x2F_d2)
        elif(shapeout==[2,3]):
            return (True, ty_mat2x3F_d2)
        elif(shapeout==[2,4]):
            return (True, ty_mat2x4F_d2)
        elif(shapeout==[3,2]):
            return (True, ty_mat3x2F_d2)
        elif(shapeout==[3,3]):
            return (True, ty_mat3x3F_d2)
        elif(shapeout==[3,4]):
            return (True, ty_mat3x4F_d2)
        elif(shapeout==[4,2]):
            return (True, ty_mat4x2F_d2)
        elif(shapeout==[4,3]):
            return (True, ty_mat4x3F_d2)
        elif(shapeout==[4,4]):
            return (True, ty_mat4x4F_d2)
        elif (shapeout==[2, 2,2]):
            return (True, ty_ten2x2x2F_d2)
        elif(shapeout==[2, 2, 3]):
            return (True, ty_ten2x2x3F_d2)
        elif(shapeout==[2, 2, 4]):
            return (True, ty_ten2x2x4F_d2)
        elif (shapeout==[2, 3,2]):
            return (True, ty_ten2x3x2F_d2)
        elif(shapeout==[2, 3, 3]):
            return (True, ty_ten2x3x3F_d2)
        elif(shapeout==[2, 3, 4]):
            return (True, ty_ten2x3x4F_d2)
        elif (shapeout==[2, 4,2]):
            return (True, ty_ten2x4x2F_d2)
        elif(shapeout==[2, 4, 3]):
            return (True, ty_ten2x4x3F_d2)
        elif(shapeout==[2, 4, 4]):
            return (True, ty_ten2x4x4F_d2)
        elif (shapeout==[3, 2,2]):
            return (True, ty_ten3x2x2F_d2)
        elif(shapeout==[3, 2, 3]):
            return (True, ty_ten3x2x3F_d2)
        elif(shapeout==[3, 2, 4]):
            return (True, ty_ten3x2x4F_d2)
        elif (shapeout==[3, 3,2]):
            return (True, ty_ten3x3x2F_d2)
        elif(shapeout==[3, 3, 3]):
            return (True, ty_ten3x3x3F_d2)
        elif(shapeout==[3, 3, 4]):
            return (True, ty_ten3x3x4F_d2)
        elif (shapeout==[3, 4,2]):
            return (True, ty_ten3x4x2F_d2)
        elif(shapeout==[3, 4, 3]):
            return (True, ty_ten3x4x3F_d2)
        elif(shapeout==[3, 4, 4]):
            return (True, ty_ten3x4x4F_d2)
        elif (shapeout==[4, 2,2]):
            return (True, ty_ten4x2x2F_d2)
        elif(shapeout==[4, 2, 3]):
            return (True, ty_ten4x2x3F_d2)
        elif(shapeout==[4, 2, 4]):
            return (True, ty_ten4x2x4F_d2)
        elif (shapeout==[4, 3,2]):
            return (True, ty_ten4x3x2F_d2)
        elif(shapeout==[4, 3, 3]):
            return (True, ty_ten4x3x3F_d2)
        elif(shapeout==[4, 3, 4]):
            return (True, ty_ten4x3x4F_d2)
        elif (shapeout==[4, 4,2]):
            return (True, ty_ten4x4x2F_d2)
        elif(shapeout==[4, 4, 3]):
            return (True, ty_ten4x4x3F_d2)
        elif(shapeout==[4, 4, 4]):
            return (True, ty_ten4x4x4F_d2)
        else:
            #print "shapeout",shapeout,"dim", dim
            return(False, "unsupported shapeout dim-2 "+str(shapeout))
    elif (dim==3):
        if (shapeout==[]):
            return (True, ty_scalarF_d3)
        elif (shapeout==[2]):
            return  (True,  ty_vec2F_d3)
        elif (shapeout==[3]):
            return  (True,  ty_vec3F_d3)
        elif (shapeout==[4]):
            return  (True,  ty_vec4F_d3)
        elif(shapeout==[2, 2]):
            return (True, ty_mat2x2F_d3)
        elif(shapeout==[2, 3]):
            return (True,  ty_mat2x3F_d3)
        elif(shapeout==[2,4]):
            return (True, ty_mat2x4F_d3)
        elif(shapeout==[3, 2]):
            return (True, ty_mat3x2F_d3)
        elif(shapeout==[3,3]):
            return (True, ty_mat3x3F_d3)
        elif(shapeout==[3, 4]):
            return (True, ty_mat3x4F_d3)
        elif(shapeout==[4, 2]):
            return (True, ty_mat4x2F_d3)
        elif(shapeout==[4, 3]):
            return (True, ty_mat4x3F_d3)
        elif(shapeout==[4, 4]):
            return (True, ty_mat4x4F_d3)
        elif (shapeout==[2, 2,2]):
            return (True, ty_ten2x2x2F_d3)
        elif(shapeout==[2, 2, 3]):
            return (True, ty_ten2x2x3F_d3)
        elif(shapeout==[2, 2, 4]):
            return (True, ty_ten2x2x4F_d3)
        elif (shapeout==[2, 3,2]):
            return (True, ty_ten2x3x2F_d3)
        elif(shapeout==[2, 3, 3]):
            return (True, ty_ten2x3x3F_d3)
        elif(shapeout==[2, 3, 4]):
            return (True, ty_ten2x3x4F_d3)
        elif (shapeout==[2, 4,2]):
            return (True, ty_ten2x4x2F_d3)
        elif(shapeout==[2, 4, 3]):
            return (True, ty_ten2x4x3F_d3)
        elif(shapeout==[2, 4, 4]):
            return (True, ty_ten2x4x4F_d3)
        elif (shapeout==[3, 2,2]):
            return (True, ty_ten3x2x2F_d3)
        elif(shapeout==[3, 2, 3]):
            return (True, ty_ten3x2x3F_d3)
        elif(shapeout==[3, 2, 4]):
            return (True, ty_ten3x2x4F_d3)
        elif (shapeout==[3, 3,2]):
            return (True, ty_ten3x3x2F_d3)
        elif(shapeout==[3, 3, 3]):
            return (True, ty_ten3x3x3F_d3)
        elif(shapeout==[3, 3, 4]):
            return (True, ty_ten3x3x4F_d3)
        elif (shapeout==[3, 4,2]):
            return (True, ty_ten3x4x2F_d3)
        elif(shapeout==[3, 4, 3]):
            return (True, ty_ten3x4x3F_d3)
        elif(shapeout==[3, 4, 4]):
            return (True, ty_ten3x4x4F_d3)
        elif (shapeout==[4, 2,2]):
            return (True, ty_ten4x2x2F_d3)
        elif(shapeout==[4, 2, 3]):
            return (True, ty_ten4x2x3F_d3)
        elif(shapeout==[4, 2, 4]):
            return (True, ty_ten4x2x4F_d3)
        elif (shapeout==[4, 3,2]):
            return (True, ty_ten4x3x2F_d3)
        elif(shapeout==[4, 3, 3]):
            return (True, ty_ten4x3x3F_d3)
        elif(shapeout==[4, 3, 4]):
            return (True, ty_ten4x3x4F_d3)
        elif (shapeout==[4, 4,2]):
            return (True, ty_ten4x4x2F_d3)
        elif(shapeout==[4, 4, 3]):
            return (True, ty_ten4x4x3F_d3)
        elif(shapeout==[4, 4, 4]):
            return (True, ty_ten4x4x4F_d3)
        else:
            return (False, "unsupported shapeout dim-3"+str(shapeout))
    else:
        return (False, "unsupported dim")
def is_nrrd(shape):
    if((shape == [])):
        return True
    elif((shape == [2]) or (shape == [3]) or (shape == [4])):
        return True
    elif((shape  == [2,2]) or  (shape == [3,3])):
        return True
    elif((shape  == [2,2,2]) or  (shape == [3,3,3])):
        return True
    else:
        return False

def shapeToTyhelper(shapeout, dim):
    if(is_nrrd(shapeout)):
        return shapeToTyhelper2(shapeout, dim)
    else:
        return (False, "data not supported")

def shapeToTy(shapeout, dim):
    (tf, shape) = shapeToTyhelper(shapeout, dim)
    if(tf):
        return shape
    else:
        raise Exception ("shapeout",shapeout, "dim", dim, "rtn:",shape)

