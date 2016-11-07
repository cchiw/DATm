import sys
import os


sys.path.insert(0, 'shared/')
sys.path.insert(0, 'visver/')

from vis_iter_cmd import *


# for quick use
# assumes first framework, and iterative search of test case
# first command is the number of arguments 
n_template = 1
shift = 1 # next command number
main_set(n_template, shift)
