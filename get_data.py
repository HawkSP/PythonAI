def get_data(folder_type_input, cut_type_input, band_select_input, band_select_main):
    import os
    import soundfile as sf
    from matplotlib import pyplot as plt
    import csv
    import time
    import gc
    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = folder_type_input
        cut_type = cut_type_input
        band_select = band_select_input
        dir_for_check = 'for_analysis/' + folder_type + folder_number_str + cut_type + band_select
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str + cut_type + band_select)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + cut_type + band_select
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        data, fs = sf.read(full_path)
        print(data.shape, fs)
        graph = plt.plot(data)
        plt.xlabel('time')
        plt.ylabel('dB')

        xydata = graph[0].get_data()
        print(xydata)
        with open (audio_dir + band_select_main, 'w') as output:
            writer = csv.writer(output)
            writer.writerow(['x', 'y'])
            for i in range(len(xydata[0])):
                writer.writerow([xydata[0][i], xydata[1][i]])


        plt.show()
        folder_number = folder_number + 1
        time.sleep(0.1)
        gc.collect(generation=2)


get_data('short/', '/30CUT/', 'DEEPBASS/', 'DEEPBASS.CSV')
get_data('short/', '/30CUT/', 'LOWBASS/', 'LOWBASS.CSV')
get_data('short/', '/30CUT/', 'MIDBASS/', 'MIDBASS.CSV')
get_data('short/', '/30CUT/', 'UPPERBASS/', 'UPPERBASS.CSV')
get_data('short/', '/30CUT/', 'LOWERMIDRANGE/', 'LOWERMIDRANGE.CSV')
get_data('short/', '/30CUT/', 'MIDDLEMIDRANGE/', 'MIDDLEMIDRANGE.CSV')
get_data('short/', '/30CUT/', 'UPPERMIDRANGE/', 'UPPERMIDRANGE.CSV')
get_data('short/', '/30CUT/', 'PRESENCERANGE/', 'PRESENCERANGE')
get_data('short/', '/30CUT/', 'HIGHEND/', 'HIGHEND.CSV')
get_data('short/', '/30CUT/', 'EXTREMEHIGHEND/', 'EXTREMEHIGHEND.CSV')
get_data('short/', '/30CUT/', 'HYPERHIGHEND/', 'HYPERHIGHEND.CSV')

get_data('short/', '/60CUT/', 'DEEPBASS/', 'DEEPBASS.CSV')
get_data('short/', '/60CUT/', 'LOWBASS/', 'LOWBASS.CSV')
get_data('short/', '/60CUT/', 'MIDBASS/', 'MIDBASS.CSV')
get_data('short/', '/60CUT/', 'UPPERBASS/', 'UPPERBASS.CSV')
get_data('short/', '/60CUT/', 'LOWERMIDRANGE/', 'LOWERMIDRANGE.CSV')
get_data('short/', '/60CUT/', 'MIDDLEMIDRANGE/', 'MIDDLEMIDRANGE.CSV')
get_data('short/', '/60CUT/', 'UPPERMIDRANGE/', 'UPPERMIDRANGE.CSV')
get_data('short/', '/60CUT/', 'PRESENCERANGE/', 'PRESENCERANGE')
get_data('short/', '/60CUT/', 'HIGHEND/', 'HIGHEND.CSV')
get_data('short/', '/60CUT/', 'EXTREMEHIGHEND/', 'EXTREMEHIGHEND.CSV')
get_data('short/', '/60CUT/', 'HYPERHIGHEND/', 'HYPERHIGHEND.CSV')

get_data('medium/', '/30CUT/', 'DEEPBASS/', 'DEEPBASS.CSV')
get_data('medium/', '/30CUT/', 'LOWBASS/', 'LOWBASS.CSV')
get_data('medium/', '/30CUT/', 'MIDBASS/', 'MIDBASS.CSV')
get_data('medium/', '/30CUT/', 'UPPERBASS/', 'UPPERBASS.CSV')
get_data('medium/', '/30CUT/', 'LOWERMIDRANGE/', 'LOWERMIDRANGE.CSV')
get_data('medium/', '/30CUT/', 'MIDDLEMIDRANGE/', 'MIDDLEMIDRANGE.CSV')
get_data('medium/', '/30CUT/', 'UPPERMIDRANGE/', 'UPPERMIDRANGE.CSV')
get_data('medium/', '/30CUT/', 'PRESENCERANGE/', 'PRESENCERANGE')
get_data('medium/', '/30CUT/', 'HIGHEND/', 'HIGHEND.CSV')
get_data('medium/', '/30CUT/', 'EXTREMEHIGHEND/', 'EXTREMEHIGHEND.CSV')
get_data('medium/', '/30CUT/', 'HYPERHIGHEND/', 'HYPERHIGHEND.CSV')

get_data('medium/', '/60CUT/', 'DEEPBASS/', 'DEEPBASS.CSV')
get_data('medium/', '/60CUT/', 'LOWBASS/', 'LOWBASS.CSV')
get_data('medium/', '/60CUT/', 'MIDBASS/', 'MIDBASS.CSV')
get_data('medium/', '/60CUT/', 'UPPERBASS/', 'UPPERBASS.CSV')
get_data('medium/', '/60CUT/', 'LOWERMIDRANGE/', 'LOWERMIDRANGE.CSV')
get_data('medium/', '/60CUT/', 'MIDDLEMIDRANGE/', 'MIDDLEMIDRANGE.CSV')
get_data('medium/', '/60CUT/', 'UPPERMIDRANGE/', 'UPPERMIDRANGE.CSV')
get_data('medium/', '/60CUT/', 'PRESENCERANGE/', 'PRESENCERANGE')
get_data('medium/', '/60CUT/', 'HIGHEND/', 'HIGHEND.CSV')
get_data('medium/', '/60CUT/', 'EXTREMEHIGHEND/', 'EXTREMEHIGHEND.CSV')
get_data('medium/', '/60CUT/', 'HYPERHIGHEND/', 'HYPERHIGHEND.CSV')