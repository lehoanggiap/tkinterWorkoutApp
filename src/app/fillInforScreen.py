from textwrap import fill
from tkinter import *
from tkinter import font
from utils.constant import Constant
from backGround.bgrImage import BgrImage
from screen import Screen
from homeScreen import homeScreen
class fillInforScreen(Screen):
    count = 1
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

        self.lblAge = Label(self.FillInfo_block, text = 'Age', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)
        self.frameAge = Frame(self.FillInfo_block, bg = Constant.black_color)                         
        self.txtAge = Entry(self.frameAge, width=30, font = f'{Constant.main_font} 14')                       
        

        self.lblExp = Label(self.FillInfo_block, text = 'Experience training level', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)      

        self.frameExp = Frame(self.FillInfo_block, bg = Constant.white_color)  
        
        exp = StringVar()                      
        self.rbtnExp1 = Radiobutton(self.frameExp, bg = Constant.white_color, variable = exp, value='Beginner', text = 'Beginner')
        self.rbtnExp2 = Radiobutton(self.frameExp, bg = Constant.white_color, variable = exp, value='Intermediate', text = 'Intermediate')
        self.rbtnExp3 = Radiobutton(self.frameExp, bg = Constant.white_color, variable = exp, value='Advanced', text = 'Advanced')

        self.btnContinue = Button(self.FillInfo_block, font = f'{Constant.main_font} 12 bold',  bg = Constant.white_color, text = 'Continue', fg = Constant.main_color)
        self.btnContinue['command'] = self.btnContinue_onClick


        tool = StringVar()
        self.lblTool = Label(self.FillInfo_block, text = 'Exercise Equipment', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)  
        self.frameTool = Frame(self.FillInfo_block, bg = Constant.white_color) 
        self.rbtnTool1 = Radiobutton(self.frameTool, bg = Constant.white_color, variable = tool, value='Have dumbbells', text = 'Have dumbbells')
        self.rbtnTool2 = Radiobutton(self.frameTool, bg = Constant.white_color, variable = tool, value= "Don't have dumbbells", text = "Don't have dumbbells")
        
        muscle1 = StringVar()
        muscle2 = StringVar()
        muscle3 = StringVar()
        self.lblMuscle = Label(self.FillInfo_block, text = 'Muscle Group You Want To Train', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color)
        self.frameMuscle = Frame(self.FillInfo_block, bg = Constant.white_color)
        self.cbtnMuscle1 = Checkbutton(self.frameMuscle, bg = Constant.white_color, variable = muscle1, onvalue='Upper Body', offvalue='',text = 'Upper Body')
        self.cbtnMuscle2 = Checkbutton(self.frameMuscle, bg = Constant.white_color, variable = muscle2, onvalue='Middle Body', offvalue='',text = 'Middle Body')
        self.cbtnMuscle3 = Checkbutton(self.frameMuscle, bg = Constant.white_color, variable = muscle3, onvalue='Lower Body', offvalue='',text = 'Lower Body')


        self.lblSession = Label(self.FillInfo_block, text = 'Training Session Duration', font = f'{Constant.main_font} 12 bold',
                               fg = Constant.main_color, bg = Constant.white_color) 
        self.frameSession = Frame(self.FillInfo_block, bg = Constant.black_color)                         
        self.txtSession = Entry(self.frameSession, width=30, font = f'{Constant.main_font} 14')    

    def createViews(self):
        self.createFrames()

    def btnContinue_onClick(self):
        if(self.count == 1):
            self.lblHeight.destroy()
            self.frameHeight.destroy()

            self.lblWeight.destroy()
            self.frameWeight.destroy()

            self.lblAge.destroy()
            self.frameAge.destroy()

            self.lblExp.grid(row = 1, column = 0, sticky = W)
            self.frameExp.grid(row = 2, column = 0, columnspan = 2, sticky = W)
            self.rbtnExp1.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)
            self.rbtnExp2.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)
            self.rbtnExp3.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)  
            
            self.lblTool.grid(row = 3, column = 0, sticky = W)
            self.frameTool.grid(row = 4, column = 0, columnspan = 2, sticky = W)
            self.rbtnTool1.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)
            self.rbtnTool2.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)
            self.count+=1
        elif(self.count == 2):
            self.lblExp.destroy()
            self.frameExp.destroy()

            self.lblTool.destroy()
            self.frameTool.destroy()

            self.lblMuscle.grid(row = 1, column = 0, sticky = W)
            self.frameMuscle.grid(row = 2, column = 0, columnspan = 2, sticky = W)
            self.cbtnMuscle1.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)
            self.cbtnMuscle2.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)
            self.cbtnMuscle3.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)

            self.lblSession.grid(row = 3, column = 0, sticky = W)
            self.frameSession.grid(row = 4, column = 0, pady = 15, sticky = 'NSEW')
            self.txtSession.pack(padx = 1,pady = 1, fill = X)
            self.count +=1
        else:
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
        self.frameHeight.grid(row = 2, column = 0, pady = 15, sticky = 'NSEW')
        self.txtHeight.pack(padx = 1,pady = 1, fill = X)

        self.lblWeight.grid(row = 3, column = 0, sticky = W)
        self.frameWeight.grid(row = 4, column = 0, pady = 15, sticky = 'NSEW')
        self.txtWeight.pack(padx = 1,pady = 1, fill = X)

        self.lblAge.grid(row = 5, column=0, sticky = W)
        self.frameAge.grid(row = 6, column= 0, pady = 15, sticky = 'NSEW')
        self.txtAge.pack(padx = 1,pady = 1, fill = X)


        self.btnContinue.grid(row = 7, column = 0, columnspan = 2, pady = 40, ipadx = 10, ipady = 5)

if __name__ == "__main__":
    screen = fillInforScreen()
    screen.onCreate()
    screen.run() 
        