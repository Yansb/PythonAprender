salario = float(input("Qual o salario do funcionario? R$ "))
aumento = salario + (salario*15/100)
print("O salario do funcionario que era {:.2f} vai virar {:.2f} se tiver 15% de aumento".format(salario, aumento))