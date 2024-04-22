from tkinter import filedialog
from tkinter import *
import pynbs
import build

def init():
    # Gui Config
    root = Tk()
    root.geometry('620x410')
    root.title('nbs convertion thingy')
    root.iconbitmap('assets/icon.ico')
    root.resizable(False,False)
    mainMenu(root)
    # build.build(pynbs.read(filename=fileName))
    print(3)

SETTING_GRAY = "#d3d3d3"
DestoryCurrentFrame = None
def simpleSetting(root:Tk):
    eventListeners = []
    settingFrame = Frame(root, bg=SETTING_GRAY, width=450, height=210, padx=8, pady = 5)
    settingFrame.place(x=160,y=190)
    settingFrame.grid_propagate(False) # Stop grid() from resizing container

    pathWindow = Toplevel(settingFrame) # so the path text can stick out of the window lol
    pathWindow.overrideredirect(True) # borderless
    eventListeners.append(('<Configure>',root.bind('<Configure>', lambda x:pathWindow.geometry(f"+{root.winfo_x()+254}+{root.winfo_y()+228}"))))#stick 2 window together
    def topmost(b:bool): # this is here so that the window sticking out won't go under the main window after you clicked something
        pathWindow.attributes('-topmost', b) # but also won't stay on top and block your view if you clicked on other windows
        if not b:pathWindow.lower()
    eventListeners.append(('<FocusIn>',root.bind('<FocusIn>',lambda x:topmost(True))))
    eventListeners.append(('<FocusOut>',root.bind('<FocusOut>',lambda x:topmost(False))))
    pathText = Label(pathWindow,text="",width=50,anchor='w')
    pathText.pack()
    pathTextOrigin = Label(settingFrame,text="",width=50,anchor='w')
    pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
    pathTextOrigin.place(x=246,y=197)
    def getPath():
        root = Tk()
        root.withdraw()
        path = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other chioce)","*.nbs")])
        root.destroy()
        if path=="": return
        pathText.configure(text=path,width=len(path))#anchor='w' if len(path)<50 else 'e')
        pathTextOrigin.configure(text=path,width=len(path))
        pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
        

    pathButton = Button(settingFrame,text="Select File",command=getPath, border=4,bg="#b9c3c7")
    pathButton.grid(column=1,row=1,sticky='w',)

    Label(settingFrame,bg=SETTING_GRAY,).grid(row=2,column=1)

    def toggle(bool:BooleanVar,button:Button):
        if bool.get():bool.set(False);button.configure(image=OFF)
        else: bool.set(True);button.configure(image=ON)
    ON = PhotoImage(file="assets/on.png")
    OFF = PhotoImage(file="assets/off.png")
    compressLayers = BooleanVar(value=True)
    compressToggle = Button(settingFrame, image = ON, border=0, bg = SETTING_GRAY,command=lambda:toggle(compressLayers,compressToggle))
    compressTitle = Label(settingFrame,text="Compress Layers",bg=SETTING_GRAY,anchor='w')
    compressToggle.grid(column=1,row=3, sticky='e')
    compressTitle.grid(column=2,row=3, sticky='w')

    lowerPercussion = BooleanVar(value=False)
    lowerPercussionToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(lowerPercussion,lowerPercussionToggle))
    lowerPercussionTitle = Label(settingFrame,text="Lower Percussions To Bottom",bg=SETTING_GRAY,anchor='w')
    lowerPercussionToggle.grid(column=1,row=4,sticky='e')
    lowerPercussionTitle.grid(column=2,row=4, sticky='w')

    includeLockedLayers = BooleanVar(value=False)
    includeLockToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(includeLockedLayers,includeLockToggle))
    includeLockTitle = Label(settingFrame,text="Include Locked Layers",bg=SETTING_GRAY,anchor='w')
    includeLockToggle.grid(column=1,row=5,sticky='e')
    includeLockTitle.grid(column=2,row=5, sticky='w')

    doubleLayers = BooleanVar(value=False)
    doubleToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(doubleLayers,doubleToggle))
    doubleTitle = Label(settingFrame,text="Sandwitch Mode",bg=SETTING_GRAY,anchor='w')
    doubleToggle.grid(column=1,row=6,sticky='e')
    doubleTitle.grid(column=2,row=6, sticky='w')

    def selfDestruct():
        for i in eventListeners:
            root.unbind(*i)
        settingFrame.destroy()
    return selfDestruct
    # skinTitle = Label(settingFrame,text="Choose a skin:",bg=SETTING_GRAY)
    # skinTitle.grid(column=1,row=2, sticky='w',pady=5)
    # skins = ["defult", "Jina Kasaga", "stoned"]
    # skinSelected = StringVar(settingFrame,"defult")
    # skinMenu = OptionMenu(settingFrame,skinSelected,*skins)
    # skinMenu.grid(column=1,row=3, pady=5, sticky='w')

def circularSetting(root:Tk):
    eventListeners = []
    settingFrame = Frame(root, bg=SETTING_GRAY, width=450, height=210, padx=8, pady = 5)
    settingFrame.place(x=160,y=190)
    settingFrame.grid_propagate(False) # Stop grid() from resizing container

    pathWindow = Toplevel(settingFrame) # so the path text can stick out of the window lol
    pathWindow.overrideredirect(True) # borderless
    eventListeners.append(('<Configure>',root.bind('<Configure>', lambda x:pathWindow.geometry(f"+{root.winfo_x()+254}+{root.winfo_y()+228}"))))#stick 2 window together
    def topmost(b:bool): # this is here so that the window sticking out won't go under the main window after you clicked something
        pathWindow.attributes('-topmost', b) # but also won't stay on top and block your view if you clicked on other windows
        if not b:pathWindow.lower()
    eventListeners.append(('<FocusIn>',root.bind('<FocusIn>',lambda x:topmost(True))))
    eventListeners.append(('<FocusOut>',root.bind('<FocusOut>',lambda x:topmost(False))))
    pathText = Label(pathWindow,text="",width=50,anchor='w')
    pathText.pack()
    pathTextOrigin = Label(settingFrame,text="",width=50,anchor='w')
    pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
    pathTextOrigin.place(x=246,y=197)
    def getPath():
        root = Tk()
        root.withdraw()
        path = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other chioce)","*.nbs")])
        root.destroy()
        if path=="": return
        pathText.configure(text=path,width=len(path))#anchor='w' if len(path)<50 else 'e')
        pathTextOrigin.configure(text=path,width=len(path))
        pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
        

    pathButton = Button(settingFrame,text="Select File",command=getPath, border=4,bg="#b9c3c7")
    pathButton.grid(column=1,row=1,sticky='w',)

    Label(settingFrame,bg=SETTING_GRAY,).grid(row=2,column=1)

    def toggle(bool:BooleanVar,button:Button):
        if bool.get():bool.set(False);button.configure(image=OFF)
        else: bool.set(True);button.configure(image=ON)
    ON = PhotoImage(file="assets/on.png")
    OFF = PhotoImage(file="assets/off.png")
    compressLayers = BooleanVar(value=True)
    compressToggle = Button(settingFrame, image = ON, border=0, bg = SETTING_GRAY,command=lambda:toggle(compressLayers,compressToggle))
    compressTitle = Label(settingFrame,text="Compress Layers",bg=SETTING_GRAY,anchor='w')
    compressToggle.grid(column=1,row=3, sticky='e')
    compressTitle.grid(column=2,row=3, sticky='w')

    lowerPercussion = BooleanVar(value=False)
    lowerPercussionToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(lowerPercussion,lowerPercussionToggle))
    lowerPercussionTitle = Label(settingFrame,text="Lower Percussions To Bottom",bg=SETTING_GRAY,anchor='w')
    lowerPercussionToggle.grid(column=1,row=4,sticky='e')
    lowerPercussionTitle.grid(column=2,row=4, sticky='w')

    includeLockedLayers = BooleanVar(value=False)
    includeLockToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(includeLockedLayers,includeLockToggle))
    includeLockTitle = Label(settingFrame,text="Include Locked Layers",bg=SETTING_GRAY,anchor='w')
    includeLockToggle.grid(column=1,row=5,sticky='e')
    includeLockTitle.grid(column=2,row=5, sticky='w')

    doubleLayers = BooleanVar(value=False)
    doubleToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(doubleLayers,doubleToggle))
    doubleTitle = Label(settingFrame,text="Sandwitch Mode",bg=SETTING_GRAY,anchor='w')
    doubleToggle.grid(column=1,row=6,sticky='e')
    doubleTitle.grid(column=2,row=6, sticky='w')

    def selfDestruct():
        for i in eventListeners:
            root.unbind(*i)
        settingFrame.destroy()
    des = Button(settingFrame,text="no more frame",command=selfDestruct)
    des.grid(column=1,row=7)

    # skinTitle = Label(settingFrame,text="Choose a skin:",bg=SETTING_GRAY)
    # skinTitle.grid(column=1,row=2, sticky='w',pady=5)
    # skins = ["defult", "Jina Kasaga", "stoned"]
    # skinSelected = StringVar(settingFrame,"defult")
    # skinMenu = OptionMenu(settingFrame,skinSelected,*skins)
    # skinMenu.grid(column=1,row=3, pady=5, sticky='w')

def spaghettiSetting(root:Tk):
    eventListeners = []
    settingFrame = Frame(root, bg=SETTING_GRAY, width=450, height=210, padx=8, pady = 5)
    settingFrame.place(x=160,y=190)
    settingFrame.grid_propagate(False) # Stop grid() from resizing container

    pathWindow = Toplevel(settingFrame) # so the path text can stick out of the window lol
    pathWindow.overrideredirect(True) # borderless
    eventListeners.append(('<Configure>',root.bind('<Configure>', lambda x:pathWindow.geometry(f"+{root.winfo_x()+254}+{root.winfo_y()+228}"))))#stick 2 window together
    def topmost(b:bool): # this is here so that the window sticking out won't go under the main window after you clicked something
        pathWindow.attributes('-topmost', b) # but also won't stay on top and block your view if you clicked on other windows
        if not b:pathWindow.lower()
    eventListeners.append(('<FocusIn>',root.bind('<FocusIn>',lambda x:topmost(True))))
    eventListeners.append(('<FocusOut>',root.bind('<FocusOut>',lambda x:topmost(False))))
    pathText = Label(pathWindow,text="",width=50,anchor='w')
    pathText.pack()
    pathTextOrigin = Label(settingFrame,text="",width=50,anchor='w')
    pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
    pathTextOrigin.place(x=246,y=197)
    def getPath():
        root = Tk()
        root.withdraw()
        path = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other chioce)","*.nbs")])
        root.destroy()
        if path=="": return
        pathText.configure(text=path,width=len(path))#anchor='w' if len(path)<50 else 'e')
        pathTextOrigin.configure(text=path,width=len(path))
        pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
        

    pathButton = Button(settingFrame,text="Select File",command=getPath, border=4,bg="#b9c3c7")
    pathButton.grid(column=1,row=1,sticky='w',)

    Label(settingFrame,bg=SETTING_GRAY,).grid(row=2,column=1)

    def toggle(bool:BooleanVar,button:Button):
        if bool.get():bool.set(False);button.configure(image=OFF)
        else: bool.set(True);button.configure(image=ON)
    ON = PhotoImage(file="assets/on.png")
    OFF = PhotoImage(file="assets/off.png")
    compressLayers = BooleanVar(value=True)
    compressToggle = Button(settingFrame, image = ON, border=0, bg = SETTING_GRAY,command=lambda:toggle(compressLayers,compressToggle))
    compressTitle = Label(settingFrame,text="Compress Layers",bg=SETTING_GRAY,anchor='w')
    compressToggle.grid(column=1,row=3, sticky='e')
    compressTitle.grid(column=2,row=3, sticky='w')

    lowerPercussion = BooleanVar(value=False)
    lowerPercussionToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(lowerPercussion,lowerPercussionToggle))
    lowerPercussionTitle = Label(settingFrame,text="Lower Percussions To Bottom",bg=SETTING_GRAY,anchor='w')
    lowerPercussionToggle.grid(column=1,row=4,sticky='e')
    lowerPercussionTitle.grid(column=2,row=4, sticky='w')

    includeLockedLayers = BooleanVar(value=False)
    includeLockToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(includeLockedLayers,includeLockToggle))
    includeLockTitle = Label(settingFrame,text="Include Locked Layers",bg=SETTING_GRAY,anchor='w')
    includeLockToggle.grid(column=1,row=5,sticky='e')
    includeLockTitle.grid(column=2,row=5, sticky='w')

    doubleLayers = BooleanVar(value=False)
    doubleToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(doubleLayers,doubleToggle))
    doubleTitle = Label(settingFrame,text="Sandwitch Mode",bg=SETTING_GRAY,anchor='w')
    doubleToggle.grid(column=1,row=6,sticky='e')
    doubleTitle.grid(column=2,row=6, sticky='w')

    def selfDestruct():
        for i in eventListeners:
            root.unbind(*i)
        settingFrame.destroy()
    des = Button(settingFrame,text="no more frame",command=selfDestruct)
    des.grid(column=1,row=7)

    # skinTitle = Label(settingFrame,text="Choose a skin:",bg=SETTING_GRAY)
    # skinTitle.grid(column=1,row=2, sticky='w',pady=5)
    # skins = ["defult", "Jina Kasaga", "stoned"]
    # skinSelected = StringVar(settingFrame,"defult")
    # skinMenu = OptionMenu(settingFrame,skinSelected,*skins)
    # skinMenu.grid(column=1,row=3, pady=5, sticky='w')

def cartSetting(root:Tk):
    eventListeners = []
    settingFrame = Frame(root, bg=SETTING_GRAY, width=450, height=210, padx=8, pady = 5)
    settingFrame.place(x=160,y=190)
    settingFrame.grid_propagate(False) # Stop grid() from resizing container

    pathWindow = Toplevel(settingFrame) # so the path text can stick out of the window lol
    pathWindow.overrideredirect(True) # borderless
    eventListeners.append(('<Configure>',root.bind('<Configure>', lambda x:pathWindow.geometry(f"+{root.winfo_x()+254}+{root.winfo_y()+228}"))))#stick 2 window together
    def topmost(b:bool): # this is here so that the window sticking out won't go under the main window after you clicked something
        pathWindow.attributes('-topmost', b) # but also won't stay on top and block your view if you clicked on other windows
        if not b:pathWindow.lower()
    eventListeners.append(('<FocusIn>',root.bind('<FocusIn>',lambda x:topmost(True))))
    eventListeners.append(('<FocusOut>',root.bind('<FocusOut>',lambda x:topmost(False))))
    pathText = Label(pathWindow,text="",width=50,anchor='w')
    pathText.pack()
    pathTextOrigin = Label(settingFrame,text="",width=50,anchor='w')
    pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
    pathTextOrigin.place(x=246,y=197)
    def getPath():
        root = Tk()
        root.withdraw()
        path = filedialog.askopenfilename(filetypes=[("The Chosen file format of NoteBlockStudio(you have no other chioce)","*.nbs")])
        root.destroy()
        if path=="": return
        pathText.configure(text=path,width=len(path))#anchor='w' if len(path)<50 else 'e')
        pathTextOrigin.configure(text=path,width=len(path))
        pathWindow.geometry(f"{pathText.winfo_reqwidth()}x{pathText.winfo_reqheight()}")
        

    pathButton = Button(settingFrame,text="Select File",command=getPath, border=4,bg="#b9c3c7")
    pathButton.grid(column=1,row=1,sticky='w',)

    Label(settingFrame,bg=SETTING_GRAY,).grid(row=2,column=1)

    def toggle(bool:BooleanVar,button:Button):
        if bool.get():bool.set(False);button.configure(image=OFF)
        else: bool.set(True);button.configure(image=ON)
    ON = PhotoImage(file="assets/on.png")
    OFF = PhotoImage(file="assets/off.png")
    compressLayers = BooleanVar(value=True)
    compressToggle = Button(settingFrame, image = ON, border=0, bg = SETTING_GRAY,command=lambda:toggle(compressLayers,compressToggle))
    compressTitle = Label(settingFrame,text="Compress Layers",bg=SETTING_GRAY,anchor='w')
    compressToggle.grid(column=1,row=3, sticky='e')
    compressTitle.grid(column=2,row=3, sticky='w')

    lowerPercussion = BooleanVar(value=False)
    lowerPercussionToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(lowerPercussion,lowerPercussionToggle))
    lowerPercussionTitle = Label(settingFrame,text="Lower Percussions To Bottom",bg=SETTING_GRAY,anchor='w')
    lowerPercussionToggle.grid(column=1,row=4,sticky='e')
    lowerPercussionTitle.grid(column=2,row=4, sticky='w')

    includeLockedLayers = BooleanVar(value=False)
    includeLockToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(includeLockedLayers,includeLockToggle))
    includeLockTitle = Label(settingFrame,text="Include Locked Layers",bg=SETTING_GRAY,anchor='w')
    includeLockToggle.grid(column=1,row=5,sticky='e')
    includeLockTitle.grid(column=2,row=5, sticky='w')

    doubleLayers = BooleanVar(value=False)
    doubleToggle = Button(settingFrame, image = OFF, border=0, bg = SETTING_GRAY,command=lambda:toggle(doubleLayers,doubleToggle))
    doubleTitle = Label(settingFrame,text="Sandwitch Mode",bg=SETTING_GRAY,anchor='w')
    doubleToggle.grid(column=1,row=6,sticky='e')
    doubleTitle.grid(column=2,row=6, sticky='w')

    def selfDestruct():
        for i in eventListeners:
            root.unbind(*i)
        settingFrame.destroy()
    des = Button(settingFrame,text="no more frame",command=selfDestruct)
    des.grid(column=1,row=7)

    # skinTitle = Label(settingFrame,text="Choose a skin:",bg=SETTING_GRAY)
    # skinTitle.grid(column=1,row=2, sticky='w',pady=5)
    # skins = ["defult", "Jina Kasaga", "stoned"]
    # skinSelected = StringVar(settingFrame,"defult")
    # skinMenu = OptionMenu(settingFrame,skinSelected,*skins)
    # skinMenu.grid(column=1,row=3, pady=5, sticky='w')

def mainMenu(root:Tk):
    # The actual gui
    banner = Label(root)
    banner.grid(column=1, row=1, sticky = W, padx=8, pady = 2)

    buildMode = IntVar()
    modeSettingFrames = [simpleSetting,circularSetting,spaghettiSetting,cartSetting]
    def modeUpdate(mode=buildMode.get()):
        global DestoryCurrentFrame
        immg = PhotoImage(file=f"assets/mode{mode}.png")
        banner.configure(image=immg)
        banner.image = immg # to prevent GC
        if DestoryCurrentFrame:DestoryCurrentFrame()
        DestoryCurrentFrame=modeSettingFrames[mode](root)

    modeTitle = Label(root,text="Select Generaction Mode:");modeTitle.grid(column=1, row=4, sticky = W, padx=8, pady = 2)
    modes = ['Simple walk way','Circular walk way','Spaghetti','Minecart ride']
    for i in range(len(modes)):
        mode = Radiobutton(master=root, text=modes[i], variable=buildMode, value=i, command=modeUpdate)
        mode.grid(column=1, sticky = W, row=5+i, padx=10,)


    # Setting Frame
    modeUpdate(0)
    # Making the gui run
    root.mainloop()
init()