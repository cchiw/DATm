import sys
import re
import os
import time

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_field import *
from obj_counter import *
from obj_frame import  *
from obj_counter import *

# specific cte programs
from cte_iter_cmd import *
from shape import *


# iterating over the different types
def set_iter():
    n_frame = int(sys.argv[2])
    shift = 3 # next command number
    main_iter(n_frame, shift)
    write_heading(testing_frame)


# shape->inner->outer
def main_shape():
    #n_frame = int(sys.argv[1])
    #args = int(sys.argv[2])
    #shift = 2 # how many commands used so far
    n_frame = 0
    # get testing framework
    testing_frame = get_testing_frame(n_frame)
    # get counter
    cnt = get_counter()
    # writing heading based on framework
    write_heading(testing_frame)
    startall = time.time()
    #choose testing range based on commands
    pick_shape(testing_frame, cnt)
    endall = time.time()
    tall = "time: all"+str(endall - startall)
    writeall(tall)
    print (tall)
    write_heading(testing_frame)
#
#
## single(inner->outer) iter ->shape
#def main5():
#    #n_frame = int(sys.argv[1])
#    #args = int(sys.argv[2])
#    #shift = 2 # how many commands used so far
#    n_frame = 0
#    shift = 1
#
#    # get testing framework
#    testing_frame = get_testing_frame(n_frame)
#    # get counter
#    cnt = get_counter()
#    # writing heading based on framework
#    #write_heading(testing_frame)
#
#    #choose testing range based on commands
#    t_inner = int(sys.argv[shift+1])
#    t_outer = int(sys.argv[shift+2])#outer  operator
#    opr_outer = id_toOpr(t_outer)
#    opr_inner = id_toOpr(t_inner)
#    writeTitle_outer(opr_inner, opr_outer)
#    
#    #choose testing range based on commands
#    pick_inner(opr_inner, opr_outer, testing_frame, cnt)
#    clean()
#
## single(inner->outer) iter ->shape
#def main_backwards_all():
#    #n_frame = int(sys.argv[1])
#    #args = int(sys.argv[2])
#    #shift = 2 # how many commands used so far
#    n_frame = 0
#    shift = 1
#    
#    # get testing framework
#    testing_frame = get_testing_frame(n_frame)
#    # get counter
#    cnt = get_counter()
#    # writing heading based on framework
#    #write_heading(testing_frame)
#    
#    #choose testing range based on commands
#    #t_inner = int(sys.argv[shift+1])
#    #t_outer = int(sys.argv[shift+2])#outer  operator
#    #opr_outer = id_toOpr(t_outer)
#    #opr_inner = id_toOpr(t_inner)
#    #writeTitle_outer(opr_inner, opr_outer)
#    #choose testing range based on commands
#    n = len(op_all)
#    startall = time.time()
#    for t_inner in range(n):
#        startx = time.time()
#        opr_inner = id_toOpr(t_inner)
#        for  t_outer in range(n):
#            starty = time.time()
#            opr_outer = id_toOpr(t_outer)
#            counter.zero_locals(cnt)
#            counter.zero_total(cnt)
#            writeTitle_outer(opr_inner, opr_outer)
#            pick_backwards(opr_inner, opr_outer, testing_frame, cnt)
#            clean()
#            endy = time.time()
#            tt = "done inner: "+opr_inner.name+" outer: "+opr_outer.name+" time: "+str(endy - starty)
#            tmp = "time: all-snapshot"+str(endy - startall)
#            writeall(tt+tmp)
#            print (tt+tmp)
#        endx = time.time()
#        tx = "done inner: "+opr_inner.name+" time: "+str(endx - startx)
#        writeall(tx)
#        print (tx)
#        tsnap = "time: all-snapshot"+str(endx - startall)
#        writeall(tsnap)
#        print (tsnap)
#    endall = time.time()
#    tall = "time: all"+str(endall - startall)
#    writeall(tall)
#    print (tall)
#
#
#def main_backwards():
#    #n_frame = int(sys.argv[1])
#    #args = int(sys.argv[2])
#    #shift = 2 # how many commands used so far
#    n_frame = 0
#    shift = 1
#    
#    # get testing framework
#    testing_frame = get_testing_frame(n_frame)
#    # get counter
#    cnt = get_counter()
#    # writing heading based on framework
#    #write_heading(testing_frame)
#    
#    #choose testing range based on commands
#    t_inner = int(sys.argv[shift+1])
#    t_outer = int(sys.argv[shift+2])#outer  operator
#    opr_outer = id_toOpr(t_outer)
#    opr_inner = id_toOpr(t_inner)
#    #writeTitle_outer(opr_inner, opr_outer)
#    #choose testing range based on commands
#    n = len(op_all)
#    startall = time.time()
#
#
#
#    counter.zero_locals(cnt)
#    counter.zero_total(cnt)
#    writeTitle_outer(opr_inner, opr_outer)
#    pick_backwards(opr_inner, opr_outer, testing_frame, cnt)
#    clean()
#    endy = time.time()
#    tt = "done inner: "+opr_inner.name+" outer: "+opr_outer.name+" time: "+str(endy - starty)
#    tmp = "time: all-snapshot"+str(endy - startall)
#    writeall(tt+tmp)
#    print (tt+tmp)
#    endall = time.time()
#    tall = "time: all"+str(endall - startall)
#    writeall(tall)
#    print (tall)
#
#
#
## inner->outer->shape
#def main_iter2():
#    #n_frame = int(sys.argv[1])
#    #args = int(sys.argv[2])
#    #shift = 2 # how many commands used so far
#    n_frame = 0
#    # get testing framework
#    testing_frame = get_testing_frame(n_frame)
#    # get counter
#    cnt = get_counter()
#    # writing heading based on framework
#    write_heading(testing_frame)
#    
#    #choose testing range based on commands
#    n = len(op_all)
#    startall = time.time()
#    for t_inner in range(n):
#        startx = time.time()
#        opr_inner = id_toOpr(t_inner)
#        for  t_outer in range(n):
#            starty = time.time()
#            opr_outer = id_toOpr(t_outer)
#            counter.zero_locals(cnt)
#            counter.zero_total(cnt)
#            writeTitle_outer(opr_inner, opr_outer)
#            #choose testing range based on commands
#            pick_inner(opr_inner, opr_outer, testing_frame, cnt)
#            clean()
#            endy = time.time()
#            tt = "done inner: "+opr_inner.name+" outer: "+opr_outer.name+" time: "+str(endy - starty)
#            tmp = "time: all-snapshot"+str(endy - startall)
#            writeall(tt+tmp)
#            print (tt+tmp)
#
#        endx = time.time()
#        tx = "done inner: "+opr_inner.name+" time: "+str(endx - startx)
#        writeall(tx)
#        print (tx)
#        tsnap = "time: all-snapshot"+str(endx - startall)
#        writeall(tsnap)
#        print (tsnap)
#
#    endall = time.time()
#    tall = "time: all"+str(endall - startall)
#    writeall(tall)
#    print (tall)
#
#

start = time.time()
x = int(sys.argv[1])
name = ""
if(x==0):
    set_iter()
    name ="previous"
elif(x==1):
    main_shape()
    name= " shape->inner->outer"
end = time.time()
t = "  time:"+str(end - start)
writeall(t)
print (t)

e= "\ntime for: "+str(x)+" "+name+"-"+t
print(e)
f = open("time.txt", 'a+')
f.write(e)
f.close()
os.system("rm *.o")
os.system("rm *.pyc")
os.system("rm *.h")
os.system("rm *.nrrd")
os.system("rm *.cxx")
os.system("rm *.diderot")
os.system("rm fs3d-vec2")
os.system("rm fs3d-vec2")