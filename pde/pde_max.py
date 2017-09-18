

def max_test(test,dim,i):
    c = 32.0 if dim==2 else 32.0
    if test == "biharmonic":
        solve_string = """
# Define Dirichlet boundary
def inside(x, on_boundary):
    return on_boundary


# Define boundary condition
u0{1} = interpolate(bexpf{1},V)
bc = DirichletBC(V, u0{1}, (1,2,3,4))

# Define trial and test functions
u = TrialFunction(V)
v = TestFunction(V)

# Define normal component, mesh size and right-hand side
h = CellSize(V.mesh())
h_avg = (h('+') + h('-'))/2.0
n = FacetNormal(V.mesh())
x = SpatialCoordinate(V.mesh())
f = (f1{1}) 

# Penalty parameter that must be played around with
alpha = Constant({0}) #dependent on the mesh, I think???

# Define bilinear form
a = inner(L(u), L(v))*dx \
  - inner(avg(L(u)), jump(grad(v), n))*dS \
  - inner(jump(grad(u), n), avg(L(v)))*dS \
  + alpha/h_avg*inner(jump(grad(u),n), jump(grad(v),n))*dS



# Define linear form
L = f*v*dx
b = assemble(L)
                """.format(c,i)
    return(solve_string)
