from pytube import Playlist
from pytube import YouTube

p = input("Enter Playlist URL: ")
 
playlist = Playlist(p)

pURL = playlist.video_urls

for video in pURL:
    yt = YouTube(video)
    ya = yt.streams.get_highest_resolution()
    ya.download('/home/aladdin/')
    print(f'Done: {yt.title}')