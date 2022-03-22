import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

chosen_word = random.choice(word_list)

end_of_game = False
lives = len(stages) - 1

display = ["_" for i in chosen_word]
print(logo)

while not end_of_game:
    print(stages[lives])
    print(' '.join(display),end='\n\n')
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print("You hae already guessed that letter... Try Again!")
      continue
    if guess in chosen_word:
        for letter in range(0, len(chosen_word)):
            if guess == chosen_word[letter]:
                display[letter] = guess
            
    else:
        print(f"Letter {guess} is not in this word.")
        lives -= 1
        if lives == 0:
            print(stages[lives])
            end_of_game = True
            print(f"You got hang'd.\nThe word was {chosen_word} YOU LOSE!!!")
    
    if "_" not in display:
        print(' '.join(display),end='\n\n')
        end_of_game = True
        print("You guessed the word... YOU WIN!!!")


