from art import *
from game_data import *
import random

print(logo)

#function to retrieve the instagram follower count
def follower_count(name_search):
    for name in data:
        if name["name"]==name_search:
            return name["follower_count"]

#function to retrieve the description
def description(name_search):
    for name in data:
        if name["name"]==name_search:
            return name["description"]
#function to retrieve the country
def country(name_search):
    for name in data:
        if name["name"]==name_search:
            return name["country"]

#function to do the comparison 
def comparison(a,b):
    follower_a=follower_count(a)
    followers_b=follower_count(b)
    if follower_a>followers_b:
        return a
    else:
        return b

#display the comparison:
def displayGame(a,b):
    desc_a=description(a)
    country_a=country(a)
    desc_b=description(b)
    country_b=country(b)
    print(f"Compare A: {a}, a {desc_a}, from {country_a}")
    print(vs)
    print(f"Compare B: {b}, a {desc_b}, from {country_b}")
    user_choice=input("Who has more followers? Type 'A' or 'B': ")
    actual_result=follower_count(a,b)
    if user_choice==actual_result:
        displayGame(a,b)


random_a=random.choice(data)["name"]
random_b=random.choice(data)["name"]
print(random_a,random_b)
