import pytube

def download(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()    










