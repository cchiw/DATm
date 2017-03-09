import sys
import re
import os

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
def write(e):
    print (e)
def writeall(e):
    #print (e)
    # if it works continue
    f = open(rst_stash+"/results_final.txt", 'a+')
    f.write(e)
    f.close()
def writesummary(e):
    #print (e)
    # if it works continue
    f = open(rst_stash+"/results_summary.txt", 'a+')
    f.write(e)
    f.close()

def writetys(e):
    #print (e)
    # if it works continue
    f = open(rst_stash+"/results_ty.txt", 'a+')
    f.write(e)
    f.close()

def writeex(e):
    print (e)
    # if it works continue
    f = open(rst_stash+"/results_ex.txt", 'a+')
    f.write(e)
    f.close()

def write_outer(e):
    print (e)
    # if it works continue
    f = open(rst_stash+"/results_outer.txt", 'a+')
    f.write(e)
    f.close()

def write_terrible(e):
    print (e)
    # if it works continue
    f = open(rst_stash+"/results_terrible.txt", 'a+')
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
    print (x)
    writeall(x)
    writesummary(x)

def writenow(xx):
    print(xx)
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
    print(x)
    writeCumulative(cnt)

# compare to ^ it print to terminal, but not to all txt files
def write_results_partial(pre, testing_frame, cnt):
    # global variables needed from testing framework
    g_branch = frame.get_branch(testing_frame)
    x= pre+"- "+g_branch
    x+=  counter.writeLocal(cnt)
    x+="\n***************************************************\n"
    writeall(x)
    #print(x)
    x = counter.writeCumulativeS(cnt)
    print(x)


def writeResults_inner(opr_inner, testing_frame, cnt):
    #print "writeResults_inner"
    y = Title_inner(opr_inner)
    write_results(y, testing_frame, cnt)

def writeResults_outer(opr_inner, opr_outer, testing_frame, cnt):
    #print "writeResults_outer"
    y = Title_outer(opr_inner, opr_outer)
    write_results(y, testing_frame, cnt)

def writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt):
    #print "writeResults3_outer"
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
    writeall(r)
    writesummary(r)
    write_terrible(r)


# copy programs and corresponding file to new directory
def writeToRst2(opname, name_file,  test_header, observed_data, observed_sphere, PARAMS, branch):
    names = name_file
    path = rst_stash+"/"+names
    os.system("mkdir "+path)
    
    
    apx = [".diderot",".nrrd",".png"]
    for i in apx:
        os.system("cp "+rst_data+"/output5_p_observ"+i+" "+path+"/test"+i)
    
    tmp ="_max.png"
    print "opname:",opname
    os.system("cp "+path+"/test.png "+path+"/"+opname+tmp)
#os.system("cp "+rst_data+"/color.png "+path+"/"+opname+"_color"+tmp)
    os.system("cp "+"rst/data/vis_color.png "+path+"/"+opname+"_color"+tmp)
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


# copy programs and corresponding file to new directory
def writeToRst(names, observed_data, correct_data,  positions, PARAMS, branch, rst):
    path = rst_stash+"/"+names
    os.system("mkdir "+path)
    print   ("cp "+rst_data+"/output5_p_observ.diderot "+path+"/"+names+".diderot")
    os.system("cp "+rst_data+"/output5_p_observ.diderot "+path+"/"+names+".diderot")
    os.system("cp output5_p_observ.diderot "+path+"/"+names+".diderot")
    print ("cp "+rst_data+"/inputfile_0.nrrd "+path+"/inputfile_0.nrrd")
    os.system("cp "+rst_data+"/inputfile_0.nrrd "+path+"/inputfile_0.nrrd")
    os.system("cp "+rst_data+"/inputfile_1.nrrd "+path+"/inputfile_1.nrrd")
    #os.system("cp data/inputfilecat_2.nrrd "+path+"/inputfilecat_2.nrrd")
    os.system("cp "+rst_data+"/inputfile_2.nrrd "+path+"/inputfile_2.nrrd")
    os.system("cp "+rst_data+"/output5_p_observ.png "+path+"/output5_p_observ.png")
    os.system("cp "+rst_data+"/output5_p_observ.png "+path+"/"+names+".png")
    a= names
    b= "\n\nobserved data from "+branch+" "+str(observed_data)
    # correct values from python
    c= "\n\ncorrect data from python"+str(correct_data)
    e = "\n\n positions"+str( positions)
    d = "\n\nParams("+str(len(PARAMS))+")"
    j = 0
    for p in PARAMS:
        d+="\n\t"+str(j)+".)"+p
        j+=1
    st = a+b+c+e+d+"\n"+rst+"\n\n"
    f = open(path+"/rst.txt", 'w+')
    f.write(st)
    f.close()




def write_rst(names, x, extraname, phrase):
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
    write_rst(names, x, extraname, rtn1)
    labl = dir+"__"+names
    x = extraname+x
    #writeToRst(labl, None, None,  positions, PARAMS, branch, x)

# does not execute
def rst_execute(names, x, extraname,  branch,  positions, PARAMS):
    rtn1 = "rtn:execute "
    dir = "r"
    write_rst(names, x, extraname, rtn1)
    labl = dir+"__"+names
    #writeToRst(labl, None, None,  positions, PARAMS, branch, x)

#raise Exception( "caught did not compile")
# not available
def rst_NA(names, x, extraname, branch):
    dir = "na"
    labl = dir+"__"+names
    write_rst(names, x, extraname, "rtn:NA")
    #writeToRst(labl, None, None, branch, x)

# check results
def rst_check(names, x, extraname, branch, observed_data, correct_data):
    dir = "k"
    labl = dir+"__"+names
    write_rst(names, x, extraname, "rtn:check")
    #writeToRst(labl, observed_data, correct_data, branch, x)
def rst_terrible(names, x, extraname,  branch, observed_data, correct_data,  positions, PARAMS) :
    dir = "t"
    labl = dir+"__"+names
    #write_rst(names, x, extraname, "rtn:terrible")
    writeToRst(labl, observed_data, correct_data,  positions, PARAMS, branch, x)


