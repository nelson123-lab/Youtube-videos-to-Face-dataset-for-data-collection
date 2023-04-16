from deepface import DeepFace
from tqdm import tqdm
import cv2
import matplotlib.pyplot as plt
import time
import os
start = time.time()
# plt.imshow(img[:,:,::-1])
# plt.show()

dire = r"C:\Users\NELSON JOSEPH\DOWNLOADS\data\Sapna Pabbi_google_data1"
for img in tqdm(os.listdir(dire)):
    path = dire+'/'+img
    try:
        # print(path)
        img = cv2.imread(path)
        result = DeepFace.analyze(img, actions= ['gender'])
        # print("Gender: ", result['gender'])
        if result['gender'] != "Woman":
            os.remove(path)
    except ValueError:
        os.remove(path)
print("All is done.")
time.sleep(1)
end = time.time()
print(f"Runtime of the program is {end-start}")

# from deepface import DeepFace
# from tqdm import tqdm
# import cv2
# import os

# dire = r"C:\Users\NELSON JOSEPH\DOWNLOADS\data\New folder"
# count = 0
# for img in tqdm(os.listdir(dire)):
#     path = dire+'/'+img
#     try:
#         img = cv2.imread(path)
#         result = DeepFace.analyze(img, actions= ['gender'])
#         if result['gender'] == "Man" or result['gender'] == "Woman":
#             count += 1
#     except ValueError:
#         pass
# print("No of human faces =",count)

