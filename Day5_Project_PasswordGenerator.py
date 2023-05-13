#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Easy level
"""
password=""
for i in range(1,nr_letters+1):
    password=password+letters[random.randint(0,nr_letters-1)]
for j in range(1,nr_symbols+1):
    password=password+numbers[random.randint(0,nr_symbols-1)]
for k in range(1,nr_numbers+1):
    password=password+symbols[random.randint(0,nr_numbers-1)]
print(password)
"""
password=""
for i in range(1,nr_letters+1):
    password=password+random.choice(letters)
for j in range(1,nr_symbols+1):
    password=password+random.choice(symbols)
for k in range(1,nr_numbers+1):
    password=password+random.choice(numbers)
print(password)


#hard level
pwd=[letters,numbers,symbols]
total_len=nr_letters+nr_symbols+nr_numbers
password=""
let=0
num=0
sym=0
for i in range(1,total_len+1):

    row=random.randint(0,2)
    if row==0 and let<nr_letters:
        col=letters[random.randint(0,len(letters)-1)]
        password=password+col
        let+=1
    elif row==1 and sym<nr_symbols:
        col=symbols[random.randint(0,len(symbols)-1)]
        password=password+co
        sym+=1
    elif row==2 and num<nr_numbers:
        col=numbers[random.randint(0,len(numbers)-1)]
        password=password+col
        num+=1
    
print(password)
