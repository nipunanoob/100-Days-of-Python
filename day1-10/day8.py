import day8_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = day8_art.logo
flag = 'yes'

print(logo)


def caesar(text, shift_amount, direction):
    new_text = ""
    if direction == 'decode':
        shift_amount = -shift_amount
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_text += alphabet[new_position]
        else:
            new_text += letter
    if direction == 'encode':
        print(f"The encoded text is {new_text}")
    else:
        print(f"The decoded text is {new_text}")

while(flag == 'yes'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    flag = input("Do you want to continue. Type yes to continue and no to exit the program...").lower()
