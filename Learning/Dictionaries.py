import shelve

fruit= {"Orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "lime": 'a sour, green citrus fruit'}

fruit["pear"]= "an odd shaped apple"
#ordered_keys = list(fruit.keys())
#ordered_keys.sort()


ordered_keys=sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f+ " - "+ fruit[f])


#Se colocar a mesma 'key' pra duas palavras diferentes ele so vai mudar o significado
while True:
    dic_key=input("Please enter a fruit: ")
    if dic_key == "quit":
        break
    if dic_key in fruit:
        description = fruit.get(dic_key)
        print(description)
    else:
        answer= input('This Fruit isnt in the dictionary, would you like to add it? (Y/N): ').upper()
        if answer == "Y":
            newf=input("what is the new fruit? \n")
            newd=input("what is the new fruit description? \n")
            fruit[newf] = newd
        else:
           break
