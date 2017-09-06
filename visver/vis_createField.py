import sys
import re
import os
import random

from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *



#convert coeffs
def llist(cmd, coeff):
    a=" -"+cmd
    for i in coeff:
        a+=" "+str(i)
    return a

#call program due to field type
def progName(itype, outSize):
    # tensor type in field type
    ten_ty = itype.tensorType
    # name of file to create field
    name_shape = tty.tyToStr(ten_ty)
    dim = itype.dim
    filename = "symb_f"+name_shape+"d"+str(dim)+"_sym"
    # get reshape size commmand based on tensor shape
    psize = tty.psize(ten_ty)
    for i in range(dim):
        psize = psize * outSize
    sizecmd = " -s 1 "+str(psize)

    return (filename, sizecmd)


# shape-input field
# outSize-samples
# orig- name of synthetic field created with coefficients
# nrrdbranch- path to diderot branch to create nrrd files
def createSingleField(itype, outSize, orig, coeffOrig, nrrdbranch, space):

    outputnrrd=orig+".nrrd"
    sout=str(outSize)
    tty = itype.tensorType
    PARAMS=""
    # range of angle
    if(space):
        PARAMS += " -angle " +str(random.randint(0, 90))

    # ret = 1 - pos*pos;
    # could use other symmetrical expressions

    (e_Orig, w_shape) = progName(itype, outSize)
    p_Orig=  e_Orig+".diderot"
    os.system("cp shared/symb/"+ p_Orig +" "+ p_Orig)

    # remove executable
    os.system(" rm "+e_Orig)
    # compile program
    os.system(nrrdbranch+p_Orig)
    # does executable exist


    txtfile = orig+".txt"
    os.system("./"+e_Orig+PARAMS+"| unu save -f nrrd -o "+outputnrrd)
    #os.system("unu reshape -i "+outputnrrd+w_shape+" | unu save -f text -o "+txtfile)
    #save nrrd file
    return PARAMS

def createField(appC,outSize, coeffs, nrrdbranch, space):
    #app = apply.get_all_Fields(appC)
    #itypes = apply.get_types(app)
    #exps =  apply.get_exps(app)
    flds = apply.get_all_Fields(appC)
    itypes = []
    exps = []
    for j in range(len(flds)):
        i = flds[j]
        itypes.append(i.fldty)
    exps = flds
    PARAMS = []
    for (i,c,s)in zip(exps, coeffs,itypes):
        if(field.get_isField(i)): # not a tensor type
            PARAMS.append(createSingleField(s,outSize,i.inputfile, c, nrrdbranch, space)+"\n\t exp:"+str(i.data))
    return PARAMS
