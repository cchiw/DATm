# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re


from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_constants import *
from base_writeDiderot import *

#strings in diderot template
foo_in="foo_in"
foo_outTen="foo_outTen"
foo_op ="foo_op"
foo_probe ="foo_probe"
foo_length="foo_length"
#otherwise variables in diderot program
foo_out="out"
foo_pos="pos"
foo_fieldOut="foo_fieldOut"# just probe output field
foo_maxfieldOut = "foo_maxfieldOut"
foo_sumfieldOut = "foo_sumfieldOut"
foo_basein="foo_basein"#check if we are inside the base fields

foo_samplespread = "foo_samplespread"
foo_colorspread = "foo_colorspread"
foo_color_mark = "foo_color_mark"
const_out ="7.2"


# positions are a list of a list of points
# for each i, thre are 4 points that are equal distance from radius
def vis_sample_spread(positions,f, app):
    foo = ""
    foo ="\tif(i==100){ pos0=[-7.2,-7.2];}\n"
    i = 0
    for p in (positions):
        pstring = ""
        pn = 0
        for (x,y) in p:
            pstring +=" pos"+str(pn)+"=["+str(x)+","+str(y)+"];"
            pn +=1
        foo +="\telse if(i=="+str(i)+"){"+pstring +"}\n"
        i+=1
    f.write(foo.encode('utf8'))
    return


def vis_color_spread(positions,f, app):
    foo = ""
    i = 0
    tab = ["a","b","c","d"]
    for p in (positions):

        pn = 0
        foo+="\n\t// int i ="+str(i)
        for (x,y) in p:
            foo+="\n\tvec2  pos"+str(i)+tab[pn]+" = get_pos"+str(pn)+"(["+str(x)+","+str(y)+"]);"
            pn +=1
        
        i+=1
    f.write(foo.encode('utf8'))
    return


def vis_color_mark(positions,f, app):
    foo = ""
    i = 0
    foo+="\n\t\tif(ss(pos,pos0a) || ss(pos,pos0b) || ss(pos,pos0c) || ss(pos,pos0d))"
    foo+="\n\t\t\t{vis_color =  mark_default;}"

    for p in (positions):
        ps = str(i)
        foo+="\n\t\telse if(ss(pos,pos"+ps+"a) || ss(pos,pos"+ps+"b) || ss(pos,pos"+ps+"c) || ss(pos,pos"+ps+"d))"
        if (i==22 or  i==0):
            foo+="\n\t\t\t{vis_color =  mark_color;}"
        else:
            foo+="\n\t\t\t{vis_color =  mark_default;}"
        i+=1
    foo+="\n\t\telse if((|ui-150|<2.0) || (|vi-150|<2.0))\n\t\t\t{vis_color =  mark_color;}"
    foo+=" \n\telse{vis_color =[F(pos),F(pos),F(pos)];}"
    f.write(foo.encode('utf8'))
    return



#itype: shape of fields
#otype: output tensor
#op1: unary operation involved
def readDiderot(p_out,app,pos,template):
    #read diderot ,template
    print "template", template
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    print "p_out+.diderot",p_out+".diderot"
    f = open(p_out+".diderot", 'w+')
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_in, line)
        if a0:
            #replace field input line
            #print "inshape"
            inShape(f,app)
            continue
        # is it output tensor line?
        b0 = re.search(foo_outTen, line)
        if b0:
            #print "outline"
            outLine(f, app)
            continue
        # operation on field
        c0 = re.search(foo_op,line)
        if c0:
            #print "replace op"
            replaceOp(f, app)
            continue
        d0 = re.search(foo_samplespread,line)
        if d0:
            vis_sample_spread(pos, f, app)
            continue
        j0 = re.search(foo_colorspread,line)
        if j0:
            vis_color_spread(pos, f, app)
            continue
        k1 = re.search(foo_color_mark, line)
        if k1:
            vis_color_mark(pos, f, app)
            continue
        g0 = re.search(foo_maxfieldOut,line)
        if g0:
            #print "probe output field type"
            foo="\n\tout = max(out, "+opfieldname1+"(pos));// update output based on last sample\n"
            f.write(foo.encode('utf8'))
            continue
        i0 = re.search(foo_sumfieldOut, line)
        if i0:
            #print "probe output field type"
            foo="\n\tout += "+opfieldname1+"(pos);// update output based on last sample\n"
            f.write(foo.encode('utf8'))
            continue
        h0 = re.search(foo_basein,line)
        if h0:
            # check if inside base fields
            foo="\n\tif (!inside(pos,"+fieldName(0)+")  // If not inside field domain,\n"
            f.write(foo.encode('utf8'))
            continue
        # length number of positions
        else:
            f.write(line)

    ftemplate.close()
    f.close()

# execute new diderot program
def runDiderot(p_out, app, pos, output, runtimepath, isNrrd, t_templatesize, nrrdname, product, PARAMS ):
    print "**********  runDidero***********"
    if(isNrrd):
        print "write diderot-isnrrd-true"
        m2=t_templatesize
        w_shape=" -s "+str(product)+" "+str(m2)
        print "./"+p_out+" -o "+nrrdname+PARAMS
        os.system("./"+p_out+" -o  "+nrrdname+PARAMS)
        os.system("./"+p_out+" -o  "+nrrdname+".nrrd "+PARAMS)
        os.system("unu reshape -i  "+nrrdname+".nrrd "+w_shape+" | unu save -f text -o "+p_out+".txt")
    else:
        print "write diderot-isnrrd-false"
        print "not is vis"
        executable = "./"+p_out+" "+ PARAMS
        print executable
        os.system(executable)


# write, compile, and execute new diderot program
# p_out names diderot program created
# names output nrrd file output
def writeDiderot(p_out, app, pos, output, runtimepath, isNrrd,t_templatesize,t_templatefile):
    print "************** writeDiderot1  aaa ********************"
    # write new diderot program
    readDiderot(p_out, app, pos,t_templatefile)
    # copy and compile diderot program
    diderotprogram = p_out+".diderot"
    os.system("cp "+p_out+".diderot "+output+".diderot")
    print "cp "+p_out+".diderot "+output+".diderot"
    os.system("rm "+p_out) # remove existing executable
    os.system(runtimepath + " " + diderotprogram)
    nrrdname = output     # name of nrrd file read
    # did it compile?
    print "************** writeDiderot1 bb ********************"
    if(not(os.path.exists(p_out))):
        # did not compile
        #print "did not compile"
        return (None, None)
    else:
        # remove txt
        print "************** writeDiderot1 cc  ********************"
        txfile  = p_out+".txt"
        os.system("rm "+txfile)
        # run executable
        shape = app.oty.shape
        # print "shape",shape
        print "************** writeDiderot1 dd********************"
        product = 1
        for x in shape:
            product *= x
        size = str(300)
        print "************** writeDiderot1 ee ********************"
        PARAMS = " -iresU "+size+" -iresV  "+size+ " -camOrtho true -camEye 8 0 0 -camFOV 15 -rayStep 0.01 "
        print "************** writeDiderot1 ff********************"
        runDiderot(p_out, app, pos, output, runtimepath, isNrrd, t_templatesize, nrrdname,product,  PARAMS )
        if(not(os.path.exists(txfile))):
            # did not execute
            #print "did not execute"
            return (true, None)
        else:
            os.system("unu quantize -b 8 -i "+ nrrdname+".nrrd -o "+output+".png")
            i = [".diderot ",".txt ",".c" ,".png "]
            for t in i:
                os.system("cp "+ p_out+t+output+t)

            os.system("rm "+p_out+"*")
            return (true, true)

