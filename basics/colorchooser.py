"""colorchooser.py

Simple Color Chooser App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog


app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


# simple color chooser function
def color_chooser():
    """color_chooser"""
    cc = ColorChooserDialog()
    cc.show()
    color = cc.result
    if color:
        label.config(text=color.rgb)
        app.config(background=color.hex)
    else:
        label.config(text="No color selected")


button = tb.Button(text="Click Me!", command=color_chooser)
button.pack(pady=40)

label = tb.Label(text="", font=(".AppleSystemUIFont", 18))
label.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()
