#SHUTIL MODULE
import shutil

# shutil.copy("day87.py","day88.py")
'''this funtion copies the file located at src to a new location 
    specified by dst. If the destination location alreadyexists,
    the original file will be overwritten.'''

shutil.copy2("day87.py","day88.py")
