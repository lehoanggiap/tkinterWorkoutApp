from tkinter import * 
import os
import sys
from PIL import ImageTk, Image
class BgrImage:
    def __init__(self, screen):
        self.backgroundImage = Label(screen)


    def create(self, path):
        path = os.path.join(sys.path[0], path)
        self.img = ImageTk.PhotoImage(Image.open(path)) 
        self.backgroundImage['image'] = self.img 
        self.backgroundImage.place(x = 0, y = 0, relwidth = 1, relheight = 1)     