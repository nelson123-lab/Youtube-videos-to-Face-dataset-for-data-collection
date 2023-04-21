# Youtube downloader

import os
import yt_dlp

link = open('C:/Users/NELSON JOSEPH/Downloads/data/links_file.txt','r') #The text file where the links to be pasted.
path = 'C:/Users/NELSON JOSEPH/Downloads/data'
os.chdir(path)
New_folder = "Downloaded_videos"
os.makedirs(New_folder)
for i in link.readlines():
    ydl_opts = {}
    os.chdir(path + "/Downloaded_videos")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([i])
    except:
        print("Some errror")
print('Task Completed!')
