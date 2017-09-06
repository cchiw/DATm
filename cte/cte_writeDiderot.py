# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re
import time

from nc_writeDiderot import nc_compileandRun, nc_setLength


# shared base programs
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_write import * 
from base_writeDiderot import *

from base_constants import *

template=c_template     # template

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

pde_test =false

#witten inside update method
#conditionals are commented out
def cte_update_method(f, pos, app):
    oty = app.oty
    if(fty.is_Field(oty)):
        # index field at random positions
        dim = oty.dim
        base_index_field_at_positions(f, pos, dim)
        check_inside(f, opfieldname1, app, pde_test)
        #foo =  "\t"+foo_out+" = "+isProbe(opfieldname1, oty)+";\n"
        #f.write(foo.encode('utf8'))
        #check_conditional(f,  opfieldname1, app)
    else:
        # get conditional for tensor argument
        check_conditional(f,  foo_out, app)

################################ search Diderot template and replace foo variable name ################################
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
            nc_setLength(f,len(pos))
            continue
        # nothing is being replaced
        else:
            f.write(line)

    ftemplate.close()
    f.close()

################################ write annd run main function ################################
# write, compile, and execute new diderot program
def writeDiderot(p_out, app, pos, output, runtimepath, isNrrd, startall):
    # write new diderot program
    readDiderot(p_out, app, pos)
    endall = time.time()
    tall = str(endall - startall)
    writeTime(24, tall)
    startall=endall
    shape = app.oty.shape
    return nc_compileandRun(p_out, shape, pos, output, runtimepath, isNrrd, startall)