import random
import hangman_words, hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
gameLogo = hangman_art.logo
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
previous_guesses = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print("****************************<???>/6 LIVES LEFT****************************")
    print(f"You have {lives} lives left")
    print(f"PG: {previous_guesses}")

    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in previous_guesses:
        print(f"You already guessed this letter: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    print(f"PG: {previous_guesses}")
    if guess not in chosen_word and guess not in previous_guesses:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")

    previous_guesses.append(guess)

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    stages = hangman_art.stages
    print(stages[lives])