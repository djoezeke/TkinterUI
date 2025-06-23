"""checkbutton.py

Checkbutton App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tb


app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


# action function
def checker():
    """checker"""
    if var1.get() == 1:
        label1.config(text="Uncheck the checkbutton")
    else:
        label1.config(text="Check the checkbutton")


# label
label1 = tb.Label(
    text="Click the checkbutton below",
    font=("Arial", 18),
)
label1.pack(pady=(40, 10))

# checkbutton
var1 = tk.IntVar()
my_check = tb.Checkbutton(
    bootstyle="primary",
    text="Check me out",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check.pack(pady=10)

# toolbutton
check2 = tb.Checkbutton(
    bootstyle="danger, toolbutton",
    text="ToolButton!!",
    onvalue=1,
    offvalue=0,
)
check2.pack(pady=20)

# outline toolbutton
check3 = tb.Checkbutton(
    bootstyle="danger, toolbutton, outline",
    text="Outlined ToolButton!!",
    onvalue=1,
    offvalue=0,
)
check3.pack(pady=20)

# round toggle button
check4 = tb.Checkbutton(
    bootstyle="success, round-toggle",
    text="Round toggle",
    onvalue=1,
    offvalue=0,
)
check4.pack(pady=10)

# square toggle button
check5 = tb.Checkbutton(
    bootstyle="primary, square-toggle",
    text="Square toggle",
    onvalue=1,
    offvalue=0,
)
check5.pack(pady=10)


if __name__ == "__main__":
    app.mainloop()
