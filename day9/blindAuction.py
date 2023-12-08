import os
from art import logo

print(logo)
print("\nWelcome to the secret auction program.")
bidders = {}
end = ""
while end != "no":
    name = input("What is your name?: ")
    bid = int(input("What is your bid amount?: $"))
    bidders[name] = bid
    end = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

highestBid = 0
winner = ""
for key, value in bidders.items():
    if value > highestBid:
        highestBid = value
        winner = key
print(f"The winner is {winner} with a bid of ${highestBid}")

