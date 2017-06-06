from obj_field import *
from obj_operator import *

##################################################################################################
# helper function for intermediate types
# shape to matching tensor type
def shape_to_tensor(shape1):
    d1 = nonefield_dim
    shapeout = shape1.shape
    print "inside shape-to tensor d1", d1 ,"shapeout", shapeout
    (tf, m)= shapeToTyhelper(shapeout, d1)
    if(tf):
        print "ok retturn it ", m.name
        return m
    else:
        print "found false"
        return None

# shape to matching field type
def shape_to_field(shape1, d1, k):
    #print " shape_to_field "," shape: ",shape1.name, " dim: ",d1
    shapeout = shape1.shape
    (tf, m)= shapeToTyhelper(shapeout, d1)
    if(tf):
        return fty.convertTy(m, k)
    else:
        return None

# can make nrrd file
def is_nrrd(shape):
    print "shape", shape
    print "ty_scalarT", ty_scalarT
    print "shape:", shape.name
    print " ty_scalarT: ",  ty_scalarT.name
    #print "shape-k:", shape.k  #tty object


    print "shape id",shape.id, "ty-sca-id",ty_scalarT.id
    if(shape.id==ty_noneT.id):
        print "none type"
        raise Exception ("none type")
    elif((shape.id == ty_scalarT.id)):
        print "matched scalar"
        return True
    elif((shape == ty_vec2T) or (shape == ty_vec3T) or (shape == ty_vec4T)):
        return True
    elif((shape  == ty_mat2x2T) or  (shape == ty_mat3x3T)):
        return True
    else:
        print "not nrrd"
        return False

# restruct output
def limit_out(shape):
    print "shape", shape
    print "ty_scalarT", ty_scalarT
    print "shape:", shape.name
    print " ty_scalarT: ",  ty_scalarT.name
    #print "shape-k:", shape.k  #tty object
    
    
    print "shape id",shape.id, "ty-sca-id",ty_scalarT.id
    if(shape.id==ty_noneT.id):
        print "none type"
        raise Exception ("none type")
    elif((shape.id == ty_scalarT.id)):
        print "matched scalar"
        return True
    elif((shape == ty_vec2T) or (shape == ty_vec3T) or (shape == ty_vec4T)):
        return True
    elif((shape  == ty_mat2x2T) or  (shape == ty_mat3x3T)):
        return True
    elif((shape  == ty_ten2x2x2T) or  (shape == ty_ten3x3x3T)):
        return True
    else:
        print "limited output"
        return False


# convert shape tensor to fty
# expected that list is order of dimension [Tensor, d1, d2, d3]
# only those that can data generated
# ty_noneT used
def shape_to_fty(shape, k):
    print "shape_to_fty:"
    if(is_nrrd(shape)):
        print "shape_to_fty-", shape.name,"isnrrd"
        return [shape_to_tensor(shape), shape_to_field(shape, 1, k), shape_to_field(shape, 2, k), shape_to_field(shape, 3, k)]
    else:
        print "shape_to_fty-", shape.name,"not nrrd"
        return [shape_to_tensor(shape), None, None,  None]

# converst rty to tshape1.
# shape to type
# if we want to force the result ot be supportedtypes
isNrrd = True# does it need to be supported by a nrrd file
def convert_rst_binary(fty1, fty2, rty, dim):
    def cvt():
        if(fty1==None or fty2==None):
            return None
        
        elif(fty.is_Field(fty1)):
            k = fty1.k
            return shape_to_field(rty, dim, k)
        elif(fty.is_Field(fty2)):
            k = fty2.k
            return shape_to_field(rty, dim, k)
        else:
            return shape_to_tensor(rty)
    # limit output
    if(not (limit_out(rty))):
        return None
    else:
        return cvt()

def convert_rst_unary(fty1, rty, dim):
    def cvt():
        if(fty1==None):
            return None
        elif(fty.is_Field(fty1)):
            k = fty1.k
            return shape_to_field(rty, dim, k)
        else:
            return shape_to_tensor(rty)
    if(not (limit_out(rty))):
        return None
    else:
        return cvt()

##################################################################################################
# actual type and dimension
# does it still pass?
def check1_tshape(op1,  ity, out_shape, dim):
    print "check1_tshape("+op1.name
    print " ity: "+ity.name
    print " out_shape: "+out_shape.name
    print " dim: "+str(dim)
    def dek(rty1):
        k = ity.k
        if(k==0):
            print "nothing"
            return None
        x = fty.convertTy(rty1, k-1)
        print "rty1:",rty1.name,"x:", x.name
        return x
    if ((op1.fieldop) and (not fty.is_Field(ity))):
        # expected to be a field operator
        return None
    elif(op1 == op_gradient):
        print "heerree"
        if (fty.is_ScalarField(ity)):
            if(dim ==1):
                return dek(ty_scalarF_d1)
            elif(dim ==2):
                return dek(ty_vec2F_d2)
            elif(dim ==3):
                return dek(ty_vec3F_d3)
        else:
            return None
    elif(op1 == op_divergence):
        print "mark a"
        if (ity.id  == ty_vec2F_d2.id):
            print "mark b"
            return dek(ty_scalarF_d2)
        elif(ity.id == ty_vec3F_d3.id):
            return dek(ty_scalarF_d3)
        return None
    elif(op1 == op_curl):
        if (ity.id  == ty_vec2F_d2.id):
            return dek(ty_scalarF_d2)
        elif(ity.id == ty_vec3F_d3.id):
                return dek(ty_vec3F_d3)
        else:
            return None
    elif(op1 == op_jacob):
        if (ity.id  == ty_vec2F_d2.id):
            return dek(ty_mat2x2F_d2)
        elif(ity.id == ty_vec3F_d3.id):
            return dek(ty_mat3x3F_d3)
        elif (ity.id  == ty_mat2x2F_d2.id):
            return dek(ty_ten2x2x2F_d2)
        elif(ity.id == ty_mat3x3F_d3.id):
            return dek(ty_ten3x3x3F_d3)
        
        else:
            return None
    else:
        return  convert_rst_unary(ity, out_shape, dim)

# same as above except for binary operations
def check2_tshape(op1,  exp1, exp2, rty, dim):
    def f(fld, e):
        k = fld.k
        return fty.convertTy(e, k)
    print "check2_tshape exp1:", exp1.name,"k:",exp1.k, "exp2:", exp2.name,"k:", exp2.k
    if( (fty.is_Field(exp1)) and (fty.is_Field(exp2))  and (not (exp1.k==exp2.k))):
        print "k is not the same"
        return None
    elif(op1==op_cross):
        if(exp1.id == ty_vec2F_d2.id):
            if(exp2.id == ty_vec2F_d2.id):
                return f(exp1,ty_scalarF_d2)
            elif(exp2.id == ty_vec2FT.id):
                return f(exp1, ty_scalarF_d2)
            return None
        elif(exp1.id == ty_vec3F_d3.id):
            if(exp2.id == ty_vec3F_d3.id):
                return f(exp1, ty_vec3F_d3)
            elif(exp2.id == ty_vec3FT.id):
                return f(exp1, ty_vec3F_d3)
        elif(exp1.id == ty_vec2FT.id):
            if(exp2.id == ty_vec2FT.id):
                return (ty_scalarFT)
            elif(exp2.id == ty_vec2F_d2.id):
                return f(exp2, ty_scalarF_d2)
            else:
                return None
        elif(exp1.id == ty_vec3FT.id):
            if(exp2.id == ty_vec3FT.id):
                return (ty_vec3FT)
            elif(exp2.id == ty_vec3F_d3.id):
                return f(exp2, ty_vec3F_d3)
            else:
                return None

        else:
            return None
                    # scaling
    else:
        print "about to convert result"
        return convert_rst_binary(exp1, exp2, rty, dim)


##################################################################################################
# given operator and input arg, what are the possibilities for second argument
# op1(shape1, shape2)=> tshape
# op1*shape1 -> (shape2, tshape)..
# tshape1 is fty1
def op1_to_shape(op1, tty1_orig):
    print "op1: ", op1.name, " tty1: ", tty1_orig.name
    shape_same = tty1_orig
    if((op1 == op_negation) or  (op1==op_copy)):
        return shape_same
    elif(op1==op_norm):
        return ty_scalarT
    elif(op1==op_normalize):
        if(tty.isSca(tty1_orig)):
           return None
        return shape_same
    elif((op1==op_trace or op1 ==op_det)):
        if(tty.isMat(tty1_orig)):
            return ty_scalarT
        return None
    elif(op1==op_transpose):
        if(tty.isMat(tty1_orig)):
            [i, j] = tty1_orig.shape
            return nToshape([j,i])
        return None
    elif(op1==op_slicem0):
        if(tty.isMat(tty1_orig)):
            [i, j] = tty1_orig.shape
            return nToshape([j])
        return None
    elif(op1==op_slicem1):
        if(tty.isMat(tty1_orig)):
            [i, j] = tty1_orig.shape
            return nToshape([i])
        return None
    elif((op1==op_slicev0) or (op1==op_slicev1)):
        if(tty.isVec(tty1_orig)):
           return ty_scalarT
        return None
    elif(op1==op_slicet0 ):
        if(tty.isTen3(tty1_orig)):
            [i, j, k] = tty1_orig.shape
            return nToshape([i,k])
        return None
    elif(op1==op_slicet1):
        if(tty.isTen3(tty1_orig)):
            [i, j, k] = tty1_orig.shape
            return nToshape([k])
        return None
    elif(op1==op_inverse):
        if(tty.isMat(tty1_orig)):
            return tty1_orig
        return None
    elif((op1==op_cosine) or  (op1==op_sine) or (op1==op_tangent)):
        if(tty.isSca(tty1_orig)):
            return tty1_orig
        return None
    elif((op1==op_acosine) or  (op1==op_asine) or (op1==op_atangent) or (op1==op_sqrt)):
        if(tty.isSca(tty1_orig)):
            return ty_scalarT
        return None
    elif(op1==op_gradient):
        if(tty.isSca (tty1_orig)):
            return ty_noneT
        return None
    elif( (op1==op_jacob)):
        if(tty.isVec (tty1_orig) or  tty.isMat (tty1_orig)):
            return ty_noneT
        return None
    elif((op1==op_divergence) or  (op1==op_curl)):
        if(tty.isVec (tty1_orig)):
            return ty_noneT
        return None
    else:
        raise Exception ("unsupported operator: "+op1.name)

def op2_to_shape(op1, tty1_orig):
    #print "op2_to_shape",op1.name, "tty1:",tty1_orig.name
    n = [2,3,4]
    # transformations to term
    def term_id(term):
        return term 
    def term_cut_front1(term):
         return term [1:]
    def term_cut_front2(term):
        return term [2:]
    # es is  a list of (types,_)
    # for each shape we add a single index to base
    # term: base+[d]
    # bshape =  transform term with f()
    def grow(ashape, es, f):
        #print "grow"
        rtn = []
        for i in es:
            (b, _ ) = i
            base = b.shape
            #print "b:", b.name
            for d in n:
                #print "d:", d
                # second argument to operator
                term = base +[d]
                bshape = f(term)
                #apend shapes
                rshape = ashape +  bshape
                ty2  = nToshape(term)
                tshape = nToshape(rshape)
                #print "Created: ty2 ", ty2 .name, " tshape: ", tshape.name
                rtn.append((ty2 , tshape))
        return rtn
    # add index to argument, and make result type
    def grow_scale(ashape, es):
        # grow bshape -> bshape
        return grow(ashape, es, term_id)
    def grow_inner(ashape, es):
        # grow bshape -> cut bshape[1:]
        return grow(ashape, es, term_cut_front1)
    def grow_double(ashape, es):
        # grow bshape -> cut bshape[1:]
        return grow(ashape, es, term_cut_front2)
    # create list of vector types
    def rtnvec_scale(tty1):
        shape =  tty1.shape
        # starting to build from index
        inner_index = []
        # ashape T_ashape
        ashape = shape
        #shape to type
        # second argument
        ty2 = nToshape(inner_index)
        # result to 1*2 arguements
        tshape = nToshape(ashape)
        sca = [(ty2, tshape)]
        # grow by a single dimension
        vec = grow_scale(ashape, sca)
        return vec
    def rtnvec_inner(tty1):
        shape =  tty1.shape
        # starting to build from index
        # shared inner index
        ix = len(shape)-1
        inner_index =  [shape[ix]]
        # ashape T_ashape
        ashape =  shape[:ix]
        #shape to type
        # second argument
        ty2 = nToshape(inner_index)
        # result to 1*2 arguements
        tshape = nToshape(ashape)
        vec = [(ty2, tshape)]
        return (ashape, vec)
    def rtnvec_double(tty1):
        shape =  tty1.shape
        # starting to build from index
        # shared inner index
        ix = len(shape)-2
        jx = len(shape)-1
        inner_index =  [shape[ix], shape[jx]]
        # ashape T_ashape
        ashape =  shape[:ix]
        #shape to type
        # second argument
        ty2 = nToshape(inner_index)
        # result to 1*2 arguements
        tshape = nToshape(ashape)
        vec = [(ty2, tshape)]
        print "vec: ","ty2:", ty2.name, "tshape:",tshape.name
        return (ashape, vec)
    
    #####################  operation specific functions   #####################
    # apply inner product to shape
    def shape_inner(tty1):
        # add index to argument, and make result type
        # first index in second argument is [2]
         # must have matching inner index
        # smallest argumment is a vector
        print("shape_inner tty1:"+tty1.name)
        if(tty.isSca(tty1)):
            return []
        else:
            if(tty.isTen3(tty1)):
                (ashape, vec) = rtnvec_inner(tty1)
                # grow by a single dimension
                mat = grow_inner(ashape, vec)
                return  vec+mat
            elif(tty.isMat(tty1)):
                (ashape, vec) = rtnvec_inner(tty1)
                # grow by a single dimension
                mat = grow_inner(ashape, vec)
                ten = grow_inner(ashape, mat)
                return  vec +mat+ten
            elif(tty.isVec(tty1)):
                (ashape, vec) = rtnvec_inner(tty1)
                # grow by a single dimension
                mat = grow_inner(ashape, vec)
                ten = grow_inner(ashape, mat)
                return  vec +mat+ten
            else:
                return []
    # double dot
    def shape_doubledot(tty1):
        if(tty.isSca(tty1) or  tty.isVec(tty1)):
            return []
        else:
            # limit output size
            if(tty.isTen3(tty1)):
                print "mark-ten3"
                (ashape, vec) = rtnvec_double(tty1)
                #print "markb"
                mat = grow_double(ashape, vec)
                #print "markc"
                #ten = grow_inner(ashape, mat)
                return  mat#+ten
            elif(tty.isMat(tty1)):
                print "mark-mat"
                (ashape, vec) = rtnvec_double(tty1)
                #print "mark-b"
                mat = grow_double(ashape, vec)
                #print "mark-c"
                    #ten = grow_inner(ashape, mat)
                return  vec+mat#+ten
            else:
                return []
    # cross product
    def shape_cross(shape):
        if(shape == ty_vec2T):
            i1 = (ty_vec2T, ty_scalarT)
            return [i1]
        elif(shape == ty_vec3T):
            i1 = (ty_vec3T, ty_vec3T)
            return [i1]
        else:
            return []
    # scaling
    def shape_scale(tty1):
        if(tty.isSca(tty1)):
            ashape =  tty1.shape
            # everything is possible
            vec = rtnvec_scale(tty1)
            mat = grow_scale(ashape, vec)
            ten = grow_scale(ashape, mat)
            l = [(tty1,tty1)]+vec+mat+ten
            return  l
        else:
            return [(ty_scalarT, tty1)]
    # apply outer product to shape
    def shape_outer(tty1):
        if(tty.isVec(tty1)):
            vec = rtnvec_scale(tty1)
            ashape= tty1.shape
            mat = grow_scale(ashape, vec)
            return  vec+mat
        elif(tty.isMat(tty1)):
            print "------tty1:",tty1.name
            vec = rtnvec_scale(tty1)
            for (i,j) in vec:
                print "i:", i.name, "j:",j.name
            return  vec
        else:# too large
            return []
     #####################  handle cases  #####################
     # inline simple ones
    if((op1==op_add) or  (op1==op_subtract)):
        # all arguments must have the same shape
        return [(tty1_orig, tty1_orig)]
    if((op1==op_modulate)):
        if(tty.isVec(tty1_orig)):
            # all arguments must have the same shape
            return [(tty1_orig, tty1_orig)]
        else:
            return []
    elif(op1==op_division):
        # second argument must be a scalar
        return [(ty_scalarT, tty1_orig)]
    elif(op1==op_cross):
        return shape_cross(tty1_orig)
    elif(op1==op_outer):
        return shape_outer(tty1_orig)
    elif(op1==op_inner):
        return shape_inner(tty1_orig)
    elif(op1==op_scale):
        return shape_scale(tty1_orig)
    elif(op1 == op_doubledot):
        print "--------------inside double dot-------------- "
        print "tty1_orig: "+tty1_orig.name
        x = shape_doubledot(tty1_orig)
        for (a,b) in x:
            print "-----> "+a.name+"-"+b.name
        return x
    else:
        raise Exception ("op1 not supported:"+op1.name)

