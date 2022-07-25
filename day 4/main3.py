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

#Write your code below this line 👇

user = input ("Choose R for rock, P for paper, S for scissors ")
user_final = user.lower() 
comp = random.randint(0, 3)
# 1 = rock
# 2 = paper
# 3 = scissors

if user == "r":
    print (f"You choose:\n{rock}\n")
    if comp == 1:
        print(f"The computer chose:\n{rock}\nYou and computer chose the same option")
    elif comp == 2:
        print (f"The computer chose:\n{paper}\nYou Lose!!")
    elif comp == 3:
        print(f"The  computer chose:\n{scissors}\nYou Win!!")
elif user == "p":
    print (f"You choose:\n{paper}\n")
    if comp == 1:
        print(f"The computer chose:\n{rock}\nYou and computer chose the same option")
    elif comp == 2:
        print (f"The computer chose:\n{paper}\nYou Lose!!")
    elif comp == 3:
        print(f"The  computer chose:\n{scissors}\nYou Win!!")
elif user == "s":
    print (f"You choose:\n{scissors}\n")
    if comp == 1:
        print(f"The computer chose:\n{rock}\nYou and computer chose the same option")
    elif comp == 2:
        print (f"The computer chose:\n{paper}\nYou Lose!!")
    elif comp == 3:
        print(f"The  computer chose:\n{scissors}\nYou Win!!")
else:
    print("Choose a valid option")
