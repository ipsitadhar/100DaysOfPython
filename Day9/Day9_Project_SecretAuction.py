import platform
import os
#HINT: You can call clear() to clear the output in the console.
from Day9.art1 import logo
print(logo)

more_bids=True
auction_data={}

while more_bids:
  name=input("What is your name?")
  bid=int(input("what's your bid? $"))
  auction_data[name]=bid
  option=input("Are there any other bidders? Type 'yes' or 'no'")
  if option=='no':
    print(auction_data)
    highest_bidder=max(auction_data)
    highest_bid=max(auction_data.values())
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    more_bids=False
    
    