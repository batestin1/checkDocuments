
#############################################################################################################################
#   filename:checkDocuments.py                                                       
#   created: 2022-03-11                                                              
#   import your librarys below                                                    
#############################################################################################################################



class cpf(object):
    def __init__(self, cpf):
        """
        Class to interact with cpf brazilian numbers
        """
        self.cpf = cpf
    
    def check(self):
        cpf = self.cpf
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) > 11 or len(cpf) < 11:
            return False
        else:
            return True

    def forpoint(self):
        cpf = self.cpf
        if cpf != cpf.replace('.', '').replace('-', ''):
            return "CPF is already in the format you want"
        else:
            return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
    def forhyphen(self):
        cpf = self.cpf
        if cpf != cpf.replace('.', '').replace('-', ''):
            return "CPF is already in the format you want"
        else:
            return f"{cpf[0:9]}-{cpf[9:11]}"
    def format(self):
        cpf = self.cpf
        if len(cpf) == 14 or len(cpf) == 12:
            return cpf.replace('.', '').replace('-', '')
        else:
            return f"CPF is already formatted!"
    def generate(self):
        cpf = self.cpf
        cpf = cpf.replace('.', '').replace('-', '')
        *s, = cpf
        number = 0
        ncpf = []
        for i in range(11):
           number = number + i
           ncpf.append(number)

        new = "".join([str(_) for _ in ncpf])
        new = new[:11]
        newCPF = f"{new[0:3]}.{new[3:6]}.{new[6:9]}-{new[9:11]}"
        return newCPF
   
##########################################################################################################################33

class rg(object):
     def __init__(self, rg):
        """
        Class to interact with rg brazilian numbers
        """
        self.rg = rg

     def check(self):
        rg = self.rg
        rg = rg.replace('.', '').replace('-', '')
        if len(rg) > 9 or len(rg) < 9:
            return False
        else:
            return True
     def format(self):
         rg = self.rg
         if len(rg) == 9:
             return f"{rg[0:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:9]}"
         else:
             return f"RG is already formatted!"
     def unformatted(self):
         rg = self.rg
         if len(rg) == 12:
             return rg.replace('.', '').replace('-', '')
         else:
             return f"RG is already unformatted"
     def generate(self):
         rg = self.rg
         rg = rg.replace('.', '').replace('-', '')
         *s, = rg
         number = 1
         nrg = []
         for i in range(11):
            number = number + i
            nrg.append(number)
 
         new = "".join([str(_) for _ in nrg])
         new = new[:9]
         newRG = f"{new[0:2]}.{new[2:5]}.{new[5:8]}-{new[8:9]}"
         return newRG
##############################################################################################################################################

class cnpj(object):
     def __init__(self, cnpj):
        """
        Class to interact with cpnj brazilian numbers
        """
        self.cnpj = cnpj

     def check(self):
        cnpj = self.cnpj
        cnpj = cnpj.replace('.', '').replace('-', '').replace('/','')
        if len(cnpj) > 14 or len(cnpj) < 14:
            return False
        else:
            return True
     def format(self):
          cnpj = self.cnpj
          if len(cnpj) == 14:
              return f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
          else:
              return f"CNPJ is already formatted!"
     def unformatted(self):
          cnpj = self.cnpj
          if len(cnpj) == 18:
              return cnpj.replace('.', '').replace('-', '').replace('/','')
          else:
              return f"CNPJ is already unformatted"
     def generate(self):
         cnpj = self.cnpj
         cnpj = cnpj.replace('.', '').replace('-', '')
         *s, = cnpj
         number = 1
         ncnpj = []
         for i in range(18):
            number = number + i
            ncnpj.append(number)
 
         new = "".join([str(_) for _ in ncnpj])
         new = new[:14]
         newCNPJ = f"{new[0:2]}.{new[2:5]}.{new[5:8]}/0000-{new[12:]}"
         return newCNPJ
 
    
##############################################################################################################################################

class PIS(object):
     def __init__(self, PIS):
        """
        Class to interact with cpnj brazilian numbers
        """
        self.PIS = PIS
     def check(self):
        PIS = self.PIS
        cnpj = PIS.replace('.', '').replace('-', '').replace('/','')
        if len(PIS) > 14 or len(PIS) < 14:
            return False
        else:
            return True
     def format(self):
          PIS = self.PIS
          if len(PIS) == 11:
              return f"{PIS[0:3]}.{PIS[3:7]}.{PIS[7:10]}-{PIS[10:]}"
          else:
              return f"PIS is already formatted!"
     def unformatted(self):
          PIS = self.PIS
          if len(PIS) == 14:
              return PIS.replace('.', '').replace('-', '').replace('/','')
          else:
              return f"PIS is already unformatted"
     def generate(self):
         PIS = self.PIS
         PIS = PIS.replace('.', '').replace('-', '')
         *s, = PIS
         number = 1
         nPIS = []
         for i in range(14):
            number = number + i
            nPIS.append(number)
 
         new = "".join([str(_) for _ in nPIS])
         new = new[:14]
         newPIS = f"{new[0:3]}.{new[3:7]}.{new[7:10]}-{new[10:11]}"
         return newPIS
