import os
import shutil

from_dir = "C:/Users/ilina/Downloads"
to_dir = "C:/Users/ilina/Downloads/sample"

listoffiles=os.listdir(from_dir)
print(listoffiles)

for file_name in listoffiles:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt','.pdf','.doc','.docx']:
        path1=from_dir+'/'+file_name
        path2 = to_dir+'/'+'document_files'
        path3 = to_dir+'/'+'document_files'+'/'+file_name
        if os.path.exists(path2):
            print("movie"+file_name+'.....')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movie"+file_name+'.....')
            shutil.move(path1,path3)