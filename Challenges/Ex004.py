variable = input("digite algo: ")
print("Sua variavel é do tipo ".format(type(variable)))

espaço= variable.isspace()
numerico= variable.isnumeric()
alfabetico= variable.isalpha()
alfanumerico= variable.isalnum()
Maiuscula= variable.isupper()
Minuscula= variable.islower()
Capitalizada= variable.istitle()
if espaço == True:
    print("Sua variavel é só espaços")
if numerico==True:
    print("Sua variavel é um numero")
if alfabetico==True:
    print("Sua variavel é alfabetica")
if alfanumerico==True:
    print("Sua variavel é alfanumerica")
if Maiuscula == True:
    print("Sua variavel é toda maiuscula")
if Minuscula ==True:
    print("Sua variavel é toda minuscula")
if Capitalizada == True:
    print("Sua variavel tem a primeira letra em maiusculo")