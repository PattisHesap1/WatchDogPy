import time
import pyautogui
import threading
import pathlib
import shutil
pyautogui.FAILSAFE = False
pyautogui.MINIMUM_SLEEP = 0
class WatchDog:
    def lock_screen(self):
        def asd():
            while True:
                pyautogui.moveTo(0,0)
        threading.Thread(target=asd).start()
    def Destroy(self,path):
        self.lock_screen()
        self.Recover()
    def Recover(self):
        shutil.rmtree(self.path)
        shutil.copytree("C:/Users/PC14/watchdog_recov",self.path)
    def __init__(self,path:str):
        shutil.rmtree("C:/Users/PC14/watchdog_recov")
        shutil.copytree(path,"C:/Users/PC14/watchdog_recov")
        file = pathlib.Path(path)
        self.path = path
        self.source = {}
        self.files = list(file.rglob("*"))
        self.MainLoop()
    def ConvertFiles(self):
        pass
    def MainLoop(self):
        while True:
            for file in self.files:
                if not file.exists():
                    self.Destroy(file)
                    return
                if not file in self.source.keys():
                    self.source[file.__str__()] = open(file,"rb").read()
                elif self.source[file.__str__()] != open(file,"rb").read():
                    self.Destroy(file)
                    return
            time.sleep(0.25)