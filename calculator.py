import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

root = tk.Tk()
root.title("Calculator")
root.geometry("305x475+50+50")
root.resizable(False, False)
root.iconbitmap("clcltr.ico")

def try_to_eval(strng):
    try:
        strng.set(round(eval(strng.get()), 7))
    except ValueError:
        showerror(title="Error", message="Please enter a proper value.")
        strng.set("")
    except ZeroDivisionError:
        showerror(title="Error", message="You can not divide by zero.")
        strng.set("")
    except SyntaxError:
        showerror(title="Error", message="Please enter a proper value.")
        strng.set("")


# Separators.
sprtr1 = ttk.Separator(root, orient="horizontal")
sprtr1.place(y=5, width=305)
sprtr2 = ttk.Separator(root, orient="horizontal")
sprtr2.place(y=95, width=305)
sprtr3 = ttk.Separator(root, orient="vertical")
sprtr3.place(x=3, height=475)
sprtr4 = ttk.Separator(root, orient="vertical")
sprtr4.place(x=302, height=475)
sprtr5 = ttk.Separator(root, orient="horizontal")
sprtr5.place(y=472, width=305)


# Display of the result.
txtvar = tk.StringVar()
txtvar.set("")
lbl1_style = ttk.Style()
lbl1_style.configure("Label1.TLabel", font=("Tempus Sans ITC", 30))
lbl1 = ttk.Label(root, textvariable=txtvar, style="Label1.TLabel")
lbl1.place(x=5, y=20)


# Buttons.
bttn_style = ttk.Style()
bttn_style.configure("Bttn.TButton", font=("Tempus Sans ITC", 35))
bttn_style.map("Bttn.TButton", foreground=[("pressed", "red"), ("active", "blue")], background=[("pressed", "red"), ("active", "blue")])
bttn_7 = ttk.Button(root, text="7", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"7"))
bttn_7.place(x=5, y=100, height=70, width=70)
bttn_8 = ttk.Button(root, text="8", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"8"))
bttn_8.place(x=80, y=100, height=70, width=70)
bttn_9 = ttk.Button(root, text="9", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"9"))
bttn_9.place(x=155, y=100, height=70, width=70)
bttn_plus = ttk.Button(root, text="+", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"+"))
bttn_plus.place(x=230, y=100, height=70, width=70)
bttn_4 = ttk.Button(root, text="4", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"4"))
bttn_4.place(x=5, y=175, height=70, width=70)
bttn_5 = ttk.Button(root, text="5", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"5"))
bttn_5.place(x=80, y=175, height=70, width=70)
bttn_6 = ttk.Button(root, text="6", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"6"))
bttn_6.place(x=155, y=175, height=70, width=70)
bttn_minus = ttk.Button(root, text="-", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"-"))
bttn_minus.place(x=230, y=175, height=70, width=70)
bttn_1 = ttk.Button(root, text="1", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"1"))
bttn_1.place(x=5, y=250, height=70, width=70)
bttn_2 = ttk.Button(root, text="2", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"2"))
bttn_2.place(x=80, y=250, height=70, width=70)
bttn_3 = ttk.Button(root, text="3", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"3"))
bttn_3.place(x=155, y=250, height=70, width=70)
bttn_cross = ttk.Button(root, text="x", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"*"))
bttn_cross.place(x=230, y=250, height=70, width=70)
bttn_c = ttk.Button(root, text="C", style="Bttn.TButton", command=lambda: txtvar.set(""))
bttn_c.place(x=5, y=325, height=70, width=70)
bttn_0 = ttk.Button(root, text="0", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"0"))
bttn_0.place(x=80, y=325, height=70, width=70)
bttn_dot = ttk.Button(root, text=".", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"."))
bttn_dot.place(x=155, y=325, height=70, width=70)
bttn_divide = ttk.Button(root, text="÷", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"/"))
bttn_divide.place(x=230, y=325, height=70, width=70)
bttn_exponent = ttk.Button(root, text="^", style="Bttn.TButton", command=lambda: txtvar.set(txtvar.get()+"**"))
bttn_exponent.place(x=155, y=400, height=70, width=70)
bttn_equals = ttk.Button(root, text="=", style="Bttn.TButton", command=lambda: try_to_eval(txtvar))
bttn_equals.place(x=230, y=400, height=70, width=70)


# The label at the bottom.
lbl2_style = ttk.Style()
lbl2_style.configure("Label2.TLabel", font=("Vladimir Script", 15), foreground="red")
lbl2 = ttk.Label(root, text="by Batuhan Akçan", style="Label2.TLabel")
lbl2.place(x=12, y=420)


root.mainloop()