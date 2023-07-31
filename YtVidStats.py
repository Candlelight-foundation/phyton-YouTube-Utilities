### YTVidStats ###
# Shows information and statistics about a youtube video
# This script only works with Python 3.7 or later.

## IMPORTS ##
from pytube import YouTube
import datetime
import sys

## MAIN CODE ##
link = ""
if len(sys.argv) > 1 and sys.argv[1] != None:
    link = sys.argv[1]

else:
    link = input("Video URL >> ")
    
video = YouTube(link)

print(f"[===== {video.title} =====]")
print(f"Link: {link}")
print(f"Title: {video.title}")
print(f"Author: {video.author} ({video.channel_id}, {video.channel_url})")
print(f"Length: {datetime.timedelta(seconds=video.length)}")
print(f"Views: {video.views}")
print(f"Published: {video.publish_date}")
print(f"Description: {video.description}")
print(f"Rating: {video.rating}")
print(f"Keywords: {video.keywords}")
print(f"Metadata: {video.metadata}")
