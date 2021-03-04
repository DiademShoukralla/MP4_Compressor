# import pylab
from matplotlib import pyplot as plot
import imageio
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import cv2

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

# filename = "C\:\Users\diade\Documents\School\Spring21\CSC367\recordings\lec5.mp4"
vid = imageio.get_reader(filename,  'ffmpeg')
num = 10
image = vid.get_data(num)
fig = plot.figure()
fig.suptitle('image', fontsize=20)
plot.imshow(image)
small_image = cv2.resize(image, (100, 100))
fig.suptitle('image resized', fontsize=20)
plot.imshow(small_image)
plot.show()