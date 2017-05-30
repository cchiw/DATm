# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re
import time
# shared base programs
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_write import * 
from base_writeDiderot import *
template="shared/template/foo.ddro"     # template

#strings in diderot template
foo_in="foo_in"
foo_outTen="foo_outTen"
foo_op ="foo_op"
foo_probe ="foo_probe"
foo_length="foo_length"
#otherwise variables in diderot program
foo_out="out"
foo_pos="pos"
const_out ="7.2"

#some functions are shared with prog* files

#witten inside update method
#conditionals are commented out
def cte_update_method(f, pos, app):
    oty = app.oty
    if(fty.is_Field(oty)):
        # index field at random positions
        base_index_field_at_positions(f, pos, oty)
        #check_inside(f, opfieldname1, app)
        foo =  "\t"+foo_out+" = "+isProbe(opfieldname1, oty)+";\n"
        f.write(foo.encode('utf8'))
        #check_conditional(f,  opfieldname1, app)
    else:
        # get conditional for tensor argument
        check_conditional(f,  foo_out, app)

def cte_setLength(f, n):
    foo="int length ="+str(n)+";"
    f.write(foo.encode('utf8'))

#itype: shape of fields
#otype: output tensor
#op1: unary operation involved
def readDiderot(p_out, app, pos):
    #read diderot template
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    f = open(p_out+".diderot", 'w+')
    #output type
 
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
        # index field at position
        d0 = re.search(foo_probe,line)
        if d0:
            #print "update_method"
            cte_update_method(f, pos, app)
            continue
        # length number of positions
        e0=re.search(foo_length, line)
        if e0:
            #print "Set length"
            cte_setLength(f,len(pos))
            continue
        # nothing is being replaced
        else:
            f.write(line)

    ftemplate.close()
    f.close()

# execute new diderot program
def runDiderot(p_out, shape, pos, output, runtimepath, isNrrd):

    product = 1
    for x in shape:
        product *= x

    if(isNrrd):
        m2 = len(pos)+1
        w_shape=" -s "+str(product)+" "+str(m2)
       
        os.system("./"+p_out+" -o tmp")
        os.system("./"+p_out+" -o tmp.nrrd")
    
        #os.system("unu head tmp.nrrd")
        os.system("unu reshape -i tmp.nrrd "+w_shape+" | unu save -f text -o "+p_out+".txt")
    else:

        # print "not is vis"
        executable = "./"+p_out
        #print executable
        os.system(executable)

def cte_compileandRun(p_out, shape, pos, output, runtimepath, isNrrd, startall):
    diderotprogram = p_out+".diderot"
    #os.system("cp "+p_out+".diderot "+output+".diderot")
    #os.system("rm "+p_out) # remove existing executable
    os.system(runtimepath + " --log " + diderotprogram)
    # gets come time
    # os.system("grep \"compiler\" "+p_out+".log >> catwriteall.txt")

    # did it compile?
    endall = time.time()
    tall = str(endall - startall)
    writeTime(25, tall)
    print(tall)
    startall=endall
    if(not(os.path.exists(p_out))):
        # did not compile
        #print "did not compile"
        endall = time.time()
        tall = str(endall - startall)
        writeTime(26, tall)
        startall=endall
        return (None, None, startall)
    else:
        # remove txt
        txfile  = p_out+".txt"
        #os.system("rm "+txfile)
        # run executable
        runDiderot(p_out, shape, pos, output, runtimepath, isNrrd)
        endall = time.time()
        tall = str(endall - startall)
        writeTime(26, tall)
        startall=endall
        if(not(os.path.exists(txfile))):
            # did not execute
            #raise Exception ("did not execute")
            return (true, None, startall)
        else:
            #print "compiled and execute"
            # copyfiles
            os.system("cp "+p_out+".txt "+output+".txt")
            #os.system("cp "+p_out+".c "+output+".c")
            #os.system("rm "+p_out+"*")
            return (true, true, startall)




# write, compile, and execute new diderot program
def writeDiderot(p_out, app, pos, output, runtimepath, isNrrd, startall):
    # write new diderot program
    readDiderot(p_out, app, pos)
    endall = time.time()
    tall = str(endall - startall)
    writeTime(24, tall)
    startall=endall
    shape = app.oty.shape
    return cte_compileandRun(p_out, shape, pos, output, runtimepath, isNrrd, startall)