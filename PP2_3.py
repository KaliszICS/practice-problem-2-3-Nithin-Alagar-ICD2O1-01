

def q1(): 
  #Write Assignment code here
  word = input("input word: ")
  if word[-1:] == "ife":
    print("-ives")
  elif word[-2:] == "ey":
    print("-eys")
  elif word[-3:] == "y":
    print("-ies")
  else:
    print("s")
  

def q2(): 
  #Write Assignment code here
  num = input("Input an integer: ")
  if num > 0:
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")
  else:

#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
