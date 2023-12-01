print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choiceOne = input("You have a tunnel to your left or a mountain to your right, which way do you go? Type 'left' or 'right'.\n").lower()
if choiceOne == "right":
    print("You fell off the mountain. Game over.")
else:
    choiceTwo = input("The tunnel leads you to an underwater resevoir. Do you want for a boat or swim? Type 'wait' or 'swim'\n").lower()
    if choiceTwo == "swim":
        print("You got eaten alive by sharks. Game over.")
    else:
        choiceThree = input("You're presented with three doors: red, yellow, blue. Which do you enter? Type 'red', 'yellow', 'blue'.\n")
        if choiceThree.lower() == "yellow":
            print("You win!")
        elif choiceThree.lower() == "blue":
            print("You met a bear. She wasn't friendly. She was, however, hungry. Game over.")
        else:
            print("Would you rather fight one horse-sized chicken, or 30 chicken-sized horses? Either way, you lost. Game over.")

