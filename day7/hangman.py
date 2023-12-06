import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_array = ['_'] * len(chosen_word)
gameEnd = False
lives = 6

print(logo)
print("Welcome to hangman!")

while not gameEnd:
    print("\n---------------------\n")
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the chosen word. You lost a life. Try again.")
        if lives == 0:
            print("\nYou lose.")
            print(f"The word was {chosen_word}")
            gameEnd = True
            break
    
    if guess in word_array:
        print(f"\nYou already guessed the letter '{guess}'. Try again.")
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            word_array[i] = guess

    print(stages[lives])
    print(f"{' '.join(word_array)}")
    if "_" not in word_array:
        gameEnd = True
        print("\nYou win.")

