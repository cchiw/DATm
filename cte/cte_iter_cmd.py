import sys
import re
import os
import time

sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')
# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_counter import *
from obj_field import *
from obj_frame import  *

# specific cte programs
from cte_iter import *



# unu save -f nrrd -e ascii -i out.nrrd | less
##################################################################################################
# possible commands
# unu grid -i inputfile.nrrd | unu save -f text
# ^ where all the points are.

##############################################################################################
def cte_cmd(testing_frame, cnt):
    shift = 0
    layer = frame.get_layer(testing_frame)
    args = len(sys.argv)-1  #number of arguments
    if (layer==1):
        if(args==0):
            # iterate over single layer
            rtn = []
            for t_inner in range(getN()):
                opr_inner = id_toOpr(t_inner)
                writeTitle_inner(opr_inner)
                single_all_ops(opr_inner, testing_frame, cnt)
                writeResults_inner(opr_inner, testing_frame, cnt)
            writeCumulative(cnt)
        elif (args==1):
            # iterate over single layer
            t_inner= int(sys.argv[shift+1])
            opr_inner = id_toOpr(t_inner)
            writeTitle_inner(opr_inner)
            single_all_ops(opr_inner, testing_frame, cnt)
            writeResults_inner(opr_inner, testing_frame, cnt)
        elif (args==2):
            t_inner= int(sys.argv[shift+1])
            opr_inner = id_toOpr(t_inner)
            t_num= int(sys.argv[shift+2])
            ex = oprToEx(opr_inner, testing_frame, cnt)
            single_specific_ex(ex, opr_inner,t_num, testing_frame, cnt)
            writeResults_inner(opr_inner, testing_frame, cnt)
        else:
            raise "unsupported"
    # assumes second or third layer
    elif (args==0):
            ##writeTime(1)
             #run all the programs
            embed2_iter_inner(testing_frame, cnt)
            writeCumulative(cnt)
    elif (args==10):
            #run all the programs
            t_start= int(sys.argv[shift+1])
            t_range = int(sys.argv[shift+2])
            embed2_iter_inner_setrange(t_start, t_range,    testing_frame, cnt)
            writeCumulative(cnt)
    elif (args==1):
           # given operator id for inner  operator
            t_inner = int(sys.argv[shift+1])
            opr_inner = id_toOpr(t_inner)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            embed_base_iter_outer(ex, opr_inner, testing_frame, cnt)
            writeCumulative(cnt)
    elif (args==2):
            # given  ids for inner and outer operators
            t_inner = int(sys.argv[shift+1])
            t_outer = int(sys.argv[shift+2])
            opr_outer = id_toOpr(t_outer)
            opr_inner = id_toOpr(t_inner)
            writeTitle_outer(opr_inner, opr_outer)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer]
            embed_base_iter_ty2(ex, oprs, testing_frame, cnt)
            writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
    elif(args==3):
        if(layer==2):
            #  run a specific iterate over double layer with unary operator
            t_inner = int(sys.argv[shift+1])
            t_outer= int(sys.argv[shift+2])
            t_num = int(sys.argv[shift+3])
            t_ty2 = None
            opr_outer = id_toOpr(t_outer)
            opr_inner = id_toOpr(t_inner)
            writeTitle_outer(opr_inner, opr_outer)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer]
            (name, ishape) = get_single_exampleEx(ex, t_num)
            embed_base_iter_ty2_wihty1(ex, oprs, name, ishape, t_num, testing_frame, cnt)
            writeResults_outer(opr_inner, opr_outer, testing_frame, cnt)
        elif (layer==3):
            # given ids for inner, outer1, and outer2 operators
            t_inner = int(sys.argv[shift+1])
            t_outer1 = int(sys.argv[shift+2])
            t_outer2 = int(sys.argv[shift+3])
            opr_inner = id_toOpr(t_inner)
            opr_outer1 = id_toOpr(t_outer1)
            opr_outer2 = id_toOpr(t_outer2)
            Title_outer3(opr_inner, opr_outer1, opr_outer2)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer1, opr_outer2]
            embed_base_iter_ty2(ex, oprs, testing_frame, cnt)
            writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        else:
            raise "unsupported"
    elif(args==4):
        if(layer==2):
            t_inner = int(sys.argv[shift+1])
            t_outer1 = int(sys.argv[shift+2])
            t_num = int(sys.argv[shift+3])
            t_ty2 = int(sys.argv[shift+4])
            opr_inner = id_toOpr(t_inner)
            opr_outer1 = id_toOpr(t_outer1)
            writeTitle_outer(opr_inner, opr_outer1)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer1]
            tys = [t_num, t_ty2]
            (name, ishape) = get_single_exampleEx(ex, t_num)
            embed_base_iter_ty2_wihty2(ex, name, ishape, oprs, tys, testing_frame, cnt)
            writeResults_outer(opr_inner, opr_outer1, testing_frame, cnt)
        elif (layer==3):
            #  run a specific iterate over double layer with unary operator
            t_inner = int(sys.argv[shift+1])
            t_outer1 = int(sys.argv[shift+2])
            t_outer2 = int(sys.argv[shift+3])
            t_num = int(sys.argv[shift+4])
            t_ty2 = None
            opr_inner = id_toOpr(t_inner)
            opr_outer1 = id_toOpr(t_outer1)
            opr_outer2 = id_toOpr(t_outer2)
            Title_outer3(opr_inner, opr_outer1, opr_outer2)

            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer1, opr_outer2]
            (name, ishape) = get_single_exampleEx(ex, t_num)
            embed_base_iter_ty2_wihty1(ex, oprs, name, ishape, t_num, testing_frame, cnt)
            writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        else:
            raise "unsupported"
    elif(args==5):
        if (layer==3):
            #  run a specific iterate over double layer with unary operator
            t_inner = int(sys.argv[shift+1])
            t_outer1 = int(sys.argv[shift+2])
            t_outer2 = int(sys.argv[shift+3])
            t_num = int(sys.argv[shift+4])
            t_ty2 = int(sys.argv[shift+5])
            opr_inner = id_toOpr(t_inner)
            opr_outer1 = id_toOpr(t_outer1)
            opr_outer2 = id_toOpr(t_outer2)
            Title_outer3(opr_inner, opr_outer1, opr_outer2)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer1, opr_outer2]
            tys = [t_num, t_ty2]
            (name, ishape) = get_single_exampleEx(ex, t_num)
            embed_base_iter_ty2_wihty2(ex, name, ishape, oprs, tys, testing_frame, cnt)
            writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        else:
            raise "unsupported"
    elif(args==6):
        if (layer==3):
            #  run a specific iterate over double layer with unary operator
            t_inner = int(sys.argv[shift+1])
            t_outer1 = int(sys.argv[shift+2])
            t_outer2 = int(sys.argv[shift+3])
            t_num = int(sys.argv[shift+4])
            t_ty2 = int(sys.argv[shift+5])
            t_ty3 = int(sys.argv[shift+6])
            opr_inner = id_toOpr(t_inner)
            opr_outer1 = id_toOpr(t_outer1)
            opr_outer2 = id_toOpr(t_outer2)
            Title_outer3(opr_inner, opr_outer1, opr_outer2)
            ex = oprToEx(opr_inner, testing_frame, cnt)
            oprs =  [opr_inner, opr_outer1, opr_outer2]
            tys = [t_num, t_ty2, t_ty3]
            (name, ishape) = get_single_exampleEx(ex, t_num)
            embed_base_iter_ty2_wihty2(ex, name, ishape, oprs, tys, testing_frame, cnt)
            writeResults_outer3(opr_inner, opr_outer1, opr_outer2, testing_frame, cnt)
        else:
            raise "unsupported"
    else:
      raise "unsupported"

