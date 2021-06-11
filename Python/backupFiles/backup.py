import os
import shutil

path = input("Enter the path of the folder you want to backup: ")
dest = input("Enter the destination path where you want to create backup: ")
path = path + "/"
dest = dest + "/"

files = os.listdir(path)
for f in files:
    shutil.copy((path + f), dest)

print("Backup created successfully!!!")