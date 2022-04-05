from tkinter import *
import os
import sys
class Screen:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    def __init__(self):
        self.screen = Tk()

    def onCreate(self):
        self.configScreen()
        self.createViews()
        
    def configScreen(self):
        window_width = self.screen.winfo_screenwidth()
        window_height = self.screen.winfo_screenheight()
        x = int(window_width/2 - self.SCREEN_WIDTH/2)
        y = int(window_height/2 - self.SCREEN_HEIGHT/2)

        self.screen.iconbitmap(os.path.join(sys.path[0], "../assets/img/fitify.ico"))
        self.screen.title('Fitify') 
        self.screen.geometry(f'{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}+{x}+{y}')
        self.screen.resizable(width= False, height= False)

    def createViews(self):
        pass

    def run(self):
        self.screen.mainloop()

