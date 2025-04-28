import random

wordList = []
word=""
guesses=""
option = int(0)
difficulty = int(0)

with open("animals.txt", 'r') as f:
    animalList = [line.strip() for line in f]

while option != 1 or option !=2 :
    option = int(input("Choose word list to be used: \n" \
    "       1. Animals\n" \
    "       2. Common Word\n"))

    if option == int(1):
        #source = https://github.com/sroberts/wordlists/blob/master/animals.txt
        with open("animals.txt", 'r') as f:
            wordList = [line.strip() for line in f]
            word = random.choice(animalList)
            break
    elif option == 2:
        #source = https://github.com/dolph/dictionary/blob/master/popular.txt
        with open("popular.txt", 'r') as f:
            wordList = [line.strip() for line in f]
            word = random.choice(animalList)
            break
    else:
        print("Select a valid option!")

while difficulty>3 or difficulty<1:
    difficulty = int(input("1. Easy\n2. Medium\n3. Hard" \
    "\nSelect Difficulty(1-3): "))

    if difficulty == 1:
        turns = 20
        break
    elif difficulty == 2:
        turns = 10
        break
    elif difficulty ==3:
        turns = 3
        break
    else:
        print("Select a valid option!")

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" \n")

        else:
            print("_\n")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses\n')

        if turns == 0:
            print("You Lose")
            print("The word was: ", word)


