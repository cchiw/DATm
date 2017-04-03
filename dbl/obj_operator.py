 # -*- coding: utf-8 -*-

from __future__ import unicode_literals

class operator:
    def __init__(self, id, name, arity, symb, placement, limit, fieldop):
        self.id=id
        self.name=name
        self.arity=arity
        self.symb=symb
        self.placement=placement
        self.limit = limit
        self.fieldop =fieldop
    def toStr(self):
        self.name, str(arity)
    def get_name(self):
        return self.name
    def isEq_id(a,b):
        return (a.id==b.id)
    def isEq_idNum(a,b):
        return (a.id==b)
    def toStr(self,s):
        if(self.arity==1):
            return self.name+"("+s+"0"+")"
        elif(self.arity==2):
            return self.name+"("+s+"0,"+s+ "1"+")"

#------------------------------ constants -----------------------------------------------------
#  Constants
# id, name, arity, symbol
# placement of the operator in respect to the arguments
place_left = "left"
place_right = "right"
place_middle = "middle"
place_split = "split"

# add limit to arguments
limit_none = None
limit_trig = "trig1"# |0.1* x| <= 1
limit_small = "small"# |x2|>0.01 , second argument in arity=2
limit_det = "det"# |det(x)|>0.01
limit_nonzero = "positive" # |x|>0


id=0
#op_none= operator(id,"none", 1,"", place_left, limit_none, False)
op_negationT = operator(0,"negT", 1,"-", place_left, limit_none, False)

op_negation = operator(id,"neg", 1,"-", place_left, limit_none, False)
op_norm = operator(id+1,"norm", 1, (u'|',u'|'), place_split, limit_none, False)
op_normalize = operator(id+2,"normalize", 1, u'normalize', place_left, limit_none, False)
op_trace = operator(id+3,"trace", 1, u'trace', place_left, limit_none, False)
op_transpose = operator(id+4,"transpose", 1, u'transpose', place_left, limit_none, False)
op_det = operator(id+5,"det", 1, u'det', place_left, limit_none, False)
op_copy= operator(id+6,"probe", 1,"", place_left, limit_none, False)
op_inverse = operator(id+7, "inverse", 1, u'inv', place_left, limit_det, False)
op_reg = [op_negation, op_norm, op_normalize, op_trace, op_transpose, op_det,op_copy,op_inverse]

id=id+len(op_reg)
#differentiation
op_gradient = operator(id, "grad", 1, u'∇', place_left, limit_none, True)
op_divergence = operator(id+1, "div", 1, u'∇•', place_left, limit_none, True)
op_curl= operator(id+2, "curl", 1, u'∇×',place_left, limit_none, True)
op_jacob= operator(id+3, "jacob", 1, u'∇⊗', place_left, limit_none, True)

op_diff =[op_gradient, op_divergence, op_curl, op_jacob]

id=id+len(op_diff)
#slicing
op_slicem0 = operator(id,"slicem0", 1, u'[1,:]', place_right, limit_none, False)
op_slicem1 = operator(id+1,"slicem1", 1, u'[:,0]', place_right, limit_none, False)
op_slicev0 = operator(id+2,"slicev0", 1, u'[0]', place_right, limit_none, False)
op_slicev1 = operator(id+3,"slicev1", 1, u'[1]', place_right, limit_none, False)
op_slicet0 = operator(id+4,"slicet0", 1, u'[:,1,:]', place_right, limit_none, False)
op_slicet1 = operator(id+5,"slicet1", 1, u'[1,0,:]', place_right, limit_none, False)
op_slice = [op_slicem0, op_slicem1, op_slicev0, op_slicev1, op_slicet0, op_slicet1]
op_unary= op_reg+ op_diff+op_slice

#binary operators
id=id+len(op_slice )
#print"addition id",id
op_add = operator(id,"addition", 2,"+", place_middle, limit_none, False)
op_subtract = operator(id+1,"subtraction", 2, "-", place_middle, limit_none, False)
op_cross = operator(id+2,"cross_product", 2, u'×', place_middle, limit_none, False)
op_outer = operator(id+3,"outer_product", 2, u'⊗', place_middle, limit_none, False)
op_inner = operator(id+4,"inner_product", 2, u'•', place_middle, limit_none, False)
op_scale = operator(id+5,"multiplication", 2, u'*', place_middle, limit_none, False)
op_division = operator(id+6,"division", 2, u'/', place_middle, limit_small, False)
op_modulate = operator(id+7,"modulate", 2, "modulate",  place_left, limit_none, False)
op_doubledot= operator(id+8,"op_doubledot", 2, u':', place_middle, limit_none, False)
op_binary = [op_add, op_subtract, op_cross, op_outer, op_inner, op_scale, op_division, op_modulate, op_doubledot]


id=id+len(op_binary)






#Trig
op_cosine = operator(id, "cosine", 1, u'cosF', place_left, limit_none, True)
op_sine = operator(id+1, "sine", 1, u'sinF', place_left, limit_none, True)

# limit- x must be between -1 and 1 for acos|asine and positive for sqrt.
# to avoid getting a bunch of (inf, or NAN)
# operator arguments are augmented here and in test_eval
op_acosine = operator(id+2, "arccosine", 1,  (u'acosF(0.01*', u')'), place_split, limit_trig, True)
op_asine = operator(id+3, "arcsine", 1,  (u'asinF(0.01*', u')'), place_split, limit_trig, True)
#note sqrt is 'sqrt' in each branch
op_sqrt = operator(id+4, "sqrt", 1, (u'sqrt(|', u'|)'), place_split, limit_nonzero, False)
op_atangent = operator(id+5, "arctangent", 1, u'atanF', place_left, limit_none, True)
op_tangent = operator(id+6, "tangent", 1, u'tanF', place_left, limit_none, True)

op_trig=[ op_cosine, op_sine, op_acosine, op_asine, op_sqrt,op_atangent, op_tangent]


# embed some operators
op_zeros_add22 = operator(id+1, "zeros_add", 1, (u'(zeros[2, 2]+', u')'), place_split, limit_none, False)
# op_zeros_scale3: scalar-> [3,3]
op_zeros_scale3 = operator(id+2, "zeros_scale", 1, (u'(', u'*zeros[3, 3])'), place_split, limit_none, False)
op_zeros_outer2 = operator(id+3, "zeros_outer", 1, (u'(zeros[2]⊗', u')'), place_split, limit_none, False)
op_crossT3 = operator(id+4,"cross product twice", 1, (u'([9, 7, 8] ×', u')'), place_split, limit_none, False)
op_hessian = operator(id+5, "hessian", 1, u'∇⊗∇', place_left, limit_none, True)

op_specialized = [op_zeros_add22, op_zeros_scale3, op_zeros_outer2, op_crossT3, op_hessian]
op_all = op_unary+op_binary+op_trig#+op_specialized



# print all the ops
def pnt_ops():
    i=0
    for op1 in op_all:
        x= "\n-"+op1.name+"("+str(op1.id)+") "
        print (x)
        if(not (op1.id==i)):
            raise Exception(x+" does not match placement "+str(i))
        i+=1
pnt_ops()

def idToStr(n):
    for i in  op_all:
        if (n==i.id):
            return i.name
    return "no match"

# get outer operator
def id_toOpr(id):
    return op_all[id]

# length of operators
def getN():
    # opr max
    return len(op_all)

# do we need to create an extra field type
def needextratype(ex_outer):
    return (ex_outer.arity==2)