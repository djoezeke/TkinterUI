"""floodgauge.py

Floodgauge App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tbs

app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x450")


def starter():
    gauge1.start()


def stopper():
    gauge1.stop()


def incrementer():
    gauge1.step(10)
    label1.config(text=f"Position: {gauge1.variable.get()}")


gauge1 = tbs.Floodgauge(
    bootstyle="default",
    font=("Arial", 18),
    mask="Pos: {}%",
    maximum=100,
    value=0,
    orient="horizontal",
    mode="determinate",
)
gauge1.pack(pady=50, fill="x", padx=30)

button_start = tbs.Button(text="Start", bootstyle="danger outline", command=starter)
button_start.pack(pady=20)

button_stop = tbs.Button(text="Stop", bootstyle="danger outline", command=stopper)
button_stop.pack(pady=20)

button_increment = tbs.Button(
    text="Increment", bootstyle="danger outline", command=incrementer
)
button_increment.pack(pady=20)

label1 = tbs.Label(text="Position: ")
label1.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()
