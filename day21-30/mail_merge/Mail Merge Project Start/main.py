# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter = './Input/Letters/starting_letter.txt'
invited_names_path = './Input/Names/invited_names.txt'

invited_names = open(invited_names_path).read().splitlines()

with open(starting_letter, mode='r') as file:
    data = file.read()

for name in invited_names:
    location = './Output/ReadyToSend/{}'
    new_file = location.format(name)
    new_data = data.replace("[name]", name)

    with open(new_file, mode='w') as file:
        file.write(new_data)


