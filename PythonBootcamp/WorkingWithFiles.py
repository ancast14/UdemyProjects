import os
import shutil
#import send2trash
import math

print(os.getcwd())

print(os.listdir("C:\\Users"))

f = open("testfile.txt", "w+")
f.write("this is a test file")
f.close()

#shutil.move("testfile.txt", "C:\\Users\\truta")

#os.unlink(path) - deletes a file at the path you provide - not reversible
#os.rmdir(path) - deletes a folder (folder must be empty) at the path you provide - not reversible
#shutil.remtree(path) - removes all files and folders contained in the path - not reversible


#help(math)

