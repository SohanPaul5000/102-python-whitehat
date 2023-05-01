import os 
import shutil


source = "C:/Users/mrsoh/Downloads"
destination = "C:/Users/mrsoh/Downloads/Download_files"

list_of_files=os.listdir(source)
#print(list_of_files)

for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    #print(extention)
    if extention == '':
        continue
    if extention in [".jpg", ".jpeg", ".png", ".gif", ".webm" ]:
        path1=source+'/'+file_name
        path2=destination+'/'+"image_files"
        path3=destination+'/'+"image_files"+'/'+file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moving")

        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving22")
    
    if extention in [".pdf", ".doc", ".docx", ".pptx" ]:
        path1=source+'/'+file_name
        path2=destination+'/'+"document_files"
        path3=destination+'/'+"document_files"+'/'+file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moving")

        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving22")

    
    if extention in [".exe", ".zip", ".rar" ]:
        path1=source+'/'+file_name
        path2=destination+'/'+"app_files"
        path3=destination+'/'+"app_files"+'/'+file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moving")

        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving22")