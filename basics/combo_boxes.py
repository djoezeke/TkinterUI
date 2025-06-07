"""combo_boxes.py

Comboboxes App using Tkinter & ttkboostrap

:author:	Sackey Ezekiel Etrue (djoezeke)
:created:	2025.04.11
"""

import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


# define functions
def clicker():
    """clicker"""
    label.config(text=f"You clicked on {combo.get()}!")


def click_bind(event):
    """click_bind"""
    label.config(text=f"You clicked on {combo.get()}!")


def reset(event):
    """reset"""
    label.config(text="Hello World!")


# create label
label = tb.Label(app, text="Hello World!", font=(".AppleSystemUIFont", 18))
label.pack(pady=30)

# create dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# create combo
combo = tb.Combobox(
    app,
    bootstyle="default",
    values=days,
)
combo.current(0)
combo.pack(pady=20)
# bind the combo box
combo.bind("<<ComboboxSelected>>", click_bind)
combo.bind("<Return>", reset)

# create button
button = tb.Button(app, text="Click Me!", command=clicker, bootstyle="danger")
button.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()
