import os

folder_name = 'my_folder'
folder_path = os.path.join(os.getcwd(), folder_name)

if os.path.exists(folder_path):
    i = 1
    while os.path.exists(folder_path):
        new_folder_name = folder_name + '_' + str(i)
        folder_path = os.path.join(os.getcwd(), new_folder_name)
        i += 1

os.mkdir(folder_path)
print("Folder created:", folder_path)

