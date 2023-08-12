import tkinter as tk
from tkinter import font
from tkinter import ttk
from ttkthemes import ThemedTk
import os
import yt_dlp
from frameExtractor import FrameExtractor

folder_path = 'C:/Users/NELSON JOSEPH/Desktop/Youtube-videos-to-Face-dataset-for-data-collection/Downloaded_videos'

for ind,vedio in enumerate(os.listdir(folder_path)):
    print(vedio)
    try:
        # fix video taking input problems
        path = folder_path +'/'+ vedio  #### In place of 'Videos' replace it by the folder name where all the video data is placed
        fe = FrameExtractor(path)
        fe.get_video_duration()
        fe.get_n_images(every_x_frame=50) ### Adjust the frame rate as per the length of video
        fe.extract_frames(every_x_frame=50, img_name=str(ind)+'Name_',dest_path = folder_path+'/'+ str(ind))
    except Exception as e:
        print(e)