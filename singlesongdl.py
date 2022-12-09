import urllib.request
import re
import os
from pytube import YouTube
def download_song():
    song_download = input("Enter Artist and Track Name: ")
    song_download = song_download.replace(" " + ':' + ';' + '!' + '"' + '£' + '$' + '%'+ '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '[' + ']' + '{' + '}' + '@' + "'" + '#' + '~' + '<' '>' + ',' + '.' + '?' + '/' + '`' + '¬', "+",)
    search_keyword = song_download
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    song_download = song_download.replace("+", " ")
    new_folder = song_download
    new_folder_str = str(new_folder)
    out_file = video.download(output_path="Songs/" + new_folder_str)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.wav'
    os.rename(out_file, new_file)

def main():
    download_song()

if __name__ == "__main__":
    main()

