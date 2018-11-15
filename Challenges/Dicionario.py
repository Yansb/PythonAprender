estado= dict()
brasil= list()
for c in range (0,3):
    estado['uf'] = input("Unidade Federativa: ")
    estado['sigla'] = input("Sigla do estado: ")
    brasil.append(estado.copy())
for e in brasil:
    #O E VAI RODAR POR DENTRO DE BRASIL PARA CADA ESTADO
    for v in e.values():
        #O V VAI RODAR DENTRO DOS ESTADOS QUE SAO UM DICIONARIO DENTRO DA LISTA BRASIL
        #E IMPRIMIR OS SEUS VALORES
        print(v, end=' ')
    print()