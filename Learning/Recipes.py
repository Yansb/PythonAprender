import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beans_on_toast = ['beans', 'bread']
# scrambled_eggs = ['eggs', 'butter', 'milk']
# soup = ['tin of soup']
# pasta = ['pasta', 'cheese']

with shelve.open('D:\\Python file\\recipes') as recipes:
    # recipes['blt'] = blt
    # recipes['beans on toast'] = beans_on_toast
    # recipes['scrambled eggs'] = scrambled_eggs
    # recipes['pasta'] = pasta
    # recipes['soup'] = soup
    #
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes['blt'] =temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes['pasta'] = temp_list
    for snack in recipes:
        print(snack, recipes[snack])
