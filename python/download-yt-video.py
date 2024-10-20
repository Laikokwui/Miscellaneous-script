# importing the module 
from pytube import Stream
from pytube import YouTube
from tqdm import tqdm
import os
  
# save file path
# file name with the filetype
# Link to YT video
SAVE_PATH = "C:/Users/LKW/Downloads"
FILE_NAME = "sample.mp4"

# Youtube link
LINK="https://youtu.be/dmeKUD2kD-E"

# video download progress
def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
    pbar.update(len(data_chunk))
    

# create the the folder
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# connection to the youtube
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(LINK, on_progress_callback=progress_callback) 
except: 
    print("\nConnection Error") #to handle exception 

# fetch and download the video
try:
    stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    pbar = tqdm(total=stream.filesize, unit="bytes")
    path = stream.download(output_path = SAVE_PATH, filename = FILE_NAME)
    pbar.close()
    print(f"\nSaved video to {path}")
except: 
    print("\nUnexpected Error!") 
     
print('\nTask Completed!') 
