catoposto = float(input("Qual o cateto oposto? "))
catadjacente = float(input("Qual o cateto adjacente"))
hipotenusa = pow(pow(catoposto,2)+pow(catadjacente,2),1/2)
print("A hipotenusa é {:.2f}".format(hipotenusa))