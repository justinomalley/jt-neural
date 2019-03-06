import ffmpy
import os
import sys
import subprocess

video_path = './input/videos/'
#video_path = sys.argv[1]

# Cut video into frames
for filename in os.listdir(video_path):
    if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
        print('oyo')
        os.system("ffmpeg -i ./video_input/min_test.mp4 ./video_input/temp/$filename%03d.png")
    else:
        continue
