import random

def random_word(file):
    with open(file, "r") as f:
        line = f.readlines()
        random_line = random.choice(line).strip().upper()
        return random_line

initial_word = random_word("mots.txt")
print(initial_word)

hangman_statuts = 0
guesses = []


done = True
while done:
    for letter in initial_word:
        if letter.upper() in guesses:
            print(letter, end= " ")
        else:
            print("_", end= " ")
    print("")
    
    guess = input()
    guesses.append(guess.upper())
    if guess.upper() not in initial_word.upper():
        hangman_statuts += 1
        if hangman_statuts == 6:
            break

    done = False
    for letter in initial_word:
        if letter.upper() not in guesses:
            done = True

if not done:
    print("Your Win !")
else:
    print("Game Over !")