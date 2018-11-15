available_exits = ['norte', 'sul','leste','oeste']
choseen_exit=''
while choseen_exit not in available_exits:
    choseen_exit = input("Qual direção voce deseja ir?")
    if choseen_exit == 'quit':
        print("Game Over!")
        break
else:
    print('Ae krl finalmente conseguiu sair')