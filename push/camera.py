import os
import subprocess

# 启动推流进程
camera_process_0 = subprocess.Popen(['ffmpeg', '-f', 'v4l2', '-framerate', '25', '-video_size', '640x480', '-i', '/dev/video0', '-f', 'mpegts', '-codec:v', 'mpeg1video', '-s', '640x480', '-b:v', '1000k', '-bf', '0', 'http://118.190.156.61:10001/camera_0'])

