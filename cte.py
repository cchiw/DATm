import sys
import os



sys.path.insert(0, 'base/')
sys.path.insert(0,'cte/')

from cte_iter_cmd import main_set


# for quick use
# assumes first framework, and iterative search of test case
# first command is the number of arguments 
n_template = 0
shift = 1 # next command number

os.system("cp  -R /Users/chariseechiw/DATm2/stash  /Users/chariseechiw/DATm2/rst/")
main_set(n_template, shift)

os.system("rm *.pyc ")
os.system("rm */*.pyc ")
os.system("rm *.o ")
os.system("rm *.cxx ")
os.system("rm *.log ")
os.system("rm *.diderot")
os.system("rm p_observ* ")
os.system("rm symb_f*")
os.system("rm *.nrrd")
os.system("rm tmp*")