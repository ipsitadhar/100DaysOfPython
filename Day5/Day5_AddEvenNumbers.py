"""
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
"""
s=0
for n in range(1,101):
    if n%2==0:
        s=s+n
print(s)