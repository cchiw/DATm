import sys
import re
import os
import random
import time
# shared base programs
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_write import *
from base_constants import *

pathToSynFiles = c_pathToSynFiles
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
    filename = pathToSynFiles+name_shape+"d"+str(dim)
    # get reshape size commmand based on tensor shape
    psize = tty.psize(ten_ty)
    for i in range(dim):
        psize = psize * outSize
    sizecmd = " -s 1 "+str(psize)
    #print  " sizecmd ",  sizecmd
    return (filename, sizecmd)

def coeffToBase_d1(pre, v):
    #convert coeff to strings:
    [a, b, c, d] = v
    return " -base"+pre+" "+str(a)+" "+str(b)+" "+str(c)+" "+str(d)


# base,xsq,ysq,diag-coeffs
def coeffToBase_d2(str, coeff):
    # print "coeff: ",len(coeff), " -",coeff
    [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p] = coeff
    setA = [a, b, c, d]
    setB =[e, f, g, h]
    setC =[i, j, k , l]
    setD =[m, n, o, p]
    COEFF = llist("setA"+str, setA)+llist("setB"+str, setB)+llist("setC"+str, setC)+llist("setD"+str, setD)
    #convert coeff to strings
    return COEFF


# base,xsq,ysq,diag-coeffs
def coeffToBase(coeff, str):
    # print "coeff: ",len(coeff), " -",coeff
    [a,b,c,d,e,f,g,h,i]= coeff
    base = [b,c]
    xsq=[d,g]
    ysq=[f,h]
    diag=[a,e,i]
    COEFF = llist("base"+str,base)+llist("xsq"+str,xsq)+llist("ysq"+str,ysq)+llist("diag"+str,diag) #convert coeff to strings
    return COEFF



# shape-input field
# outSize-samples
# orig- name of synthetic field created with coefficients
# nrrdbranch- path to diderot branch to create nrrd files
def createSingleField(itype, outSize, orig, coeffOrig, nrrdbranch, space):
    # print "inside create singlefield: "+orig+" ty: "+itype.name,"coeff:",coeff
    outputnrrd=orig+".nrrd"
    sout=str(outSize)
    tty = itype.tensorType
    
    def tyToCmd(f, str, coeff):
        if (tty==ty_scalarT):
            return f(""+ str, coeff)
        elif (tty==ty_vec2T):
            [v1, v2]=coeff
            return f("1"+ str, v1) + f("2"+ str, v2)
        elif (tty==ty_vec3T):
            [v1, v2, v3]=coeff
            return f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3)
        elif (tty==ty_vec4T):
            [v1, v2, v3, v4]=coeff
            return f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3)+ f("4"+ str, v4)
        elif(tty ==ty_mat2x2T):
            [m1, m2] = coeff
            [v1, v2] = m1
            [v3, v4] = m2
            COEFF = f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3) + f("4"+ str, v4)
            return COEFF
        elif(tty ==ty_mat2x3T):
            [m1, m2] = coeff
            [v1, v2, v3] = m1
            [v4, v5,v6] = m2
            COEFF = f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3) + f("4"+ str, v4)+f("5"+ str, v5) + f("6"+ str, v6)
            return COEFF
        elif(tty ==ty_mat3x3T):
            [m1, m2, m3] = coeff
            [v1, v2, v3] = m1
            [v4, v5, v6] = m2
            [v7, v8, v9] = m3
            COEFF = f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3)
            COEFF+= f("4"+ str, v4) + f("5"+ str, v5) + f("6"+ str, v6)
            COEFF+= f("7"+ str, v7) + f("8"+ str, v8) + f("9"+ str, v9)
            return COEFF
        elif(tty ==ty_mat4x4T):
            [m1, m2, m3, m4] = coeff
            [v1, v2, v3,v4] = m1
            [v5, v6, v7, v8] = m2
            [v9, v10, v11, v12] = m3
            [v13, v14, v15, v16] = m4
            COEFF = f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3)
            COEFF += f("4"+ str, v4) + f("5"+ str, v5) + f("6"+ str, v6)
            COEFF += f("7"+ str, v7) + f("8"+ str, v8) + f("9"+ str, v9)
            COEFF += f("10"+ str, v10) +f("11"+ str, v11) + f("12"+ str, v12)
            COEFF += f("13"+ str, v13)+f("14"+ str, v14)
            return COEFF

        elif(tty ==ty_mat3x2T):
            [m1, m2, m3] = coeff
            [v1, v2] = m1
            [v3, v4] = m2
            [v5, v6] = m3
            COEFF = f("1"+ str, v1) + f("2"+ str, v2) + f("3"+ str, v3)
            COEFF+= f("4"+ str, v4) + f("5"+ str, v5) + f("6"+ str, v6)
            return COEFF
        
        else:
            raise Exception("shape is not supported", itype.name)
    def get_Params():

        if(fty.get_dim(itype)==1):
            # convert vector coefficients to string for 1-dimension
            COEFF = tyToCmd(coeffToBase_d1, "", coeffOrig)
            SIZE=" -width 1 -sz0 "+ sout     # giving sample size
            return COEFF + SIZE
        elif(fty.get_dim(itype)==2):
            COEFF = tyToCmd(coeffToBase_d2, "", coeffOrig)
            SIZE=" -sz0 "+ sout +" -sz1 "+ sout +" -width 1"    # giving sample size
            # range of shear
            PARAMS = COEFF + SIZE
            if(space):
                PARAMS += " -shear "+str(random.randint(0, 1))
                #PARAMS += "  "#-shear 1 "#+ str(random.randint(0, 1))
            return PARAMS
        elif(fty.get_dim(itype)==3):
            if(fty.isEq_id(itype, ty_scalarF_d3)):
                [z0, z1, z2] = coeffOrig
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            elif(fty.isEq_id(itype,ty_vec2F_d3)):
                [v1, v2] = coeffOrig
                [az0,az1,az2] = v1
                [bz0,bz1,bz2] = v2
                z0 = [az0, bz0]
                z1 = [az1, bz1]
                z2 = [az2, bz2]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            elif(fty.isEq_id(itype,ty_vec3F_d3)):
                [v1, v2, v3] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                z0 = [az0, bz0, cz0]
                z1 = [az1, bz1, cz1]
                z2 = [az2, bz2, cz2]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            elif(fty.isEq_id(itype,ty_vec4F_d3)):
                [v1, v2, v3, v4] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                [dz0, dz1, dz2] = v4
                z0 = [az0, bz0, cz0, dz0]
                z1 = [az1, bz1, cz1, dz1]
                z2 = [az2, bz2, cz2, dz2]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            
            elif(fty.isEq_id(itype, ty_mat2x2F_d3)):
                [[v1, v2], [v3, v4]] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                [dz0, dz1, dz2] = v4
                z0 = [[az0, bz0], [cz0, dz0]]
                z1 = [[az1, bz1], [cz1, dz1]]
                z2 = [[az2, bz2], [cz2, dz2]]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)

                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            elif(fty.isEq_id(itype, ty_mat3x3F_d3)):
                [[v1, v2, v3], [v4, v5, v6], [v7, v8, v9]] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                [dz0, dz1, dz2] = v4
                [ez0, ez1, ez2] = v5
                [fz0, fz1, fz2] = v6
                [gz0, gz1, gz2] = v7
                [hz0, hz1, hz2] = v8
                [iz0, iz1, iz2] = v9
                z0 = [[az0, bz0, cz0], [dz0, ez0, fz0], [gz0, hz0, iz0]]
                z1 = [[az1, bz1, cz1], [dz1, ez1, fz1], [gz1, hz1, iz1]]
                z2 = [[az2, bz2, cz2], [dz2, ez2, fz2], [gz2, hz2, iz2]]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)


                #print ("cmd",COEFF)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            
            elif(fty.isEq_id(itype, ty_mat2x3F_d3)):
                [[v1, v2, v3], [v4, v5, v6]] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                [dz0, dz1, dz2] = v4
                [ez0, ez1, ez2] = v5
                [fz0, fz1, fz2] = v6
                z0 = [[az0, bz0, cz0], [dz0, ez0, fz0]]
                z1 = [[az1, bz1, cz1], [dz1, ez1, fz1]]
                z2 = [[az2, bz2, cz2], [dz2, ez2, fz2]]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)
                #print ("cmd",COEFF)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            elif(fty.isEq_id(itype, ty_mat3x2F_d3)):
                [[v1, v2], [v3, v4], [v5, v6]] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                [dz0, dz1, dz2] = v4
                [ez0, ez1, ez2] = v5
                [fz0, fz1, fz2] = v6
                z0 = [[az0, bz0], [cz0, dz0], [ez0, fz0]]
                z1 = [[az1, bz1], [cz1, dz1], [ez1, fz1]]
                z2 = [[az2, bz2], [cz2, dz2], [ez2, fz2]]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)
                
                
                #print ("cmd",COEFF)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
                                                                                                
            elif(fty.isEq_id(itype, ty_mat4x4F_d3)):
                [[v1, v2, v3, v4], [v5, v6, v7, v8], [v9, v10, v11, v12], [v13, v14, v15, v16]] = coeffOrig
                [az0, az1, az2] = v1
                [bz0, bz1, bz2] = v2
                [cz0, cz1, cz2] = v3
                [dz0, dz1, dz2] = v4
                [ez0, ez1, ez2] = v5
                [fz0, fz1, fz2] = v6
                [gz0, gz1, gz2] = v7
                [hz0, hz1, hz2] = v8
                [iz0, iz1, iz2] = v9
                [jz0, jz1, jz2] = v10
                [kz0, kz1, kz2] = v11
                [lz0, lz1, lz2] = v12
                [mz0, mz1, mz2] = v13
                [nz0, nz1, nz2] = v14
                [oz0, oz1, oz2] = v13
                [pz0, pz1, pz2] = v14
                z0 = [[az0, bz0, cz0, dz0], [ez0, fz0, gz0, hz0], [iz0, jz0, kz0, lz0], [mz0, nz0, oz0, pz0]]
                z1 = [[az1, bz1, cz1, dz1], [ez1, fz1, gz1, hz1], [iz1, jz1, kz1, lz1], [mz1, nz1, oz1, pz1]]
                z2 =[[az2, bz2, cz2, dz2], [ez2, fz2, gz2, hz2], [iz2, jz2, kz2, lz2], [mz2, nz2, oz2, pz2]]
                COEFF = tyToCmd(coeffToBase_d2, "_z0", z0)
                COEFF += tyToCmd(coeffToBase_d2, "_z1", z1)
                COEFF += tyToCmd(coeffToBase_d2, "_z2", z2)


                #print ("cmd",COEFF)
                SIZE=" -sz0 "+ sout +" -sz1 "+ sout+" -sz2 "+ sout +" -width 1"    # giving sample size
                return COEFF + SIZE
            else:
                raise "shape for dimension 3 is not supported"
        else:
            raise "dim not supported:"
    startall = time.time()

    PARAMS = get_Params()
    endall = time.time()
    tall50 = (endall - startall)

    startall=endall
    # range of angle
    if(space):
        PARAMS += " -angle " +str(random.randint(0, 90))
        #PARAMS += " -angle 45 "#+ str(random.randint(0, 90))
    endall = time.time()
    tall51 = (endall - startall)
    startall=endall
    #print "params", PARAMS,"space",space
    # get program name and which command
    #print "create field A"
    (e_Orig, w_shape) = progName(itype, outSize)

    endall = time.time()
    tall52 = (endall - startall)
    startall=endall
    
    #print "create field B"
    p_Orig=  e_Orig+".diderot"



    # remove executable
    #os.system(" rm "+e_Orig)
    # compile program

    # comment out if executable exists
    os.system("cp shared/symb/"+ p_Orig +" "+ p_Orig)
    os.system(nrrdbranch+" --log "+p_Orig)
    # does executable exist

    endall = time.time()
    tall53 =(endall - startall)
    startall=endall

    txtfile = orig+".txt"
    os.system("./"+e_Orig+PARAMS+"| unu save -f nrrd -o "+outputnrrd)
    os.system("grep \"compiler\" "+e_Orig+".log >> catcreateall.txt")
    endall = time.time()
    tall54 = (endall - startall)
    startall=endall

     #os.system("unu reshape -i "+outputnrrd+w_shape+" | unu save -f text -o "+txtfile)
    endall = time.time()
    tall55 = (endall - startall)
    startall=endall
    #save nrrd file
    #os.system("rm *.o")
    # os.system("rm *.h")
    #  os.system("rm *.c")

    return (PARAMS,tall50,tall51,tall52,tall53,tall54,tall55)

def sortField(flds, outSize, coeffs, nrrdbranch, space):
    print "outSize:",outSize
    itypes = []
    for j in range(len(flds)):
        i = flds[j]
        itypes.append(i.fldty)
    exps = flds
    PARAMS = []

    all50=0
    all51=0
    all52=0
    all53=0
    all54=0
    all55=0
    for (i,c,s)in zip(exps, coeffs,itypes):
        if(field.get_isField(i)): # not a tensor type
            (p,tall50,tall51,tall52,tall53,tall54,tall55) = createSingleField(s,outSize,i.inputfile, c, nrrdbranch, space)
            PARAMS.append(p)
            all50+=tall50
            all51+=tall51
            all52+=tall52
            all53+=tall53
            all54+=tall54
            all55+=tall55
    return (PARAMS,all50,all51,all52,all53,all54,all55)


def createField(appC,outSize, coeffs, nrrdbranch, space):
    flds = apply.get_all_Fields(appC)
    return sortField(flds, outSize, coeffs, nrrdbranch, space)


