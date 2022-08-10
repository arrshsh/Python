import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print (art.logo)
bidders_list = ""
left = True

def highest_bidder():
  highest_bid = 0
  winner = ""
  for bids in bidders_list:
    amount = bidders_list[bid]
    if amount > highest_bid:
      highest_bid = amount
      winner = bids
  print (f"The highest bid is {highest_bid}, put up by ")




while left == True:
  name = input ("Enter your name:  ")
  bid  = int(input ("Enter your bid:  ")) 
  bidders_list[name] = bid
  left = input ("Are there any more bidders left?".lower())
  if left == "yes":
    clear()
  
  else:
    left = False

highest_bid()

    
  
  
    
  

new_bid()
  
