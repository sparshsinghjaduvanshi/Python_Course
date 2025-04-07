#SHUTIL MODULE
import shutil

# shutil.copy("day87.py","day88.py")#for files only
'''this funtion copies the file located at src to a new location 
    specified by dst. If the destination location alreadyexists,
    the original file will be overwritten.'''

# shutil.copy2("day87.py","day88.py")#for files only
'''similar to the upper one but it also preserves more metadata
    about the original file,such as the timestamp'''

# shutil.copytree("sparsh singh","udai pratap")#for folders 
'''function recursively copies the directory located at src to a new 
    location specified by dst. If the destination location already exists,the 
    original directory wll be meged with it.'''

# shutil.move()
'''it moves the file located at src to a new location specified by dst.
    This function is equivalent to renaming a file in most cases.'''

# print(dir(shutil))
shutil.rmtree("sparsh singh")#for folders.
'''this function recursively deletes the 
    directary located at path ,along with all of its contents.This 
    function is similar to using the rm -rf command in a shell.'''
