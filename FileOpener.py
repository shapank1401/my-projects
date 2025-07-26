import os
import platform
import subprocess
import time
   

def open_file(path):
    print("\n⏳ Please hold for a few seconds, your file will open soon...")
    time.sleep(3)
    
    if not os.path.exists(path):
        print(f"\n❌ File not found: {path}")
        return
    
    if platform.system() == 'Darwin':       # macOS
        subprocess.run(['open', path])
    elif platform.system() == 'Windows':    # Windows
        os.startfile(path)
    else:                                   # Linux and others
        subprocess.run(['xdg-open', path])

# Example usage:

def clear_screen():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")

def opencom():
    
    
        clear_screen()
        print("-----Different type of files opening application-----")
        print("\nEnter 1 for Image.\nEnter 2 for TEXT.\nEnter 3 for PDF\nEnter 4 for Moving Out.")

        try:
            n = int(input("\nPlease select your option: "))
            

            if n in [1,2,3,4]:
                if n == 1:
                    file_path=input("\nPlease Enter IMAGE FILE address to open : ").strip() + ".jpg"
                    open_file(file_path)
                    
                elif n == 2:
                    file_path=input("\nPlease Enter TEXT FILE address to open : ").strip() + ".txt"
                    open_file(file_path)
                elif n == 3:
                    file_path=input("\nPlease Enter PDF FILE address to open : ").strip() + ".pdf"
                    open_file(file_path)
                elif n == 4:
                    print("\nMoving out!!!!")
                    time.sleep(3)
                    exit()
                else:
                    print("\n❌ Invalid option. Please select between 1 and 4.")
                    time.sleep(3)
                
            else:
                print("Wrong input provided, try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter correct input")
        

opencom()

while True:
    y=input("\nDo you want to move to Main Menu (Yes/No) : ").strip().lower()
        
    if y in ["yes","y"]:
        opencom()
    elif y in ["no","n"]:
        print("\nThank you for coming :)\nPlease come soon again.\nBye!!")
        time.sleep(3)
        break
    else:
        print("\nPlease enter correct input. ")

