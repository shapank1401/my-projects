import random
import time
import os
import platform

def clear_screen():
    system_name=platform.system()
    if system_name=="Windows":
        os.system("cls")
    else:
        os.system("clear")
 
def guessfun():
    guess=random.randint(0,100)
    print("You need to guess number between 0 to 100")
    print("---You have total 10 chances to guess the number---")
    count=1

    for i in range(0,10): 
        print("Attempt number %d"%count)
        count=count+1
        num=int(input("Enter number : "))
        if guess==num:
            print("\nBravoo! You guessed the number correctly and number is %d :)."%num)
            break
        elif num>guess:
            print("Guessed number is larger :(.")
        elif num<guess:
            print("Guessed number is smaller :(.")
        
        if i==9:
            print("\nSorry you have exhausted all your chances and lost the game :(.\n***Number was %d***\nBetter luck next time."%guess)
    
        
print("*****WELCOME TO GUESSING NUMBER GAME*****")

guessfun()
while True:
    y=input("\nDo you want to play again (Yes/No) : ")
    if y in ["yes","Yes","y","Y"]:
        clear_screen()
        print("*****WELCOME TO GUESSING NUMBER GAME*****")
        guessfun()
    elif y in ["n","N","no","No"]:
        print("\n#####Thank you for playing. Come soon again :)#####")
        time.sleep(3)
        break
    else:
        print("Please enter correct input.")

