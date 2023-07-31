### YTVid2MP3 ###
# Downloads a youtube video in .MP3 format (MP3 is an audio format).
# This script only works with Python 3.7 or later, and requires FFMPEG.

## IMPORTS ##
from pytube import YouTube
import subprocess
import shutil
import time
import os

## VARIABLES ##
FFMPEG_PATH = r"./ffmpeg.exe"
MP3_PATH = f"MusicFiles"
LOG_PATH = f"./Log.txt"
StartTime = time.time()

## MAIN CODE ##
# Open the log file
LogFile = open(LOG_PATH, "w")

# Create the output directory if it doesn't already exist
if not os.path.exists(MP3_PATH):
    os.mkdir(MP3_PATH)

# Loop through the link list and download each one
for link in open("YTLinks.txt").readlines():
    # Remove the newline character at the end of the link (this is only for visual purposes)
    link = link.replace('\n', '')

    # Get a reference to the video object via the link
    youtubeObject = YouTube(link)

    # Get the title of the video from the youtube object
    Title = youtubeObject.streams[0].title
    print(f"Downloading \"{Title}\" from \"{link}\"...")
    LogFile.write(f"Downloading \"{Title}\" from \"{link}\"...\n")

    # Retrieve the first audio stream from the youtube object
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    # Attempt to download, convert, and rename the file
    try:
        OutputFile = youtubeObject.download()
        base, ext = os.path.splitext(OutputFile)
        Dir = os.path.join(os.path.dirname(base), MP3_PATH)
        final_file = os.path.join(Dir, os.path.basename(base)) + ".mp3"

        if os.path.exists(final_file):
            if input(f"The file \"{final_file}\" already exists! would you like to replace it? (Y/n) >> ") == "Y":
                os.remove(final_file)

            else:
                raise Exception(f"The file \"{final_file}\" already exists!")

        FFMPEGOutput = subprocess.run([
            FFMPEG_PATH,
            '-i', os.path.join(os.getcwd(), OutputFile),
            os.path.join(os.getcwd(), final_file)
        ], capture_output = True, text = True)

        os.remove(OutputFile)
        LogFile.write(FFMPEGOutput.stdout + "\n")
        LogFile.write(FFMPEGOutput.stderr + "\n\n\n")        
        print("Download completed successfully!\n")

    # If something failed, print an error
    except Exception as EX:
        print(f"An error has occurred: {EX}\n")
        LogFile.write(f"[ERROR] >> {EX}\n")

# It's good practice to close the file when we're done with it
LogFile.close()

EndTime = time.time()
print(f"Operation completed. ({EndTime - StartTime} seconds)")
