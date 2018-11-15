import random
highest =1000
answer = random.randint(1, highest)
guess = int(input("Pless guess a number: "))
i = int("0")
if (guess == 0):
    quit()
if (guess > highest or guess < 1):
    guess = int(input('Please try a number between 1 and {}'.format(highest)))
elif(guess != answer):
    while guess != answer or i != 10:
        i += 1
        if (guess > answer):
            print("You guessed too high, please try a lower number: ")
        if (guess < answer):
            print("You guessed a lower number,\n try to aim a little higher: ")
        guess = int(input())
if (guess == answer):
    print("congratulations you guessed correctly !!!!!")
