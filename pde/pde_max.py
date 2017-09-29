

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


A = assemble(a,bcs=[bc])
# Define linear form
L = f*v*dx
b = assemble(L)
                """.format(c,i)
    return(solve_string)


def max_check(n):
    sovle_string="""
import numpy as np
def test_fp(A,u,bc):
    M = A.M.values
    uarray = u.dat.data
    s = u.dat.data.shape[0]
    ln = np.array(list(range(0,s)),dtype=int)
    bcn  = bc.nodes
    bs = bcn.shape[0]
    nbc = np.zeros((s-bs,),dtype=int)
    i = 0
    for x in ln:
        if x in bcn:
            continue
        else:
            nbc[i]=x
            i+=1
        
    
    Kb = np.zeros((s-bs,bs),dtype="float64")
    Ko = np.zeros((s-bs,s-bs),dtype="float64")
    ub = np.zeros((bs,),dtype="float64")
    uo = np.zeros((s-bs,),dtype="float64")
    Ko = M[np.ix_(nbc,nbc)]
    Kb = M[np.ix_(nbc,bcn)]
    ub = uarray[(bcn)]
    uo = uarray[(nbc)]

    Koinv = np.linalg.inv(Ko)
    m1 = Koinv >= 0
    m2 = (-1)*Koinv.dot(Kb) >= 0
    temp = (-1)*Koinv.dot(Kb)
    e = np.ones((bs),dtype="float64")
    m3 = temp.dot(e) <= 1
    t = m1.all() and m2.all() and m3.all()
    return(t)
t = test_fp(A,{0},bc)
if(not(t)):
    exit(25)

""".format(n)
    return(sovle_string)
