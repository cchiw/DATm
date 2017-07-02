# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs
import sys
import os
import re

# shared base programs
from obj_ex import *
from obj_apply import *
from obj_ty import *
from obj_operator import *
from obj_field import *
from base_constants import *
from base_cond import *
adj = (opr_adj)
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
opfieldname1="G"



##################################### input tensor/field #####################################
#field input line
#f: file to write to
#k:continuity
#itypes: types for input field
#inputlist: name for input data
def inShape_base(f, exps):
    #app = apply.get_root_app(appC)
    i=0
    for exp in exps:
        #print "current fld",field.toStr(exp)
        dim = field.get_dim(exp)
        fieldShape(f, exp.fldty)
        if (field.get_isField(exp)):
            krnstr = exp.krn.str
            foo= fieldName(i)+" = "+krnstr+u'⊛'+"  image(\""+exp.inputfile+".nrrd\");\n"
            f.write(foo.encode('utf8'))
        else: #tensor type
            foo= fieldName(i)+" = "+str(field.get_data(exp))+";\n"
            f.write(foo.encode('utf8'))
        i+=1
#inputlist: name for input data
def inShape(f, appC):
    exps = apply.get_all_Fields(appC)
    inShape_base(f, exps)



##################################### other #####################################
# probes field at variable position
def isProbe(exp, fld):
    if(fty.is_Field(fld)):
        return "("+exp+")(pos)"
    else:
        return "("+exp+")"

##ff: field that is being probed or tensor variable inside if statement
def check_conditional(f, ff, app):
    # probes field at variable position
    oty = app.oty
    set =  "\t"+foo_out+" = "+isProbe(ff,oty)+";\n"
    foo =  ""
    if(app.isrootlhs or oty.dim==1):
        foo = set
    else: #twice embedded
        # there might be a conditional restraint
        foo= getCond(app, set)
    f.write(foo.encode('utf8'))
    return

##################################### probe field at positions #####################################
# set positions variables
# index field at position
def base_index_field_at_positions(f, pos, dim):
    print "index at positions"
    i=0
    foo="\t\t"
    if(dim==1):
        foo+="real  "+foo_pos+"=0;\n"
    elif(dim==2):
        foo+="tensor [2] "+foo_pos+"=[0,0];\n"
    elif(dim==3):
        foo+="tensor [3] "+foo_pos+"=[0,0,0];\n"
    # does first position
    p=str(pos[0])
    foo += "\t\tif(i=="+str(i)+"){\n"
    # just sets poitions
    foo += "\t\t\t"+foo_pos+" = "+"("+p+");\n"
    # probes field at position
    foo += "\t\t}\n"
    i=i+1
    for p1 in pos:
        p=str(p1)
        foo += "\t\telse if(i=="+str(i)+"){\n"
        # just sets poitions
        foo += "\t\t\t"+foo_pos+" = "+"("+p+");\n"
        # probes field at current position
        foo += "\t\t}\n"
        i=i+1
    f.write(foo.encode('utf8'))

def index_field_at_positions(f, pos, app):
    oty = app.oty
    return base_index_field_at_positions(f, pos, oty)