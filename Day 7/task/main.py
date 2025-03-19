import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

chosenWord = []
placeHolder = []
display = []

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
for i in chosen_word:
    chosenWord.append(i)
for position in range(len(chosen_word)):
    chosenWord.append(i)


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
while display != chosenWord:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
            if position == guess:
                display[position] = chosenWord[letter]
            else:
                display[position] = "_"
    print(display)
