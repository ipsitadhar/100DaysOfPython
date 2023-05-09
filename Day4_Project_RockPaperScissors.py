#Rock wins against scissors; paper wins against rock; and scissors wins against paper.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
optionUser=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors"))
if optionUser==0:
    print(rock)
elif optionUser==1:
    print(paper)
else:
    print(scissors)
optionComp=random.randint(0,2)
print("computer chose:")
if optionComp==0:
    print(rock)
elif optionComp==1:
    print(paper)
else:
    print(scissors)

if optionUser==0:
    if optionComp==0:
        print("It's a draw")
    if optionComp==1:
        print("You lose")
    if optionComp==2:
        print("You Win !")

if optionUser==1:
    if optionComp==0:
        print("You Win!")
    if optionComp==1:
        print("It's a draw")
    if optionComp==2:
        print("You Lose")
if optionUser==2:
    if optionComp==0:
        print("You Lose!")
    if optionComp==1:
        print("You Win !")
    if optionComp==2:
        print("It's a draw")