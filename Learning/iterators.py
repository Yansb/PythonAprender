string = ['1','2','3','4','5','6','7']

meu_iterator = iter(string)
for i in range(0, len(string)):
    print(next(meu_iterator))
    i +=1