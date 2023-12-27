import random
import os
from art import logo

def calculateScores(deck):

    # Check for blackjack
    if 11 and 10 in deck and sum(deck) == 21:
        return 0
    
    # Check for ace
    if sum(deck) > 21:
        if 11 in deck:
            deck[deck.index(11)] = 1
            return sum(deck)
        else:
            return sum(deck)
        
    # Return score
    return sum(deck)

def compare(userScore, computerScore):
    if userScore == computerScore:
        return "It's a draw!"
    elif computerScore == 0:
        return "Computer had a blackjack. You lost!"
    elif userScore == 0:
        return "You had a blackjack. You won!"
    elif userScore > 21:
        return "You went over. You lost!"
    elif computerScore > 21:
        return "Computer went over. You won!"
    elif userScore > computerScore:
        return "You had the higher score. You won!"
    else:
        return "Computer had the higher score. You lost!"

def blackjack():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    userDeck = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
    computerDeck = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
    userScore = calculateScores(userDeck)
    computerScore = calculateScores(computerDeck)

    print(f"Your hand: {userDeck}, current score: {userScore}")
    print(f"Computer's first card: {computerDeck[0]}")
    game = input("Type 'y' to get another card, type 'n' to pass: ")

    # Continue game
    while game == "y" and userScore <= 21 and userScore != 0 and computerScore != 0:

        # User gets another card
        userDeck.append(cards[random.randint(0, len(cards) - 1)])
        userScore = calculateScores(userDeck)
        print(f"Your cards: {userDeck}, current score: {userScore}")
        print(f"Computer's first card: {computerDeck[0]}")
        game = input("Type 'y' to get another card, type 'n' to pass: ")

        # Once user finished, computer plays
        if game == "n":
            while computerScore < 17:
                computerDeck.append(cards[random.randint(0, len(cards) - 1)])
                computerScore = calculateScores(computerDeck)

    # End game
    print(f"Your final hand: {userDeck}, final score: {userScore}")
    print(f"Computer's final hand: {computerDeck}, final score: {computerScore}")
    print(compare(userScore, computerScore))

    # Ask for new game
    newGame = input("Type 'y' if you would like a new game: ")
    if newGame == "y":
        blackjack()

blackjack()