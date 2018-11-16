import shelve
with shelve.open("D:\Python file\location") as location:
    with shelve.open("D:\\Python file\\vocabulary") as vocabulary:

        loc = '1'
        while True:
            availableExits = ", ".join(location[loc]["exits"].keys())

            print(location[loc]["desc"])

            if loc == '0':
                break
            else:
                allExits = location[loc]["exits"].copy()
                allExits.update(location[loc]["namedExits"])

            direction = input("Available exits are " + availableExits).upper()
            print()

            # Parse the user input, using our vocabulary dictionary if necessary
            if len(direction) > 1:  # more than 1 letter, so check vocab
                words = direction.split()
                for word in words:
                    if word in vocabulary:   # does it contain a word we know?
                        direction = vocabulary[word]
                        break

            if direction in allExits:
                loc = allExits[direction]
            else:
                print("You cannot go in that direction")