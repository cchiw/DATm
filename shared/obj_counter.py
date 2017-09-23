
class counter:
    def __init__(self):
        self.rst_cnt = 0
        self.rst_l = 0
        self.rst_t = 0
        self.rst_t_compile = 0
        self.rst_t_terrible = 0
        self.rst_t_check= 0
        self.rst_t_good =0
        self.rst_t_eh= 0
        self.rst_t_NA = 0
        self.rst_t_run = 0
        self.rst_good = 0
        self.rst_eh = 0
        self.rst_terrible = 0
        self.rst_check = 0
        self.rst_compile = 0
        self.rst_cumulative = 0
        self.rst_NA = 0
        self.rst_run = 0
        self.rst_fp = 0
        self.cnt21=0
        self.cnt22=0
        self.cnt23=0
        self.cnt24=0
        self.cnt25=0
        self.cnt26=0
        self.cnt27=0
        self.cnt28=0
        self.cnt29=0
        self.cnt30=0
    def get_totals(self):
        return (self.rst_t_NA, self.rst_t_good, self.rst_t_eh, self.rst_t_check, self.rst_t_terrible, self.rst_t_compile, self.rst_t_run)
    def get_locals(self):
        return (self.rst_NA, self.rst_good, self.rst_eh, self.rst_check, self.rst_terrible, self.rst_compile, self.rst_run)
    def get_cnt(self):
        return self.cnt
    def get_cumulative(rst_self):
        return self.rst_cumulative
    def inc_compile(self):
        self.rst_compile +=1
        self.rst_t_compile +=1
    def inc_run(self):
        self.rst_run +=1
        self.rst_t_run +=1
    def inc_NA(self):
        self.rst_t_NA  +=1
        self.rst_NA  +=1
    def inc_cnt(self):
        self.rst_cnt += 1
    def inc_cumulative(self):
        self.rst_cumulative += 1
    def inc_total(self):
        self.rst_l+= 1
        self.rst_t+= 1
    def inc_fp(self):
        self.rst_fp += 1
    def inc_locals(self, rtn):
        # collect results
        (rtn_1, rst_good_1, rst_eh_1, rst_check_1, rst_terrible_1, rst_NA_1) = rtn
        self.rst_good +=  rst_good_1
        self.rst_t_good +=  rst_good_1
        self.rst_eh += rst_eh_1
        self.rst_t_eh += rst_eh_1
        self.rst_check  += rst_check_1
        self.rst_t_check+=rst_check_1
        self.rst_terrible += rst_terrible_1
        self.rst_t_terrible += rst_terrible_1
        self.rst_NA += rst_NA_1
        self.rst_t_NA += rst_NA_1
    def zero_locals(self):
        # zero locals
        self.rst_good =  0
        self.rst_eh = 0
        self.rst_terrible = 0
        self.rst_check  = 0
        self.rst_compile = 0
        self.rst_run = 0
        self.rst_NA = 0
        self.rst_cnt = 0
    def zero_total(self):
        self.rst_l = 0
    def writeCumulativeS(self):
        rst_t_good = self.rst_t_good
        rst_t_eh = self.rst_t_eh
        rst_t_check = self.rst_t_check
        rst_t_terrible = self.rst_t_terrible
        rst_t_NA = self.rst_t_NA
        rst_t_compile = self.rst_t_compile
        rst_t_run= self.rst_t_run
        rst_cumulative = self.rst_cumulative
        rst_l = self.rst_l
        rst_t = self.rst_t
        rst_cnt = self.rst_cnt
        rst_fp = self.rst_fp
        x= "\n\n # cumulative break down  # "+str(rst_cumulative)
        if(rst_t_good >0):
            x+=" total A:"+str(rst_t_good) +"|"+str(rst_cumulative)
        if(rst_t_eh>0):
            x+=" total  B:"+str(rst_t_eh)+"|"+str(rst_cumulative)
        if(rst_t_check >0):
            x+=" total  C:"+str(rst_t_check )+"|"+str(rst_cumulative)
        if(rst_t_terrible>0):
            x+=" total  D:"+str(rst_t_terrible)+"|"+str(rst_cumulative)
        if (rst_t_NA>0):
            x+=" total  NA:"+str(rst_t_NA)+"|"+str(rst_cumulative)
        if(rst_t_compile>0):
            x+=" total  did not compile :"+str(rst_t_compile)+"|"+str(rst_cumulative)
        if(rst_t_run>0):
            x+=" total  did not run :"+str(rst_t_run)+"|"+str(rst_cumulative)
        if (rst_fp >0):
            x+= "total ran but delivered a false positive:" + str(rst_t_run)+"|"+str(rst_cumulative)
        
        x+= " total  iterations-t: " +str(rst_t)
        x+= " total  cumulative: "+str(rst_cumulative)
        x+= " total  cnt: "+str(rst_cnt)
        return x
    def  writeLocal(self):
        rst_cnt = self.rst_cnt
        rst_good = self.rst_good
        rst_eh = self.rst_eh
        rst_check = self.rst_check
        rst_terrible = self.rst_terrible
        rst_NA = self.rst_NA
        rst_cumulative = self.rst_cumulative
        rst_l  = self.rst_l
        rst_t  = self.rst_t
        rst_compile = self.rst_compile
        rst_run= self.rst_run
        x= ""
        if(rst_good>0):
            x+=" A:"+str(rst_good)+"|"+str(rst_cnt)
        if(rst_eh>0):
            x+=" B:"+str( rst_eh)+"|"+str(rst_cnt)
        if(rst_check>0):
            x+=" C:"+str( rst_check)+"|"+str(rst_cnt)
        if(rst_terrible>0):
            x+=" D:"+str( rst_terrible)+"|"+str(rst_cnt)
        if (rst_NA>0):
            x+=" NA:"+str(rst_NA)+"|"+str(rst_cnt)
        if(rst_compile>0):
            x+=" did not compile: "+str( rst_compile)
        if(rst_run>0):
            x+=" did not run: "+str( rst_run)
        x+= " ran: "+str(rst_cnt)
        x+= " iterations-l: " +str(rst_l)
        x+= " iterations-t: " +str(rst_t)
        x+= " cumulative: "+str(rst_cumulative)
        return x

def get_counter():
    return counter()
