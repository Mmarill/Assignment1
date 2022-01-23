class Datasource():

    cstmr_txt = "customers.txt"

    def ds_conn(self):
        try:
            file = open(self.cstmr_txt)
            ds = (True, "You are connected", self.cstmr_txt)
        except:
            ds = (False, "Connection failed", self.cstmr_txt)
        finally:
            file.close(self.cstmr_txt)
        return ds
    
