############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
length = len(cards)

def new_card(n):
  card_n_number = random.randint(0, length-1)
  card_n = cards[card_n_number]
  return card_n

def pull_new():
    want_to_continue = input ("Do you want to take a new card? Type y or n")

    if want_to_continue == "y":
      dealer_card.remove(card_3)
      user_card =+ card_3
      print(user_card)
      # if sum(user_card) < 21:
      #   pull_new()
      # else:
      #   to_play = False
      pull_new()
    else:
      to_play = False


to_play = True
while to_play:
  
  # print (length)
  
  # card_2_number = random.randint(0, length-1)
  # card_2 = cards[card_2_number]
  

  # card_3_number = random.randint(0, length-1)
  # card_3 = cards[card_3_number]
  # card_4_number = random.randint(0, length-1)
  # card_4 = cards[card_4_number]
  card_1 = new_card(1)
  card_2 = new_card(2)
  card_3 = new_card(3)
  card_4 = new_card(4)
  card_5 = new_card(5)
  card_6 = new_card(6)

  user_card = [card_1, card_2]
  dealer_card = [card_3, card_4, card_6]
  score = sum(user_card)
  print (f"Your cards: {user_card}\nYour score: {score}")
  print (f"Dealer's cards: {card_3}")
  pull_new

  

  user_sum = sum(user_card)
  dealer_sum = sum(dealer_card)
  if user_sum > 21:
    print(f"Your score: {user_sum}, You looose as yo went over!!")

  else:
    if user_sum > dealer_sum & user_sum <21:
      print(f"You win with a score {user_sum}")
    elif user_sum < dealer_sum & user_sum <21:
      print(f"You loose!!\nYour score = {user_sum}, Dealer's score = {dealer_sum}")
    


  to_play = False


  
