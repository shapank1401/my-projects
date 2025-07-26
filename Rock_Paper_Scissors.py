import random
import time
import os
import platform


def clear_screen():
    sys_name=platform.system()
    if sys_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def comp_pick():
    choices=["rock","paper","scissor"]
    return (random.choice(choices))
    


def rock_paper_scissor():
    print("xxxxx---WELCOME TO ROCK PAPER & SCISSOR GAME---xxxxx\n")
    user_input=input("Please enter your choice from [rock, paper, scissor] : ").lower()
    
    comp_input=comp_pick()
    
    if user_input not in ["rock","paper","scissor"]:
        print("\nWrong input. Please enter correct choice.")
        
    elif (user_input == "rock" and comp_input == "scissor") or\
         (user_input == "scissor" and comp_input == "paper") or\
         (user_input == "paper" and comp_input == "rock") :
        print(f"\nYou choose : {user_input} and Computer choose : {comp_input} ")
        print("\nBRAVOOOO!!! YOU WON :) ")
    elif user_input == comp_input:
        print(f"\nYou choose : {user_input} and Computer choose : {comp_input} ")
        print("\nOH!! Thats a TIE :)\nYou both WoN :). ")
    else:
        print(f"\nYou choose : {user_input} and Computer choose : {comp_input} ")
        print("\nOOPS Sorry !!! YOU LOOSE :( ")

rock_paper_scissor()

while True:
    y=input("\nDo you want to play again (Yes/No) : ")
    
    if y in ["Yes","yes","y","Y"]:
        clear_screen()
        rock_paper_scissor()
    elif y in ["No","no","n","N"]:
        print("\nThank you for playing :)\nPlease come soon again.\nBye!!")
        time.sleep(3)
        break
    else:
        print("\nPlease enter correct input. ")
        
        
        
        
        