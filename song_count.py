folder_count = 0
def song_count_check(self):
    import os

    folder_count = 0  # type: int
    input_path = self  # type: str
    for folders in os.listdir(input_path):  # loop over all files
        if os.path.isdir(os.path.join(input_path, folders)):  # if it's a directory
            folder_count += 1  # increment counter

    print("There are {} Tracks".format(folder_count))

'''
        path = 'for_analysis/short'
        song_count_check(path)
        if folder_count == 50:
            path = 'for_analysis/medium'
            song_count_check(path)
            if folder_count == 50:
                print('Sounds have been downloaded')
            else:
                shutil.rmtree('for_analysis/short')
                shutil.rmtree('for_analysis/medium')
                get_sound()
                path = 'for_analysis/short'
                song_count_check(path)
                if folder_count == 50:
                    folder_count = 0
                    path = 'for_analysis/medium'
                    song_count_check(path)
                    if folder_count == 50:
                        print('Sounds have been downloaded')
                    else:
                        shutil.rmtree('for_analysis/short')
                        shutil.rmtree('for_analysis/medium')
                        print('ERROR QUITING')
                        quit()

                else:
                    shutil.rmtree('for_analysis/short')
                    shutil.rmtree('for_analysis/medium')
                    print('ERROR QUITING')
                    quit()

        else:
            shutil.rmtree('for_analysis/short')
            shutil.rmtree('for_analysis/medium')
            get_sound()
            path = 'for_analysis/short'
            song_count_check(path)
            if folder_count == 50:
                path = 'for_analysis/medium'
                song_count_check(path)
                if folder_count == 50:
                    print('Sounds have been downloaded')
                else:
                    shutil.rmtree('for_analysis/short')
                    shutil.rmtree('for_analysis/medium')
                    get_sound()
                    path = 'for_analysis/short'
                    song_count_check(path)
                    if folder_count == 50:
                        folder_count = 0
                        path = 'for_analysis/medium'
                        song_count_check(path)
                        if folder_count == 50:
                            print('Sounds have been downloaded')
                        else:
                            shutil.rmtree('for_analysis/short')
                            shutil.rmtree('for_analysis/medium')
                            print('ERROR QUITING')
                            quit()

                    else:
                        shutil.rmtree('for_analysis/short')
                        shutil.rmtree('for_analysis/medium')
                        print('ERROR QUITING')
                        quit()

            else:
                shutil.rmtree('for_analysis/short')
                shutil.rmtree('for_analysis/medium')
                get_sound()
                path = 'for_analysis/short'
                song_count_check(path)
                if folder_count == 50:
                    folder_count = 0
                    path = 'for_analysis/medium'
                    song_count_check(path)
                    if folder_count == 50:
                        print('Sounds have been downloaded')
                    else:
                        shutil.rmtree('for_analysis/short')
                        shutil.rmtree('for_analysis/medium')
                        print('ERROR QUITING')
                        quit()

                else:
                    shutil.rmtree('for_analysis/short')
                    shutil.rmtree('for_analysis/medium')
                    print('ERROR QUITING')
                    quit()
'''
