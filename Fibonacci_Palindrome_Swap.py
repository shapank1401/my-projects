import time
def swap():
  a=int(input("Enter first number A : "))
  b=int(input("Enter second number B : "))

  print("Number A is %d and B is %d before swapping."%(a,b))
  a,b=b,a
  print(f"Number A is {a} and b is {b} after swapping.")


def palindrome():
  a=input("Please enter series : ")
  l=list(a)

  if l==l[::-1]:
    print(f"Series {a} is Palindrome.")
  else:
    print(f"Series {a} is not Palindrome.")

def fibonacci():
  n=int(input("Enter number of terms : "))
  a,b,c=0,1,0
  l=[0,1]

  for i in range(0,n-2):
    c=a+b
    l.append(c)
    a,b=b,c
  print(f"Fibonacci series of {n} terms is {l}.")


def funcall():
  
  print("Please select your option:")
  print("""
  -Enter 1 for Palindrome.
  -Enter 2 for Fibonacci.
  -Enter 3 for Swap""")

  choice=input("\nEnter your choice : ")

  if choice in ["1","2","3"]:
      try:
          if choice=="1": palindrome()
          if choice=="2": fibonacci()
          if choice=="3": swap()
      except ValueError:
          print("Wrong Input")
  else:
      print("Please enter correct option.")
if __name__=="__main__":
  print("*****WELCOME*****")
  funcall()
  while 1:
    
    y=input("Do you want to use Continue (Yes/No) : ")
    if y=="Yes" or y=="yes" or y=="y":
      funcall()
    elif y=="Yes" or y=="yes" or y=="n":
      print("Thank you for using Calculator! \nMeet you again soon :).")
      time.sleep(3)
      break
    else:
      print("Please enter correct input.")

    
