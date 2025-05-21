"""button.py

Button App using Tkinter & ttkboostrap

:author:	Sackey Ezekiel Etrue (djoezeke)
:created:	2025.04.01
"""

import tkinter
import ttkbootstrap as tb
from ttkbootstrap.constants import *

app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


button_1 = tb.Button(app, text="Button 1", bootstyle=SUCCESS)
button_1.pack(side="left", padx=(200, 0), pady=10, anchor="center")

button_2 = tb.Button(app, text="Button 2", bootstyle=(INFO, OUTLINE))
button_2.pack(side="left", padx=5, pady=10, anchor="center")

if __name__ == "__main__":

    app.mainloop()
