import tkinter as tk
from tkinter import filedialog
import pynbs
import build

def init():
    root = tk.Tk()
    root.withdraw()
    fileName = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other chioce)","*.nbs")])
    build.build(pynbs.read(filename=fileName))
init()