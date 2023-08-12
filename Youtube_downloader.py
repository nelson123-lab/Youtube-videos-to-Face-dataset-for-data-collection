# Youtube downloader

import os
import yt_dlp

# link = open('C:/Users/NELSON JOSEPH/Downloads/data/links_file.txt','r') #The text file where the links to be pasted.
url = ['https://youtu.be/a-7yQsgOB7w?list=RDB_1wqoWhYQo']
current_path = os.getcwd()
os.chdir(current_path)
New_folder = "Downloaded_videos"
os.makedirs(New_folder)
# for i in link.readlines():
for i in url:
    ydl_opts = {}
    os.chdir(current_path + "/Downloaded_videos")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([i])
    except:
        print("Some errror")
print('Task Completed!')
