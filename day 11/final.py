import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
length = len(cards)

def new_card(n):
  card_n_number = random.randint(0, length-1)
  card_n = cards[card_n_number]
  return card_n

card_1 = new_card(1)
card_2 = new_card(2)
card_3 = new_card(3)
card_4 = new_card(4)
card_5 = new_card(5)
card_6 = new_card(6)

user_deck = [card_1, card_2]
dealer_deck = [card_3, card_4, card_5, card_6]



def pull_new():
  temp = random.choice(dealer_deck)
  user_deck.append(temp)
  dealer_deck.remove(temp)

def update():
  print(f"Your cards: {user_deck}, current score: {user_score}")
  print(f"Computer's first card: {dealer_deck[0]}")

def final_result():
  print (f"Your final hand: {user_deck}, final score: {user_score}")
  print (f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
  if user_score < 21:
    if user_score > dealer_score:
      print("You win!!")
      return 0
    elif user_score < dealer_score:
      print("You loose!!")
      return 0
    else:
      print("It's a draw!")
      return 0

  else:
    print("You went over, you loose!")
    return 0
    



from art import logo
print(logo)
to_play = input ("Do you want to play a game of black jack? Type y or n:  ")
while to_play == "y":
  
  user_score = sum(user_deck)
  dealer_score = sum(dealer_deck)
  print(f"Your cards: {user_deck}, current score: {user_score}")
  print(f"Computer's first card: {dealer_deck[0]}")
  new_card = input("Type y to get another card, type n to pass:  ")
  if new_card == "y":
    pull_new()
    user_score = sum(user_deck)
    dealer_score = sum(dealer_deck)
    update()
    if user_score > 21:
      final_result()
    
  elif new_card == "n":
    final_result()

      
  








    




