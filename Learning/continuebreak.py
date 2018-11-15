meal = ["egg", "bacon", "spam", "sausages"]
for item in meal:
    if item == 'spam':
        nasty_food_item =item
        break

if nasty_food_item:
    print("cant i have anything without spam in it?")