locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = {0: {"Q":0},
         1: {"W":2,"E":3,"N":5,"S":4, "Q":0},
         2: {"N":5,"Q":0},
         3: {"W":1,"Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2,"S":1,"Q":0}}

name_exits ={1: {"2":2,"3":3,"5":5,"4":4},
             2: {"5":5},
             3: {"3":3},
             4: {"1":1,"2":2},
             5: {"2":2,"1":1}}

words = {"NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W",
         "QUIT" : "Q",
         "ROAD": "1",
         "HILL": "2",
         "BUILDING": "3",
         "VALLEY": "4",
         "FOREST": "5"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc =1
while True:
    availableExists=", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
         allExits=exits.copy()
         allExits.update(exits)
    direction = input("Available exits are "+ availableExists+ " ").upper()
    print()
    #PARSE USER INPUT USING OUR VOCABULARY DICTIONARY IF NECESSARY
    if len(direction)>1: #more than 1 letter, check words
        voc = direction.split()
        for word in voc:
            if word in words:
                direction=words[word]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cant go this direction")

