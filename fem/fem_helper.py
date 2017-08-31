def ty_toMesh(dim):
    if(dim==2):
        return "UnitSquareMesh(2,2)"
    elif(dim==3):
        return "UnitCubeMesh(2,2,2)"

def ty_toK():
    k_order = "2"
    return k_order

def ty_toElement():
    element ="Lagrange"
    return  element

