import shelve

with shelve.open('D:\Python file\ShelfTest')as fruit:
    # fruit['orange'] = "a sweet, orange, citrus fruit"
    # fruit['apple'] = "good for making cinder"
    # fruit['lemon'] = "a sour, yellow citrus fruit "
    # fruit['grape'] = "a small, sweet fruit growing in bunches"
    # fruit['lime'] = "a sour, green citrus fruit"
    
    # while True:
    #     shelf_key = input("Please enter a fruit: ")
    #     if shelf_key =="quit":
    #         break
    #     if shelf_key in fruit:
    #         description = fruit.get(shelf_key)
    #         print(description)
    #     else:
    #         question= input("We dont have this fruit, would you like to add it? (Y/N) ").upper()
    #         if (question == "Y"):
    #             fruitn= input("Whats the fruit name? ")
    #             fruitd= input("How would you describe this fruit? ")
    #             fruit[fruitn] = fruitd
    ordered_keys = list(fruit.keys())
    #caso eu queria so imprimir em ordem
    #print(sorted(ordered_keys))
    #porem se precisar por algum motivo da lista na ordem certa:
    ordered_keys.sort()
    for f in ordered_keys:
        print(f +" - "+ fruit[f])

