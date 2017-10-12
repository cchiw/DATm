import sys
import os

os.system("source ../../fire/firedrake/bin/activate")

sys.path.insert(0, 'base/')
sys.path.insert(0,'fem/')

from fem_iter_cmd import main_set, loop_main

pset=[99,19,9,0]
for p in pset:
    n = 5
    layer =1
    loop_main(n,layer, p)


pset=[99,19,9,0]
for p in pset:
    n = 1
    layer =2
    loop_main(n,layer, p)

pset=[99]
for p in pset:
    n = 1
    layer =3
    loop_main(n,layer, p)


pset=[99,19,9,0]
for p in pset:
    n = 4
    layer =2
    loop_main(n,layer, p)

pset=[99]
for p in pset:
    n = 4
    layer =3
    loop_main(n,layer, p)

#main_set()
    
