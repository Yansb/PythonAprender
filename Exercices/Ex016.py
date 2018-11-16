import math
numero = float(input("digite um numero: "))
pardec, parint = math.modf(numero)
print("a parte inteira desse numero é {:.0f} e a decimal é{:.2f}".format(parint, pardec))