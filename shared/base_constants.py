#top layer of dependence


#-------------- Different Field Definitions ----------------------
field_pde = "pde field"
field_cfe = "closed-form expression field"
field_conv = "dicrete image data field"



#-------------- PDE test variables ----------------------
#flag_vis_test = False
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
branch_dev = "Diderot-Dev"
branch_fem = "femprime"
branch_other = "*/"



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
c_version =""



#strings in diderot template
foo_in="foo_in"
foo_outTen="foo_outTen"
foo_op ="foo_op"
foo_probe ="foo_probe"
foo_length="foo_length"
foo_limits = "foo_limits"
foo_posIn = "foo_posIn"
foo_posLast = "foo_posLast"
foo_basis = "foo_basis"
#otherwise variables in diderot program
foo_out="out"
foo_pos="pos"
const_out ="7.2"
const_probeG_cfe = "GCFE"
const_probeG_conv = "G"