"""button.py

Button App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tb

app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


button1 = tb.Button(app, text="Button 1", bootstyle="success")
button1.pack(side="left", padx=(200, 0), pady=10, anchor="center")

button2 = tb.Button(app, text="Button 2", bootstyle=("info", "outline"))
button2.pack(side="left", padx=5, pady=10, anchor="center")

if __name__ == "__main__":
    app.mainloop()
