from base_constants import *

class frame:
    def __init__(self, name, branch, revision, precision, path, coeff_style, in_tys, rst_ty, ucoeff_range, lpos, upos, num_pos, samples, krn, random_range, random_limit, space, layer, template):
        self.name = name
        # branch information
        self.branch = branch
        self.revision = revision
        self.precision = precision
        self.path = path
        # order of coefficients
        self.coeff_style = coeff_style
        # what type of arguments do we want to test?
        self.in_tys = in_tys
        # op1(t1) -> t2, what is the type of t2?
        self.rst_ty = rst_ty
        #coeff bounds
        self.ucoeff_range = ucoeff_range
        #position bounds
        if(lpos<-0.5 or  upos>0.5):
            return Exception ("outside position range ",lpos,upos)
        self.lpos = lpos
        self.upos = upos
        # number of positions
        if(num_pos>10):
            return Exception ("Too many positions: ", num_pos)
        self.num_pos = num_pos
        # number of samples
        if(num_pos>150):
            return Exception ("Too many samples: ", samples)
        self.samples = samples
        # some hardcoded pieces
        p_Observ = "p_observ"
        stash  = rst_data 
        # name of diderot program testing function created
        self.p_Observ = p_Observ
        # directory to stash tmp files
        self.stash = stash
        # name of output file with observed data
        self.output = stash+"/output5_"+p_Observ
         # name of synthetic field created
        self.inputfile = stash+"/inputfile"
        self.krn = krn
        #------------------- randomize
        self.random_limit = random_limit
        # needs to be an interger
        #if(random_limit == None):
        self.random_range = random_range
        self.space = space
        #------------------- layer of operators
        self.layer = layer

        self.template = template
    #-------------------- translation --------------------
    def get_name(self):
        return self.name
    def get_rst_ty(self):
        return self.rst_ty
    def get_in_tys (self):
        return self.in_tys
    def get_coeff_style(self):
        return self.coeff_style
    def get_samples(self):
        return self.samples
    def g_ucoeff(self):
        return self.ucoeff_range
    def get_lpos(self):
        return self.lpos
    def get_upos(self):
        return self.upos
    def get_num_pos(self):
        return self.num_pos
    def get_branch(self):
        return self.branch
    def get_revision(self):
        return self.revision
    def get_path(self):
        return self.path
    def get_precision(self):
        return self.precision
    def get_p_Observ(self):
        return self.p_Observ
    def get_output(self):
        return self.output
    def get_inputfile(self):
        return self.inputfile
    def get_krn(self):
        return self.krn
    def get_random_range(self):
        return self.random_range
    def get_random_limit(self):
        return self.random_limit
    def get_space(self):
        return self.space
    def get_layer(self):
        return self.layer
    def get_template(self):
        return  self.template
    
    def transform_fullpath(self,  branch, precision):
        path = self.path
        if(branch == branch_vis15):
            path+= "vis15/bin/diderotc --exec "
        elif(branch == branch_chiw17):
            path+= "chiw17/bin/diderotc --exec "
        elif(branch == branch_ein16):
            path+= "ein16/bin/diderotc "
        elif(branch == branch_other):
            path+= branch_other+"bin/diderotc  "
        if(precision ==precision_double):
            path+= " --double "
        return path
    
    def transform_runtimepath(self):
        path = self.path
        branch = self.branch
        precision = self.precision
        return frame.transform_fullpath(self,  branch, precision)

    def transform_nrrdpath(self):
        # decides to use vis15 path to create nrrd files
        path = self.path
        if(self.branch==branch_other):
            return frame.transform_fullpath(self, branch_vis15, precision_single)
        else:
            return frame.transform_fullpath(self, branch_vis15, precision_single)

    # does the branch create nrrd file
    # if so need to convert file to a text file
    def transform_isNrrd(self):
        branch = self.branch
        if(branch == branch_vis15 or branch==branch_chiw17):
            return True
        elif(branch == branch_ein16):
            return False
        elif(branch == branch_other):
            return False # assumption

    def transform_template_size(self):
        if(self.template==template_isIso):
            return 300
        elif(self.template ==template_isMipMax or  self.template ==template_isMipSum):
            return 300 #300x300
        elif(self.template==template_isPlain):
            raise Exception ("plain template"+self.template)

    def transform_template_file(self):
        if(self.template==template_isPlain):
            return "shared/template/foo.ddro"
        elif(self.template==template_isMipMax):
            return "shared/template/sum.ddro"
        elif(self.template==template_isMipSum):
            return "shared/template/mip.ddro"
        elif(self.template==template_isIso):
            return "shared/template/iso.ddro"
