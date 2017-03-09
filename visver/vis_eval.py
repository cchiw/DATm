#r4300


#evalaute output by sampling output
# then comparing points equaldistant apart

import sys
import os

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')


from base_observed import getObserv_t
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
def mk_samplefile(p_out, app, positions):

    print "---------------  mk samplefile ----------------------"
    t_file_b = "shared/template/"+p_out +".ddro"
    readDiderot(p_out, app, positions, t_file_b)

    return

# create diderot program from template
def mk_vis_files(app, positions,arg_inc, arg_positions):

    print "---------------  mk vis ifles----------------------"
    positions = get_x(arg_inc, arg_positions)
    p_out = "vis_sample_out"
    mk_samplefile(p_out, app, positions)
    p_out = "vis_color"
    mk_samplefile(p_out, app, positions)
    return

def copy_all(p_sample):
    print "---------------  copy all ----------------------"
    os.system("unu save -f text -i "+p_sample+".nrrd -o "+p_sample +".txt")
    output ="rst/data/"+p_sample
    i = [".diderot ",".txt ",".png ",".nrrd "]
    for t in i:
        os.system("cp "+ p_sample+t+output+t)



#############  compile and execute program

# run sampling program on output
# currently using eval.diderot as constant sampling program
def run_sample(runtimepath, arg_center, arg_positions, arg_inc):
    print "gen vis sample"

    # run sampling program on output
    p_sample ="vis_sample_out"
    diderotprogram = p_sample+".diderot"
    print " compile vis sample out "
    os.system(runtimepath+" "+diderotprogram)
    os.system("/Users/chariseechiw/diderot/vis15/bin/diderotc --exec "+diderotprogram)
    # run
    PARAMS =" -incx "+str(arg_inc)+" -incy "+str(arg_inc)+" -midx "+ str(arg_center)+" -midy "+ str(arg_center)
    print "about to execute vis sample out "
    executable = "./"+p_sample+PARAMS+ " -positions  "+str(arg_positions)
    os.system(executable)
    executable = "./"+p_sample+PARAMS+ " -positions  "+str(arg_positions)+ " -o "+p_sample+".nrrd"
    os.system(executable)
    print "executable",executable
    print "post compile vis sample out "
    # copy over files
    copy_all(p_sample)
    print "compile vis color"
    # run sampling program on output
    p_color ="vis_color"
    diderotprogram = p_color +".diderot"
    os.system(runtimepath+" "+diderotprogram)
    os.system("/Users/chariseechiw/diderot/vis15/bin/diderotc --exec "+diderotprogram)
    print "post compile"
    executable = "./"+p_color +PARAMS+ " -o "+p_color
    os.system( executable)
    executable = "./"+p_color +PARAMS+ " -o "+p_color+".nrrd"
    os.system( executable)
    print "post executable",executable
    os.system("unu quantize -b 8  -i "+p_color +".nrrd -o "+p_color +".png")
    os.system("cp "+p_color +".png"+"rst/data/color.png")
    print "gen image"
    copy_all(p_color )
    print "about to observe "

    #os.system("unu quantize -b 8 -i "+ p_sample+".nrrd -o "+output+".png")
    arg_perline = 9 # output of mip program
    observed_sphere  = getObserv_t(p_sample, arg_perline)
    
    os.system(" rm "+p_sample+"*")
    os.system(" rm "+  p_color+"*")
    return observed_sphere






#############   Evaluation
# evaluate results 
def toStr( dstr, maxcoeffvar, maxdiff, sumdiff, o6, length):
    per=0
    if(o6>0):
        per = 100*maxdiff/o6
    
    def transform(name, e):
        return "\n\t"+name+" : "+str(round(e, 4))
    x = dstr+transform("max diff",maxdiff)+transform("sumdiff",sumdiff)
    x += transform("observed",o6)+transform("%",per)

    rst_good = 0
    rst_eh = 0
    rst_check = 0
    rst_terrible= 0
    def append(e):
        return (e+"- max diff: "+str(maxdiff)+" "+dstr, "\n\t\t"+e+x)
    if ( maxcoeffvar<=0.0005):
        rtn = append("Rst: RA-a ")
        rst_good = 1
    if ( maxcoeffvar<=0.001):
        rtn = append("Rst: RA-b ")
        rst_good = 1
    if ( maxcoeffvar<=0.005):
        rtn = append("Rst: RB-a ")
        rst_eh = 1
    elif(maxcoeffvar<=0.01):
        rtn = append("Rst: RB-b ")
        rst_eh = 1
    elif(maxcoeffvar<=0.05):
        rtn = append("Rst: RC-a")
        rst_check = 1
    elif(maxcoeffvar<=0.1):
        rtn = append("Rst: RC-b ")
        rst_check = 1
    elif(maxcoeffvar<=0.5):
        rtn = append("Rst: RD-a ")
        rst_terrible = 1
    else:
        rtn = append("Rst: RD-b ")
        rst_terrible = 1

    rst_NA_1 = 0
    return (rtn, rst_good, rst_eh, rst_check, rst_terrible, rst_NA_1)


#############  Compare points equal distance from radius

# compare probed positions
# 4 at each probed position
def eval_sample(observed_sphere):
    maxdiff= -999
    sumdiff = 0
    o6 = 0.0
    length = len(observed_sphere)
    num = 4
    maxcoeffvar = -999
    dstr=""
    for j in observed_sphere:
        print "j:",j
        # each line is the result of sampling 4 points at equal distance from center
        # rad: distance of point from center
        # probe_0 = F(pos_0)
        [i, rad_0, rad_1, rad_2, rad_3, probe_0, probe_1, probe_2, probe_3] = j
        
        maxp = max(max(max(probe_0,probe_1),probe_2),probe_3)
        minp = min(min(min(probe_0,probe_1),probe_2),probe_3)
        diff = maxp-minp
        sumdiff +=  diff
        if(diff>maxdiff):
            o6 = maxp
            maxdiff = diff
        mean = (probe_0+ probe_1+ probe_2+ probe_3)/ num
        v0 = (probe_0-mean)
        v1 = (probe_1-mean)
        v2 = (probe_2-mean)
        v3 = (probe_3-mean)
        variance=((v0*v0)+(v1*v1)+(v2*v2)+(v3*v3))/ num
        stdev = sqrt(variance)
        coeffvar=0
        if ((sqrt(mean*mean)>0.001)):
            coeffvar = stdev/mean

            if(coeffvar>maxcoeffvar):
                maxcoeffvar = coeffvar
        dstr = "maxcoeffvar:"+str(maxcoeffvar)+"  mean :"+ str(mean)+"  variance:"+str( variance)+" stdev:"+str(stdev)
    return toStr(dstr, maxcoeffvar, maxdiff, sumdiff, o6, length)
