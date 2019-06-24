import os
import random

name="sanjeev"

def hangman(to_guess,guessed_outputs,guessed_word,no_of_tries):
    if not len(to_guess)<=4:
        guessed_output_two=""
        print("to guess is:",to_guess)
        user_guess = input("Enter your guess:")
        if user_guess in to_guess:
            guessed_word = guessed_word+user_guess
            indices = to_guess.index(user_guess)
            guessed_output_two = guessed_outputs[:indices]+user_guess+guessed_outputs[indices:]
            print(guessed_output_two)
        else:
            no_of_tries -= 1
            guess_to=input("Enter another choice:")
            hangman(to_guess, guessed_outputs, guess_to, no_of_tries)
    else:
        print("error")
        #search_random_words()


def search_random_words():

    try:
        open_list = open("words")
        read_words = open_list.readlines()
        to_guess = random.choice(read_words)
        print(to_guess)
        lentoguess=len(to_guess)-1
        guessed_output = ""
        while lentoguess > 0:
            guessed_output = guessed_output+"_"+" "
            lentoguess -= 1
        print(guessed_output)
        guessed_word = ""
        no_of_try = 6
        hangman(to_guess, guessed_output, guessed_word, no_of_try)

    except Exception:
        print("exception", Exception)


#inputName = input("Enter your Name::")
#search_random_words(inputName)
search_random_words()


