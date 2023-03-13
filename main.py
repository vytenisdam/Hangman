#Step 5
from replit import clear
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
import random

print(logo)
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
#New comment
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
wrong_letters = []
for _ in range(word_length):
    display += "_"
#print(display)
print(f"{' '.join(display)}")
print(f'The word has {len(chosen_word)} letters.')
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You already guessed letter '{guess}'")
        print(f' Letters that cost you a limb {wrong_letters}')
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(f' Letters that cost you a limb {wrong_letters}')
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(
            f'Letter "{guess}" is not in the word. You lose a life. Lives left - {lives} Try again.'
        )
        #galima keliais budais su append ir su +=
        #wrong_letters.append(guess)
        wrong_letters += guess
        print(f' Letters that cost you a limb {wrong_letters}')
        if lives == 0:
            end_of_game = True
            print(f"You lose. Word was - {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
