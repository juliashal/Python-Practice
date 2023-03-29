'''In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
'''

'''NOTE: as a word can be >6 letters, in this code attempts deducted only when the letter is guessed incorrectly'''

from Pick_word import random_word
hidden_word = random_word()


def game(hidden_word):

    word_length = len(hidden_word)
    print(f"Welcome to Hangman!\n Word length is {word_length}")
    user_word = ['_']*word_length
    count_empty = user_word.count('_')

    guess_count = 6

    while count_empty > 0 and guess_count > 0:

        print(f"You have {guess_count} guess(es) left\n")
        while True:
            guess = input("Guess your letter: ")
            if guess.isalpha() and len(guess) == 1:  # only 1 letter at a time
                break

        guess = guess.upper()

        for i in range(len(hidden_word)):
            if guess == hidden_word[i]:
                print('Correct!')
                user_word[i] = guess

        if guess not in hidden_word:
            print('Incorrect!')
            guess_count -= 1 #deduct number of attempts only when the letter is not in the hidden word

        print(' '.join(user_word))

        count_empty = user_word.count('_')

    return count_empty, (6-guess_count)


letters_left_to_guess, num_guesses = game(hidden_word)

if letters_left_to_guess:
    print(f"You haven't guessed the word. It was {hidden_word}")
else:
    print(f"You WON! You guessed a word in {num_guesses} attempts")
