import os
import re

def rename_files():
    #get file names from a folder
    file_names = os.listdir(r"W:/Udacity Nanodegree/prank")
    #print (file_names)
    save_path = os.getcwd()
    print("Current working directory is "+save_path)
    os.chdir(r"W:/Udacity Nanodegree/prank")
    saved_path = os.getcwd()
    print (saved_path)
    #Rename each file
    for file_name in file_names:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.strip("0123456789"))
        os.rename(file_name,file_name.strip("0123456789"))
    os.chdir(save_path)
rename_files()
