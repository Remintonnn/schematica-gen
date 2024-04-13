import pynbs
import json
import tkinter as tk
from tkinter import filedialog
import mcschematic
import math

settings = {}
baseKey = 33 #note.key-baseKey = noteblock's pitch

def getSettings():
    global settings
    with open('settings.json') as f:
        settings = json.load(f)
    
def saveSettings():
    pass

# for tick, chord in song:
    #     print(tick, [f"{settings.get('instruments')[note.instrument].get('id')}:{note.key-baseKey}" for note in chord])
def build(song):
    sideLength = settings.get("sideLength")
    def buildHead(sch = mcschematic.MCSchematic()):
        #build the wall stone part
        sch._initFromFile("assets/head_origin.schem")# where the buttom at
        extension = mcschematic.MCSchematic();extension._initFromFile("assets/head_layer_extention.schem")
        for i in range(layerNeed-1):
            sch.placeSchematic(extension,(0,-3*(i+1),0))
        #the right turn from buttom to the first line
        rightTurn = mcschematic.MCSchematic();rightTurn._initFromFile("assets/right_turn.schem")
        for i in range(layerNeed):
            sch.placeSchematic(rightTurn,(sideLength*2+1,-3*i,0))
        #the wire leading to the right turn
        for i in range(sideLength*2):
            for it in range(layerNeed):
                sch.setBlock((i+1,it*-3,0),"minecraft:redstone_wire[east=side,west=side]")
                sch.setBlock((i+1,it*-3-1,0),"minecraft:warped_planks")
        #place the repeaters so signal actually reach the end
        wireLen = 3 #wires on the right turn
        for i in range(sideLength*2):
            wireLen+=1
            if wireLen<0:
                block = "minecraft:warped_planks" if wireLen!=-2 else "minecraft:repeater[facing=west]"
                for it in range(layerNeed): sch.setBlock((sideLength*2-i,it*-3,0),block)
            elif wireLen>=15:
                wireLen = -3 if wireLen==sideLength*2-1 or wireLen==sideLength*2-3 else -4
        


    def module(layer):
        pass
    def turn(layer):
        pass
    def getlayerNeeded():
        # song.header.song_layers is unrelyable as it won't go down after it went up
        # a.k.a won't react to manual song compression 
        result = 0
        for tick, chord in song:
            for note in chord:
                if note.layer>result: result=note.layer
        result+= 1
        result = math.ceil(result/4)
        return result
    
    layerNeed = getlayerNeeded()
    schem = mcschematic.MCSchematic()
    buildHead(schem)
    schem.save("D:\Minecraft\PrismLauncher\instence\Me\.minecraft\schematics\Task", "output", mcschematic.Version.JE_1_20_1)

def init():
    getSettings()
    root = tk.Tk()
    root.withdraw()
    fileName = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other cho)","*.nbs")])
    build(pynbs.read(filename=fileName))
init()