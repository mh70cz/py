import shutil
import os
 
path_src = "/data/user/0/ru.iiec.pydroid3/files/aw/data"
path_dst = "/storage/emulated/0/mypy/aw/data"
 
src = path_src + "/idnes+lidovky2018-02-19.csv"
dst = path_dst + "/idnes+lidovky2018-02-19.csv"

print("working folder")
print(os.getcwd())

files_path_scr = os.listdir(path_src)
print("files in path_src")
print (files_path_scr)

files_path_dst = os.listdir(path_dst)
print("Files in path_dst")
print (files_path_dst)

shutil.copyfile(src, dst)