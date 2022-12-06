def uncompress_bz2_to_csv_func(folder_type_input, cut_type_input, band_select_input, band_select_main, folder_number_input):
    folder_number = folder_number_input
    import bz2
    import os
    import shutil
    import zipfile
    folder_number_str = str(folder_number)
    folder_type = folder_type_input
    cut_type = cut_type_input
    band_select = band_select_input
    filepath = 'for_analysis/' + folder_type + folder_number_str + cut_type + band_select + band_select_main
    zipfile = bz2.BZ2File(filepath) # open the file
    data = zipfile.read() # get the decompressed data
    newfilepath = filepath[:-4] # assuming the filepath ends with .bz2
    open(newfilepath, 'wb').write(data) # write a uncompressed file

