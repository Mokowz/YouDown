from pytube import YouTube
import os

link = input("Enter a link: ")
yt = YouTube(link)

print(f"The video's title is: {yt.title}")
print(" ")
print(f"Number of views: {yt.views}")
print(" ")
print(f"length: {yt.length} seconds")
print(" ")
print(f"Rating: {yt.rating}")

# yt.streams

# print(yt.streams.filter(progressive=True))

# ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')

print("Downloading...")
ys.download(r"C:\Users\ronni\Videos\YouDown")
print("Download completed!")