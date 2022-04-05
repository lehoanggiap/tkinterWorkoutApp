from tkinter import *
from tkinter import font
from utils.constant import Constant
from backGround.bgrImage import BgrImage
from screen import Screen
from homeScreen import homeScreen
class fillInforScreen(Screen):
    def __init__(self):
        super().__init__()
        
        self.frameIntro = Frame(self.screen, bg = Constant.main_color)
        self.Intro_block = Frame(self.frameIntro,  bg = Constant.main_color)
        self.Intro_Title = Label(self.Intro_block, text = 'Welcome to App', 
                                 font = f'{Constant.main_font} 18 bold', 
                                 fg = Constant.white_color, bg = Constant.main_color)
        self.Intro_Content = Label(self.Intro_block, text = Constant.introText,
                                 font = f'{Constant.main_font} 12', fg = Constant.white_color,
                                 justify = LEFT, wraplength=350, bg = Constant.main_color)     
        
        self.frameFillInfo = Frame(self.screen, bg = Constant.white_color)
        self.FillInfo_block = Frame(self.frameFillInfo, bg = Constant.white_color) 
        self.FillInfo_Title = Label(self.FillInfo_block, text = 'We will help you more with these information', 
                                 font = f'{Constant.main_font} 18 bold', 
                                 fg = Constant.main_color, bg = Constant.white_color,
                                wraplength=400, justify = LEFT)        
        self.lblHeight = Label(self.FillInfo_block, text = 'Height', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)  
        self.frameHeight = Frame(self.FillInfo_block, bg = Constant.black_color)                         
        self.txtHeight = Entry(self.frameHeight, width=30, font = f'{Constant.main_font} 14') 

        self.lblWeight = Label(self.FillInfo_block, text = 'Weight', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)
        self.frameWeight = Frame(self.FillInfo_block, bg = Constant.black_color)                         
        self.txtWeight = Entry(self.frameWeight, width=30, font = f'{Constant.main_font} 14')        

        self.lblExp = Label(self.FillInfo_block, text = 'Experience training level', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)      

        self.frameExp = Frame(self.FillInfo_block, bg = Constant.white_color)  

        exp = StringVar()    
                        
        self.rbtnExp1 = Radiobutton(self.frameExp, bg = Constant.white_color, variable = exp, value='Primary', text = 'Primary')
        self.rbtnExp2 = Radiobutton(self.frameExp, bg = Constant.white_color, variable = exp, value='Intermediate', text = 'Intermediate')
        self.rbtnExp3 = Radiobutton(self.frameExp, bg = Constant.white_color, variable = exp, value='Advanced', text = 'Advanced')

        self.btnContinue = Button(self.FillInfo_block, font = f'{Constant.main_font} 12 bold',  bg = Constant.white_color, text = 'Continue', fg = Constant.main_color)
        self.btnContinue['command'] = self.goToHomeScreen
        

    def createViews(self):
        self.createFrames()

    def goToHomeScreen(self):
        self.screen.destroy()
        self.homeScreen = homeScreen()
        self.homeScreen.onCreate()
        self.homeScreen.run()    

    def createFrames(self):
        self.frameIntro.place(relwidth = .5, relheight = 1, anchor = NW)
        self.Intro_block.place(relx = .1, rely = .2)
        self.Intro_Title.grid(row = 0, column = 0, sticky = W, pady =20)
        self.Intro_Content.grid(row = 1, column = 0, columnspan= 2, sticky = W)


        self.frameFillInfo.place(relx = .5, rely = 0, relwidth= .5, relheight= 1)
        self.FillInfo_block.place(relx = .1, rely = .1)
        self.FillInfo_Title.grid(row = 0, column = 0, sticky = W, pady =20)
        self.lblHeight.grid(row = 1, column = 0, sticky = W)
        self.frameHeight.grid(row = 2, column = 0, pady = 10, sticky = W)
        self.txtHeight.pack(padx = 1, pady = 1)

        self.lblWeight.grid(row = 3, column = 0, sticky = W)
        self.frameWeight.grid(row = 4, column = 0, pady = 10, sticky = W)
        self.txtWeight.pack(padx = 1, pady = 1)

        self.lblExp.grid(row = 5, column = 0, sticky = W)
        self.frameExp.grid(row = 6, column = 0, columnspan = 2, sticky = W)
        self.rbtnExp1.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)
        self.rbtnExp2.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)
        self.rbtnExp3.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)

        self.btnContinue.grid(row = 7, column = 0, columnspan = 2, pady = 40, ipadx = 10, ipady = 5)

if __name__ == "__main__":
    screen = fillInforScreen()
    screen.onCreate()
    screen.run() 
        