from pytube import YouTube

link = input('Digite o Link do Video do YouTube para realizar o Download: ')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

