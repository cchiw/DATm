#top layer of dependence
#-------------- order of coefficients ----------------------
# chooose order of coefficients
coeff_cubic = "cubic"
coeff_quadratic ="quadratic"
coeff_linear ="linear"
coeff_order4 ="order4"

#-------------------------- types --------------------------
ty_F ="all fields"
ty_T ="all tensors"
ty_All ="mix of tensors and fields"


branch_chiw17 = "chiw17"
branch_vis15 = "vis15"
branch_ein16 = "ein16"


branch_other = "femprime/"


precision_double ="double"
precision_single ="singe"

#kernel(name, str, continuity, order) set in obj_Field
h_bs3 = "bspln3"
h_hex = "c4hexic"
h_tent= "tent"
h_ctmr= "ctmr"
h_mixcbc = "mix" # [h_hex,h_bs3,h_hex]
h_mixcbt = "mixt"
h_bs5 = "bspln5"


elem_Lagrange = "Lagrange"
elem_P = "P"
elem_random ="r" #randomly select element

mesh_UnitSquareMesh = "UnitSquareMesh"
mesh_UnitCubeMesh = "UnitCubeMesh"

fnspace_sca = "FunctionSpace"
fnspace_vec = "VectorFunctionSpace"
fnspace_ten = "TensorFunctionSpace"


template_isPlain = "t_plain"
template_isMipMax = "t_mipMax"
template_isMipSum = "t_mipSum"
template_isIso = "t_iso"
template_isFem = "t_fem"


#directory to save programs
rst_data = "rst/data"
rst_stash="rst/stash"

opr_adj = 0.1


c_pathToSynFiles = "shared/symb/symb_f"

 # template
c_template="shared/template/foo.ddro"

flag_vis_test = False
#flag_vis_test = True
#c_pde_test = False
c_pde_test = True
#c_pde_Inside = False #is inside implemented?
c_pde_Inside =  True

c_version ="" #current
#c_version ="_Aug27"
#c_version ="_Aug31"
