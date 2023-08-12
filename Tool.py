import tkinter as tk
from tkinter import font
from tkinter import ttk
from ttkthemes import ThemedTk
import os
import yt_dlp
from frameExtractor import FrameExtractor



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
    # Creating a new folder where the downloaded videos will be located.
    folder_name = 'Downloaded_videos'
    folder_path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(folder_path):
        i = 1
        while os.path.exists(folder_path):
            new_folder_name = folder_name + '_' + str(i)
            folder_path = os.path.join(os.getcwd(), new_folder_name)
            i += 1

    os.mkdir(folder_path)
    input_text = text_box.get("1.0", tk.END)  # Get the text from the text box
    url = input_text.split("\n")  # Split the text into lines
    # print("You entered:")
    for line in url:
        if len(line) == 0:
            pass
        else:
            ydl_opts = {}
            os.chdir(folder_path)
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([line])
            except:
                print("Some errror")
                print("working")
        print('Task Completed!')
      ### Main folder path where all the code and subfolders are placed
    # vedios = os.listdir(folder_path)  #### In place of 'Videos' replace it by the folder name where all the video data is placed
    # print(vedios)
    for ind,vedio in enumerate(os.listdir(folder_path)):
        try:
            # fix video taking input problems
            path = folder_path+'/'+'New folder'+'/'+vedio  #### In place of 'Videos' replace it by the folder name where all the video data is placed
            fe = FrameExtractor(path)
            fe.get_video_duration()
            fe.get_n_images(every_x_frame=50) ### Adjust the frame rate as per the length of video
            fe.extract_frames(every_x_frame=50, img_name=str(ind)+'Name_',dest_path=folder_path+'/'+'vedio')
        except Exception as e:
            print(e)

button.config(command=button_click)

# Start the mainloop
window.mainloop()












