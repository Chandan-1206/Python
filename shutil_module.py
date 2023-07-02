# shutil module 

import shutil 
import os
shutil.copy("main.py","main_copy.py") # it copies data from a file to another
# we can also use copy2 which is same as copy but preserves more data like timestamps

# we first have to make a folder named tutorial and a file in it names file.file before running the below code
# shutil.copytree(".tutorial", "mytutorial") # it copies data from a folder to another
# shutil.move(".tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial") # it deletes the folder
# os.remove("file.file") # to remove a file we have to use os module as their is no function in shutil module to remove files
