import tkinter as tk
import random

guess = random.randint(0, 100)
count=0
blink_id = None

def reset_game():
    global guess, count
    stop_blink()
    guess = random.randint(0, 100)
    count = 0
    txt_field.delete(0, tk.END)
    label4.config(text="",bg="#d1abf7")
    label5.config(text = "", font=("Arial", 8, "bold"), width=70, bg="#d1abf7")

    btnsubmit.config(state="normal")
    txt_field.focus_set()

def blink():
    global blink_id
    color=label5.cget("fg")
    next_color="white" if color == "black" else "black"
    label5.config(fg=next_color)
    blink_id=label5.after(500, blink)

def stop_blink():
    global blink_id
    if blink_id is not None:
        label5.after_cancel(blink_id)
        blink_id = None
        label5.config(fg="black")

def submit(event=None):
    global guess
    global count
    num=txt_field.get().strip()
    count += 1

    label4.config(text = "Attempt number %d" % count, bg="#6cf0a0")


    if num and num.isdigit():
        num=int(num)
        if guess == num:

            label5.config(text= "Bravoo! You guessed the number correctly and number is %d :)\nRestarting the game...." % num, bg="gold")
            label5.config(font=("Gabriola",13,"bold"))
            btnsubmit.config(state="disabled")
            root.after(3000, reset_game)

        elif num > guess:
            label5.config(text ="Guessed number %d is larger :("%num, bg="#CC6808")
            stop_blink()
            blink()
        elif num < guess:
            label5.config(text ="Guessed number %d is smaller :("%num, bg="#007175")
            stop_blink()
            blink()
        else:
            pass
        if count >= 10 and guess != num:
            label5.config(
                text=f"Sorry, you've used all your chances!\nThe correct number was {guess}.\nRestarting the game..."
            , bg="grey")
            btnsubmit.config(state="disabled")
            root.after(3000, reset_game)
    else:
        if count >= 10 and guess != num:
            label5.config(
                text=f"Sorry, you've used all your chances!\nThe correct number was {guess}.\nRestarting the game..."
            , bg="grey")
            btnsubmit.config(state="disabled")
            root.after(3000, reset_game)

        else:
            label5.config(
                text="OH!\nYou missed your chance.", bg="red"
            )
            stop_blink()
            blink()
    txt_field.delete(0, tk.END)



def validate_input(new_value):
    if not new_value:
        return True  # allow empty input (helps while typing)
    if new_value.isdigit():
        value = int(new_value)
        return 0 <= value <= 100
    return False


root=tk.Tk()
root.geometry("400x300")
root.title("Number Guessing Game")
root.configure(bg="#d1abf7")


label1=tk.Label(root, text="Welcome to Number Guessing Game", width=40, fg="blue",font=("Helvetica",16,"bold"))
label1.pack(pady=10)

label2=tk.Label(root, font=("Arial",8,"bold"),text="You have total 10 chances to guess the number ", width=70, bg="#caf7ab", )
label2.pack()

label3=tk.Label(root, font=("Arial",8,"italic bold"),text="Please enter any number between 0 to 100", width=70, bg="#d1abf7", )
label3.pack()

vcmd = (root.register(validate_input), '%P')

txt_field=tk.Entry(root,validate='key', validatecommand=vcmd, width=10,  font=("Times New Roman",10))
txt_field.pack(pady=20)
txt_field.focus_set()

btnsubmit=tk.Button(root, text="Submit",font=("Arial",10,"bold"), width=15, fg="red", command=submit)
btnsubmit.pack(pady=10)

label4=tk.Label(root, font=("Fixedsys",8,), width=70, bg="#d1abf7" )
label4.pack()

label5=tk.Label(root, font=("Arial",8,"bold"), width=70, bg="#d1abf7", fg="black")
label5.pack(pady=10)

root.bind("<Return>",submit)
root.mainloop()