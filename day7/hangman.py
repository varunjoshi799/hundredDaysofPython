import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

word_array = ['_'] * len(chosen_word)
gameEnd = False

while not gameEnd:
    print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            word_array[i] = guess

    print(word_array)
    if "_" not in word_array:
        gameEnd = True

print("You win.")