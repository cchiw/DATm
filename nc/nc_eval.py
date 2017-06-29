import sympy
from sympy import *
#symbols
x,y,z, A, B, D =symbols('x y z A B C')
import sys
import re
import math

# shared base programs
from obj_ty import *
from obj_apply import *
from obj_operator import *
from obj_field import *
from base_constants import *
adj = (opr_adj)

# ***************************  unary operators ***************************
# binary operators
def fn_add(exp1,exp2):
    return exp1+exp2
def fn_subtract(exp1,exp2):
    return exp1-exp2
def fn_modulate(exp1,exp2):
    return exp1*exp2
# scaling operator
def fn_multiplication(exp_s, t):
    exp_t = field.get_data(t)
    ityp1 = field.get_ty(t)
    shape1 = fty.get_shape(ityp1)
    
    ##print "inside multiplication **********"

    ###print "shape1", shape1
    if(field.is_Scalar(t)):
        return  exp_s*  exp_t
    elif(field.is_Vector(t)):
        [n1] =  shape1 #vector
        rtn = []
        for i in range(n1):
            rtn.append(exp_s*exp_t[i])
        return rtn
    elif(field.is_Matrix(t)):
        ##print "second is a matrix as execpted"
        [n1,n2] =  shape1
        ##print "shape1", shape1
        rtn = []
        for i in range(n1):
            tmp = []
            for j in range(n2):
                tmp.append(exp_s*exp_t[i][j])
            rtn.append(tmp)
        return rtn
    elif(field.is_Ten3(t)):
        [n1,n2,n3] =  shape1
        rtn = []
        for i in range(n1):
            tmpI = []
            for j in range(n2):
                tmpJ = []
                for k in range(n3):
                    tmpJ.append(exp_s*exp_t[i][j][k])
                tmpI.append(tmpJ)
            rtn.append(tmpI)
        return rtn
    else:
        raise "unsupported scaling"

#scaling of a field
def fn_scaling(fld1, fld2):
    def get_sca():
        if(field.is_Scalar(fld1)):
            return (fld1, fld2)
        else:
            return (fld2, fld1)
    (s, t) = get_sca()
   
    exp_s = field.get_data(s)
    return fn_multiplication(exp_s, t)

#division of a field
def fn_division(t, s):
    if(field.is_Scalar(s)):
        ###print "** should be 2:", field.get_data(s)
        exp_s = (1.0)/field.get_data(s)
        ##print "_________________________________________________________________"

        return fn_multiplication(exp_s, t)
    else:
        raise Exception ("err second arg in division should be a scalar")


# sine  of field
def fn_negation(exp):
    return -1*exp

def fn_cross_exp(exp1, exp2, n1):
    ###print fn_cross_exp, exp1, exp2, n1
    if(n1==2):
        return (exp1[0]*exp2[1]) -(exp1[1]*exp2[0])
    elif(n1==3):
        x0= (exp1[1]*exp2[2]) -(exp1[2]*exp2[1])
        x1= (exp1[2]*exp2[0]) -(exp1[0]*exp2[2])
        x2= (exp1[0]*exp2[1]) -(exp1[1]*exp2[0])
        return [x0,x1,x2]
    else:
        raise "unsupported type for cross product"



def fn_cross(fld1, fld2):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    exp2 = field.get_data(fld2)
    ityp2 = field.get_ty(fld2)
    ###print " exp1: ",exp1," exp2: ",exp2
    # vectors
    n1 = fty.get_vecLength(ityp1) #vector
    n2 = fty.get_vecLength(ityp2)
    return fn_cross_exp(exp1, exp2, n1)

#gradient of field
def fn_grad(exp, dim):
    print "grad is getting", exp
    exp_x = diff(exp,x)

    if (dim==1):
        return exp_x
    elif (dim==2):
        exp_y = diff(exp,y)
        return [ exp_x, exp_y]
    elif (dim==3):
        exp_y = diff(exp,y)
        exp_z = diff(exp,z)
        return [exp_x, exp_y, exp_z]
    else:
        raise "dimension not supported"


#gradient of field
def fn_hessian(exp, dim):
    ###print "inside hessian got expression:", exp
    exp_x = diff(exp,x)
    exp_y = diff(exp,y)
    exp_xy = diff(exp_x,y)
    exp_xx = diff(exp_x,x)
    exp_yy = diff(exp_y,y)
    if (dim==2):
        return [[ exp_xx, exp_xy], [exp_xy,  exp_yy]]
    elif (dim==3):
        exp_z = diff(exp,z)
        exp_xz = diff(exp_x, z)
        exp_yz = diff(exp_y, z)
        exp_zz = diff(exp_z, z)
        return [[exp_xx, exp_xy, exp_xz],[exp_xy, exp_yy, exp_yz], [exp_xz, exp_yz, exp_zz]]
    else:
        raise "dimension not supported"

#evaluate divergence
def fn_divergence(fld):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    ###print " exp1: ",exp1," exp2: ",exp2
    # vectors
    n1 = fty.get_vecLength(ityp) #vector
    if(n1==2):
        return diff(exp[0],x)+diff(exp[1],y)
    elif(n1==3):
        
        return diff(exp[0],x)+diff(exp[1],y)+diff(exp[2],z)
    else:
        raise "unsupported type for divergence"

#evaluate cross product
def fn_curl(fld):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    dim = field.get_dim(fld)
    n = fty.get_vecLength(ityp) #vector
    if(n!=dim):
        raise (" type not supported for curl")
    if(n==2):
       return diff(exp[1], x) - diff(exp[0], y)
    elif(n==3):
        x0= diff(exp[2],y) - diff(exp[1],z)
        x1= diff(exp[0],z) - diff(exp[2],x)
        x2= diff(exp[1],x) - diff(exp[0],y)
        return [x0,x1,x2]
    else:
        raise "unsupported type for cross product"

#evaluate jacob
def fn_jacob(fld):
    exp = field.get_data(fld)
    # ##print "inside jacob it got: ", exp
    ityp = field.get_ty(fld)
    dim = field.get_dim(fld)
    shape = fty.get_shape(ityp)
    # vectors
    if(field.is_VectorField (fld)):

        [n] = shape #vector
        if(n!=dim):
            raise (" type not supported for jacob")
        if(dim==2):
            return [[diff(exp[0],x), diff(exp[0],y)],
                    [diff(exp[1],x), diff(exp[1],y)]]
        elif(dim==3):
            return  [[diff(exp[0],x), diff(exp[0],y), diff(exp[0],z)],
                     [diff(exp[1],x), diff(exp[1],y), diff(exp[1],z)],
                     [diff(exp[2],x), diff(exp[2],y), diff(exp[2],z)]]
        else:
            raise (" type not supported for jacob")
    elif(field.is_Matrix (fld)):
        ###print "inside matrix"
        [n,m] = shape #vector
        if(n!=dim and n!=m):
            raise (" type not supported for jacob")
        elif(dim==2):
            e_00 = exp[0][0]
            e_10 = exp[1][0]
            e_01 = exp[0][1]
            e_11 = exp[1][1]
            f_00 = [diff(e_00,x), diff(e_00,y)]
            f_01 = [diff(e_01,x), diff(e_01,y)]
            f_10 = [diff(e_10,x), diff(e_10,y)]
            f_11 = [diff(e_11,x), diff(e_11,y)]
            return [[f_00,f_01],[f_10,f_11]]
        elif(dim==3):
            e_00 = exp[0][0]
            e_10 = exp[1][0]
            e_20 = exp[2][0]
            e_01 = exp[0][1]
            e_11 = exp[1][1]
            e_21 = exp[2][1]
            e_02 = exp[0][2]
            e_12 = exp[1][2]
            e_22 = exp[2][2]
            def diff_d3(e):
                return [diff(e,x), diff(e,y), diff(e,z)]
            f_00 = diff_d3(e_00)
            f_01 = diff_d3(e_01)
            f_02 = diff_d3(e_02)
            f_10 = diff_d3(e_10)
            f_11 = diff_d3(e_11)
            f_12 = diff_d3(e_12)
            f_20 = diff_d3(e_20)
            f_21 = diff_d3(e_21)
            f_22 = diff_d3(e_22)
            return [[f_00,f_01,f_02],[f_10,f_11,f_12],[f_20,f_21,f_22]]
        else:
            raise (" type not supported for jacob")
    else:
        raise "unsupported type for jacob"

#evaluate norm
def fn_norm(fld, dim):
    #print "here inside norm"
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    dim = field.get_dim(fld)
    ###print " exp1: ",exp1," exp2: ",exp2
    # vectors
    def iter (es):
        sum = 0
        for i in es:
            t=i*i
            ###print "t",t
            sum+=t
        ###print "\nsum",sum
        rtn  = sqrt(sum)
        ###print "\nrtn",rtn
        return rtn
    if(field.is_Scalar(fld)):
        [] = fty.get_shape(ityp)
        #print "scalar exp:",exp
    
        t =sqrt(exp*exp)
        #print "t",t
      
        return t
    elif(field.is_Vector(fld)):
        [n] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            rtn.append(exp[i])
        return iter(rtn)
    elif(field.is_Matrix(fld)):
        [n, m] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            for j in range(m):
                rtn.append(exp[i][j])
        return iter(rtn)
    elif(field.is_Ten3(fld)):
        [n, m, p] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            for j in range(m):
                for k in range(p):
                    rtn.append(exp[i][j][k])
        return iter(rtn)
    else:
        raise "unsupported type for norm"

#evaluate norm
def fn_normalize(fld, dim):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    dim = field.get_dim(fld)
    ###print " exp1: ",exp1," exp2: ",exp2
    norm = fn_norm(fld, dim)
    if(field.is_Scalar(fld)):
        ###print "scal",exp
        return exp
    elif(field.is_Vector(fld)):
        [n] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            rtn.append(exp[i]/norm)
        ###print "vec",rtn
        return rtn
    elif(field.is_Matrix(fld)):
        [n, m] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            rtni = []
            for j in range(m):
                rtni.append(exp[i][j]/norm)
            rtn.append(rtni)
            ###print "matrix:",rtn
        return rtn
    elif(field.is_Ten3(fld)):
        [n, m, p] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            rtni = []
            for j in range(m):
                rtnj = []
                for k in range(p):
                    rtnj.append(exp[i][j][k]/norm)
                rtni.append( rtnj)
            rtn.append( rtni)
###print "ten3",rtn
        return rtn
    else:
        raise "unsupported type for norm"

#[0]
def fn_slicev0(fld1):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    return exp1[0]


#evaluate slice
#[1]
def fn_slicev1(fld1):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    return exp1[1]

#evaluate slice
#[1,:]
def fn_slicem0(fld1):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    rtn=[]
    if(fty.is_Matrix(ityp1)):
        [n2,n3] = fty.get_shape(ityp1)
        for i in range(n3):
            rtn.append(exp1[1][i])
        return rtn
    else:
        raise "unsupported type for slice"

#evaluate slice
#[:,0]
def fn_slicem1(fld1):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    rtn=[]
    if(fty.is_Matrix(ityp1)):
        [n2,n3] = fty.get_shape(ityp1)
        for i in range(n2):
            rtn.append(exp1[i][0])
        return rtn
    else:
        raise "unsupported type for slice"

#evaluate slice
#[:,1,:]
def fn_slicet0(fld1):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    rtn=[]
    if(fty.is_Ten3(ityp1)):
        [n1, n2,n3] = fty.get_shape(ityp1)
        for i in range(n1):
            rtnj=[]
            for j in range(n3):
                rtnj.append(exp1[i][1][j])
            rtn.append(rtnj)
        return rtn
    else:
        raise "unsupported type for slice"

#evaluate slice
#[1,0,:]
def fn_slicet1(fld1):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    rtn=[]
    if(fty.is_Ten3(ityp1)):
        [n1, n2, n3] = fty.get_shape(ityp1)
        for i in range(n3):
            rtn.append(exp1[1][0][i])
        return rtn
    else:
        raise "unsupported type for slice"




#evaluate trace
def fn_trace(fld):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    rtn=[]
    if(field.is_Matrix(fld)):
        [n, m] = fty.get_shape(ityp)
        if (n!=m):
            raise Exception("matrix is not identitical")
        rtn = exp[0][0]+exp[1][1]
        if(n==2):
            return rtn
        elif(n==3):
            return rtn+exp[2][2]
        elif(n==3):
            return rtn+exp[2][2]+exp[3][3]
        else:
            raise "unsupported matrix field"
    else:
        raise "unsupported trace"

#evaluate transpose
def fn_transpose(fld):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    if(field.is_Matrix(fld)):
        [n, m] = fty.get_shape(ityp)
        rtn = []
        for i in range(n):
            rtni = []
            for j in range(m):
                rtni.append(exp[j][i])
            rtn.append(rtni)
        return rtn
    else:
        raise "unsupported transpose"

def fn_doubledot(fld1, fld2):
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    ityp1 = field.get_ty(fld1)
    if(field.is_Matrix(fld1)):
        rtn = 0
        [n, m] = fty.get_shape(ityp1)
        for i in range(n):
            for j in range(m):
                rtn+=exp1[i][j]*exp2[i][j]
        return rtn
    elif(field.is_Ten3(fld1)):
        rtn = []
        [n, m, l] = fty.get_shape(ityp1)
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    rtn.append(exp1[i][j][k]*exp2[i][j][k])
        return rtn
    else:
        raise "unsupported double dot"



#evaluate det
def fn_det(fld):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    rtn=[]
    if(field.is_Matrix(fld)):
        [n, m] = fty.get_shape(ityp)
        if (n!=m):
            raise Exception("matrix is not identitical")
        a = exp[0][0]
        d = exp[1][1]
        c = exp[1][0]
        b = exp[0][1]
        if(n==2):
            x= a*d-b*c
            ##print x 
            return x
        elif(n==3):
            a = exp[0][0]
            b = exp[0][1]
            c = exp[0][2]
            d = exp[1][0]
            e = exp[1][1]
            f = exp[1][2]
            g = exp[2][0]
            h = exp[2][1]
            i = exp[2][2]
            return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
        else:
            raise "unsupported matrix field"
    else:
        raise "unsupported trace"

#evaluate det
def fn_inverse(fld):
    exp = field.get_data(fld)
    ityp = field.get_ty(fld)
    rtn=[]
    if(field.is_Matrix(fld)):
        [n, m] = fty.get_shape(ityp)
        if (n!=m):
            raise Exception("matrix is not identitical")
        a = exp[0][0]
        d = exp[1][1]
        c = exp[1][0]
        b = exp[0][1]
        if(n==2):
            denom = a*d-b*c
            return [[d/denom,-b/denom],[-c/denom, a/denom]]
        elif(n==3):
            a = exp[0][0]
            b = exp[0][1]
            c = exp[0][2]
            d = exp[1][0]
            e = exp[1][1]
            f = exp[1][2]
            g = exp[2][0]
            h = exp[2][1]
            i = exp[2][2]
            denom  =  a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
            num1 = [(e*i - f*h), -(b*i - c*h), (b*f - c*e)]
            num2 = [-(d*i - f*g), (a*i -c*g), -(a*f - c*d)]
            num3 = [(d*h - e*g), -(a*h - b*g),(a*e - b*d)]
            num =[num1,num2,num3]
            
            rtn = []
            for i in range(n):
                tmp = []
                for j in range(n):
                    tmp.append(num[i][j]/denom)
                rtn.append(tmp)
            return rtn
        else:
            raise "unsupported matrix field"
    else:
        raise "unsupported trace"





#evaluate outer product
def fn_outer(fld1, fld2):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    exp2 = field.get_data(fld2)
    ityp2 = field.get_ty(fld2)
    ashape = fty.get_shape(ityp1)
    bshape = fty.get_shape(ityp2)
    x= "ashape", ashape, "bshape", bshape
    ###print "****************fn_outer:",x
    #print "exp1","ityp1",ityp1.name,"-length",len(exp1)
    #print "exp2","ityp2",ityp2.name,"-length",len(exp2)
    rtn = [] 
    if(fty.is_Vector(ityp1)):
        [n1] = fty.get_shape(ityp1)
        #print "ityp1 is a vector"
        if(fty.is_Vector(ityp2)):
            #both vectors
            [n2] = fty.get_shape(ityp2)
            #print "\n outer made shape:"+(str(n1)+","+str(n2))

            for i in  range(n1):
                tmpI = []
                for j in range(n2):
                    k = exp1[i]*exp2[j]
                    ##print "i", i,"exp1[i]:", exp1[i]
                    ##print "j", j,"exp2[j]:", exp2[j]
                    ###print "result:",k
                    tmpI.append(k)
                rtn.append(tmpI)
            return rtn
        elif(fty.is_Matrix(ityp2)):
            [n2,n3] = fty.get_shape(ityp2)
            for i in  range(n1):
                tmpI = []
                for j in range(n2):
                    tmpJ = []
                    for k in range(n3):
                        tmpJ.append(exp1[i]*exp2[j][k])
                    tmpI.append(tmpJ)
                rtn.append(tmpI)
            return rtn
        else:
            raise Exception("outer product is not supported")
    elif(fty.is_Matrix(ityp1)):
        [n1,n2] = fty.get_shape(ityp1)
        #print "ityp1 is a matrix "
        if(fty.is_Vector(ityp2)):
            [n3] = fty.get_shape(ityp2)
            for i in  range(n1):
                tmpI = []
                for j in range(n2):
                    tmpJ = []
                    for k in range(n3):
                        tmpJ.append(exp1[i][j]*exp2[k])
                    tmpI.append(tmpJ)
                rtn.append(tmpI)
            return rtn
        elif(fty.is_Matrix(ityp2)):
            [n3, n4] = fty.get_shape(ityp2)

            for i in  range(n1):
                tmpI = []
                for j in range(n2):
                    tmpJ = []
                    for k in range(n3):
                        tmpK = []
                        for l in range(n4):
                            tmpK.append(exp1[i][j]*exp2[k][l])
                        tmpJ.append(tmpK)
                    tmpI.append(tmpJ)
                rtn.append(tmpI)
            return rtn
        else:
            raise Exception("outer product is not supported")
    else:
        raise Exception("outer product is not supported")

def getConcatV(n, exp1):
    rtn1 = []
    for i in range(n):
        rtn1.append(exp1[i])
    return rtn1

def getConcatM(n,m,exp1):
    rtn1 = []
    for i in range(n):
        rtn2=[]
        for j in range(m):
            rtn2.append(exp1[i][j])
        rtn1.append(rtn2)
    return rtn1

def fn_concat2(fld1, fld2):
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    ityp1 = field.get_ty(fld1)
    ityp2 = field.get_ty(fld2)
    if(fty.is_Scalar(ityp1)):
        return [exp1,exp2]
    elif(fty.is_Vector(ityp2)):
        [n] = fty.get_shape(ityp2)
        rtn1 = getConcatV(n, exp1)
        rtn2 = getConcatV(n, exp2)
        return [rtn1, rtn2]

    elif(fty.is_Matrix(ityp2)):
        [n, m] = fty.get_shape(ityp2)
        rtn1 = getConcatM(n,m,exp1)
        rtn2 = getConcatM(n,m,exp2)
        return [rtn1, rtn2]

    else:
        raise Exception("concat of higher level is not supported")

def fn_concat3(fld1, fld2, fld3):
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    exp3 = field.get_data(fld3)
    ityp1 = field.get_ty(fld1)
    ityp2 = field.get_ty(fld2)
    if(fty.is_Scalar(ityp1)):
        return [exp1,exp2, exp3]
    elif(fty.is_Vector(ityp2)):
        [n] = fty.get_shape(ityp2)
        rtn1 = getConcatV(n, exp1)
        rtn2 = getConcatV(n, exp2)
        rtn3 = getConcatV(n, exp3)
        return [rtn1, rtn2, rtn3]
    
    elif(fty.is_Matrix(ityp2)):
        [n, m] = fty.get_shape(ityp2)
        rtn1 = getConcatM(n,m,exp1)
        rtn2 = getConcatM(n,m,exp2)
        rtn3 = getConcatM(n,m,exp3)
        return [rtn1, rtn2, rtn3]
    else:
        raise Exception("concat of higher level is not supported")

# field composition
#note augementing by 0.01
def fn_comp(fld1, fld2):
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    ##print "exp1:", exp1
    ##print "exp2:", exp2
    ityp1 = field.get_ty(fld1)
    ityp2 = field.get_ty(fld2)
    ###print "ityp1.name",ityp1.name
    ###print ityp2, ityp2.name, ityp2.dim
    bshape = fty.get_shape(ityp2) #  determine x, y ,z
    
  
    def replaceX(a,b):
        r =  a.subs(A,b*adj)
        ##print "replace x : for ", a," with:",b,"=>", r
        return r
    def replaceY(a,b):
        r=a.subs(B,b*adj)
        ###print "replace y : for ", a," with:",b,"=>", r
        return r
    def replaceZ(a,b):
        r= a.subs(D,b*adj)
        ###print "replace z : for ", a," with:",b,"=>", r
        return r
    def replaceD1(a,b):
        a = a.subs(x,A)
        return replaceX(a,b)
    def replaceD2(a,b):
        a = a.subs(x,A)
        a = a.subs(y,B)
        print "a:", a
        print "b:", b
        t1 = replaceX(a, b[0])
        print "t1:", t1
        t2 = replaceY(t1, b[1])
        print "t2:", t2
        return t2
    def replaceD3(a,b):
        ##print "here1",a
        a = a.subs(x, A)
        ##print "here2", a
        a = a.subs(y, B)
        #print "here3", a
        a = a.subs(z, D)
        #print "here4", a
        return replaceZ(replaceY(replaceX(a,b[0]),b[1]),b[2])
    
    def getF():
        if(bshape ==[]):
            return replaceD1
        elif(bshape ==[2]):
            return replaceD2
        elif(bshape ==[3]):
            return replaceD3
    f = getF()
    if(fty.is_Scalar(ityp1)):
        k = f(exp1,exp2)
        #print "kSca:",k
        return k
    elif(fty.is_Vector(ityp1)):
        [a1] = fty.get_shape(ityp1)
        rtn = []
        for i in range(a1):
            rtn.append(f(exp1[i],exp2))
        #print "kVec:", rtn
        return rtn
    elif(fty.is_Matrix(ityp1)):
        [a1, a2] = fty.get_shape(ityp1)
        rtn = []
        for i in range(a1):
            rtnj = []
            for j in range(a2):
                rtnj.append(f(exp1[i][j],exp2))
            rtn.append(rtnj)
        #print "kMat:", rtn
        return rtn
    elif(fty.is_Ten3(ityp1)):
        [a1, a2, a3] = fty.get_shape(ityp1)
        rtn = []
        for i in range(a1):
            rtnj = []
            for j in range(a2):
                rtnk = []
                for k in range(a3):
                    rtnk.append(f(exp1[i][j][k],exp2))
                rtnj.append(rtnk)
            rtn.append(rtnj)
        #print "kTen3:", rtn
        return rtn
    else:
        raise Exception("composition is not supported")

#evaluate inner product
def fn_inner(fld1, fld2):
    exp1 = field.get_data(fld1)
    ityp1 = field.get_ty(fld1)
    exp2 = field.get_data(fld2)
    ityp2 = field.get_ty(fld2)
    ashape = fty.get_shape(ityp1)
    bshape = fty.get_shape(ityp2)
    x= "ashape", ashape, "bshape", bshape
    if(fty.is_Vector(ityp1)):
        [a1] = fty.get_shape(ityp1)
        if(fty.is_Vector(ityp2)):
            #length of vetors
            rtn=0
            [b1] = fty.get_shape(ityp2)
            if(a1!=b1):
                raise x
            for s in  range(a1):
                rtn += exp1[s]*exp2[s]
            return rtn
        elif(fty.is_Matrix(ityp2)):
            [b1,b2] = fty.get_shape(ityp2)
            rtn=[]
            if(a1!=b1):
                raise x
            for i in  range(b2):
                sumrtn=0
                for s in  range(a1):
                    sumrtn +=  exp1[s]*exp2[s][i]
                rtn.append(sumrtn)
            return rtn
        elif(fty.is_Ten3(ityp2)):
            [b1, b2, b3] = fty.get_shape(ityp2)
            rtn = []
            if(a1!=b1):
                raise x
            for i in  range(b2):
                tmpJ = []
                for j in  range(b3):
                    sumrtn=0
                    for s in  range(a1):
                        sumrtn +=  exp1[s]*exp2[s][i][j]
                    tmpJ.append(sumrtn)
                rtn.append(tmpJ)
            return rtn
        else:
            raise "inner product is not supported"
    elif(fty.is_Matrix(ityp1)):
        [a1,a2] = fty.get_shape(ityp1)
        if(fty.is_Vector(ityp2)):
            [b1] = fty.get_shape(ityp2)
            if(a2!=b1):
                raise x
            rtn=[]
            for i in  range(a1):
                sumrtn=0
                for s in  range(a2):
                    sumrtn += exp1[i][s]*exp2[s]
                rtn.append(sumrtn)
            return rtn
        elif(fty.is_Matrix(ityp2)):
            [b1,b2] = fty.get_shape(ityp2)
            rtn=[]
            if(a2!=b1):
                raise x
            for i in  range(a1):
                rtnj = []
                for j in  range(b2):
                    sumrtn=0
                    for s in  range(a2):
                        sumrtn += exp1[i][s]*exp2[s][j]
                    rtnj.append(sumrtn)
                rtn.append(rtnj)
            return rtn
        elif(fty.is_Ten3(ityp2)):
            [b1,b2, b3] = fty.get_shape(ityp2)
            rtn=[]
            if(a2!=b1):
                raise x
            for i in  range(a1):
                rtnj = []
                for j in  range(b2):
                    rtnk = []
                    for k in range(b3):
                        sumrtn=0
                        for s in  range(a2):
                            sumrtn += exp1[i][s]*exp2[s][j][k]
                        rtnk.append(sumrtn)
                    rtnj.append(rtnk)
                rtn.append(rtnj)
            return rtn
                    
        else:
            raise "inner product is not supported"
    elif(fty.is_Ten3(ityp1)):
        [a1,a2, a3] = ashape
        if(fty.is_Vector(ityp2)):
            [b1] = bshape
            if(a3!=b1):
                raise x
            rtn=[]
            for i in  range(a1):
                tmpI=[]
                for j in  range(a2):
                    sumrtn=0
                    for s in  range(a3):
                        sumrtn += exp1[i][j][s]*exp2[s]
                    tmpI.append(sumrtn)
                rtn.append(tmpI)
            return rtn
        if(fty.is_Matrix(ityp2)):
            [b1,b2] = bshape
            if(a3!=b1):
                raise x
            rtn=[]
            for i in  range(a1):
                tmpI=[]
                for j in  range(a2):
                    tmpJ = []
                    for k in range(b2):
                        sumrtn=0
                        for s in  range(a3):
                            sumrtn += exp1[i][j][s]*exp2[s][k]
                        tmpJ.append(sumrtn)
                    tmpI.append(tmpJ)
                rtn.append(tmpI)
            return rtn
        else:
            raise "inner product is not supported"
    else:
        raise "inner product is not supported"

def build_zero(n1, n2):
    rtn = []
    for i in  range(n1):
        tmpI = []
        for j in range(n2):
            tmpI.append(0*x)
        rtn.append(tmpI)
    return rtn

# ***************************  generic apply operators ***************************
#unary operator on a vector
def applyToVector(vec, unary):
    rtn = []
    for v in vec:
        rtn.append(unary(v))
    return rtn
#binary operator on a vector
def applyToVectors(vecA, vecB,  binary):
    rtn = []
    for (a,b) in zip(vecA,vecB):
        x= binary(a,b)
        rtn.append(x)
    return rtn

def applyToM(vec, unary):
    rtn = []
    for i in vec:
        tmpI = []
        for v in i:
            tmpI.append(unary(v))
        rtn.append(tmpI)
    return rtn

def applyToMs(vecA,vecB, unary):
    rtn = []
    for (a,b) in zip(vecA,vecB):
        tmpI = []
        for (u,v) in zip(a,b):
            tmpI.append(unary(u, v))
        rtn.append(tmpI)
    return rtn


def applyToT3(vec, unary):
    rtn = []
    for i in vec:
        tmpI = []
        for j in i:
            tmpJ = []
            for v in j:
                tmpJ.append(unary(v))
            tmpI.append(tmpJ)
        rtn.append(tmpI)
    return rtn

def applyToT3s(vecA, vecB, unary):
    rtn = []
    for (a,b) in zip(vecA, vecB):
        tmpI = []
        for (i,j) in zip(a,b):
            tmpJ = []
            for (u,v) in zip(i,j):
                tmpJ.append(unary(u, v))
            tmpI.append(tmpJ)
        rtn.append(tmpI)
    return rtn


# ***************************  apply to scalars or vectors ***************************
#apply operators to expression
# return output types and expression
# unary operator
# exp: scalar types

def applyToExp_U_S(fn_name, fld):
    ##print "inside apply exp to unary"
    exp = field.get_data(fld)
    dim = field.get_dim(fld)

    ##print fn_name
    ##print fn_name.id
    ##print op_sqrt.id
    if(op_copy==fn_name): #probing
        return  exp
    elif(op_negation==fn_name): #negation
        return fn_negation(exp)
    elif(op_cosine==fn_name): #cosine
        return cos(exp)
    elif(op_sine==fn_name): #sine
        return sin(exp)
    elif(op_tangent==fn_name): # tangent
        return tan(exp)
    elif(op_atangent==fn_name): #atan
        return atan(exp)
    elif(op_gradient==fn_name):
        ##print "inside gradient"
        return fn_grad(exp, dim)
    elif(op_hessian == fn_name):
        return fn_hessian(exp, dim)
    elif(op_asine==fn_name): #asine mag(x)<=1
        frac = 0.01*exp
        return asin(frac)
    elif(op_acosine==fn_name): #acos  mag(x)<=1
        frac = 0.01*exp
        return acos(frac)
    elif(op_sqrt.id==fn_name.id): #sqrt
        # gets norm first to make sure value is positive.
        ##print "exp"
        #s = exp*exp
        ##print "pow"
        #norm = sqrt(s)
        ##print "norm"
        return sqrt(exp)
    elif(op_zeros_scale3.id ==fn_name.id):
        return build_zero(3,3)
    else:
        raise Exception("unsupported unary operator on scalar field:"+ fn_name.name)

# unary operator
# exp: vector  types
def applyToExp_U_V(fn_name, fld):
    exp = field.get_data(fld)
    # ##print "applyToExp_U_V", "fld:", fld.name, "exp:", exp
    if(op_copy==fn_name): #probing
        return exp
    elif(op_negation==fn_name): #negation
        return applyToVector(exp, fn_negation)
    elif(op_divergence==fn_name):
        return fn_divergence(fld)
    elif(op_curl==fn_name):
        return fn_curl(fld)
    elif(op_jacob==fn_name): #jacob
        return fn_jacob(fld)
    elif(op_slicev0==fn_name) :
        return fn_slicev0(fld)
    elif(op_slicev1==fn_name):
        return fn_slicev1(fld)
    elif(op_gradient == fn_name):
        return fn_grad(fld)
    elif(op_zeros_outer2.id == fn_name.id):
        return build_zero(2)
    elif(op_crossT3.id  == fn_name.id):
        return fn_cross_exp([9, 7, 8], exp, 3)
    else:
        raise Exception("unsupported unary operator:"+ fn_name.name)

def applyToExp_U_M(fn_name, fld):
    exp = field.get_data(fld)
    if(op_copy==fn_name): #probing
        return exp
    elif(op_negation==fn_name): #negation
        return applyToM(exp, fn_negation)
    elif(op_jacob==fn_name): #jacob
        ###print "app u-m"
        x = fn_jacob(fld)
        ###print "x", x
        return x
    elif(op_slicem0==fn_name) :
        return fn_slicem0(fld)
    elif(op_slicem1==fn_name):
        return fn_slicem1(fld)
    elif(op_trace == fn_name):
        return fn_trace(fld)
    elif(op_transpose==fn_name):
        return fn_transpose(fld)
    elif(op_det==fn_name):
        return fn_det(fld)
    elif(op_inverse == fn_name):
        return fn_inverse(fld)
    elif(op_zeros_add22.id ==fn_name.id):
        return exp

    else:
        raise Exception("unsupported unary operator:"+ fn_name.name)

def applyToExp_U_T3(fn_name, fld):
    exp = field.get_data(fld)
    if(op_copy==fn_name): #probing
        return exp
    elif(op_negation==fn_name): #negation
        return applyToT3(exp, fn_negation)
    elif(op_jacob==fn_name): #jacob
        return fn_jacob(fld)
    elif(op_slicet0==fn_name) :
        return fn_slicet0(fld)
    elif(op_slicet1==fn_name):
        return fn_slicet1(fld)
    else:
        raise Exception("unsupported unary operator:"+ fn_name.name)

# binary, args do not need to have the same shape
def applyToExp_B_rest(e):
    fn_name=e.opr
    (fld1,fld2) =  apply.get_binary(e)
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    if(op_outer==fn_name):
        return fn_outer(fld1, fld2)
    elif(op_inner==fn_name):
        return fn_inner(fld1, fld2)
    elif(op_scale==fn_name): #scaling
        return fn_scaling(fld1,fld2)
    else:
        raise Exception("unsupported unary operator:"+fn_name.name)

# binary operator
# exp: scalar types
def applyToExp_B_S(e):
    fn_name=e.opr

    (fld1,fld2) =  apply.get_binary(e)
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    ###print fn_name
    if(op_add==fn_name):#addition
        return fn_add(exp1,exp2)
    elif(op_subtract==fn_name):#subtract
        return fn_subtract(exp1,exp2)
    elif(op_modulate==fn_name):#modulate
        return fn_modulate(exp1,exp2)
    elif(op_scale==fn_name): #scaling
        return fn_scaling(fld1,fld2)
    elif(op_division==fn_name): #division
        return fn_division(fld1,fld2)
    else:
        raise Exception("unsupported binary operator on scalar fields:"+ fn_name.name)


# binary operator
# args have the same shape
def applyToExp_B_V(e):

    fn_name=e.opr
    (fld1,fld2) =  apply.get_binary(e)
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    if(op_add==fn_name):#addition
        return applyToVectors(exp1, exp2,  fn_add)
    elif(op_subtract==fn_name):#subtract
        return  applyToVectors(exp1, exp2, fn_subtract)
    elif(op_modulate==fn_name):#modulate
        return applyToVectors(exp1,exp2 ,fn_modulate)
    elif(op_cross==fn_name):
        return fn_cross(fld1, fld2)

    else:
       return applyToExp_B_rest(e)

def applyToExp_B_M(e):

    fn_name=e.opr
    (fld1,fld2) =  apply.get_binary(e)
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    if(op_add==fn_name):#addition
        return applyToMs(exp1, exp2,  fn_add)
    elif(op_subtract==fn_name):#subtract
        return  applyToMs(exp1, exp2, fn_subtract)
    elif(op_modulate==fn_name):#modulate
        return applyToMs(exp1,exp2,fn_modulate)
    else:
        return applyToExp_B_rest(e)

def applyToExp_B_T3(e):

    fn_name=e.opr
    (fld1,fld2) =  apply.get_binary(e)
    exp1 = field.get_data(fld1)
    exp2 = field.get_data(fld2)
    if(op_add==fn_name):#addition
        return applyToT3s(exp1, exp2,  fn_add)
    elif(op_subtract==fn_name):#subtract
        return  applyToT3s(exp1, exp2, fn_subtract)
    elif(op_modulate==fn_name):#modulate
        return applyToT3s(exp1,exp2,fn_modulate)
    else:
        return applyToExp_B_rest(e)


# ***************************  unary/binary operators ***************************
def unary(e):

 
    fld =apply.get_unary(e)
    fn_name=e.opr
    exp = field.get_data(fld)
    dim = field.get_dim(fld)

    if(op_norm==fn_name):#norm
        return fn_norm(fld, dim)
    elif(op_normalize==fn_name):#normalize
        x= fn_normalize(fld, dim)
        return x
    elif(op_zeros_outer2.id == fn_name.id):
        [i,j] = e.oty.shape
        return build_zero(2,j)
    elif (field.is_Scalar(fld)):
        ##print "input is a scalar field"
        return applyToExp_U_S(fn_name, fld)
    elif(field.is_Vector(fld)):
        ##print "input is a vector field"
        return applyToExp_U_V(fn_name, fld)
    elif(field.is_Matrix(fld)):
        ##print "input is a matrix"
        return applyToExp_U_M(fn_name, fld)
    else:
        return applyToExp_U_T3(fn_name, fld)

def binary(e):
    (f, g) =apply.get_binary(e)
    fn_name = e.opr

    # type is checked elsewhere or does not matter
    if(op_division==fn_name): #division
        return fn_division(f, g)
    elif(op_doubledot==fn_name):#op_doubledot
        return fn_doubledot (f, g)
    elif(op_outer==fn_name):
        return fn_outer(f, g)
    elif(op_inner==fn_name):
        return fn_inner(f, g)
    elif(op_scale==fn_name): #scaling
        return fn_scaling(f,g)
    elif(op_concat2==fn_name):#concat 2
        return fn_concat2(f,g)
    elif(op_comp==fn_name): # composition of functions
        x = fn_comp(f,g)
        ##print " rtn exp: ",x
        return x
    elif (field.is_Scalar(f) and field.is_Scalar(g)): # input is a scalar field
        return applyToExp_B_S(e)
    elif (field.is_Vector(f) and field.is_Vector(g)):
            return applyToExp_B_V(e)
    elif (field.is_Matrix(f) and field.is_Matrix(g)):
        return applyToExp_B_M(e)
    elif (field.is_Ten3(f) and field.is_Ten3(g)):
        return applyToExp_B_T3(e)
    else:
         return applyToExp_B_rest(e)


def third(e):
    fn_name = e.opr
    
    if(op_concat3==fn_name): #division
        return fn_concat3(e.lhs, e.rhs, e.third)
    else:
        raise Exception("unhandled third arity")




# sort all applications
def sort(e):
    #a ssingle application
    def simple_apply(c_layer, app):
        arity = apply.get_arity(app)
        oty = apply.get_oty (app)
        if (arity ==1):
            return (oty, unary(app))
        elif (arity ==2):
            return (oty, binary(app))
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
            (oty_outer, oexp_tmp) =  applyUnaryOnce(oexp_inner, app_inner, app_tmp)
            return (oty_outer, oexp_tmp)
        elif(arity==2):
            (app_outer1, rhs) =  apply.get_binary(app_tmp)
            # apply 1st and second layer
            (_, oexp_tmp) = gfnc(c_layer-1, app_outer1)
            # applies third layer
            (oty_outer, oexp_tmp) = applyBinaryOnce(oexp_tmp, app_outer1, app_tmp, rhs)
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
        ##print "layers", c_layer
        return embed(c_layer, e)
# ***************************  evaluate at positions ***************************
#evaluate scalar field exp
def eval_d0(pos0, exp):
    return exp


def eval_d1(pos0, exp):
    ###print "eval vec d1"
    ###print "exp:",exp
    ###print "pos0",pos0
    #evaluate field defined by coefficients at position
    exp = exp.subs(x,pos0)
    ###print "exp",exp
    return exp

def eval_d2(pos0, pos1, exp):
    ###print "exp:",exp
    #evaluate field defined by coefficients at position
    exp = exp.subs(x,pos0)
    exp = exp.subs(y,pos1)
    return exp

def eval_d3(pos0, pos1, pos2, exp):
    #evaluate field defined by coefficients at position
    exp = exp.subs(x,pos0)
    exp = exp.subs(y,pos1)
    exp = exp.subs(z,pos2)
    return exp

#evaluate vector field [exp]
def eval_vec_d1(pos0, vec):
    ###print "eval vec d1"
    rtn = []
    for v in vec:
        rtn.append(eval_d1(pos0, v))
    return rtn

#evaluate vector field [exp,exp]
def eval_vec_d2(pos0, pos1, vec):
    ###print "eval_vec_d2 vec:",vec
    rtn = []
    for v in vec:
        rtn.append(eval_d2(pos0, pos1, v))
    return rtn

def eval_ten3_d1(pos0,ten3):
    rtn = []
    for i in ten3:
        for j in i:
            for v in j:
                rtn.append(eval_d1(pos0, v))
    return rtn



#evaluate vector field [exp,exp]
def eval_mat_d1(pos0, mat):
    ###print "eval_vec_d2 vec:",vec
    rtn = []
    for i in mat:
        for v in i:
            rtn.append(eval_d1(pos0, v))
    return rtn

#evaluate vector field [exp,exp]
def eval_mat_d2(pos0, pos1, mat):
    ###print "eval_vec_d2 vec:",vec
    rtn = []
    ###print "eval_mat_d2 mat",mat
    for i in mat:
        for v in i:
            rtn.append(eval_d2(pos0, pos1, v))
    return rtn

def eval_ten3_d2(pos0, pos1, ten3):
    ###print "eval_vec_d2 vec:",vec
    rtn = []
    for i in ten3:
        for j in i:
            for v in j:
                rtn.append(eval_d2(pos0, pos1, v))
    return rtn



#evaluate vector field [exp,exp]
def eval_vec_d3(pos0, pos1, pos2, vec):
    rtn = []
    for v in vec:
        rtn.append(eval_d3(pos0, pos1, pos2, v))
    return rtn


#evaluate vector field [exp,exp]
def eval_mat_d3(pos0, pos1, pos2, mat):
    ###print "eval_vec_d2 vec:",vec
    rtn = []
    for i in mat:
        for v in i:
            rtn.append(eval_d3(pos0, pos1, pos2, v))
    return rtn

def eval_ten3_d3(pos0, pos1, pos2,ten3):
    rtn = []
    for i in ten3:

        for j in i:

            for v in j:

                rtn.append(eval_d3(pos0, pos1, pos2, v))
    return rtn



def iter_d1(k, pos, exp):
    corr = []
    for x in pos:
        val = k(x, exp)
        corr.append(val)
    return corr

def iter_d2(k, pos, exp):
    corr = []
    ###print "iter expr:", exp
    ###print "pos", pos
    for p in pos:
        ###print "p", p
        x=p[0]
        y=p[1]
        val = k(x,y,exp)
        corr.append(val)
    return corr

def iter_d3(k, pos, exp):
    corr = []
    ###print "iter exp:", exp
    for p in pos:
        x=p[0]
        y=p[1]
        z=p[2]
        val = k(x,y,z, exp)
        ###print "pos: ",x,y,z, " val:", val
        corr.append(val)
    return corr

def probeField(otyp1,pos, ortn):
    dim = fty.get_dim(otyp1)
    ###print "output type"+otyp1.name
    ###print "inside probe field ortn", ortn

    if (dim==nonefield_dim):
        #still need to flatten
        rtn = []
        if (fty.is_Matrix(otyp1)):
            for i in ortn:
                for j in i :
                    rtn.append(j)
            return [rtn]
        elif (fty.is_Ten3(otyp1)):
            for i in ortn:
                for j in i :
                    for k in  j:
                        rtn.append(k)
            return [rtn]
                
        else:
            return [ortn]
    
    elif (dim==1):
        def get_k():
            if (fty.is_ScalarField(otyp1)): # output is a scalar field
                ###print "s_d1"
                return eval_d1
            elif (fty.is_VectorField(otyp1)):
                ###print "v_d1"
                return eval_vec_d1
            elif (fty.is_Matrix(otyp1)):
                return eval_mat_d1
            elif(fty.is_Ten3(otyp1)):
                return eval_ten3_d1
            else:
                raise "error"+otyp1.name
        return iter_d1(get_k(), pos, ortn)
    elif (dim==2):
        def get_k():
            if (fty.is_ScalarField(otyp1)): # output is a scalar field
                return eval_d2
            elif (fty.is_VectorField(otyp1)):
                return eval_vec_d2
            elif (fty.is_Matrix(otyp1)):
                return eval_mat_d2
            elif(fty.is_Ten3(otyp1)):
                return eval_ten3_d2
            else:
                raise "error"+otyp1.name
        return iter_d2(get_k(), pos, ortn)
    elif (dim==3):
        def get_k():
            if (fty.is_ScalarField(otyp1)): # output is a scalar field
                return eval_d3
            elif (fty.is_VectorField(otyp1)):
                return eval_vec_d3
            elif (fty.is_Matrix(otyp1)):
                return eval_mat_d3
            elif(fty.is_Ten3(otyp1)):
                return eval_ten3_d3
            else:
                raise "error"+otyp1.name
        return iter_d3(get_k(), pos, ortn)
    else:
        raise "unsupported dimension"

# ***************************  main  ***************************

# operators with scalar field and vector field
def eval(app, pos):
    ###print "evalname",app.name
    ###print apply.toStr(app,3)
    (otyp1, ortn) = sort(app) #apply operations to expressions
    # ##print "ortn|:", ortn
    rtn = probeField(otyp1, pos, ortn) #evaluate expression at positions
    ###print "rtn", rtn
    return rtn
