import os
os.system("pip install tk")
from tkinter import *
import getpass
import pathlib
import threading
import time
import shutil
#os.system("clear")


class AA:
     
    # constructor
    def __init__(self):
        Menu = Tk()
        Menu.geometry("300x500")
        Menu.title("Autostart Applications")
        root = Menu

        EnabledScroll = Scrollbar(Menu,orient="vertical")
        Enabled = Listbox(Menu,yscrollcommand=EnabledScroll.set,height=10,bg="#000000",selectbackground="#212121")
        EnabledText = Label(text="Enabled",highlightthickness=1,highlightbackground="#212121",bg="#000000",foreground="white")
        DisabledScroll = Scrollbar(Menu,highlightthickness=1,highlightbackground="#212121",bg="#000000",highlightcolor="#000000")
        Disabled = Listbox(Menu,yscrollcommand=DisabledScroll.set,height=10,bg="#000000",selectbackground="#212121")
        DisabledText = Label(text="Disabled",highlightthickness=1,highlightbackground="#212121",bg="#000000",foreground="white")

        Enabled.place(anchor=NW,x=5,y=24)
        EnabledText.place(anchor=NW,x=38,y=3)
        EnabledScroll.place(height=162,width=15,x=127,y=25)
        Disabled.place(anchor=NW,x=5,y=211)
        DisabledText.place(anchor=NW,x=38,y=190)
        DisabledScroll.place(height=162,width=15,x=127,y=210)

        User = getpass.getuser()
        print(User)
        #os.chdir("D:")
        Drive = pathlib.Path.home().drive
        os.chdir(Drive)
        #os.chdir(f"Users\{User}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
        if os.getcwd is not Drive:
            os.chdir("..\..\..\..\..\..\..\..\..")
        print(f"{User}, {os.getcwd()}")
        os.chdir("Users")
        os.chdir(f"{User}")
        os.chdir("AppData")
        os.chdir("Roaming")
        os.chdir("Microsoft")
        os.chdir("Windows")
        os.chdir("Start Menu")
        os.chdir("Programs")
        os.chdir("Startup")
        files = os.listdir()
        files.remove('desktop.ini')
        files.remove('Autostart.py.lnk')
        def ReloadFiles():
            files = os.listdir()
            files.remove('desktop.ini')
            files.remove('Autostart.py.lnk')
            Enabled.delete(0,END)
            Disabled.delete(0,END)
            FileCount = len(files)
            for FileL in range(FileCount):
                ere = "".join([f"{FileL}: ",str(files[FileL])])
                Enabled.insert(END, ere)
                Enabled.itemconfig(FileL, {'foreground':'white'})
            files = os.listdir("..\Dodo Co\Disabled")
            FileCount = len(files)
            for FileL in range(FileCount):
                ere = "".join([f"{FileL}: ",str(files[FileL])])
                Disabled.insert(END, ere)
                Disabled.itemconfig(FileL, {'foreground':'white'})
        
        def ReloadError():
            ReloadLog.config(text="Already Reloading")
            time.sleep(0.75)
            ReloadLog.config(text="")
        
        def ReloadThread():
            if ReloadButton['text'] == "Reload":
                x = threading.Thread(target=Reload)
            else:
                x = threading.Thread(target=ReloadError)
            x.start()
        
        def Reload():
            ReloadButton.config(text="Reloading...")
            threading.Thread(target=ReloadFiles).start()
            time.sleep(0.5)
            ReloadButton.config(text="Reloaded")
            time.sleep(2)
            ReloadButton.config(text="Reload")
        
        def SS1():
            SelectedE = Enabled.curselection()
            SelectedE = str(SelectedE).replace("(","").replace(")","").replace(",","")
            Selected = "".join(SelectedE)
            print(f"1: {SelectedE}-2: {Selected}")
            FileE = os.listdir()
            FileE.remove('Autostart.py.lnk')
            FileE.remove('desktop.ini')
            FileTarget = FileE[int(SelectedE)]
            shutil.move(f"..\Startup\{FileTarget}","..\Dodo Co\Disabled")
            ReloadFiles()
        def SS2():
            SelectedD = Disabled.curselection()
            SelectedD = str(SelectedD).replace("(","").replace(")","").replace(",","")
            Selected = "".join(SelectedD)
            print(f"1: {SelectedD}-2: {Selected}")
            FileE = os.listdir("..\Dodo Co\Disabled")
            FileTarget = FileE[int(SelectedD)]
            shutil.move(f"Disabled\{FileTarget}","..\Startup")
            ReloadFiles()
        def RestartPC():
            os.system("shutdown /r /f /t 0")
            

        ReloadFiles()
        ReloadButton = Button(text="Reload",anchor=NE,command=ReloadThread)
        ReloadButton.place(x=190,y=5)
        ReloadLog = Label(text="",anchor=NE)
        ReloadLog.place(x=165,y=35)
        SSB = Button(text="Disable\nThe selected files",command=SS1)
        SSB.place(x=165,y=60)
        SSB = Button(text="Enable\nThe selected files",command=SS2)
        SSB.place(x=165,y=120)
        Restart = Button(text="!!!RESTART!!!\nThis will restart your pc\nThere is no confirmation\nSo be careful",command=RestartPC)
        Restart.place(x=150,y=160)
        Menu.mainloop()

AA()
