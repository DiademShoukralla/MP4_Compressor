from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames
import os
import subprocess
import datetime

input_file = "temp.txt"

def create_input_file(filenames):
    filenames = [f'{fname}\n' for fname in filenames]
    with open(input_file, 'w') as f:
        f.writelines(filenames)


def destroy_input_file():
    os.remove(input_file)

output_file = f'combined_{datetime.datetime.now().strftime("%f")}.mp4'
open(output_file, 'w').close()

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filenames = askopenfilenames() # show an "Open" dialog box and return the path to the selected file

create_input_file(filenames)

process = subprocess.Popen(f'ffmpeg -f concat -i {input_file} -c copy {output_file}')

process.wait() 

destroy_input_file()