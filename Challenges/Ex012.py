preço = float(input("Qual o preço do produto? R$ "))
desconto = (preço*5)/100
preço_final = preço-desconto
print("O seu produto que custava {}, fica {:.2f} com 5% de desconto".format(preço, preço_final))
