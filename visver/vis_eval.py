#r4300


#evalaute output by sampling output
# then comparing points equaldistant apart

import sys
import os

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')


from base_observed import getObserv_t
from vis_writeDiderot import *



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
    print "[i, rad_0, rad_1, rad_2, rad_3, probe_0, probe_1, probe_2, probe_3]"
    for j in observed_sphere:
        #print "j:",j
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
