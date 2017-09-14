

def max_test(test):
    solve_string = """
# Define Dirichlet boundary
def inside(x, on_boundary):
    return on_boundary


# Define boundary condition
u0 = Constant(f2)
bc = DirichletBC(V, u0, (1,2,3,4))

# Define trial and test functions
u = TrialFunction(V)
v = TestFunction(V)

# Define normal component, mesh size and right-hand side
h = CellSize(V.mesh())
h_avg = (h('+') + h('-'))/2.0
n = FacetNormal(V.mesh())
x = SpatialCoordinate(V.mesh())
f = Constant(f1) #interpolate(Expression("(x[0]*x[0]+x[1]*x[1])*(x[0]*x[0]+x[1]*x[1])"),V)

# Penalty parameter that must be played around with
alpha = Constant(8.0) #dependent on the mesh, I think???

# Define bilinear form
a = inner(div(grad(u)), div(grad(v)))*dx \
  - inner(avg(div(grad(u))), jump(grad(v), n))*dS \
  - inner(jump(grad(u), n), avg(div(grad(v))))*dS \
  + alpha/h_avg*inner(jump(grad(u),n), jump(grad(v),n))*dS



# Define linear form
L = f*v*dx
b = assemble(L)
                """
    return(solve_string)
