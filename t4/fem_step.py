import sys
import os


sys.path.insert(0, '../')
sys.path.insert(0, '../shared/')
sys.path.insert(0,'../fem/')
sys.path.insert(0,'../cte/')
sys.path.insert(0,'../nc/')


from fem_iter_cmd import main_set


main_set()

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
