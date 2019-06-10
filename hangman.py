import random


fileopen = open("wordlist", "r")
read_words = fileopen.readlines()
random_word = random.choice(read_words).upper()
print(random_word)
to_guess = []
for i in range(len(random_word)-1):
    to_guess.append("_ ")
print(''.join(to_guess))
no_of_turns=8
while no_of_turns!=0:
    user_guess = input("Enter your Guess:").upper()
    if user_guess in random_word:
        new_index=0
        guessed=""
        for guess in random_word:
            if guess==user_guess:
                to_guess[new_index]=guess
            new_index+=1
            guessed=''.join(to_guess)
        print(''.join(to_guess))
        if "_ " in to_guess:
            continue
        else:
            print("Congratulations")
            break

    else:
        print("Wrong Choice")
        no_of_turns-=1
if(no_of_turns==0):
    print("Dead")