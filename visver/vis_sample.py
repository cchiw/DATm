#r4300


#evalaute output by sampling output
# then comparing points equaldistant apart

import sys
import os

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')


from base_observed import getObserv_t
from base_write import copyFiles
from vis_writeDiderot import *

def pnt(dist, p):
    pp = p*p;
    rr = dist*dist;
    return sqrt(rr-pp);


def get_x(inc, top):
    pos=[]
    for i in range(top):
        dist = i*inc # distance from center
        tmp = []
        for j in range(4):
            pos_x = random.randint(0, dist)
            pos_y =  pnt(dist, pos_x)
            t = (pos_x, pos_y)
            tmp.append(t)
        pos.append(tmp)
    return pos

#############  generate diderot programs from template
# create diderot program from template
def mk_vis_files(app, positions,arg_inc, arg_positions):
    # FIXME in foo.ddro inline     p_Observ = "observ" name for nrrd files
    positions = get_x(arg_inc, arg_positions)
    
    ###### sample program
    p_out = "vis_sample_out"
    t_file_b = "shared/template/"+p_out +".ddro"
    readDiderot(p_out, app, positions, t_file_b)

    #### color program
    p_out = "vis_color"
    t_file_b = "shared/template/"+p_out +".ddro"
    readDiderot(p_out, app, positions, t_file_b)
    return

def copy_all(n):
    src_path = ""
    dst_path ="rst/data/"
    os.system("unu save -f text -i "+n+".nrrd -o "+src_path +n+".txt")
    copyFiles(n, src_path, dst_path)




#############  compile and execute program

# run sampling program on output
# currently using eval.diderot as constant sampling program
def run_sample_main(runtimepath, PARAMS, p_name, mkImage):
    # compile program
    diderotprogram = p_name+".diderot"
    os.system(runtimepath+" "+diderotprogram)
    # did program compile
    if(not(os.path.exists(p_name))):
        raise (false, "did not find:"+ p_name)
    # run program
    executable = "./"+p_name+PARAMS+ " -o "+p_name+".nrrd"
    os.system(executable)
    # did the program run
    if(not(os.path.exists(p_name+".nrrd"))):
        raise (false, "did not find:"+p_name)
    if(mkImage):
        # create vis for program
        os.system("unu quantize -b 8  -i "+p_name +".nrrd -o "+p_name +".png")
        #os.system("open "+p_name +".png")
        os.system("cp "+p_name +".png"+" rst/data/"+p_name+".png")


    # copy over files
    copy_all(p_name)
    return (true, p_name)


def run_sample(runtimepath, arg_center, arg_inc,arg_positions):
    runtimepath = "/Users/chariseechiw/diderot/vis15/bin/diderotc --exec --double "
    PARAMS =" -incx "+str(arg_inc)+" -incy "+str(arg_inc)+" -midx "+ str(arg_center)+" -midy "+ str(arg_center)
    p_sample ="vis_sample_out"
    PARAMSAUG = PARAMS + " -positions  "+str(arg_positions)
    (tf, msg)= run_sample_main(runtimepath, PARAMSAUG, p_sample, false)
    if(tf):
        p_color ="vis_color"
        (tf, msg)= run_sample_main(runtimepath, PARAMS, p_color, true)
        if(tf):
            arg_perline = 9 # output of mip program
            observed_sphere  = getObserv_t(p_sample, arg_perline)
            return observed_sphere
        else:
            raise Exception (msg)
    else:
        raise Exception (msg)
