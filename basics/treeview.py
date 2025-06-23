"""treeview.py

Treeview App using Tkinter & ttkboostrap
"""

import tkinter
import ttkbootstrap as tbs


app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")
app.geometry("500x350")

# define columns
columns = ("first_name", "last_name", "email")

# create treeview
tree1 = tbs.Treeview(
    style="dark",
    columns=columns,
    show="headings",
    height=15,
)
tree1.pack(pady=40, padx=40)

# define headings
tree1.heading("first_name", text="First Name")
tree1.heading("last_name", text="Last Name")
tree1.heading("email", text="Email")

# create sample data
contacts = []
for n in range(1, 20):
    contacts.append((f"First {n}", f"Last {n}", f"email{n}@address.com"))

# add data to treeview
for contact in contacts:
    tree1.insert("", "end", values=contact)


if __name__ == "__main__":
    app.mainloop()
