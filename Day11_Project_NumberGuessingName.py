
"""
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

"""
from random import randint
from art2 import logo
print(logo)
print("Welcome to the number guessing game !!")
print("I am thinking of a number between 1 and 100")
answer=randint(1,100)
print(f"Pssst, the correct number is {answer}")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' :")
if difficulty=="easy":
    attempts=10
else:
    attempts=5
print(f"You have {attempts} attempts remaining to guess the number")
for n in range(1,attempts+1):
    guess=int(input("Make a guess:"))
    if guess==answer:
        print(f"You got it ! The answer was {answer}")
        break
    else:
        if guess>answer:
            result="high"
        else:
            result="low"
        attempts-=1
        print(f"Too {result}")
        if attempts!=0:
            print("Guess Again")
            print(f"You have {attempts} attempts remaining to guess the number")
if guess!=answer:
    print("You've run out of guesses, you lose.")
"""
#Function to check user's guess against actual answer.
def check_Answer(guess,answer,turns):
    if guess==answer:
        print(f"You got it ! The answer was {answer}")      
    else:
        if guess>answer:
            result="high"
        else:
            result="low"
        turns-=1
        print(f"Too {result}.")
        return turns

#Make function to set difficulty.
def set_difficulty():
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard' :")
"""