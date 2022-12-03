import os

os.system("ffmpeg -i input.mp4 -vf scale=320:240 output.mp4")