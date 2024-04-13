import pynbs
import json
import tkinter as tk
from tkinter import filedialog
import mcschematic

settings = {}
baseKey = 33 #note.key-baseKey = noteblock's pitch

def getSettings():
    global settings
    with open('settings.json') as f:
        settings = json.load(f)
    
def saveSettings():
    pass

def build(song):
    # song.header.song_layers is unrelyable as it won't go down after it went up
    # a.k.a won't react to manual song compression 
    layerNeed = 0
    for tick, chord in song:
        for note in chord:
            if note.layer>layerNeed: layerNeed=note.layer
    print(layerNeed)
    # for tick, chord in song:
    #     print(tick, [f"{settings.get('instruments')[note.instrument].get('id')}:{note.key-baseKey}" for note in chord])
    return
    # schem = mcschematic.MCSchematic()

    # schem.setBlock(  (0, -1, 0), "minecraft:stone"  )

    # schem.save( "", "output", mcschematic.Version.JE_1_18_2,False)
    def buildHead(layer):
        pass
    def module(layer):
        pass
    def turn(layer):
        pass

def init():
    getSettings()
    root = tk.Tk()
    root.withdraw()
    fileName = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other cho)","*.nbs")])
    build(pynbs.read(filename=fileName))
init()