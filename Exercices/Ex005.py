a= int(input("Digite um numero: "))
antes= a-1
depois= a+1
print("O antecessor de {0} é {1} e o seu sucessor é {2}".format(a, antes, depois))
#Forma mais facil e mais eficiente pois so precisa de uma atividade
#################################
print("O antecessor de {0} é {1} e o seu sucessor é {2}".format(a, (a-1), (a+1)))