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
optionComp=random.randint(0,2)

if optionUser<0 or optionUser>=3:
    print("You entered an invalid number. You Lose!!")
elif optionUser==0:
    print(rock)
    print("computer chose:")
    if optionComp==0:
        print(rock)
        print("It's a draw")
    if optionComp==1:
        print(paper)
        print("You lose")
    if optionComp==2:
        print(scissors)
        print("You Win !")
elif optionUser==1:
    print(paper)
    print("computer chose:")
    if optionComp==0:
        print(rock)
        print("You Win!")
    if optionComp==1:
        print(paper)
        print("It's a draw")
    if optionComp==2:
        print(scissors)
        print("You Lose")
else:
    print(scissors)
    print("computer chose:")
    if optionComp==0:
        print(rock)
        print("You Lose!")
    if optionComp==1:
        print(paper)
        print("You Win !")
    if optionComp==2:
        print(scissors)
        print("It's a draw")

#solution using list

all_options=[rock,paper,scissors] #create a list of the variables holding the diagrams
optionUser=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors"))
if optionUser<0 or optionUser>=3:
    print("You entered an invalid number. You Lose!!")
else:
    print(all_options[optionUser])
    print("computer chose:")
    optionComp=random.randint(0,2)
    print(all_options[optionComp])


    if optionUser==0:
    
        if optionComp==0:
        
            print("It's a draw")
        if optionComp==1:
        
            print("You lose")
        if optionComp==2:
            
            print("You Win !")
    elif optionUser==1:
        
        print("computer chose:")
        if optionComp==0:
            
            print("You Win!")
        if optionComp==1:
            
            print("It's a draw")
        if optionComp==2:
            
            print("You Lose")
    else:
        
        if optionComp==0:
        
            print("You Lose!")
        if optionComp==1:
        
            print("You Win !")
        if optionComp==2:
        
            print("It's a draw")
            