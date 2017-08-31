make clean
make ex1.o
make ex1_init.o
make ex1_init.so
py.test -v ex1.py
rm *.o
rm *.so
rm *.h
rm *.log