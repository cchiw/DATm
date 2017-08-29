import re
import os
from obj_ty import *
from obj_operator import *

# read observed data
#programs organized by number of output per line
#one input per line
def getObserv_1(p_out):
    print  "getObserv_1"
    obs = []
    name = p_out+".txt"
    if(os.path.exists(name)):
        obsf = open(name, 'r')
        obsf.readline()
        for line in obsf:
            #print "line",line
            m = re.split(r'\n',line)
            if m:
                u0 = m[0]
                obs.append(float(u0))
        return obs
    return []

#n inputs per line
def getObserv_t(p_out, n):
    print "getObserv_t", p_out, n
    obs = []
    name = p_out+".txt"
    #print "looking for-t",name
    if(os.path.exists(name)):
        #print "thinks we have it"
        obsf = open(name, 'r')
        obsf.readline()
        for line in obsf:
            #print "line",line
            m = re.split(r'\s',line)
            if m:
                cur= []
                for i in range(n):
                    #print "i:",i,"m[i]:",m[i]
                    u0 = m[i]
                    cur.append(float(u0))
                obs.append(cur)
        return obs
    return []
#chooose function based on number of input per line
def base_observed(oty, p_out):
    ex_rtn = fty.get_tensorType(oty)
    print "ex_rtn", ex_rtn
    print "p_out", p_out
    if(ty_scalarT==ex_rtn):
        return getObserv_1(p_out)
    else:
        a=1
        for s in (ex_rtn.shape):
            a= a*s
        return getObserv_t(p_out, a)



#chooose function based on number of input per line
def observed(app, p_out):
    print "here"
    return base_observed(app.oty, p_out)
