 #needs output tensor types
import math
import numbers

# shared base programs
from obj_ty import *
from obj_operator import *
divConstant=7.2



#difference and error between observed data and correct data
#output is length 1
def checkdiff_1(name, obv):
    maxdiff = 0
    sumdiff = 0
    length = 0
    obs=0.0
    o6 = 0.0
    c6 = 0.0
    per = 0.0
    t = 0
    for (o1) in (obv):
        #print ("observed:",o,"correct:",c)
        length+=1
        
        if(o1=="nan" or o1=="inf" or o1=="-inf"):
            continue
        elif (float('nan')==o1):
            continue
        elif(math.isnan(o1)):
            continue
        elif(isinstance(o1, float)):
            if (float('-inf') < float(o1) < float('inf')):
                if(abs(o1-divConstant)<0.01) :
                    continue
                else:
                    t+=1
            else:
                continue
        else:
            continue

    if(t==0):
        return  False
    else:
        return True

def checkdiff(name, obv):
    no = len(obv)
    maxdiff=0
    sumdiff = 0
    length = 0
    s=""
    o6 = 0.0
    c6 = 0.0
    per= 0.0
    size =len(obv[0])
    #print "no ",no," size: ",size
    pre =""
    t= 0

    for i in range(no):
        for j in range(size):
            length+=1
            o1=obv[i][j]

            if(o1=="nan" or o1=="inf" or o1=="-inf"):
                continue
            elif (float('nan')==o1):
                continue
            elif(math.isnan(o1)):
                continue
            elif(isinstance(o1, float)):
                if (float('-inf') < float(o1) < float('inf')):
                    if(abs(o1-divConstant)<0.01) :
                        continue
                    else:
                        t+=1
                else:
                    continue
            else:
                continue


    if(t==0):

        return  False
    else:
        return True

#chose function based on length of output
def check(app, obv):
    ex_otype = fty.get_tensorType(app.oty)
    if(ty_scalarT==ex_otype):
        return checkdiff_1(app.name, obv)
    else:
        return checkdiff(app.name, obv)