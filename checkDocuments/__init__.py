
#############################################################################################################################
#   filename:checkDocuments.py                                                       
#   created: 2022-03-11                                                              
#   import your librarys below                                                    
#############################################################################################################################

from .checkDocuments import cpf, rg, cnpj, PIS

####################### METODO CPF ###############################################
#para verificar se o cpf existe, use o metodo abaixo!
#funciona com pontos e com -
#para visualizar o retorno, use o print()
#cpf("123456617-39").check()
############################
# para formatar com pontuação o cpf
#cpf("12345661739").forpoint() 
####################################
#para formatação com hifem
#cpf("12345661739").forhyphen()
#####################################
#para formatação correta do cpf
#cpf("123.456.789-39").format()
#para gerar um novo cpf use o metodo abaixo.
#cpf("123.456.789-39").generate()
############################### metodo RG #########################################
#para o padrão RG nacional, usamos como referencia as versões SP e RJ
#para checar se o rg é verdadeiro
#rg("12.345.678-9").check()
####################################################################
# para formatar o rg no padrão nacional
# rg("123456789").format()
###################################################################
# para reverter o processo de formatação
# rg("12.345.678-9").unformatted()
###################################################################
# para gerar novo rg
#rg("12.345.678-9").generate()

####################################################################################

#CPNPJ

# para verificar se o cnpj existe ou não
#cnpj("12.345.678/0000-90").check()
#para formatar o cnpj no padrão brasileiro
#cnpj("12345678000090").format()
#para o processo inverso da formatação
#cnpj("12.345.678/0000-90").unformatted()
# para gerar novos cnpjs
#cnpj("12.345.678/0000-90").generate()

#####################################################################################

#PIS
#para verificar se o pis existe ou não
#PIS("120.4602.746-0").check()
############################################
#para formatar o PIS no padrão brasileiro
#120.4602.746-0
#PIS("12046027460").format()
#para reverter o processo de formatação
#PIS("120.4602.746-0").unformatted()
#para gerar um novo PIS
#PIS("120.4602.746-0").generate()

