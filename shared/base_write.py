import sys
import re
import os
import time

from obj_counter import *
from obj_frame import  *
from base_constants import * 
##################################################################################################
def Title_inner(opr_inner):
    return "\n\n"+" "+opr_inner.name+"_ * |"+str(opr_inner.id)+"_ *"

def Title_outer(opr_inner, opr_outer):
    return "\n "+opr_outer.name+ "("+ opr_inner.name+") |"+str(opr_inner.id)+"_"+str(opr_outer.id)

def Title_outer3(opr_inner, opr_outer1, opr_outer2):
    return "\n "+opr_outer2.name+ "("+opr_outer1.name+ "("+ opr_inner.name+")) |"+str(opr_inner.id)+"_"+str(opr_outer1.id)+"_"+str(opr_outer2.id)

def Title_outer2(opr_outer):
    return "\n"+ "* _"+ opr_outer.name+" |* _"+str(opr_outer.id)+"\n"

def Title_num(opr_inner, opr_outer):
    return "\n"+opr_outer.name+ "("+ opr_inner.name+")|"+str(opr_inner.id)+"_"+str(opr_outer.id)


def writeTime(n, t):
    return 
    e="\n"+ (n)+",\t\t\t"+t
    f = open("rst/stash/results_time.txt", 'a+')
    f.write(e)
    f.close()

def write(e):
    print (e)
    
def writeall(e):
    ###print (e)
    # if it works continue
    f = open("rst/stash/results_final.txt", 'a+')
    f.write(e)
    f.close()
def writesummary(e):
    ###print (e)
    # if it works continue
    f = open("rst/stash/results_summary.txt", 'a+')
    f.write(e)
    f.close()

def writetys(e):
    ###print (e)
    # if it works continue
    f = open("rst/stash/results_ty.txt", 'a+')
    f.write(e)
    f.close()

def writeex(e):
    ##print (e)
    # if it works continue
    f = open("rst/stash/results_ex.txt", 'a+')
    f.write(e)
    f.close()

def write_outer(e):
    ##print (e)
    # if it works continue
    f = open("rst/stash/results_outer.txt", 'a+')
    f.write(e)
    f.close()

def write_terrible(e):
    ##print (e)
    # if it works continue
    f = open("rst/stash/results_terrible.txt", 'a+')
    f.write(e)
    f.close()


def writeTitle_inner(opr_inner):
    y = Title_inner(opr_inner)
    writetys(y)
    writeall(y)

def writeTitle_outer2(opr_outer):
    y = Title_outer2(opr_outer)
    writetys(y)
    writeall(y)


def writeTitle_outer(opr_inner, opr_outer):
    y = Title_outer(opr_inner, opr_outer)
    writetys("\n"+y)
    writeall(y)

def writeTitle_outer3(opr_inner, opr_outer1, opr_outer2):
    y = Title_outer3(opr_inner, opr_outer1, opr_outer2)
    writetys("\n"+y)
    writeall(y)


def writeCumulative(cnt):
    # get cumulative breakdown
    x = counter.writeCumulativeS(cnt)
    ##print (x)
    writeall(x)
    writesummary(x)

def writeFinalCumulative(x):
    f = open("../../results_multiple_time.txt", 'a+')
    f.write(x)
    f.close()


    

def writenow(xx):
    ##print(xx)
    writeall(xx)
    writesummary(xx)


def write_results(pre, testing_frame, cnt):
    # global variables needed from testing framework
    g_branch = frame.get_branch(testing_frame)
    x= pre+"- "+g_branch
    x+=  counter.writeLocal(cnt)
    x+="\n***************************************************\n"
    writeall(x)
    writesummary(x)
    ##print(x)
    writeCumulative(cnt)

# compare to ^ it ##print to terminal, but not to all txt files
def write_results_partial(pre, testing_frame, cnt):
    # global variables needed from testing framework
    g_branch = frame.get_branch(testing_frame)
    x= pre+"- "+g_branch
    x+=  counter.writeLocal(cnt)
    x+="\n***************************************************\n"
    writeall(x)
    ###print(x)
    x = counter.writeCumulativeS(cnt)
    ##print(x)


def writeResults_inner(opr_inner, testing_frame, cnt):
    ###print "writeResults_inner"
    y = Title_inner(opr_inner)
    write_results(y, testing_frame, cnt)

def writeResults_outer(opr_inner, opr_outer, testing_frame, cnt):
    ###print "writeResults_outer"
    y = Title_outer(opr_inner, opr_outer)
    write_results(y, testing_frame, cnt)

def writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt):
    ###print "writeResults3_outer"
    y = Title_outer3(opr_inner, opr_outer1, opr_outer2)
    write_results_partial(y, testing_frame, cnt)


## starts with writing heading in each txt file
def write_heading(testing_frame):
    name = "\n-name: "+frame.get_name(testing_frame)+ "\n template"+frame.get_template(testing_frame)
    runtimepath = "\n-runtimepath: "+ frame.transform_runtimepath(testing_frame)
    coeff_style = "\n-coeff: "+frame.get_coeff_style(testing_frame)
    samples = "\n-samples: "+str(frame.get_samples(testing_frame))
    branch = "\n-branch: "+frame.get_branch(testing_frame)
    revision = "\n-revision: "+frame.get_revision(testing_frame)
    precision = "\n-precision:"+frame.get_precision(testing_frame)
    num_pos = "\n-number of positions:"+str(frame.get_num_pos(testing_frame))
    k = "\n kernel:"+frame.get_krn(testing_frame)
    s = "\n space:"+str(frame.get_space(testing_frame))
    l = "\n layer:" + str(frame.get_layer(testing_frame))
    s+= "\n random range: "+ str(frame.get_random_range(testing_frame))
    s+= "\n random limit:  "+ str(frame.get_random_limit(testing_frame))
    r = "\n\n----- Testing framework -----"+name+coeff_style+(samples)+ num_pos+branch+ precision+revision+runtimepath+k+s+l+"\n"
    print(r)
    writeall(r)
    writesummary(r)
    write_terrible(r)


# copy programs and corresponding file to new directory
def writeToRst2(opname, name_file,  test_header, observed_data, observed_sphere, PARAMS, branch):
    names = name_file
    path = "rst/stash/"+names
    os.system("mkdir "+path)
    
    
    apx = [".diderot",".nrrd",".png"]
    for i in apx:
        os.system("cp "+rst_data+"/observ"+i+" "+path+"/test"+i)
    
    tmp ="_max.png"
    ##print "opname:",opname
    os.system("cp "+path+"/test.png "+path+"/"+opname+tmp)

    os.system("cp "+" rst/data/vis_color.png "+path+"/"+opname+"_color"+tmp)
    os.system("rm "+path+"/test.png ")
    for i in range(3):
        os.system("cp "+rst_data+"/inputfile"+str(i)+".nrrd "+path+"/inputfile_"+str(i)+".nrrd")

    a = "\n\n test_header:"+test_header
    b = "\n\nobserved data from "+branch+" "+str(observed_data)

    d= "\n\n\t with Params("+str(len(PARAMS))+")"
    e= "\n\nobserved_sphere"+str(observed_sphere)

    j = 0
    for p in PARAMS:
        d+="\n\t"+str(j)+".)"+p
        j+=1
    st = a+b+d+e
    f = open(path+"/rst.txt", 'w+')
    f.write(st)
    os.system("open  "+path+"/"+opname+"_color.png")
    #os.system("open  "+path+"/"+opname+"_max.png")
    return

def copyFiles(n, src_path, dst_path):
    filetys = [".diderot",".png", ".nrrd", "_init.c",".py",".txt",".c"]
    for t in filetys:
        tmpname = n+t
        os.system("cp "+src_path+tmpname+" "+dst_path+"/"+tmpname)
        os.system("cp "+src_path+tmpname+" "+dst_path+tmpname)


def rmFiles(n, src_path):
    filetys = [".diderot",".png", ".nrrd", "_init.c",".py",".txt","",".o",".h",".c",".cxx"]
    for t in filetys:
        os.system("rm "+src_path+n+t)




# copy programs and corresponding file to new directory
def writeToRst(names, observed_data, correct_data,  positions, PARAMS, branch, rst):
    path = "rst/stash/"+names
    os.system("mkdir "+path)

    # single and double nrrd file
    filetys = ["_sng.nrrd", "_dbl.nrrd"]
    for i in filetys:
        os.system("cp rst/tmp/correct"+i+" "+path+"/correct"+i)
    
    # input field f
    #nrrdNames =["inputfile_","inputfile", "inputfileF"]
    nrrdNames =["inputfile"]
    for i in  nrrdNames:
        for j in range(3):
            k = i+str(j)
            os.system("cp "+rst_data+"/"+k+".nrrd "+path+"/"+k+".nrrd")

    #copy of observ programs
    filename =["observ", "vis_sample_out", "vis_color"]
    for n in filename:

        copyFiles(n, rst_data+"/", path+"/")

    # added for fem
    os.system("cp Makefile " +path+"/Makefile")
    os.system("cp observ.py " +path+"/observ.py")

    # for rst txt file
    b = "\n\nobserved data from "+branch+" "+str(observed_data)
    c= "\n\ncorrect data from python"+str(correct_data)
    d = "\n\n positions"+str( positions)+"\n\nParams("+str(len(PARAMS))+")"
    st = names+b+c+d
    e = ""
    j = 0
    for p in PARAMS:
        e+="\n\t"+str(j)+".)"+p
        j+=1
    st = st+"\n"+rst+"\n\n"
    f = open(path+"/rst.txt", 'w+')
    f.write(st)
    f.close()


def write_rstG(names, x, extraname, phrase):
    x = "\n\t-"+x+"\n\t"+phrase
    m = "\n\n***"+ phrase+"__"+names +"\n\t -: " + extraname+x
    writeall(x)
    print(x)
    return

def write_rstT(names, x, extraname, phrase):
    x = "\n\t-"+x+"\n\t"+phrase
    m = "\n\n***"+ phrase+"__"+names +"\n\t -: " + extraname+x
    writeall(x)
    writesummary(x)
    write_terrible(m)
    print (x)
    return


# does not compile
def rst_compile(names, x, extraname,  branch,  positions, PARAMS):

    rtn1 = "rtn:compile "
    dir = "c"
    write_rstT(names, x, extraname, rtn1)
    labl = dir+"__"+names
    x = extraname+x

    #writeToRst(labl, None, None,  positions, PARAMS, branch, x)


# does not execute
def rst_execute(names, x, extraname,  branch,  positions, PARAMS):
    rtn1 = "rtn:execute "
    dir = "r"
    write_rstT(names, x, extraname, rtn1)
    labl = dir+"__"+names

def rst_fp(names, x, extraname,  branch,  positions, PARAMS):
    rtn1 = "rtn:fp "
    dir = "r"
    write_rstG(names, x, extraname, rtn1)
    labl = dir+"__"+names
    #writeToRst(labl, None, None,  positions, PARAMS, branch, x)

#raise Exception( "caught did not compile")
# not available
def rst_NA(names, x, extraname, branch):
    dir = "na"
    labl = dir+"__"+names
    #write_rstG(names, x, extraname, "rtn:NA")
    #writeToRst(labl, None, None, branch, x)

# check results
def rst_check(names, x, extraname, branch, observed_data, correct_data):
    dir = "k"
    labl = dir+"__"+names
    write_rstG(names, x, extraname, "rtn:check")
    #writeToRst(labl, observed_data, correct_data, branch, x)
def rst_terrible(names, x, extraname,  branch, observed_data, correct_data,  positions, PARAMS) :
    dir = "t"
    labl = dir+"__"+names
    write_rstT(names, x, extraname, "rtn:terrible")

    #writeToRst(labl, observed_data, correct_data,  positions, PARAMS, branch, x)

def rst_good(names, x, extraname,  branch, observed_data, correct_data,  positions, PARAMS) :
    dir = "p"
    labl = dir+"_"+names
    write_rstG(names, x, extraname, "rtn:general")

    #writeToRst(labl, observed_data, correct_data,  positions, PARAMS, branch, x)


def analyze(name_file, name_ty, name_describe, cnt, rtn, observed_data, correct_data,  positions, PARAMS, branch):
    (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) =  rtn
    #print "X", x
    x = "\n-"+name_file+" "+name_describe+"| "+name_ty+"| "+rtn_1
    writeall(x)
    print  (x)
    
    # collect results
    counter.inc_locals(cnt, rtn)
    #writeCumulative(cnt)
    # check results
    if (rst_check_1==7):
        rst_check(fname_file, x, name_describe, branch, observed_data, correct_data)
    elif (rst_terrible_1==1):
        rst_terrible(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)
        print("observed:",observed_data)
        print("correct_data:",correct_data)
        #raise Fail("stop here:terrible")
    elif (rst_NA_1==9):
        rst_NA(name_file, x, name_describe,  branch)
    #elif (rst_good_1==1 or rst_eh_1==1):
        #elif(rst_good_1==1):
    #raise Exception ("stop")
    #rst_good(name_file, x, name_describe, branch, observed_data, correct_data,  positions, PARAMS)


def cleanup(output, p_out):
    os.system("rm ex1.o")
    os.system("rm ex1_init.o")
    os.system("rm ex1_init.so")
    os.system("rm ex1.cxx")
    os.system("rm ex1.diderot")
    os.system("rm *.c")
    os.system("rm *.h")
    os.system("rm *.txt")
    os.system("rm *.nrrd")
    os.system("rm observ.diderot")
    os.system("rm "+output+"*")
    os.system("rm cat.nrrd")
    os.system("rm  "+p_out+".nrrd")
    os.system("rm  "+output+".txt")
    os.system("rm  "+p_out+".txt")
