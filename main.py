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

def build(song):
    sideLength = settings.get("sideLength")
    def buildHead(sch = mcschematic.MCSchematic()):#the defult value here it's just for typing info
        #build the wall stone part
        sch._initFromFile("assets/head_origin.schem")# where the buttom at
        extension = mcschematic.MCSchematic();extension._initFromFile("assets/head_layer_extention.schem")
        for i in range(layerNeed-1):
            sch.placeSchematic(extension,(0,-3*(i+1),0))

        #the right turn from buttom to the first line
        rightTurn = mcschematic.MCSchematic();rightTurn._initFromFile("assets/init_turn.schem")
        for i in range(layerNeed):
            sch.placeSchematic(rightTurn,(sideLength*2-1,-3*i,0))

        #the wire leading to the right turn
        for i in range(sideLength*2-2):
            for it in range(layerNeed):
                sch.setBlock((i+1,it*-3,0),"minecraft:redstone_wire[east=side,west=side]")
                sch.setBlock((i+1,it*-3-1,0),"minecraft:warped_planks")

        #place the repeaters so signal actually reach the end
        wireLen = 3 #wires on the right turn
        for i in range(sideLength*2-2):
            wireLen+=1
            if wireLen<0:
                block = "minecraft:warped_planks" if wireLen!=-2 else "minecraft:repeater[facing=west]"
                for it in range(layerNeed): sch.setBlock((sideLength*2-2-i,it*-3,0),block)
            elif wireLen>=15:
                wireLen = -3 if wireLen==sideLength*2-1 or wireLen==sideLength*2-3 else -4
    
    modulePos = [2*sideLength-2,0,3] #where the top module's repeater at
    row = [0] #otherwise row+=1 in line 59 would cause error
    module = mcschematic.MCSchematic();module._initFromFile("assets/note_unit.schem")
    turn = mcschematic.MCSchematic();turn._initFromFile("assets/mid_turn.schem")
    def addFrame(delay,sch=mcschematic.MCSchematic()):
        leftToRight = row[0] %2 ==0
        while delay>0:
            if (leftToRight and modulePos[0]<=sideLength*-2-2) or (not leftToRight and  modulePos[0]>=sideLength*2-2):
                for i in range(layerNeed): sch.placeSchematic(turn,(modulePos[0],modulePos[1]-3*i,modulePos[2]))
                modulePos[2]+=3
                leftToRight = not leftToRight;row[0]+=1
                module.getStructure().flip((0,0,0),"yz",True)
                turn.getStructure().flip((0,0,0),"yz",True)
            d = 4 if delay>=4 else delay; delay -= d
            for i in range(layerNeed):
                sch.placeSchematic(module,(modulePos[0],modulePos[1]-3*i,modulePos[2]))
                sch.setBlock((modulePos[0],modulePos[1]-3*i,modulePos[2]),f"minecraft:repeater[facing={'east' if leftToRight else 'west'},delay={d}]")
            modulePos[0] += -2 if leftToRight else 2
        
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

    lastTick = -1
    for tick, chord in song:
        addFrame(tick-lastTick,schem);lastTick=tick
        # print(tick, [f"{settings.get('instruments')[note.instrument].get('id')}:{note.key-baseKey}" for note in chord])
    
    schem.save("D:\Minecraft\PrismLauncher\instence\Me\.minecraft\schematics\Task", "output", mcschematic.Version.JE_1_20_1)

def init():
    getSettings()
    root = tk.Tk()
    root.withdraw()
    fileName = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other chioce)","*.nbs")])
    build(pynbs.read(filename=fileName))
init()