import tkinter as tk
from tkinter import font
from tkinter import ttk
from ttkthemes import ThemedTk

# Create a themed Tkinter window

# Initializing a list to store the URl Data
url = []

# Create a window
window = ThemedTk(theme="equilux")


# Set the window size
window.geometry("800x500")

# Set the window title with a larger font size
title_font = font.Font(family="Helvetica", size=20, weight="bold")  # Customize the font size and style
title_bar = tk.Label(window, text="Face Data Extractor from Youtube", font=title_font)
title_bar.pack()


# Add a text box to the window
text_box = tk.Text(window, width=70, height=20, highlightbackground="black", highlightthickness=2)
text_box.pack(pady = 20)

def on_select(event):
    selected_value = dropdown.get()
    print(f"Selected value: {selected_value}")

dropdown = ttk.Combobox(window, values=["All Gender", "Male", "Female"])
dropdown.current(0)  # Set the default selection to the first element
dropdown.bind("<<ComboboxSelected>>", on_select)
dropdown.pack(pady = 5)

# Add a button to the window
button = tk.Button(text="Convert to face data")
button.pack()

# Define a function to handle button click
def button_click():
    input_text = text_box.get("1.0", tk.END)  # Get the text from the text box
    lines = input_text.split("\n")  # Split the text into lines
    # print("You entered:")
    for line in lines:
        url.append(line)
    print(url)


button.config(command=button_click)

# Start the mainloop
window.mainloop()













