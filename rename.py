# encoding: Big5
import os

folder_path = 'C:/Users/User/Documents/錄音'

file_list = os.listdir(folder_path)

i = 101
for old_name in file_list:

    new_name = f"back{i}.wav"

    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    i += 1
