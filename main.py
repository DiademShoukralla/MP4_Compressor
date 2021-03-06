from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames
import os
import subprocess

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filenames = askopenfilenames() # show an "Open" dialog box and return the path to the selected file

for filename in filenames:
    file_dir = os.path.abspath(filename).rsplit("\\", 1)
    compressed_dir = "compressed"
    output_dir = os.path.join(file_dir[0], compressed_dir)
    output_file = os.path.join(output_dir, file_dir[1])
    print(output_file)
    subprocess.Popen(f'ffmpeg -i {filename} -c:v libx264 -s 1440x786 {output_file}')
