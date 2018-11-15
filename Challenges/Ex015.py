dias = int(input("Quantos dias foi alugado? "))
quilometragem = int(input("Quantos kilometros foram andados? "))
preçodia = dias*60
preçokm = quilometragem*0.15
preçototal = preçodia+preçokm
print("O total a pagar é: {}".format(preçototal))
