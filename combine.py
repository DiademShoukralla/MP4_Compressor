from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames, askdirectory
from tkinter.simpledialog import askstring
import os
import subprocess
import datetime

input_file = "temp.txt"

def create_input_file(filenames):
    filenames = [f'file \'{fname}\'\n' for fname in filenames]
    print(filenames)
    with open(input_file, 'w') as f:
        f.writelines(filenames)


def destroy_input_file():
    os.remove(input_file)


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filenames = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
if not filenames or len(filenames.length) == 0:
    print("No input files were provided")
    exit()

output_dir = askdirectory()
output_file = f'{askstring("Combined File Name", "Please provide filename (without extension) to generate")}.mp4'
output_file = os.path.join(output_dir, output_file)

create_input_file(filenames)

process = subprocess.Popen(f'ffmpeg -f concat -safe 0 -i {input_file} -c copy {output_file}')

process.wait() 

destroy_input_file()