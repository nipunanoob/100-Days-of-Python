import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

print("Converting letters of word to list of NATO phonetic alphabets....")
while True:
    try:
        name = input("Enter word: ").upper()
        nato_list = [nato_dictionary[letter] for letter in name]
    except KeyError:
        print("Input letters in the alphabet please...")
    else:
        print(nato_list)
        break
