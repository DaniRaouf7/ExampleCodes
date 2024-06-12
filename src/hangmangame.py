import random

from hangmanwordlist import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Create the while loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Already chosen this letter
    if guess in display:
        print(f"You have already guessed {guess}")
        
    #Check guessed letter    
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose, bitch!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    from hangman_art import stages
    print(stages[lives])

