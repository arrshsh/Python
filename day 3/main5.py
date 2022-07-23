# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

size_final = size.lower()
add_pepperoni_final = add_pepperoni.lower()
extra_cheese_final = extra_cheese.lower()

cost = 0
if size_final == "s":
    cost = 15
    if add_pepperoni_final == "y":
        cost += 2
elif size_final == "m":
    cost = 20
    if add_pepperoni_final == "y":
        cost += 3
else:
    cost = 25
    if add_pepperoni_final == "y":
        cost += 3

if extra_cheese_final  == "y":
    cost += 1

print(f"Your final bill is ${cost}")
