




def add(n1, n2):
  return n1 + n2

def sub (n1, n2):
  return n1-n2

def mul(n1, n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

should_continue = True

while should_continue:
  from art import logo
  print (logo)
  n1 = int(input ("Enter the first number:  "))
  n2 = int(input("Enter the second number:  "))
  
  operators = {
    "+": add(n1, n2),
    "-": sub(n1, n2),
    "*": mul(n1, n2),
    "/": div(n1, n2)
  }
  
  
  
  for signs in operators:
    print(signs)          
  
  user = input ("Choose the sign whose operation you want to perform:  ")
  for sign in operators:
    if sign == user:
      result = operators[sign]
      
      
  
  print (f"{n1} {user} {n2} = {result} ")

  new = input ("Do you want to perform any new operations? Type yes or no:  ").lower()
  if new == "yes":
    should_continue = True
  else:
    should_continue = False
    print ("Thank you for using us")
  