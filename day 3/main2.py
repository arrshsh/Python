# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
w = float(weight)
h = float(height)
bmi = w/ (h*h)
bmi = round(bmi, 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight")
elif 18.5<bmi< 25:
    print (f"Your BMI is {bmi}, you have normal weight")
elif 25<bmi<30:
    print (f"Your BMI is {bmi}, you are slightly overweight")
elif 30<bmi<35:
    print (f"Your BMI is {bmi}, you are pbese")
else:
    print (f"Your BMI is {bmi}, you are clinically obese")

