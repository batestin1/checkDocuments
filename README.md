
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

<p> For all methods, and this includes CPF, CNPJ, PIS and RG, the commands are the same

check() to check
format() to format
unformatted() to unformat
generate() to generate a new one

</p>

<p> <b> EXEMPLES </b> </p>

>> CPF method 

<p> To check if the CPF exists </p>

```
from checkDocuments import cpf, rg, cnpj, PIS

cpf("123456617-39").check()

#Output can be TRUE or FALSE

```
<p> To format the CPF with punctuation </p>

```
from checkDocuments import cpf, rg, cnpj, PIS

cpf("12345661739").forpoint() 

#Output can be 123.456.617.39

```

<p> For hyphen formatting </p>

```
from checkDocuments import cpf, rg, cnpj, PIS

cpf("12345661739").forhyphen()

output can ben 123456173-39

```

<p> For full formatting </p>

```
from checkDocuments import cpf, rg, cnpj, PIS

cpf("123.456.789-39").format()

output can ben 123.456.173-39

```
<p> To generate a new number from the entered number </p>

```
from checkDocuments import cpf, rg, cnpj, PIS

cpf("123.456.789-39").generate()

output can ben 116.176.923-09

```


