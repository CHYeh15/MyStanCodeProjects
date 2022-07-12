"""
File: hangman.py
Name: Kevin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Randomly generate a word as answer, and use the game function
    to determine whether the user’s guess is correct.
    """
    ans = random_word()
    guess = ''
    for i in range(len(ans)):
        guess += '-'
    print('The word looks like:' + guess)
    print('You have ' + str(N_TURNS) + ' guesses left. ')
    game(ans, guess)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def format(f):
    """
    Determine whether the guess entered by
    the user conforms to the format.
    ---------------------------------------------------
    :param f: str, user guess
    :return :  str
    """
    while True:
        if len(f) >= 2:  # Determine whether to enter two letters at a time.
            print('Illegal format.')
            f = input('Your guess: ')
        elif f.isalpha() == 0:  # Determine whether to enter a non-letter.
            print('Illegal format.')
            f = input('Your guess: ')
        else:
            f = f.upper()
            break
    return f


def game(ans, guess):
    """
    Determine whether the user's guess is correct and
    how many opportunities are left.
    ---------------------------------------------------
    :param ans: str, answer
    :param guess: str, user guess
    """
    chance = N_TURNS
    while True:
        player_guess = input('Your guess: ')
        player_guess = format(player_guess)
        if ans.find(player_guess) == -1:
            chance = chance-1
            if chance > 0:
                print('There is no ' + player_guess + "'s in the word.")
                print('The word looks like:' + guess)
                print('You have ' + str(chance) + ' guesses left. ')

            else:
                print('There is no ' + player_guess + "'s in the word.")
                print('You are completely hung : ( ')
                print('The word is: ' + ans)
                break
        else:
            chance = chance
            for i in range(len(ans)):
                if player_guess == ans[i]:
                    guess = guess[0:i] + player_guess + guess[i+1:]
                else:
                    guess = guess
            if guess == ans:
                print('You are correct! ')
                print('You win!! ')
                print('The word was: ' + guess)
                break
            else:
                print('You are correct! : ')
                print('The word looks like: ' + guess)
                print('You have ' + str(chance) + ' guesses left. ')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
