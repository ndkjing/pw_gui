import cv2
import pyffmpeg

dir(pyffmpeg)
src = 'D:\pythonProject\pw_gui\streamvideo_save\dist\output.avi'
dst = 'D:\pythonProject\pw_gui\streamvideo_save\dist\output.mp4'


import ffmpy3
ffmpy3.FFmpeg(inputs={src: None}, outputs={dst:None}).run()
