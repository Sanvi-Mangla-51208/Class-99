import os
import shutil
source="a"
dest="b"

source = source + '/'
dest=dest+'/'
list_of_files=os.listdir(source)
for files in list_of_files:
    shutil.copy((source+files),dest)