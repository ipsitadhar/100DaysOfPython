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

password=""
for i in range(1,nr_letters+1):
    password=password+random.choice(letters)
for j in range(1,nr_symbols+1):
    password=password+random.choice(symbols)
for k in range(1,nr_numbers+1):
    password=password+random.choice(numbers)
print(password)


#hard level
letter=0
symbol=0
number=0
position=0
pwd=[letters,numbers,symbols]
total_len=nr_letters+nr_symbols+nr_numbers
password=["_"] * total_len
print(password)
#for position in range(len(password)):
while "_" in password:
    guess=random.choice(random.choice(pwd))
    print(guess)
    if guess in letters:
        letter+=1
        if letter<=nr_letters:
            password[position]=guess
            position+=1
    if guess in symbols:
        symbol+=1
        if symbol<=nr_symbols:
            password[position]=guess
            position+=1
    if guess in numbers:
        number+=1
        if number<=nr_numbers:
            password[position]=guess
            position+=1
    
 
print(f"{' '.join(password)}")

#another way of hard level 
password=[]
for i in range(1,nr_letters+1):
    password.append(random.choice(letters))
for j in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
for k in range(1,nr_numbers+1):
    password.append(random.choice(numbers))
random.shuffle(password)
print(f"{''.join(password)}")



