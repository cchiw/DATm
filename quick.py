import sys
import os


sys.path.insert(0, 'cte/')
sys.path.insert(0, 'base/')
from cte_iter_cmd import *


# for quick use
# assumes first framework, and iterative search of test case
# first command is the number of arguments 
n_template = 0
shift = 1 # next command number
main_set(n_template, shift)
