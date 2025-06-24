"""frames.py

A simple Frame App using Tkinter & ttkbootstrap.

This example demonstrates how to use frames, entries, buttons, and labels
with the ttkbootstrap theme for a modern look.
"""

# Import the standard tkinter library (required for some variable types)
import tkinter

# Import ttkbootstrap as tbs for themed widgets and window
import ttkbootstrap as tbs

# Create the main application window with a specific theme
app = tbs.Window(themename="cosmo")
app.title("TTK Bootstrap!")  # Set the window title
app.geometry("500x350")  # Set the window size


# Define the callback function for the button click event
def button_clicked():
    """
    This function is called when the button is clicked.
    It retrieves the text from the entry widget and updates the label.
    """
    user_text = entry1.get()  # Get the text entered by the user
    if user_text.strip():
        label1.config(text=f"You entered: {user_text}")
    else:
        label1.config(text="Please enter something above!")


# Create a frame to group related widgets together
# Frames help organize the layout of the window
frame1 = tbs.Frame(app, bootstyle="light")  # Use a light style for the frame
frame1.pack(pady=40)  # Add vertical padding around the frame

# Add an entry widget inside the frame for user input
entry1 = tbs.Entry(frame1, font=("Arial", 18))
entry1.pack(pady=20, padx=20)  # Add padding inside the frame

# Add a button inside the frame that triggers the button_clicked function
button1 = tbs.Button(
    frame1,
    text="CLICK ME!",
    bootstyle="outline",  # Use an outlined style for the button
    command=button_clicked,  # Set the function to call on click
)
button1.pack(pady=20, padx=20)

# Add a label below the frame to display messages to the user
label1 = tbs.Label(
    app,
    text="Hello there!",  # Initial text
    font=("Arial", 18),
    bootstyle="dark",  # Use a dark style for the label
)
label1.pack(pady=20)

# Start the Tkinter event loop if this script is run directly
if __name__ == "__main__":
    app.mainloop()
