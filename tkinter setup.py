import tkinter as tk
from tkinter import font
from tkinter import ttk

# Initializing a list to store the URl Data
url = []

# Create a window
window = tk.Tk()


# Set the window size
window.geometry("800x500")

# Set the window title with a larger font size
title_font = font.Font(family="Helvetica", size=20, weight="bold")  # Customize the font size and style
title_bar = tk.Label(window, text="Face Data Extractor from Youtube", font=title_font)
title_bar.pack()


# Add a text box to the window
text_box = tk.Text()
text_box.pack()

def on_select(event):
    selected_value = dropdown.get()
    print(f"Selected value: {selected_value}")

dropdown = ttk.Combobox(window, values=["All Gender", "Male", "Female"])
dropdown.current(0)  # Set the default selection to the first element
dropdown.bind("<<ComboboxSelected>>", on_select)
dropdown.pack()

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



# Bind the button click event to the function
button.config(command=button_click)

# Start the mainloop
window.mainloop()














