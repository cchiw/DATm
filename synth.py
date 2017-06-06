import sys
import os



sys.path.insert(0, 'shared/')
sys.path.insert(0,'synProg/')
sys.path.insert(0,'nc/')

from prog_current import *

os.system("rm rst/data/*")


# for quick use
# assumes first framework, and iterative search of test case
# first command is the number of arguments 
n_template = 0
# get testing framework
testing_frame = set_template(n_template)
# get counter
cnt = get_counter()
attempt(testing_frame, cnt)


os.system("rm *.pyc ")
os.system("rm */*.pyc ")
os.system("rm *.o ")
os.system("rm *.cxx ")
os.system("rm *.log ")
os.system("rm *.diderot")
os.system("rm p_observ*")
os.system("rm symb_f*")
os.system("rm *.nrrd")
os.system("rm tmp*")
