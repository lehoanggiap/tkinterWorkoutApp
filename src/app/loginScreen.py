import sys
from tkinter import *
from PIL import ImageTk, Image
from form.loginForm import loginForm
from backGround.bgrImage import BgrImage
import os
from screen import Screen

class loginScreen(Screen):
    def __init__(self, bgrPath):
        super().__init__()
        self.bgrPath = bgrPath
        self.backgroundImage = BgrImage(self.screen)
        self.loginForm = loginForm(self.screen)
        

    def createViews(self):
        self.backgroundImage.create(self.bgrPath)
        self.loginForm.create()


if __name__ == "__main__":
    path = "../assets/img/fitify_cover.jpg"
    screen = loginScreen(path)
    screen.onCreate()
    screen.run()



