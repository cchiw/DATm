import sys
import os

sys.path.insert(0,'cte/')
sys.path.insert(0,'fem/')
sys.path.insert(0, 'shared/')

from base_write import *
from input import get_testing_frame, c_pde_test

# shared base programs
from obj_apply import *
from obj_ex import  *
from obj_counter import *
from obj_field import *
from obj_frame import  *

# specific fem programs
from fem_iter_cmd import fem_cmd
from cte_iter_cmd import cte_cmd


# get testing framework
testing_frame = get_testing_frame()
# writing heading based on framework
write_heading(testing_frame)
# get counter
cnt = get_counter()

start_standard = time.time()
########################
if(c_pde_test):
    fem_cmd(testing_frame, cnt)
else:
    cte_cmd(testing_frame, cnt)
########################
end_standard = time.time()
tt_standard  = " time all _standard "+str(end_standard  - start_standard )
writeall(tt_standard )
print (tt_standard )
x = counter.writeCumulativeS(cnt)
writeFinalCumulative(x)
writeFinalCumulative(tt_standard)





