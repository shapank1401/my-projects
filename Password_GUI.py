import tkinter as tk
import string
import random


num=""
def num_value(n):
    global num
    num+=str(n)
    txt_field1.delete(0, tk.END)
    txt_field1.insert(0, num)

def clear_field():
    global num
    num = ""
    txt_field1.delete(0, tk.END)
    txt_field2.delete("1.0", tk.END)

def reset_fields(message):
    txt_field1.delete(0, tk.END)
    txt_field2.delete("1.0", tk.END)
    label3.configure(text=message)


def is_valid_password(s):
        has_lower = any(char.islower() for char in s)
        has_upper = any(char.isupper() for char in s)
        has_digit = any(char.isdigit() for char in s)
        has_special = any(not char.isalnum() for char in s)
        return has_lower and has_upper and has_digit and has_special

# Function to generate a valid password of given length
def generatepw():
    global num
    num=""
    password=""
    all_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

    text_input = txt_field1.get().strip()
    if text_input and text_input.isdigit():
        if int(text_input) >=4:
            while True:
                password = ''.join(random.choice(all_chars) for _ in range(int(text_input)))
                if is_valid_password(password):
                    txt_field1.delete(0, tk.END)
                    txt_field2.delete("1.0", tk.END)
                    txt_field2.insert("1.0", password)
                    label3.configure(text="")
                    break
        else:
            reset_fields("Please enter count greater then 4")
    else:
        reset_fields("Please enter valid number")



root=tk.Tk()
root.geometry("375x400")
root.title("Password Generator")
root.configure(bg="lightblue")

label = tk.Label(root, text="Enter upto what length you want to \n generate password :", font=("Times New Roman", 12, "bold"), bg="light grey", width=41)
label.grid()

txt_field1=tk.Entry(root, font=("Arial", 12), width=12, relief="sunken")
txt_field1.grid(pady=20)


button_frame = tk.Frame(root, height=128, width=256, bg="light green")
button_frame.grid(pady=20)
button_frame.grid_propagate(False)

bt1=tk.Button(button_frame, text="1", font=("Arial", 12), width=6, command=lambda: num_value("1"))
bt1.grid(row=0,column=0)

bt2=tk.Button(button_frame,text="2", font=("Arial", 12), width=6, command=lambda: num_value("2"))
bt2.grid(row=1,column=0)

bt3=tk.Button(button_frame,text="3", font=("Arial", 12), width=6, command=lambda: num_value("3"))
bt3.grid(row=2,column=0)

bt4=tk.Button(button_frame,text="4", font=("Arial", 12), width=6, command=lambda: num_value("4"))
bt4.grid(row=0,column=1)

bt5=tk.Button(button_frame, text="5", font=("Arial", 12), width=6, command=lambda: num_value("5"))
bt5.grid(row=1,column=1)

bt6=tk.Button(button_frame,text="6", font=("Arial", 12), width=6, command=lambda: num_value("6"))
bt6.grid(row=2,column=1)

bt7=tk.Button(button_frame,text="7", font=("Arial", 12), width=6, command=lambda: num_value("7"))
bt7.grid(row=0,column=2)

bt8=tk.Button(button_frame,text="8", font=("Arial", 12), width=6, command=lambda: num_value("8"))
bt8.grid(row=1,column=2)

bt9=tk.Button(button_frame,text="9", font=("Arial", 12), width=6, command=lambda: num_value("9"))
bt9.grid(row=2,column=2)

bt0=tk.Button(button_frame,text="0", font=("Arial", 12), width=6, command=lambda: num_value("0"))
bt0.grid(row=3,column=1)

btclr=tk.Button(button_frame,text="CLR", font=("Arial", 12), width=6, command=clear_field)
btclr.grid(row=1,column=3)

btgen=tk.Button(button_frame, text="Generate", font=("Arial", 12), width=13, command=lambda: generatepw())
btgen.grid(row=3, column=2, columnspan=4)


label2 = tk.Label(root, text="Generated Password:", font=("Times New Roman", 12, "bold"), bg="light grey", width=41)
label2.grid()


txt_field2=tk.Text(root, height=1, width=20, font=("Arial", 12), relief="sunken")
txt_field2.grid(pady=10)


label3=tk.Label(root,font=("Times New Roman", 12, "bold"), fg="red",bg="khaki", width=41)
label3.grid(pady=10)

root.mainloop()