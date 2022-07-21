# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

x = int (input ("What is your current age?"))
y = 90 - x
days = y * 365
weeks = y * 52
months = y * 12
print (f"You have {days} days, {weeks} weeks, {months} months left to live")
