from pytube import YouTube
from sys import  argv  

link = argv[1]
yt = YouTube(link)

print("title:" , yt.title)
 
print("View:" , yt.views)

print("View2:" , yt.length)
#ya = yt.streams.get_by_resolution(resolution="720p")


#ya = yt.streams.get_audio_only()

ya = yt.streams.get_highest_resolution()

ya.download('/home/aladdin/')

print("done")
