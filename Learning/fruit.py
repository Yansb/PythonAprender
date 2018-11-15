fruit= {"Orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "lime": 'a sour, green citrus fruit'}

print(fruit)
veg= {"cabbage":"every child favourite",
      "sprouts":"mmmm,lovely",
      "spinach":"can i have some more fruits please?"
}
# print(veg)
#
# veg.update(fruit)
# print(veg)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)