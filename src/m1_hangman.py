# """
# Hangman.
#
# Authors: Zach Witonsky & Landen Berlin.
# """  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
#
# # DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
#
# Stage 1
# -----------------------------------

import random

def main():

    min_length = int(input('Enter minimum number of letters: '))
    max_guess = int(input('Enter number of lives for game: '))

    word = item(min_length)

    print("\nThis word has", len(word), "characters")

    guess_word = []
    store_letter = []

    blank(word, guess_word)
    guessing(word, guess_word, max_guess, store_letter)

def item(min_length):
    while True:
        with open('words.txt') as f:
            f.readline()
            string = f.read()
            words = string.split()

        r = random.randrange(0, len(words))
        word = words[r]

        if len(word) > min_length:
            return word

def blank(word, guess_word):

    for k in range(len(word)):
        guess_word.append("-")
    print("Word to guess: {0} \n".format(" ".join(guess_word)))

def guessing(word, guess_word, max_guess, store_letter):
    guess_left = max_guess
    print("You have {0} guesses left. ".format(guess_left))

    while guess_left > 0:
        user_guess = input("Enter 1 letter: ")
        print()

        if user_guess in store_letter:
            print("You have already tried that. Try again.\n")
            print("----------------------------------------\n")

        else:
            store_letter.append(user_guess)

            if user_guess in word:
                print("Good guess. Guess again! ")
                print("----------------------------------------\n")

                for k in range(len(word)):
                    if word[k] == user_guess:
                        guess_word[k] = user_guess

                print("Word to guess: {0}\n".format(" ".join(guess_word)))

                if not '-' in guess_word:
                    print("You won! Good job.")
                    break
                print("You still have {0} guesses left.".format(guess_left))

            else:
                print("Letter not in word. Try Again.\n")
                print("----------------------------------------\n")
                guess_left -= 1
                print("Word to guess: {0}\n".format(" ".join(guess_word)))
                print("You have {0} guesses left.".format(guess_left))

                if guess_left == 0:
                    print("You lose... The word was {0}".format(word))

main()




























