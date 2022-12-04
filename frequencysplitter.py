def frequency_splitter_Short_30CUT():
    import numpy as np
    import sounddevice as sd
    import os
    import soundfile as sf
    import matplotlib.pyplot as plt
    import scipy.signal as sig
    import shutil
    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = 'short/'
        cut_type = '/30CUT/'
        dir_for_check = 'for_analysis/' + folder_type + folder_number_str + '/30CUT'
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str + cut_type)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + cut_type
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        data, fs = sf.read(full_path)
        print(data.shape, fs)
        plt.plot(data)

        def apply_fade(signal):
            # Use a half-cosine window
            window = sig.hann(8192)
            # Use just the half of it
            fade_length = window.shape[0] // 2
            # Fade-in
            signal[:fade_length] *= window[:fade_length]
            # Fade-out
            signal[-fade_length:] *= window[fade_length:]
            # Return the modified signal
            return signal

        def second_order_filter(break_frequency, BW, fs2):
            tan = np.tan(np.pi * BW / fs)
            c = (tan - 1) / (tan + 1)
            d = - np.cos(2 * np.pi * break_frequency / fs2)

            b = [-c, d * (1 - c), 1]
            a = [1, d * (1 - c), -c]

            return b, a

        def bandstop_bandpass(signal, Q, center_frequency, fs2, bandpass=False):
            filtered = np.zeros_like(signal)

            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0

            for i in range(signal.shape[0]):
                BW = center_frequency[i] / Q

                b, a = second_order_filter(center_frequency[i], BW, fs2)

                x = signal[i]

                y = b[0] * x + b[1] * x1 + b[2] * x2 - a[1] * y1 - a[2] * y2

                y2 = y1
                y1 = y
                x2 = x1
                x1 = x

                filtered[i] = y

            sign = -1 if bandpass else 1

            output = 0.5 * (signal + sign * filtered)

            return output

        def split():
            fs2 = 44100
            length_seconds = 30
            length_samples = fs * length_seconds
            Q = 10
            band = 1
            while band <12:
                if band == 1:
                    center_frequency = np.geomspace(30, 30, length_samples)
                    band_select = 'DEEPBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 2:
                    center_frequency = np.geomspace(60, 60, length_samples)
                    band_select = 'LOWBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 3:
                    center_frequency = np.geomspace(120, 120, length_samples)
                    band_select = 'MIDBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 4:
                    center_frequency = np.geomspace(230, 230, length_samples)
                    band_select = 'UPPERBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 5:
                    center_frequency = np.geomspace(450, 450, length_samples)
                    band_select = 'LOWERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 6:
                    center_frequency = np.geomspace(900, 900, length_samples)
                    band_select = 'MIDDLEMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 7:
                    center_frequency = np.geomspace(1800, 1800, length_samples)
                    band_select = 'UPPERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 8:
                    center_frequency = np.geomspace(3700, 3700, length_samples)
                    band_select = 'PRESENCERANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 9:
                    center_frequency = np.geomspace(7500, 7500, length_samples)
                    band_select = 'HIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 10:
                    center_frequency = np.geomspace(15000, 15000, length_samples)
                    band_select = 'EXTREMEHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 11:
                    center_frequency = np.geomspace(17500, 17500, length_samples)
                    band_select = 'HYPERHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                bandstop_filtered = bandstop_bandpass(data, Q, center_frequency, fs2)

                bandpass_filtered = bandstop_bandpass(data, Q, center_frequency, fs2,
                                                                   bandpass=True)
                amplitude = 0.5
                bandstop_filtered *= amplitude
                bandpass_filtered *= amplitude

                sf.write(os.path.join(path, '30CUT' + band_select + '_Bandstop-' + audio_file_dir), bandstop_filtered, fs2)
                sf.write(os.path.join(path, '30CUT' + band_select + '_Bandpass-' + audio_file_dir), bandpass_filtered, fs2)
                band = band + 1


        folder_count = 0  # type: int
        input_path = 'for_analysis/short/'+ folder_number_str + '/30CUT' # type: str
        for folders in os.listdir(input_path):  # loop over all files
            if os.path.isdir(os.path.join(input_path, folders)):  # if it's a directory
                folder_count += 1  # increment counter
                print(folder_count)

        if folder_count == 11:
            print('Files already created for:' + audio_file_dir)
            folder_number = folder_number + 1
            sf.close(full_path)

        elif folder_count == 0:
            split()
            folder_number = folder_number + 1
            sf.close(full_path)
        else:
            shutil.rmtree(dir_for_check + '/DEEPBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDDLEMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/PRESENCERANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/EXTREMEHIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HYPERHIGHEND', ignore_errors=True)
            split()
            folder_number = folder_number + 1
            sf.close(full_path)


def frequency_splitter_Short_60CUT():
    import numpy as np
    import sounddevice as sd
    import os
    import soundfile as sf
    import matplotlib.pyplot as plt
    import scipy.signal as sig
    import shutil
    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = 'short/'
        cut_type = '/60CUT/'
        dir_for_check = 'for_analysis/' + folder_type + folder_number_str + '/60CUT'
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str + cut_type)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + cut_type
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        data, fs = sf.read(full_path)
        print(data.shape, fs)
        plt.plot(data)

        def apply_fade(signal):
            # Use a half-cosine window
            window = sig.hann(8192)
            # Use just the half of it
            fade_length = window.shape[0] // 2
            # Fade-in
            signal[:fade_length] *= window[:fade_length]
            # Fade-out
            signal[-fade_length:] *= window[fade_length:]
            # Return the modified signal
            return signal

        def second_order_filter(break_frequency, BW, fs2):
            tan = np.tan(np.pi * BW / fs)
            c = (tan - 1) / (tan + 1)
            d = - np.cos(2 * np.pi * break_frequency / fs2)

            b = [-c, d * (1 - c), 1]
            a = [1, d * (1 - c), -c]

            return b, a

        def bandstop_bandpass(signal, Q, center_frequency, fs2, bandpass=False):
            filtered = np.zeros_like(signal)

            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0

            for i in range(signal.shape[0]):
                BW = center_frequency[i] / Q

                b, a = second_order_filter(center_frequency[i], BW, fs2)

                x = signal[i]

                y = b[0] * x + b[1] * x1 + b[2] * x2 - a[1] * y1 - a[2] * y2

                y2 = y1
                y1 = y
                x2 = x1
                x1 = x

                filtered[i] = y

            sign = -1 if bandpass else 1

            output = 0.5 * (signal + sign * filtered)

            return output

        def split():
            fs2 = 44100
            length_seconds = 60
            length_samples = fs * length_seconds
            Q = 10
            band = 1
            while band <12:
                if band == 1:
                    center_frequency = np.geomspace(30, 30, length_samples)
                    band_select = 'DEEPBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 2:
                    center_frequency = np.geomspace(60, 60, length_samples)
                    band_select = 'LOWBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 3:
                    center_frequency = np.geomspace(120, 120, length_samples)
                    band_select = 'MIDBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 4:
                    center_frequency = np.geomspace(230, 230, length_samples)
                    band_select = 'UPPERBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 5:
                    center_frequency = np.geomspace(450, 450, length_samples)
                    band_select = 'LOWERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 6:
                    center_frequency = np.geomspace(900, 900, length_samples)
                    band_select = 'MIDDLEMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 7:
                    center_frequency = np.geomspace(1800, 1800, length_samples)
                    band_select = 'UPPERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 8:
                    center_frequency = np.geomspace(3700, 3700, length_samples)
                    band_select = 'PRESENCERANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 9:
                    center_frequency = np.geomspace(7500, 7500, length_samples)
                    band_select = 'HIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 10:
                    center_frequency = np.geomspace(15000, 15000, length_samples)
                    band_select = 'EXTREMEHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 11:
                    center_frequency = np.geomspace(17500, 17500, length_samples)
                    band_select = 'HYPERHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                bandstop_filtered = bandstop_bandpass(data, Q, center_frequency, fs2)

                bandpass_filtered = bandstop_bandpass(data, Q, center_frequency, fs2,
                                                                   bandpass=True)
                amplitude = 0.5
                bandstop_filtered *= amplitude
                bandpass_filtered *= amplitude

                sf.write(os.path.join(path, '60CUT' + band_select + '_Bandstop-' + audio_file_dir), bandstop_filtered, fs2)
                sf.write(os.path.join(path, '60CUT' + band_select + '_Bandpass-' + audio_file_dir), bandpass_filtered, fs2)
                band = band + 1

        folder_count = 0  # type: int
        input_path = 'for_analysis/short/'+ folder_number_str + '/60CUT' # type: str
        for folders in os.listdir(input_path):  # loop over all files
            if os.path.isdir(os.path.join(input_path, folders)):  # if it's a directory
                folder_count += 1  # increment counter
                print(folder_count)

        if folder_count == 11:
            print('Files already created for:' + audio_file_dir)
            folder_number = folder_number + 1
            sf.close(full_path)
        elif folder_count == 0:
            split()
            folder_number = folder_number + 1
            sf.close(full_path)
        else:
            shutil.rmtree(dir_for_check + '/DEEPBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDDLEMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/PRESENCERANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/EXTREMEHIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HYPERHIGHEND', ignore_errors=True)
            split()
            folder_number = folder_number + 1
            sf.close(full_path)



def frequency_splitter_Medium_30CUT():
    import numpy as np
    import sounddevice as sd
    import os
    import soundfile as sf
    import matplotlib.pyplot as plt
    import scipy.signal as sig
    import shutil
    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = 'medium/'
        cut_type = '/30CUT/'
        dir_for_check = 'for_analysis/' + folder_type + folder_number_str + '/30CUT'
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str + cut_type)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + cut_type
        print(dir_for_check)
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        data, fs = sf.read(full_path)
        print(data.shape, fs)
        plt.plot(data)

        def apply_fade(signal):
            # Use a half-cosine window
            window = sig.hann(8192)
            # Use just the half of it
            fade_length = window.shape[0] // 2
            # Fade-in
            signal[:fade_length] *= window[:fade_length]
            # Fade-out
            signal[-fade_length:] *= window[fade_length:]
            # Return the modified signal
            return signal

        def second_order_filter(break_frequency, BW, fs2):
            tan = np.tan(np.pi * BW / fs)
            c = (tan - 1) / (tan + 1)
            d = - np.cos(2 * np.pi * break_frequency / fs2)

            b = [-c, d * (1 - c), 1]
            a = [1, d * (1 - c), -c]

            return b, a

        def bandstop_bandpass(signal, Q, center_frequency, fs2, bandpass=False):
            filtered = np.zeros_like(signal)

            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0

            for i in range(signal.shape[0]):
                BW = center_frequency[i] / Q

                b, a = second_order_filter(center_frequency[i], BW, fs2)

                x = signal[i]

                y = b[0] * x + b[1] * x1 + b[2] * x2 - a[1] * y1 - a[2] * y2

                y2 = y1
                y1 = y
                x2 = x1
                x1 = x

                filtered[i] = y

            sign = -1 if bandpass else 1

            output = 0.5 * (signal + sign * filtered)

            return output

        def split():
            fs2 = 44100
            length_seconds = 30
            length_samples = fs * length_seconds
            Q = 10
            band = 1
            while band <12:
                if band == 1:
                    center_frequency = np.geomspace(30, 30, length_samples)
                    band_select = 'DEEPBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 2:
                    center_frequency = np.geomspace(60, 60, length_samples)
                    band_select = 'LOWBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 3:
                    center_frequency = np.geomspace(120, 120, length_samples)
                    band_select = 'MIDBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 4:
                    center_frequency = np.geomspace(230, 230, length_samples)
                    band_select = 'UPPERBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 5:
                    center_frequency = np.geomspace(450, 450, length_samples)
                    band_select = 'LOWERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 6:
                    center_frequency = np.geomspace(900, 900, length_samples)
                    band_select = 'MIDDLEMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 7:
                    center_frequency = np.geomspace(1800, 1800, length_samples)
                    band_select = 'UPPERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 8:
                    center_frequency = np.geomspace(3700, 3700, length_samples)
                    band_select = 'PRESENCERANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 9:
                    center_frequency = np.geomspace(7500, 7500, length_samples)
                    band_select = 'HIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 10:
                    center_frequency = np.geomspace(15000, 15000, length_samples)
                    band_select = 'EXTREMEHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 11:
                    center_frequency = np.geomspace(17500, 17500, length_samples)
                    band_select = 'HYPERHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                bandstop_filtered = bandstop_bandpass(data, Q, center_frequency, fs2)

                bandpass_filtered = bandstop_bandpass(data, Q, center_frequency, fs2,
                                                                   bandpass=True)
                amplitude = 0.5
                bandstop_filtered *= amplitude
                bandpass_filtered *= amplitude
                sf.write(os.path.join(path, '30CUT' + band_select + '_Bandstop-' + audio_file_dir), bandstop_filtered, fs2)
                sf.write(os.path.join(path, '30CUT' + band_select + '_Bandpass-' + audio_file_dir), bandpass_filtered, fs2)
                band = band + 1

        folder_count = 0  # type: int
        input_path = 'for_analysis/medium/'+ folder_number_str + '/30CUT' # type: str
        for folders in os.listdir(input_path):  # loop over all files
            if os.path.isdir(os.path.join(input_path, folders)):  # if it's a directory
                folder_count += 1  # increment counter
                print(folder_count)

        if folder_count == 11:
            print('Files already created for:' + audio_file_dir)
            folder_number = folder_number + 1
            sf.close(full_path)
        elif folder_count == 0:
            split()
            folder_number = folder_number + 1
            sf.close(full_path)
        else:
            shutil.rmtree(dir_for_check + '/DEEPBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDDLEMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/PRESENCERANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/EXTREMEHIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HYPERHIGHEND', ignore_errors=True)
            split()
            folder_number = folder_number + 1
            sf.close(full_path)

def frequency_splitter_Medium_60CUT():
    import numpy as np
    import sounddevice as sd
    import os
    import soundfile as sf
    import matplotlib.pyplot as plt
    import scipy.signal as sig
    import shutil
    folder_number = 1
    while folder_number <= 50:
        folder_number_str = str(folder_number)
        folder_type = 'medium/'
        cut_type = '/60CUT/'
        dir_for_check = 'for_analysis/' + folder_type + folder_number_str + '/60CUT'
        audio_file_dir = os.listdir('for_analysis/' + folder_type + folder_number_str + cut_type)[0]
        audio_dir = 'for_analysis/' + folder_type + folder_number_str + cut_type
        print(audio_dir)
        print(audio_file_dir)
        length = len(audio_dir)
        file_format = audio_dir[length - 3:]
        full_path = audio_dir + audio_file_dir
        print(full_path)
        data, fs = sf.read(full_path)
        print(data.shape, fs)
        plt.plot(data)

        def apply_fade(signal):
            # Use a half-cosine window
            window = sig.hann(8192)
            # Use just the half of it
            fade_length = window.shape[0] // 2
            # Fade-in
            signal[:fade_length] *= window[:fade_length]
            # Fade-out
            signal[-fade_length:] *= window[fade_length:]
            # Return the modified signal
            return signal

        def second_order_filter(break_frequency, BW, fs2):
            tan = np.tan(np.pi * BW / fs)
            c = (tan - 1) / (tan + 1)
            d = - np.cos(2 * np.pi * break_frequency / fs2)

            b = [-c, d * (1 - c), 1]
            a = [1, d * (1 - c), -c]

            return b, a

        def bandstop_bandpass(signal, Q, center_frequency, fs2, bandpass=False):
            filtered = np.zeros_like(signal)

            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0

            for i in range(signal.shape[0]):
                BW = center_frequency[i] / Q

                b, a = second_order_filter(center_frequency[i], BW, fs2)

                x = signal[i]

                y = b[0] * x + b[1] * x1 + b[2] * x2 - a[1] * y1 - a[2] * y2

                y2 = y1
                y1 = y
                x2 = x1
                x1 = x

                filtered[i] = y

            sign = -1 if bandpass else 1

            output = 0.5 * (signal + sign * filtered)

            return output

        def split():
            fs2 = 44100
            length_seconds = 60
            length_samples = fs * length_seconds
            Q = 10
            band = 1
            while band <12:
                if band == 1:
                    center_frequency = np.geomspace(30, 30, length_samples)
                    band_select = 'DEEPBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 2:
                    center_frequency = np.geomspace(60, 60, length_samples)
                    band_select = 'LOWBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 3:
                    center_frequency = np.geomspace(120, 120, length_samples)
                    band_select = 'MIDBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 4:
                    center_frequency = np.geomspace(230, 230, length_samples)
                    band_select = 'UPPERBASS'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 5:
                    center_frequency = np.geomspace(450, 450, length_samples)
                    band_select = 'LOWERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 6:
                    center_frequency = np.geomspace(900, 900, length_samples)
                    band_select = 'MIDDLEMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 7:
                    center_frequency = np.geomspace(1800, 1800, length_samples)
                    band_select = 'UPPERMIDRANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 8:
                    center_frequency = np.geomspace(3700, 3700, length_samples)
                    band_select = 'PRESENCERANGE'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 9:
                    center_frequency = np.geomspace(7500, 7500, length_samples)
                    band_select = 'HIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 10:
                    center_frequency = np.geomspace(15000, 15000, length_samples)
                    band_select = 'EXTREMEHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                elif band == 11:
                    center_frequency = np.geomspace(17500, 17500, length_samples)
                    band_select = 'HYPERHIGHEND'
                    directory = band_select
                    path = os.path.join(audio_dir, directory)
                    os.mkdir(path)
                    print(band_select)
                bandstop_filtered = bandstop_bandpass(data, Q, center_frequency, fs2)

                bandpass_filtered = bandstop_bandpass(data, Q, center_frequency, fs2,
                                                                   bandpass=True)
                amplitude = 0.5
                bandstop_filtered *= amplitude
                bandpass_filtered *= amplitude

                sf.write(os.path.join(path, '60CUT' + band_select + '_Bandstop-' + audio_file_dir), bandstop_filtered, fs2)
                sf.write(os.path.join(path, '60CUT' + band_select + '_Bandpass-' + audio_file_dir), bandpass_filtered, fs2)
                band = band + 1

        folder_count = 0  # type: int
        input_path = 'for_analysis/medium/'+ folder_number_str + '/60CUT' # type: str
        for folders in os.listdir(input_path):  # loop over all files
            if os.path.isdir(os.path.join(input_path, folders)):  # if it's a directory
                folder_count += 1  # increment counter
                print(folder_count)

        if folder_count == 11:
            print('Files already created for:' + audio_file_dir)
            folder_number = folder_number + 1
            sf.close(full_path)
        elif folder_count == 0:
            split()
            folder_number = folder_number + 1
            sf.close(full_path)
        else:
            shutil.rmtree(dir_for_check + '/DEEPBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERBASS', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/LOWERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/MIDDLEMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/UPPERMIDRANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/PRESENCERANGE', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/EXTREMEHIGHEND', ignore_errors=True)
            shutil.rmtree(dir_for_check + '/HYPERHIGHEND', ignore_errors=True)
            split()
            folder_number = folder_number + 1
            sf.close(full_path)
'''''



    cutoff_frequency = np.geomspace(50, 50, input_signal.shape[0])
    allpass_output = np.zeros_like(input_signal)
    dn_1 = 0

    for n in range(input_signal.shape[0]):
        break_frequency = cutoff_frequency[n]
        tan = np.tan(np.pi * break_frequency / sampling_rate)
        a1 = (tan - 1) / (tan + 1)
        allpass_output[n] = a1 * input_signal[n] + dn_1
        dn_1 = input_signal[n] - a1 * allpass_output[n]

    if highpass:
        allpass_output *= -1

    filter_output = input_signal + allpass_output

    filter_output *= 0.5

    filter_output *= amplitude

    sd.play(filter_output, sampling_rate)
    sd.wait()
'''''

