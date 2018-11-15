livro = "Harry Potter"

letter = input("Enter a character: ")

if letter in livro:
    print("Give me an {} letter".format(letter))
else:
    print("I dont need that letter")