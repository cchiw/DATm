 #needs output tensor types
from sympy import *
import math
import numbers

# shared base programs
from obj_ty import *
from obj_operator import *
divConstant=7.2

def toStr(name, var, maxdiff, sumdiff, per, s):
    # f = open("results_tmp.txt", 'a+')
    #f.write("\n\n **********")
    ##print (name)
    x= " max diff: "+str(round(maxdiff,4))+" sumdiff: "+str(round(sumdiff,4))+" per: "+str(per)
    ##print "x",x
    #f.write(name)
    rst_good = 0
    rst_eh = 0
    rst_check = 0
    rst_terrible= 0
    def append(rtn):
        return "\n\t\t"+rtn+s
    
    if (maxdiff<=0.0001):
        rtn = "Rst: V-0 RA"
        rst_good = 1
    elif (maxdiff<=0.001):
        if(per>10):
            rtn = append("Rst: W+3 RC")
            rst_check = 1
        elif(per>1):
            rtn = append("Rst: W-2 RB")
            rst_eh = 1
        elif(per>0.1):
            rtn = "Rst: W-1 RA"
            rst_good = 1
        else:
            rtn = "Rst: W-0 RA"
            rst_good = 1
    elif (maxdiff<=0.01):
        if(per>10):
            rtn = append("Rst: X+3 RC")
            rst_check = 1
        elif(per>1):
            rtn = "Rst: X-2 RB"+x
            rst_eh = 1
        elif(per>0.1):
            rtn = "Rst: X-1 RB"+x
            rst_eh = 1
        else:
            rtn = "Rst: X-0 RA"
            rst_good = 1
    elif(maxdiff<=0.1):
        if(per>10):
            rtn = append("Rst: Y-3 RD ")
            rst_terrible = 1
        elif(per>1):
            rtn = append("Rst: Y-2 RC")
            rst_check = 1
        elif(per>0.1):
            rtn = "Rst: Y-1 RB"+x
            rst_eh = 1
        else:
            rtn = "Rst: Y-0 RB"
            rst_eh = 1
    else:
        if(per>10):
            rtn = append("Rst: Z-3 RD ")
            rst_terrible = 1
        elif(per>1):
            rtn = append("Rst: Z-2 RD ")
            rst_terrible = 1
        elif(per>0.1):
            rtn = append("Rst: Z-1 RC")
            rst_check = 1
        else:
            rtn = "Rst: Z-0 RB "
            rst_eh = 1
    rst_NA_1 = 0
    return (rtn, rst_good, rst_eh, rst_check, rst_terrible, rst_NA_1)

# check is observed and correct is a float
def check_float(o1, c1):
    if(o1 == "nan" or o1 == "inf" or o1 == "-inf"):
        return false
    elif (float('nan')==o1):
        return false
    elif(math.isnan(o1)):
        return false
    elif(isinstance(o1, float)):
        if (float('-inf') < float(o1) < float('inf')):
            if(abs(o1-divConstant)<0.01) :
               return false
            else:
               
                if(not (c1.compare(zoo))):
                    #print "FalseA"
                    return false
                if(c1=="nan" or c1=="inf" or c1=="-inf"):
                    #print "FalseB"
                    return false
                elif (float('nan')==c1):
                    #print "FalseC"
                    return false
                (r, i) =c1.as_real_imag()
                ##print "xx:",(r,i)
                if(not (i==0)):
                    #print "FalseD"
                    return false
                elif(math.isnan(c1)):
                    #print "FalseE"
                    return false
                elif (float('-inf') < float(c1) < float('inf')):
                    #print "true"
                    return true
                else:
                    return false
    return false

#difference and error between observed data and correct data
#output is length 1
def checkdiff_1(name, obv, cor):
    maxdiff = 0
    sumdiff = 0
    length = 0
    obs=0.0
    o6 = 0.0
    c6 = 0.0
    per = 0.0
    t = 0
    for (o1,c1) in zip(obv,cor):
        ##print ("observed:",o,"correct:",c)
        length+=1
        if(check_float(o1, c1)):
            t+=1
            diff=abs(o1-c1)
            sumdiff += diff
            if(diff > maxdiff):
                maxdiff = diff
                o6 = o1
                c6 = c1
        else:
            continue

    if(t==0):
        rtn ="NAN-single"
        return  (rtn, 0, 0, 0, 0, 1)
    else:
        if(o6==0):
            per = 0.0
        else:
            per  = abs(100*(maxdiff/o6))
        avg = sumdiff/length
        s1=round(maxdiff,4)
        s2=round(avg,4)
        s3=round(per,4)
        s=" max diff: "+str(s1)+" sumdiff: "+str(s2)+" "+ str(s3)+"% c:"+str( c6)+ " o:"+str(o6)
        return toStr(name,"x0", maxdiff,avg, per ,s)


def checkdiff_1Zero(name, obv):
    maxdiff = 0
    sumdiff = 0
    length = 0
    obs=0.0
    o6 = 0.0
    c6 = 0.0
    per = 0.0
    t = 0
    c1 =0.0
    for o1 in obv:
        length+=1
        t+=1
        diff=abs(o1-c1)
        sumdiff += diff
        if(diff > maxdiff):
            maxdiff = diff
            o6 = o1
            c6 = c1
        else:
            continue

    if(t==0):
        rtn ="NAN-single"
        return  (rtn, 0, 0, 0, 0, 1)
    else:
        if(o6==0):
            per = 0.0
        else:
            per  = abs(100*(maxdiff/o6))
        avg = sumdiff/length
        s1=round(maxdiff,4)
        s2=round(avg,4)
        s3=round(per,4)
        s=" max diff: "+str(s1)+" sumdiff: "+str(s2)+" "+ str(s3)+"% c:"+str( c6)+ " o:"+str(o6)
    return toStr(name,"x0", maxdiff,avg, per ,s)



def checkdiff(name, obv, cor):
    no = len(obv)
    nc = len(cor)
    if(no!=nc):
        #print "obv", obv
        #print "cor", cor
        raise ("different size for data- observed: "+str(no)+"correct: "+str(nc))
    maxdiff=0
    sumdiff = 0
    length = 0
    s=""
    o6 = 0.0
    c6 = 0.0
    per= 0.0
    size =len(obv[0])
    ##print "no ",no," size: ",size
    pre =""
    t= 0

    for i in range(no):
        for j in range(size):
            length+=1
            o1 = obv[i][j]
            c1 = cor[i][j]
            if(check_float(o1, c1)):
                t+=1
                diff=abs(o1-c1)
                sumdiff += diff
                if(diff > maxdiff):
                    maxdiff = diff
                    o6 = o1
                    c6 = c1
            else:
                continue
    if(o6==0):
        per = 0.0
    else:
        per  = abs(100*(maxdiff/o6))

    if(t==0):
        rtn ="NAN-multiple"
        return  (rtn, 0, 0, 0, 0, 1)
    else:
        avg = sumdiff/length

        s1=round(maxdiff,4)
        s2=round(avg,4)
        s3=round(per,4)
        s=" max diff: "+str(s1)+" sumdiff: "+str(s2)+" "+ str(s3)+"% c:"+str( c6)+ " o:"+str(o6)+pre
        return toStr(name,"x0", maxdiff,avg, per ,s)

#chose function based on length of output
def compare(ex_otype, name, obv, cor):
   
    if(fty.is_Scalar(ex_otype)):
        return checkdiff_1(name, obv, cor)
    else:
        return checkdiff(name, obv, cor)


#expects every value to be 0
def compare_zero(ex_otype, name, obv):
    
    if(fty.is_Scalar(ex_otype)):
        return checkdiff_1Zero(name, obv)
