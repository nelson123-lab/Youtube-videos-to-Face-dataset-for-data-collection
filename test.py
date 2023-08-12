import tkinter as tk
from tqdm import tqdm
from tkinter import ttk

root = tk.Tk()

def start_progress():
    progress_bar.start()

def stop_progress():
    progress_bar.stop()

# Create a progress bar
progress_bar = ttk.Progressbar(root, mode='indeterminate')

# Create buttons to start and stop the progress bar
start_button = tk.Button(root, text='Start', command=start_progress)
stop_button = tk.Button(root, text='Stop', command=stop_progress)

# Pack the progress bar and buttons into the window


def update_progress_bar(value):
    progress_bar.set_postfix(progress=value)
    root.update()

root = tk.Tk()
root.title("Progress Bar Example")

progress_bar = tqdm(total=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=80)
progress_bar.set_postfix(progress=0)

# Update the progress bar value and the Tkinter window
for i in range(100):
    progress_bar.update(1)
    update_progress_bar(i)

progress_bar.pack()
start_button.pack()
stop_button.pack()
progress_bar.close()

root.mainloop()


