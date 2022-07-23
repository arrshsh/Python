# 🚨 Don't change the code below 👇
from re import X


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_final = name1.lower()
name2_final = name2.lower()

x1 = name1_final.count("t")
x2 = name1_final.count("r")
x3 = name1_final.count("u")
x4 = name1_final.count("e")
x5 = name2_final.count("t")
x6 = name2_final.count("r")
x7 = name2_final.count("u")
x8 = name2_final.count("e")

x = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

print (x)

y1 = name1_final.count("l")
y2 = name1_final.count("o")
y3 = name1_final.count("v")
y4 = name1_final.count("e")
y5 = name2_final.count("l")
y6 = name2_final.count("o")
y7 = name2_final.count("v")
y8 = name2_final.count("e")

y = y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8

print (y)

z = (10 * x) + y
print (z)

