import sys
import re
import os

from obj_ty import *
from base_constants import *
import random
import sympy
from sympy import *
#symbols
x,y,z =symbols('x y z')

#------------------------------ get coeff ------------------------------
#-------------------- Synthetic field --------------------
# coefficients for synthetic field

# a, b*x + c*y
# d*x*x, e*x*y,f*y*y
# g*y*x*x, h*x*y*y, i*x*x*y*y
#get coeffs depending on dimension and coeff_order


#debug1: makes it [x]

def get_coeffs_debug1(dim, coeff_style, ucoeff):
    lcoeff = ucoeff*(-1)
    def mk_coeffs(c):
        coeffs=[]
        def get_int():
            return random.randint(lcoeff, ucoeff)
        for i in range(c):
            coeffs.append(random.randint(lcoeff, ucoeff))
        return coeffs
    if (dim==0): #tensor type
        return [random.randint(lcoeff, ucoeff),0,0,0,0,0,0,0,0]
    elif (dim==1):
        return [1, 0, 0, 0]
    elif (dim==2):
        return [0,0,0,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif (dim==3):
        coeffs=[]
        xx = [0,0,0,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        xz = [0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        coeffs = [xx,xz,xz]
        return coeffs
    else:
        raise "dimension is not supported"
def get_coeffs_debug2(dim, coeff_style, ucoeff):
    lcoeff = ucoeff*(-1)
    def mk_coeffs(c):
        coeffs=[]
        def get_int():
            return random.randint(lcoeff, ucoeff)
        for i in range(c):
            coeffs.append(random.randint(lcoeff, ucoeff))
        return coeffs
    if (dim==0): #tensor type
        return [random.randint(lcoeff, ucoeff),0,0,0,0,0,0,0,0]
    elif (dim==1):
        return [2, 0, 0, 0]
    elif (dim==2):
        return [2,random.randint(lcoeff, ucoeff),0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif (dim==3):
        coeffs=[]
        for i in range(dim):
            coeffs.append([2,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        return coeffs
    else:
        raise "dimension is not supported"
def get_coeffs(dim, coeff_style, ucoeff):
    lcoeff = ucoeff*(-1)
    def mk_coeffs(c):
        coeffs=[]
        def get_int():
            return random.randint(lcoeff, ucoeff)
        for i in range(c):
            coeffs.append(random.randint(lcoeff, ucoeff))
        return coeffs
    def mk_CoeffSet_d2():
        if (coeff_style == coeff_cubic):
            return mk_coeffs(16)
        elif(coeff_style == coeff_quadratic):
            return mk_coeffs(9)+[0, 0, 0, 0, 0, 0, 0]
        elif(coeff_style == coeff_linear):
            return mk_coeffs(4)+[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (dim==0): #tensor type
        return [random.randint(lcoeff, ucoeff),0,0,0,0,0,0,0,0]
    if (dim==1):
        # a+ bx+ cx^2 +dx^3
        if (coeff_style == coeff_cubic):
            return mk_coeffs(4)
        elif(coeff_style == coeff_quadratic):
            # forces cubic index to be 0
            return mk_coeffs(3)+[0]
        elif(coeff_style == coeff_linear):
            return mk_coeffs(2)+[0, 0]
        else:
            raise Exception("coeff style ", coeff_style, "unsupported")
    if (dim==2):
        return mk_CoeffSet_d2()
    if (dim==3):
        coeffs=[]
        for i in range(dim):
            coeffs.append(mk_CoeffSet_d2())
        return coeffs
        #return [coeffs[0],zero+[0],zero+[0]]
    else:
        raise "dimension is not supported"
#------------------------------ coeff to expression------------------------------
# unravel pack of coeffs
def toExp_cubic(coeff):
    # digest coefficients
    ##print "inside to exp coeff",coeff
    ##print "len",len(coeff)
    [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p] = coeff
    # transform to expression
    tA = a + b*y + c*x*y+ d*x;
    tB = ((e+f*x+g*(x*x))*y*y) + (h*(x*x)*y);
    tC = i*(x*x) + (j+k*x+l*(x*x))*y*y*y;
    tD = (x*x*x)*((m*y*y*y)+(n*y*y)+(o*y)+p);
    return  tA+tB+tC+tD;
# unravel pack of coeffs
def toExp_quad(coeff, zvalue):
    # digest coefficients
    ##print "inside to exp coeff",coeff
    [a,b,c,d,e,f,g,h,i] = coeff
    # transform to expression
    t0 = b*x + c*y
    t1 = d*x*x + g*y*x*x
    t2 = f*y*y + h*x*y*y
    t3 = a + e*x*y + i*(y*y)*(x*x)
    exp = zvalue*(t0+t1+t2+t3)
    return exp
def coeffToExp(coeff, dim):
    ##print "coeff",coeff
    ##print "dim",dim
    if (dim==0):
        zvalue = 1 # no z is use
        return toExp_quad(coeff, zvalue)
    elif (dim==1):
        [a, b, c, d] = coeff
        return a+b*x+c*x*x+d*x*x*x
    elif (dim==2):
        zvalue = 1 # no z is used
        return toExp_cubic(coeff)
    elif(dim==3):
        #digest coefficients
        [z0,z1,z2] = coeff
        e0 = toExp_cubic(z0) # no z is used
        e1 = toExp_cubic(z1) * z # multiply with one z
        e2 = toExp_cubic(z2) * z*z #z^2
        exp = e0+e1+e2
        ##print "\n ******* exp\n e0:",e0,"\n e1:", e1,"\n e2:",e2
        return exp
    else :
        raise "unsupported field dimension"
#------------------------------ mk exp ------------------------------
def mk_exp(dim, coeff_style, ucoeff,t_template):
    if (t_template==template_isPlain):
        #print "using regular template"
        coeff1= get_coeffs_debug1(dim, coeff_style, ucoeff)
        exp1 = coeffToExp(coeff1, dim)
        return (coeff1, exp1)
    else:
        #print "using mip template"
        return (0,[]) # does not get use
def mk_exp_debug1(dim, coeff_style, ucoeff,t_template):
    if (t_template==template_isPlain):
        #print "using regular template"
        coeff1= get_coeffs_debug1(dim, coeff_style, ucoeff)
        exp1 = coeffToExp(coeff1, dim)
        return (coeff1, exp1)
    else:
        #print "using mip template"
        return (0,[]) # does not get used
def mk_exp_debug2(dim, coeff_style, ucoeff,t_template):
    if (t_template==template_isPlain):
        #print "using regular template"
        coeff1= get_coeffs_debug2(dim, coeff_style, ucoeff)
        exp1 = coeffToExp(coeff1, dim)
        return (coeff1, exp1)
    else:
        #print "using mip template"
        return (0,[]) # does not get used