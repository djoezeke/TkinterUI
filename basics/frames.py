"""frames.py

Frame App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tbs

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")


def button_clicked():
    "button_clicked"


frame1 = tbs.Frame(app, bootstyle="light")
frame1.pack(pady=40)

entry1 = tbs.Entry(frame1, font=("Arial", 18))
entry1.pack(pady=20, padx=20)

button1 = tbs.Button(
    frame1, text="CLICK ME!", bootstyle="outline", command=button_clicked
)
button1.pack(pady=20, padx=20)

label1 = tbs.Label(app, text="Hello there!", font=("Arial", 18), bootstyle="dark")
label1.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()
