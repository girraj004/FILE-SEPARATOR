import os
import shutil
def create(file_name):
    os.mkdir("/home/black_star/Documents/Black_Star/FileSeprator"+"/"+file_name)
    shutil.move(source+i,destination+file_name)

def edit(fe):
    shutil.move(source+i,destination+fe)

source = "/home/black_star/Documents/Black_Star/FileSeprator/fol/"
destination = "/home/black_star/Documents/Black_Star/FileSeprator/"

file_list  = os.listdir(source)
for i in file_list:
    b = i.find(".")
    c = i[b+1:]
    fileSep_data = os.listdir(destination)
    if c not in fileSep_data:
        create(c)
    else:
        edit(c)
     
