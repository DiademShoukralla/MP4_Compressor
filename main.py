# import pylab
from matplotlib import pyplot as plot
import imageio
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

# filename = "C\:\Users\diade\Documents\School\Spring21\CSC367\recordings\lec5.mp4"
vid = imageio.get_reader(filename,  'ffmpeg')
nums = [10, 287]
for num in nums:
    image = vid.get_data(num)
    fig = plot.figure()
    fig.suptitle('image #{}'.format(num), fontsize=20)
    plot.imshow(image)
plot.show(block=False)