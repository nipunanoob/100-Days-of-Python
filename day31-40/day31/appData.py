import csv
with open('data/french_words.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    french_words_list = list(reader)
    # for row in reader:
    #     print(row['French'])  # Access by column header instead of column number
    #     print(row['English'])
