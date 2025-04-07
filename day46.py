'''The os module in python is a built-in library that provides functions for interacting 
    with the operating system .It allows you to perform a wide cariety of tasks 
    ,such as reading and writing files,interacting with the file system ,and
    running system commands.'''

# some common tasks you can perform with the os module:

'''reading and writing files the os module provides functions for opening ,reading,
    and writing files.
    for example,to open a file for reading, you can use open function.'''

# import os 
# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/day{i+1}")
# to rename
# for i in range(0,100):
    # os.rename(f"data/day{i+1}",f"data/tutorial {i+1}")
    # os.rename(f"data/tutorial{i+1}",f"data/tutorial {i+1}")
    # the first (f"data/day{i+1}") is the source where I want the chang eto happen,second is what change (f"data/tutorial{i+1}") i want to happen

#to search/check folders
# folders = os.listdir("data")
# print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

import os

# # Absolute paths for the current and new folder names
# old_path = r"F:\CODING\python\day48.py"
# new_path = r"F:\CODING\python\day49.py"

# # Check if the directory exists before renaming
# if os.path.exists(old_path):
#     os.rename(old_path, new_path)
#     print(f"Renamed '{old_path}' to '{new_path}' successfully!")
# else:
#     print(f"The directory '{old_path}' does not exist.")

if os.path.exists("day.py"):
    os.rename("day.py","day46.py")
