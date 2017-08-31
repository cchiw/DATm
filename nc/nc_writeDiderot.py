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


def nc_setLength(f, n):
    foo="int length ="+str(n)+";"
    f.write(foo.encode('utf8'))

################################  compile and run a diderot program ################################
# execute new diderot program
def runDiderot(p_out, shape, pos, output, runtimepath, isNrrd):
    product = 1
    for x in shape:
        product *= x
    if(isNrrd):
        m2 = len(pos)+1
        w_shape=" -s "+str(product)+" "+str(m2)
        os.system("rm tmp.nrrd")
        os.system("./"+p_out+" -o tmp.nrrd")
        os.system("unu reshape -i tmp.nrrd "+w_shape+" | unu save -f text -o "+p_out+".txt")
        diderotprogram = p_out+".diderot"
   
        # comment in if creating rtests
        #os.system("rm rst/tmp/*.nrrd")
        #os.system("/Users/chariseechiw/diderot/vis15/bin/diderotc --exec  " + diderotprogram)
        #os.system("./"+p_out+" -o "+ "rst/tmp/correct_sng.nrrd")
        #os.system("/Users/chariseechiw/diderot/vis15/bin/diderotc --exec --double " + diderotprogram)
        #os.system("./"+p_out+" -o "+  "rst/tmp/correct_dbl.nrrd")

    else:
        # not is vis
        executable = "./"+p_out
        os.system(executable)

def nc_compileandRun(p_out, shape, pos, output, runtimepath, isNrrd, startall):
    diderotprogram = p_out+".diderot"
    os.system("cp "+p_out+".diderot "+output+".diderot")
    os.system("rm "+p_out) # remove existing executable
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
        os.system("rm "+txfile)
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
