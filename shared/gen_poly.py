import numpy as np
from itertools import repeat
from sympy.parsing.sympy_parser import parse_expr




def mult(string, reps):
    if reps == 0:
        return("1.0")
    temp = " * ".join(repeat(string,reps))
    return("(" + temp + ")")


def polyString(variable_names, coords):
    cs = coords.shape
    cshape_len = len(cs)
    vname = len(variable_names)
    if (vname != cshape_len):
        raise ValueError("Number of coordinate arrays not in accordane with number of variables")
    if (vname == 1):
        v = variable_names[0]
        print(cs[0])
        print(len(coords))
        print(range(cs[0]))
        terms = map(lambda x: str(coords[x]) + " * " + mult(v,x), range(cs[0]))
        temp = " + ".join(terms)
        return("(" + temp + ")")
    else:
        v = variable_names[0]
        new_variable_names = variable_names[1:]
        terms = map(lambda x : polyString(new_variable_names, coords[x]) + " * " + mult(v,x), range(cs[0]))
        temp = " + ".join(terms)
        return("(" + temp + ")" )
        
        

class poly:
    def __init__(self,dim,degree,coords):
        """
        This class is deserving of 
        """
        d = degree +1
        spec_shape = tuple([(d) for x in range(dim)])
        array_var_names = map(lambda x: "x["+str(x)+"]",range(dim))
        array_poly = polyString(array_var_names,coords)
        self.array_poly = array_poly
        normal_var_names = map(lambda x: "x"+str(x),range(dim))
        normal_poly = polyString(normal_var_names,coords)
        self.normal_poly = normal_poly
        
      
        
        if(spec_shape == coords.shape):
            raise ValueError("Polynomial coords shape not in accordance with dim and degree")
        self.coords = coords
        self.python_func = "lambda x: " + array_poly
        self.sympy_exp = parse_expr(normal_poly)

    def did_function (self,name):
        "function " + "tensor[{0}] ".format(self.dim) + name + "(x) = " + self.array_poly + " ;"
