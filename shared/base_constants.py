#top layer of dependence
#-------------- order of coefficients ----------------------
# chooose order of coefficients
coeff_cubic = "cubic"
coeff_quadratic ="quadratic"
coeff_linear ="linear"

#-------------------------- types --------------------------
ty_F ="all fields"
ty_T ="all tensors"
ty_All ="mix of tensors and fields"


branch_chiw17 = "chiw17"
branch_vis15 = "vis15"
branch_ein16 = "ein16"
branch_other = "vis15-old/"
branch_other = "dev_old/"

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


template_isPlain = "t_plain"
template_isMipMax = "t_mipMax"
template_isMipSum = "t_mipSum"
template_isIso = "t_iso"


#directory to save programs
rst_data = "rst/data"
rst_stash="rst/stash"