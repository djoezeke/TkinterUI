"""entry.py

Entry App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tb

app = tb.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


def command():
    label1.config(text=f"You typed: {entry1.get()}")


entry1 = tb.Entry(
    bootstyle="success",
    font=("Arial", 18),
    foreground="red",
    width=25,
    show="*",
)
entry1.pack(pady=50)

button1 = tb.Button(text="Click Me!", bootstyle="danger outline", command=command)
button1.pack(pady=20)

label1 = tb.Label(text="")
label1.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()
