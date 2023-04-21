
import os
import math
import datetime
import cv2
from mtcnn.mtcnn import MTCNN
import yt_dlp

# The text file where the links to be pasted. Multiple videos can be downloaded at the same time by pasting each links per line.
link = open('C:/Users/NELSON JOSEPH/Downloads/data/links_file.txt','r') 

# The path in which a new folder named downloaded folder will be created.
path = 'C:/Users/NELSON JOSEPH/Downloads/data'

# Changing the directory to the path.
os.chdir(path)

# The folder to be made in the data folder.
New_folder = "Downloaded_videos"

# Making the directory named "Downloaded_videos" in the data folder so that the vedios will be saved in the "Downloaded_videos" folder.
os.makedirs(New_folder)

# Iterating through the links folder.
for i in link.readlines():
    ydl_opts = {}
    # Changing the directory to the "Downloaded_videos" so that the videos will be saved here.
    os.chdir(path + "/Downloaded_videos")
    # Trying to download from the uploader id.
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download each video one by one.
            ydl.download([i])
    except:
        print("Some errror")
print('Task Completed!')

"""  To Convert Videos to frames  """

class FrameExtractor():
    '''
    Class used for extracting frames from a video file.
    '''
    def __init__(self, video_path):
        self.video_path = video_path
        self.vid_cap = cv2.VideoCapture(video_path)
        self.n_frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.vid_cap.get(cv2.CAP_PROP_FPS))
        
    def get_video_duration(self):
        duration = self.n_frames/self.fps
        print(f'Duration: {datetime.timedelta(seconds=duration)}')
        
    def get_n_images(self, every_x_frame):
        n_images = math.floor(self.n_frames / every_x_frame) + 1
        print(f'Extracting every {every_x_frame} (nd/rd/th) frame would result in {n_images} images.')
        
    def extract_frames(self, every_x_frame, img_name, dest_path=None, img_ext = '.jpg'):
        if not self.vid_cap.isOpened():
            self.vid_cap = cv2.VideoCapture(self.video_path)
        
        if dest_path is None:
            dest_path = os.getcwd()
        else:
            if not os.path.isdir(dest_path):
                os.mkdir(dest_path)
                print(f'Created the following directory: {dest_path}')
        
        frame_cnt = 0
        img_cnt = 0

        while self.vid_cap.isOpened():
            
            success,image = self.vid_cap.read() 
            
            if not success:
                break
            
            if frame_cnt % every_x_frame == 0:
                img_path = os.path.join(dest_path, ''.join([img_name, '_', str(img_cnt), img_ext]))
                cv2.imwrite(img_path, image)  
                img_cnt += 1
                
            frame_cnt += 1
        
        self.vid_cap.release()
        cv2.destroyAllWindows()
#######################################loop on each downloaded vedio
        
dire=r"C:/Users/NELSON JOSEPH/Downloads/data"  ### Main folder path where all the code and subfolders are placed
vedios= os.listdir(dire+'/'+'Downloaded_videos'+'/')  #### In place of 'Videos' replace it by the folder name where all the video data is placed
for ind,vedio in enumerate(vedios):
    try:
        path= dire+'/'+'Downloaded_videos'+'/'+vedio  #### In place of 'Videos' replace it by the folder name where all the video data is placed
        fe = FrameExtractor(path)
        fe.get_video_duration()
        fe.get_n_images(every_x_frame=30) ### Adjust the frame rate as per the length of video
        fe.extract_frames(every_x_frame=30, img_name=str(ind)+'shakti_kapoor_',dest_path=dire+'/'+'shakti_kapoor')
    except Exception as e:
        print(e)
  

dire=r"C:\Users\NELSON JOSEPH\DOWNLOADS\data\shakti_kapoor" # folder which has the frames or data

dire1=r"C:\Users\NELSON JOSEPH\DOWNLOADS\data\shakti_kapoor_frame" # folder where faces will be cropped and stored
os.makedirs(dire1, exist_ok = True)

detector = MTCNN()

def face_detect(path,save):
    image = cv2.imread(path,1)
    result=detector.detect_faces(image)
    if not result:
        print("Their is no any face: ",path)
    if result:
        b=result[0]['box']
        img1=image[b[1]-70:b[1]+b[3]+70,b[0]-70:b[0]+b[2]+70]
        face = cv2.resize(img1, (300, 300))
        cv2.imwrite(save,face)
        return(img)
        
for img in os.listdir(dire):
    try:
        path=dire+'/'+img
        save=dire1+"/"+img
        img2=face_detect(path,save)
    except Exception as e:
        print(e)
print("All is done.")


