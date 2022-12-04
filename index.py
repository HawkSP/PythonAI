import os
import shutil
start_up = True
if __name__ == "__main__":
    if start_up:
        from soundsplitter import sound_splitter
        from main import get_sound
        from song_count import *
        from login import account_login
        from tkinter import *
        from functools import partial
        get_sound()
        sound_splitter()
        print('Sounds have been split')
        start_up = False

if __name__ == "__main__":
    if not start_up:
        from frequencysplitter import frequency_splitter_Short_30CUT, frequency_splitter_Short_60CUT, \
            frequency_splitter_Medium_30CUT, frequency_splitter_Medium_60CUT
        import multiprocessing

        p1 = multiprocessing.Process(target=frequency_splitter_Short_30CUT)
        p2 = multiprocessing.Process(target=frequency_splitter_Short_60CUT)
        p3 = multiprocessing.Process(target=frequency_splitter_Medium_30CUT)
        p4 = multiprocessing.Process(target=frequency_splitter_Medium_60CUT)

        p1.start()
        p2.start()
        p3.start()
        p4.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()