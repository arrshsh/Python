#Write your code below this line 👇
import math
def prime_checker(number):
  for n in range(2, int (math.sqrt(number))+1):
    if number % n == 0:
      print ("Not a prime number")
      break
    else:
      print ("It is a prime number")
      break




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)




