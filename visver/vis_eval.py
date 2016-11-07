#evalaute output by sampling output
# then comparing points equaldistant apart

import sys
import os

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')


from base_observed import getObserv_t

# evaluate results 
def toStr(maxdiff, sumdiff, o6, length):
    per=0
    if(o6>0):
        per = 100*maxdiff/o6
    
    def transform(name, e):
        return "\n\t"+name+" : "+str(round(e, 4))
    x = transform("max diff",maxdiff)+transform("sumdiff",sumdiff)
    x += transform("observed",o6)+transform("%",per)

    rst_good = 0
    rst_eh = 0
    rst_check = 0
    rst_terrible= 0
    def append(e):
        return (e+":"+str(maxdiff), "\n\t\t"+e+x)
    if (maxdiff<=0.01):
        if(per<20):
            rtn = append("Rst: RA-x")
            rst_good = 1
        else:
            rtn = append("Rst: RB-x")
            rst_eh = 1
    elif(maxdiff<=0.1):
        if(per<10):
            rtn = append("Rst: RA-y")
            rst_good = 1
        elif(per<20):
            rtn = append("Rst: RB-y")
            rst_eh = 1
        else:
            rtn = append("Rst: RC-y")
            rst_check = 1
    else:
        if(per<2):
            rtn = append("Rst: RC-z")
            rst_check = 1
        else:
            rtn = append("Rst: RD-z ")
            rst_terrible = 1

    rst_NA_1 = 0
    return (rtn, rst_good, rst_eh, rst_check, rst_terrible, rst_NA_1)

# compare probed positions
# 4 at each probed position
def eval_sample(observed_sphere):
    maxdiff= -999
    sumdiff = 0
    o6 = 0.0
    length = len(observed_sphere)
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
    return toStr(maxdiff, sumdiff, o6, length)

# run sampling program on output
# currently using eval.diderot as constant sampling program
def run_sample(runtimepath, arg_center, arg_positions, arg_inc):
    # constant
    print "\n ******************************   A0"
    os.system("rm ev.nrrd")
    os.system("rm eval")
    os.system("rm ev.txt")
    p_sample ="vis_sample_out"
    # compile
    diderotprogram = p_sample+".diderot"
    print "\n ******************************   A1"
    os.system("cp visver/" + diderotprogram +" "+ diderotprogram)
    os.system(runtimepath + " " + diderotprogram)
    print "runtimepath + " " + diderotprogram:",runtimepath + " " + diderotprogram
    arg_perline = 9 # output of mip program
    PARAMS = " -incx "+str(arg_inc)+" -incy  "+str(arg_inc)+" -midx "+ str(arg_center)+" -midy "+ str(arg_center)+ " -positions  "+str(arg_positions)
    # run
    print "\n ******************************   B"
    executable = "./"+p_sample+PARAMS
    os.system( executable)
    print "\n ******************************   C"
    print "executable",executable
    # convert to text file
    os.system("unu save -f text -i ev.nrrd -o ev.txt")
    print "\n ******************************   D"
    observed_sphere  = getObserv_t("ev", arg_perline)
    print "\n ******************************   E"
    print "observed_sphere ",observed_sphere
    return observed_sphere