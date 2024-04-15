import mcschematic
import math
import setting
import random

settings = setting.getSettings()
def build(song):
    sideLength = settings.get("sideLength")
    def buildHead(sch:mcschematic.MCSchematic):
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

    modulePos = [2*sideLength,0,3] #where the top module's repeater at
    row = [0] #otherwise row+=1 in line 59 would cause error
    module = mcschematic.MCSchematic();module._initFromFile("assets/note_unit.schem")
    turn = mcschematic.MCSchematic();turn._initFromFile("assets/mid_turn.schem")
    orangeLine = [0]
    def addFrame(delay:int,sch:mcschematic.MCSchematic):
        leftToRight = row[0] %2 ==0
        while delay>0:
            d = 4 if delay>=4 else delay; delay -= d
            modulePos[0] += -2 if leftToRight else 2
            if (leftToRight and modulePos[0]<=sideLength*-2-2) or (not leftToRight and  modulePos[0]>=sideLength*2-2):
                for i in range(layerNeed): sch.placeSchematic(turn,(modulePos[0],modulePos[1]-3*i,modulePos[2]))
                modulePos[2]+=3
                leftToRight = not leftToRight;row[0]+=1
                module.getStructure().flip((0,0,0),"yz",True)
                turn.getStructure().flip((0,0,0),"yz",True)
                orangeLine[0]=0
            
            #for better skin control
            moud = mcschematic.MCSchematic();moud._initFromMCStructure(module.getStructure().makeCopy())
            if modulePos[0]+2<=sideLength*-2*0.8 or modulePos[0]+2>=sideLength*2*0.8:
                replaceBlock(moud,"minecraft:bamboo_planks","minecraft:warped_planks")
            elif orangeLine[0]>0:
                orangeLine[0]-=1
                replaceBlock(moud,"minecraft:bamboo_planks","minecraft:acacia_planks")
            elif random.randint(1,30)<=1:
                replaceBlock(moud,"minecraft:bamboo_planks","minecraft:acacia_planks")
                orangeLine[0] = random.randint(2,5)
            elif random.randint(1,10)<=1:
                replaceBlock(moud,"minecraft:bamboo_planks","minecraft:acacia_planks")
            for i in range(layerNeed):
                sch.placeSchematic(moud,(modulePos[0],modulePos[1]-3*i,modulePos[2]))
                sch.setBlock((modulePos[0],modulePos[1]-3*i,modulePos[2]),f"minecraft:repeater[facing={'east' if leftToRight else 'west'},delay={d}]")

    ins = settings.get('instruments')
    baseKey = 33 #note.key-baseKey = noteblock's pitch
    notePos = [[[-2,-1,-1],[-2,-1,1],[-1,0,-1],[-1,0,1]],[[2,-1,-1],[2,-1,1],[1,0,-1],[1,0,1]]]
    def addNote(notes:list,sch:mcschematic.MCSchematic):
        for note in notes:
            layer = note.layer# + 4-highestNote%4 #to push the song down and make the buttom layer touch ground
            np = notePos[row[0]%2][layer%4]
            layerOffset = (layer//4)*-3
            sch.setBlock((modulePos[0]+np[0],modulePos[1]+np[1]+layerOffset,modulePos[2]+np[2]),
                            f"minecraft:note_block[instrument={ins[note.instrument].get('id')},note={note.key-baseKey}]")
            sch.setBlock((modulePos[0]+np[0],modulePos[1]+np[1]+layerOffset-1,modulePos[2]+np[2]),
                            ins[note.instrument].get('block'))
            if(ins[note.instrument].get('block')=="sand"):
                sch.setBlock((modulePos[0]+np[0],modulePos[1]+np[1]+layerOffset-2,modulePos[2]+np[2]),"stone")
            sch.setBlock((modulePos[0]-1+2*(row[0]%2),modulePos[1]-1+layerOffset,modulePos[2]),
                            "minecraft:redstone_wire[east=side,south=side,north=side,west=side]")

    def addWalkWay(sch:mcschematic.MCSchematic):
        for x in range(3):
            for z in range(3*row[0]):
                sch.setBlock((-3+x,2,3+z),"minecraft:stone")
    def addBottonPlate(sch:mcschematic.MCSchematic):
        for z in range(3*(2+row[0])):
            for x in range(3+4*sideLength):
                if (z-1)%3!=0:
                    if sch.getBlockDataAt((-3-2*sideLength+x,1-3*layerNeed,-1+z))=="minecraft:air":
                        sch.setBlock( (-3-2*sideLength+x,1-3*layerNeed,-1+z),"minecraft:mud")
                    continue
                sch.setBlock( (-3-2*sideLength+x,1-3*layerNeed,-1+z),"minecraft:stone")

    def counteLayer():
        # song.header.song_layers is unrelyable as it won't go down after it went up
        # a.k.a won't react to manual song compression 
        highest = 0
        for tick, chord in song:
            for note in chord:
                if note.layer>highest: highest=note.layer
        highest+= 1
        return math.ceil(highest/4), highest

    def replaceBlock(sch:mcschematic.MCSchematic,target:str,replacement:str):
        lower, higher= sch.getStructure().getBounds()
        x1,y1,z1 = lower; x2,y2,z2 = higher
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    if sch.getBlockDataAt((x,y,z))!=target:continue
                    sch.setBlock((x,y,z),replacement)

    # VVV layer of frame needed, 4note per layer
    layerNeed, highestNote = counteLayer()
    schem = mcschematic.MCSchematic()
    buildHead(schem)

    lastTick = -1
    for tick, chord in song:
        addFrame(tick-lastTick,schem);lastTick=tick
        addNote(chord,schem)
    addWalkWay(schem)
    addBottonPlate(schem)
    schem.save("D:\Minecraft\PrismLauncher\instence\Me\.minecraft\schematics\Task", "output", mcschematic.Version.JE_1_20_1)

import pynbs
if __name__ == '__main__': # don't mind me just for testing
    build(pynbs.read("D:/MUSIC THING/Songs/Yeaa Woo/God's Hand Relying on Dreams zip.nbs"))