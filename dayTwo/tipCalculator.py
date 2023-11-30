print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

total_bill_with_tip = float(total_bill) * (1 + int(tip) / 100)
per_person_split = total_bill_with_tip / int(split)

print(f"Each person should pay ${round(per_person_split, 2)}")