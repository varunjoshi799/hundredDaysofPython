alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    output = ""
    for letter in text:
        if direction == 'encode':
            new_letter = alphabet.index(letter) + shift
            output += alphabet[new_letter % len(alphabet)]
        if direction == 'decode':
            new_letter = alphabet.index(letter) - shift
            output += alphabet[new_letter]
    print(f"The {direction}d text is {output}")

caesar(direction, text, shift)



