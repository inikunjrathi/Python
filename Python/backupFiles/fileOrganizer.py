import os
import shutil

path = input("Enter the path of the folder you want to organize: ")
listOfFiles = os.listdir(path)

for file in listOfFiles:
    name,ext = os.path.splitext(file)
    extensions = ext[1:]
    if extensions == "":
        continue
    if os.path.exists(path + '/' + extensions):
        #we will move the file only
        shutil.move(path + '/' + file, path + '/' + extensions + "/" + file)
    else:
        os.makedirs(path + '/' + extensions)
        shutil.move(path + '/' + file, path + '/' + extensions + "/" + file)

print("Folder Organized Successfully!!!")
