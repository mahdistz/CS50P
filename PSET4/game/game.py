import random

while True:
    level = input("Level: ")
    if not level.isdigit():
        continue
    number = random.randint(0, int(level))
    while True:
        guess = input("Guess: ")
        if not guess.isdigit() or int(guess) > int(level):
            continue
        if int(guess) > number:
            print("Too large!")
        elif int(guess) < number:
            print("Too small!")
        else:
            print("Just right!")
            break
    break
