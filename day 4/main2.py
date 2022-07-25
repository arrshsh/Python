# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count = len (names)
count -= 1
rand = random.randint (0, count)
print (f"{names[rand]} is going to pay the bill!!")

 

