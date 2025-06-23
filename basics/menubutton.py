"""menubutton.py

Menu Button App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tb


app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


def stuff(x):
    """Callback function for menu item selection."""
    menubutton.config(bootstyle=x)
    label1.config(text=f"You selected: {x}")


# create the menu button
menubutton = tb.Menubutton(text="Things!", compound="text")
menubutton.pack(pady=50)

# create basic menu
menu = tb.Menu(menubutton)

# items in menus
item_var = tb.StringVar()
for x in [
    "primary",
    "secondary",
    "success",
    "danger",
    "info",
    "outline primary",
    "outline secondary",
]:
    menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

# Associate menu with menu button
menubutton["menu"] = menu

label1 = tb.Label()
label1.pack(pady=40)

if __name__ == "__main__":
    app.mainloop()
