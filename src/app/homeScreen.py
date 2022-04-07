from matplotlib.pyplot import text
from screen import Screen
from tkinter import *
from utils.constant import Constant
from PIL import ImageTk, Image
import os
import sys
from statisticsScreen import statisticsScreen
class homeScreen(Screen):
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 700
    def __init__(self):
        super().__init__()
        self.navBar = Frame(self.screen, bg = Constant.main_color)
        self.btnProfile = Button(self.navBar, bg = Constant.main_color, borderwidth= 0, activebackground = Constant.main_color)
        self.btnStatistics = Button(self.navBar, bg = Constant.main_color, borderwidth= 0, activebackground = Constant.main_color)
        self.btnExercise = Button(self.navBar, bg = Constant.main_color, borderwidth= 0, activebackground = Constant.main_color)
        self.exercises_block = Frame(self.screen, bg = Constant.list_color) 

        self.totalTime = Label(self.exercises_block, text = "Total time\n00:00", font = f'{Constant.main_color} 16', fg = Constant.white_color, bg = Constant.list_color)
        self.btnNext = Button(self.exercises_block, bg = Constant.list_color, borderwidth= 0, activebackground = Constant.list_color)
        self.btnPrev = Button(self.exercises_block, bg = Constant.list_color, borderwidth= 0, activebackground = Constant.list_color)


        self.upperBody_list = Frame(self.exercises_block, bg = Constant.white_color)
        self.upperBody_title = Label(self.upperBody_list, bg = Constant.white_color, 
                                    fg = Constant.main_color, text = "Upper body",
                                    font = f'{Constant.main_font} 16 bold')      

        self.active_exercise_block = Frame(self.screen, bg = Constant.white_color)
        self.active_exercise_name = Label(self.active_exercise_block, bg = Constant.white_color,
                                    fg = Constant.main_color, text = "Stretching",
                                    font = f'{Constant.main_font} 16 bold')
        self.active_exercise_image = Label(self.active_exercise_block, bg = Constant.white_color)
        self.active_exercise_intro = Label(self.active_exercise_block, bg = Constant.white_color, font = f'{Constant.main_font} 12',
        justify = LEFT, wraplength= 300)
        self.active_time_countdown = Label(self.active_exercise_block, text = "00:00", font = f'{Constant.main_font} 18')
        self.active_calories_burn = Label(self.active_exercise_block, text = "Calories burn: 0", font = f'{Constant.main_font} 18' )

        self.active_btn_frame = Frame(self.active_exercise_block, bg = Constant.white_color)
        self.btnNext_Ex = Button(self.active_btn_frame, bg = Constant.white_color, borderwidth= 0, activebackground = Constant.white_color)
        self.btnPause_Ex = Button(self.active_btn_frame, bg = Constant.white_color, borderwidth= 0, activebackground = Constant.white_color)
        self.btnPrev_Ex = Button(self.active_btn_frame, bg = Constant.white_color, borderwidth= 0, activebackground = Constant.white_color)

    def createViews(self):
        self.createNavBar()
        self.createExercisesList()
        self.createActiveExercise()

    def redirect(self):
        self.openScreen = statisticsScreen("../assets/img/dashboard-bgr.jpg")
        self.openScreen.onCreate()


    def createNavBar(self):
        self.navBar.place(relwidth = .05, relheight = 1)
        
        self.iconProfile = self.createImage('../assets/img/profile.png')
        self.btnProfile['image'] = self.iconProfile
        self.btnProfile.pack(pady = 10)

        self.iconStatistics = self.createImage('../assets/img/statistics.png')
        self.btnStatistics['image'] = self.iconStatistics
        self.btnStatistics.pack(pady = 10)
        self.btnStatistics['command'] = self.redirect

        self.iconExercise = self.createImage('../assets/img/exercise.png', {'width': 30, 'height': 20})
        self.btnExercise['image'] = self.iconExercise
        self.btnExercise.pack(pady = 10)

    def createExercisesList(self):    
        self.exercises_block.place(relx = .05,relwidth = .45, relheight = 1)
        self.totalTime.place(relx = .15, rely = .02)

        self.iconNext = self.createImage('../assets/img/next-icon.png', {'width': 40, 'height': 40})
        self.btnNext['image'] = self.iconNext
        self.btnNext.place(relx= .85 , rely = .02)

        self.iconPrev = self.createImage('../assets/img/prev-icon.png', {'width': 40, 'height': 40})
        self.btnPrev['image'] = self.iconPrev
        self.btnPrev.place(relx = .7, rely = .02)

        self.upperBody_list.place(relx = .15, rely = .16, relwidth = .7, relheight = .68)
        self.upperBody_title.pack(pady= 5, fill = X)

        self.loadExData()
        self.loadExercises()

    def createActiveExercise(self):    
        self.active_exercise_block.place(relx = .5, relwidth = .5, relheight = 1)
        self.active_exercise_name.pack(pady = 20)

        #khi có index thì lấy ra từ data
        self.active_image = self.createImage('../assets/img/stretching.jpg', {'width': 300, 'height': 200})
        self.active_exercise_image['image'] = self.active_image
        self.active_exercise_image.pack()

        self.active_exercise_intro['text'] = 'This is introduction for stretching exercise. First, you need...'
        self.active_exercise_intro.pack(pady = 10)

        self.active_time_countdown.pack(pady = 10, ipadx = 5, ipady = 5)
        self.active_calories_burn.pack(pady = 10, ipadx = 5, ipady = 5)
        self.active_btn_frame.pack(pady = 50)

        self.btnPrev_Ex['image'] = self.iconPrev
        self.btnPrev_Ex.pack(side = LEFT, padx = 10)

        self.iconPause = self.createImage('../assets/img/pause-icon.png', {'width': 40, 'height': 40})
        self.btnPause_Ex['image'] = self.iconPause
        self.btnPause_Ex.pack(side = LEFT)

        self.btnNext_Ex['image'] = self.iconNext
        self.btnNext_Ex.pack(side = LEFT,  padx = 10)


    def loadExercises(self):
        for i in range(len(self.ex_images)):
            self.ex_items[i]['image'] = self.ex_images[i]
            self.ex_items[i].pack(fill = X, pady = 10)

    def loadExData(self):    
        self.ex_images = []
        self.ex_items = []
        for i in range(6):
            img = self.createImage('../assets/img/stretching.jpg', {'width': 60, 'height': 60})
            self.ex_images.append(img)
        for i in range(6):
            time = '01:30'
            btn = Button(self.upperBody_list, text = f'     Stretching\t{time}\t', bg = Constant.white_color, compound= LEFT, borderwidth = 0)  
            btn['font'] = f'{Constant.main_font} 12'
            btn['fg'] = Constant.list_color 
            self.ex_items.append(btn)


    def createImage(self, path, config = None):
        width = 20
        height = 20
        if(config): 
            width = config['width']
            height = config['height']
        path = os.path.join(sys.path[0], path)
        img = Image.open(path)
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img) 
        return img

if __name__ == '__main__':
    home = homeScreen()
    home.onCreate()
    home.run()

