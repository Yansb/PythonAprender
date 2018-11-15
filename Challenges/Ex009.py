entrada = int(input("digite um numero para ver sua tabuada: "))
cont=0
print("_"*40)
for cont in range(0,11):
    mult = entrada * cont
    print("{} X {} = {}".format(entrada, cont,mult))
    cont += 1
print("_"*40)