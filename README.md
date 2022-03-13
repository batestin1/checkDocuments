
<h1 align="center">
<img src="https://img.shields.io/static/v1?label=CHECKDOCUMENTS%20POR&message=Bates&color=7159c1&style=flat-square&logo=ghost"/>
<h3> <p align="center">CHECKDOCUMENTS </p> </h3>
<h3> <p align="center"> ================= </p> </h3>
>> <h3> Resume </h3>
<p> checkDocuments allows you to validate, format, unformat and generate new numbers of the main Brazilian documents such as <b> CPF, CNPJ, RG and PIS </b>
Each document <b> (CPF, CNPJ, RG and PIS) </b> has its own method that can be followed according to the examples below </p>
>> <h3> How install </h3>
```
pip install checkDocuments

```
>> <h3> How Works </h3>

<p> <b> EXEMPLES </b> </p>
####################### CPF method ###############################################
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

