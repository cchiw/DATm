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
from cte_writeDiderot import cte_compileandRun, cte_setLength
# ^ builds from cte but perhaps move these functions to a new shared directory

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



#decide to skip conditional for this type of program
def prog_update_method(f, oty, pos):
    if(fty.is_Field(oty)):
        print "this is a field"
        # index field at random positions
        base_index_field_at_positions(f, pos, oty)
        foo =  "\t"+foo_out+" = "+isProbe(opfieldname1, oty)+";\n"
        f.write(foo.encode('utf8'))

#write operation between fields
#get output var name-lhs
def prog_printline(f, program):
    lines = program.lines
    for line in lines:
        print "line",line
        op1 = line.opr
        arity = op1.arity
        # output
        output = line.var
        oty = output.ty
        oname = output.name
        # names of lhs variables
        def rtn_rhs():
            if (arity==1):
                f0 = line.lhs.name
                return prntUnary(op1, f0)
            elif(arity==2):
                f0 = line.lhs.name
                f1 = line.rhs.name
                return prntBinary(op1, f0, f1)
            else:
                raise Exception("unsupported arity")
        rhs = rtn_rhs()
        pre = ""
        write_shape(pre, f, oty, oname, rhs)
    return

def prog_outLine(f, oty):
    print "\n outline-","type: ",oty.name
    if (fty.is_Field(oty)):
        #print "isfld-layer 1"
        outLineF(f, oty)
#skipping tensor part for now
#    else:
#        if(app.isrootlhs):
#            return gotop1(f,app, "\toutput ", foo_out)
#        elif((app.lhs).isrootlhs):
#            #print "twice embedded"
#            return gotop2(f,app, "\toutput ", foo_out)
#        else:
#            #print "third layers"
#            return gotop3(f, app, "\toutput ", foo_out

#itype: shape of fields
#otype: output tensor
#op1: unary operation involved
def prog_readDiderot(p_out, oty, program, fields, pos):
    print "oty", oty.name
    #read diderot template
    ftemplate = open(template, 'r')
    ftemplate.readline()
    #write diderot program
    f = open(p_out+".diderot", 'w+')
    for line in ftemplate:
        # is it initial field line?
        a0 = re.search(foo_in, line)
        if a0:
            #replace field input line
            inShape_base(f, fields)
            continue
        # is it output tensor line?
        b0 = re.search(foo_outTen, line)
        if b0:
            #print "outline"
            prog_outLine(f, oty)
            continue
        # operation on field
        c0 = re.search(foo_op, line)
        if c0:
            #print "replace op"
            prog_printline(f, program)
            continue
        # index field at position
        d0 = re.search(foo_probe,line)
        if d0:
            #print "update_method"
            prog_update_method(f, oty, pos)
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



# write, compile, and execute new diderot program
def prog_writeDiderot(p_out, program, fields, pos, output, runtimepath, isNrrd):
    # write new diderot program
    oty = program.oty
    prog_readDiderot(p_out, oty, program, fields, pos)

    #needed to pass
    startall = time.time()
    return cte_compileandRun(p_out, oty.shape, pos, output, runtimepath, isNrrd, startall)
    
