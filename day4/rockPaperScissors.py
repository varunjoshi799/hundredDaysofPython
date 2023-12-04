import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
bot = random.randint(0, 2)
win = True
draw = False

option = [rock, paper, scissors]

if option[user] == option[bot]:
    draw = True
elif ((option[user] == rock and option[bot] == paper) 
    or (option[user] == paper and option[bot] == scissors)
    or (option[user] == scissors and option[bot] == rock)):
    win = False


print(option[user])
print("Computer chose:")
print(option[bot])
if draw == True:
    print("It's a draw!")
elif win == True:
    print("You won!")
else:
    print("You lost!")
