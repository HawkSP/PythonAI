def get_sound():
    from cryptography.fernet import Fernet
    import csv
    import pandas as pd
    import os
    import json
    import spotipy.util as util
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    import urllib.request
    import re
    from pytube import YouTube
    from os.path import exists

    key = ''
    with open('auth.key', 'rb') as file:
        key = file.read()

    encryptedData = ''
    with open('auth-info.txt', 'rb') as file:
        encryptedData = file.read()

    encrypt_key = Fernet(key)

    decryptedData = encrypt_key.decrypt(encryptedData)

    cid = decryptedData.decode()

    encryptedData = ''
    with open('auth-info-secret.txt', 'rb') as file:
        encryptedData = file.read()

    encrypt_key = Fernet(key)

    decryptedData = encrypt_key.decrypt(encryptedData)

    secret = decryptedData.decode()


    os.environ['SPOTIPY_CLIENT_ID'] = cid
    os.environ['SPOTIPY_CLIENT_SECRET'] = secret
    os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'
    username = ""
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
        for song in range(50):
            list = []
            list.append(results)
            with open('short_top50_data.json', 'w', encoding='utf-8') as f:
                json.dump(list, f, ensure_ascii=False, indent=4)
    else:
        print("Can't get token for", username)

    with open('short_top50_data.json') as f:
        data = json.load(f)

    list_of_results = data[0]["items"]
    list_of_artist_names = []
    list_of_artist_uri = []
    list_of_song_names = []
    list_of_song_uri = []
    list_of_durations_ms = []
    list_of_explicit = []
    list_of_albums = []
    list_of_popularity = []
    list_of_release_date = []

    for result in list_of_results:
        result["album"]
        this_artists_name = result["artists"][0]["name"]
        list_of_artist_names.append(this_artists_name)
        this_artists_uri = result["artists"][0]["uri"]
        list_of_artist_uri.append(this_artists_uri)
        list_of_songs = result["name"]
        list_of_song_names.append(list_of_songs)
        song_uri = result["uri"]
        list_of_song_uri.append(song_uri)
        list_of_duration = result["duration_ms"]
        list_of_durations_ms.append(list_of_duration)
        song_explicit = result["explicit"]
        list_of_explicit.append(song_explicit)
        this_album = result["album"]["name"]
        list_of_albums.append(this_album)
        song_popularity = result["popularity"]
        list_of_popularity.append(song_popularity)
        release_date = result["album"]["release_date"]
        list_of_release_date.append(release_date)

    all_songs = pd.DataFrame(
        {'artist': list_of_artist_names,
         'artist_uri': list_of_artist_uri,
         'song': list_of_song_names,
         'song_uri': list_of_song_uri,
         'duration_ms': list_of_durations_ms,
         'explicit': list_of_explicit,
         'album': list_of_albums,
         'popularity': list_of_popularity,
         'release_date': list_of_release_date

         })

    all_songs_saved = all_songs.to_csv('short_top50_data.json')

    data = []
    with open('short_top50_data.json', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    col = [x[1] for x in data]
    col2 = [x[3] for x in data]
    col3 = [x[9] for x in data]
    count = 1
    new_folder = 0

    def isascii(s):
        """Check if the characters in string s are in ASCII, U+0-U+7F."""
        return len(s) == len(s.encode())


    while count < 51:
        song_download = col[count] + " " + col2[count]
        name_of_song = col[count] + " " + col2[count]
        if isascii(song_download):
            print(song_download)
            song_download = song_download.replace(" " + ':' + ';' + '!' + '"' + '£' + '$' + '%'+ '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '[' + ']' + '{' + '}' + '@' + "'" + '#' + '~' + '<' '>' + ',' + '.' + '?' + '/' + '`' + '¬', "+")
            search_keyword = song_download
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + video_ids[0]
            count = count + 1
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            new_folder = new_folder + 1
            new_folder_str = str(new_folder)
            out_file = video.download(output_path="for_analysis/" + "short/" + new_folder_str)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.wav'
            os.rename(out_file, new_file)
            file_exists = exists("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.wav")
            if file_exists:
                os.remove("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.wav")
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path="for_analysis/" + "short/" + new_folder_str)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                file_exists = exists("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.mp3")
                if file_exists:
                    os.remove("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.mp3")
                    yt = YouTube(url)
                    video = yt.streams.filter(only_audio=True).first()
                    out_file = video.download(output_path="for_analysis/" + "short/" + new_folder_str)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    file_exists = exists("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.mp3")
                    if file_exists:
                        print("File Unsuccessfully Downloaded")
                        new_folder = new_folder - 1
                    else:
                        print("File Successfully Downloaded as .mp3")
                else:
                    print("File Successfully Downloaded as .mp3")
            else:
                print("File Successfully Downloaded as .wav")
        else:
            song_download = col[count] + " " + col3[count]
            name_of_song = col[count]
            print(song_download)
            song_download = song_download.replace(" " + ':' + ';' + '!' + '"' + '£' + '$' + '%'+ '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '[' + ']' + '{' + '}' + '@' + "'" + '#' + '~' + '<' '>' + ',' + '.' + '?' + '/' + '`' + '¬', "+")
            search_keyword = song_download
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + video_ids[0]
            count = count + 1
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            new_folder = new_folder + 1
            new_folder_str = str(new_folder)
            out_file = video.download(output_path="for_analysis/" + "short/" + new_folder_str)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.wav'
            os.rename(out_file, new_file)
            file_exists = exists("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.wav")
            if file_exists:
                os.remove("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.wav")
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path="for_analysis/" + "short/" + new_folder_str)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                file_exists = exists("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.mp3")
                if file_exists:
                    search_keyword = search_keyword + "+" + col3[count]
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    url = "https://www.youtube.com/watch?v=" + video_ids[0]
                    os.remove("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.mp3")
                    yt = YouTube(url)
                    video = yt.streams.filter(only_audio=True).first()
                    out_file = video.download(output_path="for_analysis/" + "short/" + new_folder_str)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    file_exists = exists("for_analysis/" + "short/" + new_folder_str + "/Video Not Available.mp3")
                    if file_exists:
                        print("File Unsuccessfully Downloaded")
                        new_folder = new_folder - 1

                    else:
                        print("File Successfully Downloaded as .mp3")
                else:
                    print("File Successfully Downloaded as .mp3")
            else:
                print("File Successfully Downloaded as .wav")

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
        for song in range(50):
            list = []
            list.append(results)
            with open('medium_top50_data.json', 'w', encoding='utf-8') as f:
                json.dump(list, f, ensure_ascii=False, indent=4)
    else:
        print("Can't get token for", username)

    with open('medium_top50_data.json') as f:
        data = json.load(f)

    list_of_results = data[0]["items"]
    list_of_artist_names = []
    list_of_artist_uri = []
    list_of_song_names = []
    list_of_song_uri = []
    list_of_durations_ms = []
    list_of_explicit = []
    list_of_albums = []
    list_of_popularity = []
    list_of_release_date = []

    for result in list_of_results:
        result["album"]
        this_artists_name = result["artists"][0]["name"]
        list_of_artist_names.append(this_artists_name)
        this_artists_uri = result["artists"][0]["uri"]
        list_of_artist_uri.append(this_artists_uri)
        list_of_songs = result["name"]
        list_of_song_names.append(list_of_songs)
        song_uri = result["uri"]
        list_of_song_uri.append(song_uri)
        list_of_duration = result["duration_ms"]
        list_of_durations_ms.append(list_of_duration)
        song_explicit = result["explicit"]
        list_of_explicit.append(song_explicit)
        this_album = result["album"]["name"]
        list_of_albums.append(this_album)
        song_popularity = result["popularity"]
        list_of_popularity.append(song_popularity)
        release_date = result["album"]["release_date"]
        list_of_release_date.append(release_date)

    all_songs = pd.DataFrame(
        {'artist': list_of_artist_names,
         'artist_uri': list_of_artist_uri,
         'song': list_of_song_names,
         'song_uri': list_of_song_uri,
         'duration_ms': list_of_durations_ms,
         'explicit': list_of_explicit,
         'album': list_of_albums,
         'popularity': list_of_popularity,
         'release_date': list_of_release_date

         })

    all_songs_saved = all_songs.to_csv('medium_top50_data.json')

    data = []
    with open('medium_top50_data.json', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    col = [x[1] for x in data]
    col2 = [x[3] for x in data]
    col3 = [x[9] for x in data]
    count = 1
    new_folder = 0

    def isascii(s):
        """Check if the characters in string s are in ASCII, U+0-U+7F."""
        return len(s) == len(s.encode())


    while count < 51:
        song_download = col[count] + " " + col2[count]
        name_of_song = col[count] + " " + col2[count]
        if isascii(song_download):
            print(song_download)
            song_download = song_download.replace(" " + ':' + ';' + '!' + '"' + '£' + '$' + '%'+ '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '[' + ']' + '{' + '}' + '@' + "'" + '#' + '~' + '<' '>' + ',' + '.' + '?' + '/' + '`' + '¬', "+")
            search_keyword = song_download
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + video_ids[0]
            count = count + 1
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            new_folder = new_folder + 1
            new_folder_str = str(new_folder)
            out_file = video.download(output_path="for_analysis/" + "medium/" + new_folder_str)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.wav'
            os.rename(out_file, new_file)
            file_exists = exists("for_analysis/" + "medium/"+ new_folder_str + "/Video Not Available.wav")
            if file_exists:
                os.remove("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.wav")
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path="for_analysis/" + "medium/" + new_folder_str)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                file_exists = exists("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.mp3")
                if file_exists:
                    search_keyword = search_keyword + "+" + col3[count]
                    os.remove("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.mp3")
                    yt = YouTube(url)
                    video = yt.streams.filter(only_audio=True).first()
                    out_file = video.download(output_path="for_analysis/" + "medium/" + new_folder_str)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    file_exists = exists("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.mp3")
                    if file_exists:
                        print("File Unsuccessfully Downloaded")
                        new_folder = new_folder - 1
                    else:
                        print("File Successfully Downloaded as .mp3")
                else:
                    print("File Successfully Downloaded as .mp3")
            else:
                print("File Successfully Downloaded as .wav")
        else:
            song_download = col[count] + " " + col3[count]
            name_of_song = col[count]
            print(song_download)
            song_download = song_download.replace(" " + ':' + ';' + '!' + '"' + '£' + '$' + '%'+ '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '[' + ']' + '{' + '}' + '@' + "'" + '#' + '~' + '<' '>' + ',' + '.' + '?' + '/' + '`' + '¬', "+")
            search_keyword = song_download
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + video_ids[0]
            count = count + 1
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            new_folder = new_folder + 1
            new_folder_str = str(new_folder)
            out_file = video.download(output_path="for_analysis/" + "medium/" + new_folder_str)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.wav'
            os.rename(out_file, new_file)
            file_exists = exists("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.wav")
            if file_exists:
                os.remove("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.wav")
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path="for_analysis/" + "medium/" + new_folder_str)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                file_exists = exists("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.mp3")
                if file_exists:
                    search_keyword = search_keyword + "+" + col3[count]
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    url = "https://www.youtube.com/watch?v=" + video_ids[0]
                    os.remove("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.mp3")
                    yt = YouTube(url)
                    video = yt.streams.filter(only_audio=True).first()
                    out_file = video.download(output_path="for_analysis/" + "medium/" + new_folder_str)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    file_exists = exists("for_analysis/" + "medium/" + new_folder_str + "/Video Not Available.mp3")
                    if file_exists:
                        print("File Unsuccessfully Downloaded")
                        new_folder = new_folder - 1
                    else:
                        print("File Successfully Downloaded as .mp3")
                else:
                    print("File Successfully Downloaded as .mp3")
            else:
                print("File Successfully Downloaded as .wav")
