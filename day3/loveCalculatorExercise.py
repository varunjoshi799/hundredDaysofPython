print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1lower = name1.lower()
name2lower = name2.lower()
word1Count = 0
word2Count = 0
for letter in "true":
  word1Count += name1lower.count(letter)
  word1Count += name2lower.count(letter)
for letter in "love:":
  word2Count += name1lower.count(letter)
  word2Count += name2lower.count(letter)

string_score = str(word1Count) + str(word2Count)
score = int(string_score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")

