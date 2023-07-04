from pytube import YouTube
url=YouTube("")# enter url in inverted commas
video=url.streams.first()
video.download()
print("downloaded successfully")