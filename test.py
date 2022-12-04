'''
import os
folder_number = 1
while folder_number <=50:
    folder_number_str = str(folder_number)
    folder_count = 0  # type: int
    input_path = 'for_analysis/medium/' + folder_number_str + '/60CUT'  # type: str
    for folders in os.listdir(input_path):  # loop over all files
        if os.path.isdir(os.path.join(input_path, folders)):  # if it's a directory
            folder_count += 1  # increment counter
            print(folder_count)
    folder_number += 1
'''
import bz2
import os
import shutil
import zipfile

filepath ='for_analysis/short/1/30CUT/DEEPBASS/DEEPBASS.CSV.BZ2'
zipfile = bz2.BZ2File(filepath) # open the file
data = zipfile.read() # get the decompressed data
newfilepath = filepath[:-4] # assuming the filepath ends with .bz2
open(newfilepath, 'wb').write(data) # write a uncompressed file