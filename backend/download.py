from pytube import YouTube
yt = YouTube('https://youtu.be/G7sDNrtH6rg')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()