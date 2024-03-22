import os
import shutil

new_dirc = "/Users/Omar Ahmed/Desktop"
os.chdir(new_dirc)
shortcut_file = "SHORTCUTS"
new_location = os.path.join(new_dirc, shortcut_file)
if(os.path.exists("/Users/Omar Ahmed/Desktop/SHORTCUTS")):
    print("file already exists")
else:
    os.mkdir(os.path.join(new_dirc, shortcut_file))

files = os.listdir(new_dirc)

for file in files:
    if file.endswith('.lnk'):
        file_path = os.path.join(new_dirc, file)
        shutil.move(file_path,new_location)

files_Shortcuts = os.listdir(new_location)

files_sorted = sorted(files_Shortcuts, key=lambda x: os.path.getmtime(os.path.join(new_location, x)))

for file in files_sorted:
    file_path = os.path.join(new_location, file)
    modification_time = os.path.getmtime(file_path)
    print(f"File name: {file} ; Pahth of file: {file_path} ; Date: {modification_time}")