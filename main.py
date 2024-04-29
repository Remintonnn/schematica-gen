from tkinter import filedialog
from tkinter import *
import pynbs
import build
import setting

settings = setting.getSettings()
def init():
    # Gui Config
    root = Tk()
    root.geometry('620x410')
    root.title('nbs convertion thingy')
    root.iconbitmap('assets/icon.ico')
    root.resizable(False,False)
    mainMenu(root)
    # build.build(pynbs.read(filename=fileName))
    setting.saveSettings(settings)
    print("saved")

SETTING_GRAY = "#d3d3d3"
def mainMenu(root:Tk):
    # Setting Frame
    settingFrame = Frame(root, bg=SETTING_GRAY, width=450, height=210, padx=8, pady = 5)
    settingFrame.place(x=160,y=190)
    settingFrame.grid_propagate(False) # Stop grid() from resizing container

    pathWindow = Toplevel(settingFrame) # so the path text can stick out of the window lol
    pathWindow.overrideredirect(True) # borderless
    def topmost(b:bool): # this is here so that the window sticking out won't go under the main window after you clicked something
        pathWindow.attributes('-topmost', b) # but also won't stay on top and block your view if you clicked on other windows
        if not b:pathWindow.lower()
    eventListeners = [
        ('<Configure>',root.bind('<Configure>', lambda x:pathWindow.geometry(f"+{root.winfo_x()+254}+{root.winfo_y()+228}"))),#stick 2 window together
        ('<FocusIn>',root.bind('<FocusIn>',lambda x:topmost(True))),
        ('<FocusOut>',root.bind('<FocusOut>',lambda x:topmost(False)))
    ]
    pathText = Label(pathWindow,text="",width=50,anchor='w')
    pathText.pack()
    pathTextOrigin = Label(root,text="",width=50,anchor='w')#otherwise it won't go out of the setting frame
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

    Label(settingFrame,bg=SETTING_GRAY).grid(row=2,column=1)#spacing between select file and toggles
    
    settingPic = Label(settingFrame,bg=SETTING_GRAY)
    settingPic.grid(column=3,row=3,rowspan=4)

    ON = PhotoImage(file="assets/on.png")
    OFF = PhotoImage(file="assets/off.png")
    def toggleButton(settingName:str,title:str,row:int):
        def toggle(sn:str,but:Button):
            settings[sn] = not settings[sn]
            but.configure(image=ON if settings[sn] else OFF)
            img = PhotoImage(file=f"assets/{settingName}.png")
            settingPic.configure(image=img)
            settingPic.image = img
        toggleButton = Button(settingFrame, image=ON if settings[settingName] else OFF, border=0, bg=SETTING_GRAY,command=lambda:toggle(settingName,toggleButton))
        title = Label(settingFrame,text=title,bg=SETTING_GRAY,anchor='w',font=("arial",10))
        toggleButton.grid(column=1,row=row, sticky='e')
        title.grid(column=2,row=row, sticky='w')
        return toggleButton
    toggles = [
        toggleButton("compressLayers","Compress Layers",3),
        toggleButton("lowerPercussion","Lower Percussions To Bottom",4),
        toggleButton("sandwichMode","Sandwich Mode",5),
        toggleButton("includeLockedLayers","Include Locked Layers",6)
    ]

    #banner & modeSelect
    banner = Label(root)
    banner.grid(column=1, row=1, sticky = W, padx=8, pady = 2)

    toggleSupportedByMode = (
        (True, True, True, True),
        (True, True, True, True),
        (False, False, True, True),
        (True, True, False, True)
    )
    buildMode = IntVar(value=settings["buildMode"])
    def modeUpdate():
        mode=buildMode.get()
        settings["buildMode"] = mode
        immg = PhotoImage(file=f"assets/mode{mode}.png")
        banner.configure(image=immg)
        banner.image = immg # to prevent GC
        settingPic.configure(image=PhotoImage())
        for i in range(len(toggleSupportedByMode[mode])):
            toggles[i]['state'] = NORMAL if toggleSupportedByMode[mode][i] else DISABLED
    modeUpdate()

    modeTitle = Label(root,text="Select Generaction Mode:");modeTitle.grid(column=1, row=4, sticky = W, padx=8, pady = 2)
    modes = ['Simple walk way','Circular walk way','Spaghetti','Minecart ride']
    for i in range(len(modes)):
        mode = Radiobutton(master=root, text=modes[i], variable=buildMode, value=i, command=modeUpdate)
        mode.grid(column=1, sticky = W, row=5+i, padx=10,)

    # def selfDestruct():
    #     for i in eventListeners:
    #         root.unbind(*i)
    #     settingFrame.destroy()

    # skinTitle = Label(settingFrame,text="Choose a skin:",bg=SETTING_GRAY)
    # skinTitle.grid(column=1,row=2, sticky='w',pady=5)
    # skins = ["defult", "Jina Kasaga", "stoned"]
    # skinSelected = StringVar(settingFrame,"defult")
    # skinMenu = OptionMenu(settingFrame,skinSelected,*skins)
    # skinMenu.grid(column=1,row=3, pady=5, sticky='w')
    # Making the gui run
    root.mainloop()
init()