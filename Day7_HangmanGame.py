"""
1. Generate a random word. 
2. Genrate a blank list 0f '_' corresponding to the length of the chosen word
3. Guess a letter.There are 6 lives i.e six guessing mistakes till you lose
4. If the letter is present in the chosen word then continue or else reduce lives by 1.
5. if the letter is present , replace the '_' with the letter wherever it should be
6. If all letters are replaced correctly display You Won
7. Display the hangman stage

"""
from hangman_art import stages,logo
from hangman_words import word_list
import random


end_of_game = False
lives=6
chosen_word=random.choice(word_list)
display=["_"] * len(chosen_word)

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

while not end_of_game:
    guess=input("Guess a letter.")
    if guess in display:
        print("You have already guessed "+guess)
        guess=input("Guess a letter.")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life")
        lives=lives-1
        if lives==0:
            print("You lose")
            break

    for position in range(len(chosen_word)):
        
        if chosen_word[position]==guess:
            display[position]=guess
            
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
   

    if "_" not in display:
        print("You win")
        end_of_game=True
    
print(stages[lives])