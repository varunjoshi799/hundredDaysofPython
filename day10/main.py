# Operations
from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    first = float(input("What's the first number?: "))
    user = "y"

    while user == 'y':
        for keys in operations:
            print(keys)
        symbol = input("Pick an operation from the line above: ")
        second = float(input("What's the next number?: "))
        answer = operations[symbol](first, second)
        print(f"{first} {symbol} {second} = {answer}")
        first = answer
        user = input(f"Type 'y' to continue calculating with {first}, or type 'n' to start a new calculation: ")
        if user == "n":
            calculator()


calculator()
    