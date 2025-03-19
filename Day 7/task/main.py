import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

chosenWord = []
placeHolder = ""
display = []

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
for size in range(len(chosen_word)):
    placeHolder += "_"

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
for i in chosen_word:
    chosenWord.append(i)
    display.append("_")

print(placeHolder)

while display != chosenWord:
    result = ""
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    for i in display:
        result += i
    print(display)
    print(result)

print("Congratulations you win !")