def sound_splitter():
    from pydub import AudioSegment
    import os
    import shutil
    from os.path import exists
    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = 'short/'
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + '/'
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        sound = AudioSegment.from_file(full_path)
        print(sound)
        first_cut_point = (1 * 00 + 0) * 1000
        last_cut_point = (1 * 00 + 30) * 1000

        sound_clip = sound[first_cut_point:last_cut_point]
        directory = '30CUT/'
        path = os.path.join(audio_dir, directory)
        os.mkdir(path)
        sound_clip.export(os.path.join(audio_dir + '30CUT/', '30CUT-' + audio_file_dir))
        first_cut_point = (1 * 00 + 0) * 1000
        last_cut_point = (1 * 60 + 0) * 1000

        sound_clip = sound[first_cut_point:last_cut_point]
        directory = '60CUT/'
        path = os.path.join(audio_dir, directory)
        os.mkdir(path)

        sound_clip.export(os.path.join(audio_dir + '60CUT/', '60CUT-' + audio_file_dir))
        folder_number = folder_number + 1

    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = 'medium/'
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + '/'
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        sound = AudioSegment.from_file(full_path)
        print(sound)
        first_cut_point = (1 * 00 + 0) * 1000
        last_cut_point = (1 * 00 + 30) * 1000

        sound_clip = sound[first_cut_point:last_cut_point]

        directory = '30CUT/'
        path = os.path.join(audio_dir, directory)
        os.mkdir(path)

        sound_clip.export(os.path.join(audio_dir + '30CUT/', '30CUT-' + audio_file_dir))
        first_cut_point = (1 * 00 + 0) * 1000
        last_cut_point = (1 * 60 + 0) * 1000

        sound_clip = sound[first_cut_point:last_cut_point]

        directory = '60CUT/'
        path = os.path.join(audio_dir, directory)
        os.mkdir(path)

        sound_clip.export(os.path.join(audio_dir + '60CUT/', '60CUT-' + audio_file_dir))
        folder_number = folder_number + 1
