import time

def sum(a,b): return a+b
def sub(a,b): return (a-b)
def mul(a,b): return a*b
def div(a,b):
  try:
      a/b
  except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
  else: 
    print("Error!! Can't divide by Zero")

def po(a,b): return a**b
def mod(a,b): return a%b

def cal():
  
  print("Please select your option:")
  print("""
  -Enter 1 for Addition (+).
  -Enter 2 for Subtraction (-).
  -Enter 3 for Multiplication (x).
  -Enter 4 for Division (/).
  -Enter 5 for Power function(^).
  -Enter 6 for Modulus(%).""")
 
  choice=(input("\nEnter your choice : "))

  if choice in ["1","2","3","4","5","6"]:
        try:
            a=float(input("Enter first number : "))
            b=float(input("Enter second number : "))
            if choice=="1":
                print("Result : %d"%sum(a,b))
            elif choice=="2":
                print("Result : %d"%sub(a,b))
            elif choice=="3":
                print("Result : %d"%mul(a,b))
            elif choice=="4":
                print("Result : %d"%div(a,b))
            elif choice=="5":
                print("Result : %d"%po(a,b))
            elif choice=="6":
                print("Result : %d"%mod(a,b))
        except ValueError:
            print("Invalid input. Please enter numeric values")
  else:
      print("Invalid choice. Please select correct option. ")
  
if __name__=="__main__":
  print("*****Welcome to Calculator*****")
  cal()
  while 1:
    
    y=input("Do you want to use Calculator (Yes/No) : ")
   
    if y=="Yes" or y=="yes" or y=="y":
      cal()
    elif y=="Yes" or y=="yes" or y=="n":
      print("Thank you for using Calculator! \nMeet you again soon :).")
      time.sleep(3)
      break
    else:
      print("Please enter correct input.")
