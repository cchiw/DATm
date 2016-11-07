from obj_ty import *
from base_constants import *
import random

# depends on objects, and var
# used by run.py

# input(global variables)=> uses var.py
#list of types
def transform_tys(in_tys):
    if(in_tys==ty_All):
        return (l_all_T1, l_all_F1, l_all1)
    elif(in_tys==ty_F):
        return ([], l_all_F1, l_all_F1)
    elif(in_tys==ty_T):
        return (l_all_T1, [], l_all_T1)
    else:
        raise Exception("unsupported")

#get_extra
def get_all_types(rst_ty, in_tys):
    (t, f, a) = transform_tys(in_tys)

    if(rst_ty==ty_T):
        return t
    elif(rst_ty==ty_F):
        return f
    elif(rst_ty==ty_All):
        return a
    else:
        raise Exception ("types unsupported", rst_ty)

# argument types
def getArgs(argsL, rst_ty):
    if(rst_ty==ty_All):
        return argsL[3]
    elif(rst_ty==ty_T):
        return argsL[1]
    elif(rst_ty==ty_F):
        return argsL[2]
    else:
        raise Exception ("unsupport rst_ty", rst_ty)


# testing positions
def get_positions(dim, lpos, upos, num_pos):
    if(dim==1):
        posL=[]
        for s in range(num_pos):
            # random number for positions
            x=random.uniform(lpos, upos)
            posL.append(round(x ,2))
        return posL
    elif(dim==2 or dim==3):
        posL=[]
        for s in range(num_pos):
            pos=[]
            for i in range(dim):
                # random number for positions
                x=random.uniform(lpos, upos)
                pos.append(round(x ,2))
            posL.append(pos)
        return posL
    else:
        return [0]
