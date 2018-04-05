import sys
import os



sys.path.insert(0, 'base/')
sys.path.insert(0,'cte/')

from cte_iter_cmd import cte_main_set


os.system("rm  -r rst/stash/*")
os.system("mkdir rst")
os.system("cp  -R clean/rst  .")
os.system("mkdir rst")
os.system("mkdir rst/tmp")

def cte_main_set():
    # get testing framework
    shift = 1 # next command number
    testing_frame = get_testing_frame()
    # get counter
    cnt = get_counter()
    # writing heading based on framework
    write_heading(testing_frame)
    # constants (decides layer of testing)
    layer = frame.get_layer(testing_frame)
    # layer, and shift from constants (decides layer of testing)
    start_standard = time.time()
    #choose testing range based on commands
    args = int(sys.argv[shift])
    cmd(layer, testing_frame, cnt, shift, args)
    end_standard = time.time()
    tt_standard  = " time all _standard "+str(end_standard  - start_standard )
    writeall(tt_standard )
    print (tt_standard )



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