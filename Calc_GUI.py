import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    txt_result.delete(1.0,"end")
    txt_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0,calculation)
    except:
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0,"ERROR")

def clear_field():
    global calculation
    calculation=""
    txt_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("309x310")
root.title("Calculator")
txt_result= tk.Text(root, height=2, width=17, font=("Arial", 24))
txt_result.grid(columnspan=5)

btn_1=tk.Button(root, text="1", font=("Arial", 14), width=6, command=lambda: add_to_calculation(1))
btn_1.grid(row=2, column=1)

btn_2=tk.Button(root, text="2", font=("Arial", 14), width=6, command=lambda: add_to_calculation(2))
btn_2.grid(row=2, column=2)

btn_3=tk.Button(root, text="3", font=("Arial", 14), width=6, command=lambda: add_to_calculation(3))
btn_3.grid(row=2, column=3)

btn_4=tk.Button(root, text="4", font=("Arial", 14), width=6, command=lambda: add_to_calculation(4))
btn_4.grid(row=3, column=1)

btn_5=tk.Button(root, text="5", font=("Arial", 14), width=6, command=lambda: add_to_calculation(5))
btn_5.grid(row=3, column=2)

btn_6=tk.Button(root, text="6", font=("Arial", 14), width=6, command=lambda: add_to_calculation(6))
btn_6.grid(row=3, column=3)

btn_7=tk.Button(root, text="7", font=("Arial", 14), width=6, command=lambda: add_to_calculation(7))
btn_7.grid(row=4, column=1)

btn_8=tk.Button(root, text="8", font=("Arial", 14), width=6, command=lambda: add_to_calculation(8))
btn_8.grid(row=4, column=2)

btn_9=tk.Button(root, text="9", font=("Arial", 14), width=6, command=lambda: add_to_calculation(9))
btn_9.grid(row=4, column=3)

btn_0=tk.Button(root, text="0", font=("Arial", 14), width=6, command=lambda: add_to_calculation(0))
btn_0.grid(row=5, column=2)

btn_add=tk.Button(root, text="+", font=("Arial", 14), width=6, command=lambda: add_to_calculation("+"))
btn_add.grid(row=2, column=4)

btn_sub=tk.Button(root, text="-", font=("Arial", 14), width=6, command=lambda: add_to_calculation("-"))
btn_sub.grid(row=3, column=4)

btn_mul=tk.Button(root, text="x", font=("Arial", 14), width=6, command=lambda: add_to_calculation("*"))
btn_mul.grid(row=4, column=4)

btn_div=tk.Button(root, text="/", font=("Arial", 14), width=6, command=lambda: add_to_calculation("/"))
btn_div.grid(row=5, column=4)

btn_open=tk.Button(root, text="(", font=("Arial", 14), width=6, command=lambda: add_to_calculation("("))
btn_open.grid(row=5, column=1)

btn_close=tk.Button(root, text=")", font=("Arial", 14), width=6, command=lambda: add_to_calculation(")"))
btn_close.grid(row=5, column=3)

btn_pow=tk.Button(root, text="**", font=("Arial", 14), width=6, command=lambda: add_to_calculation("**"))
btn_pow.grid(row=6, column=1)

btn_mod=tk.Button(root, text="%", font=("Arial", 14), width=6, command=lambda: add_to_calculation("%"))
btn_mod.grid(row=6, column=3)

btn_clr=tk.Button(root, text="CLR", font=("Arial", 14), width=6, command=clear_field)
btn_clr.grid(row=6, column=4)

btn_eql=tk.Button(root, text="=", font=("Arial", 14), width=6, command=evaluate_calculation)
btn_eql.grid(row=6, column=2)

btn_period=tk.Button(root, text=".", font=("Arial", 14), width=6, command=lambda: add_to_calculation("."))
btn_period.grid(row=7, column=1)

btn_extra1=tk.Button(root, text="Extra1", font=("Arial", 14), width=6)
btn_extra1.grid(row=7, column=2)

btn_extra2=tk.Button(root, text="Extra2", font=("Arial", 14), width=6)
btn_extra2.grid(row=7, column=3)

btn_extra3=tk.Button(root, text="Extra3", font=("Arial", 14), width=6)
btn_extra3.grid(row=7, column=4)

root.mainloop()


