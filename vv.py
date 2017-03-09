import sys
import os


sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')

from vis_iter_cmd import *


# for quick use
# assumes first framework, and iterative search of test case
# first command is the number of arguments 
#n_template = 1 # summation
n_template = 2 # max
#n_template = 3 # isosurface

shift = 1 # next command number
main_set(n_template, shift)
