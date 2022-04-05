from tkinter import *
from screen import Screen
from utils.constant import Constant
from PIL import ImageTk, Image
from backGround.bgrImage import BgrImage
import os
import sys

class statisticsScreen(Screen):
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 700
    def __init__(self, bgrPath):
        self.screen = Toplevel()
        # super().__init__()
        self.bgrPath = bgrPath
        self.backgroundImage = BgrImage(self.screen)
        self.screen['bg'] = Constant.main_color
        self.title_screen = Label(self.screen, text = 'STATISTICS INFORMATION', bg = Constant.main_color, 
        font = f'{Constant.main_font} 16 bold', fg = Constant.white_color)
        self.btnBack = Button(self.screen)

        self.main_block = Frame(self.screen, bg = Constant.list_color)
        self.detail_infor = Frame(self.main_block, bg = Constant.main_color)
        self.detail_title = Label(self.detail_infor, text = "Detail exercise performance", font = f'{Constant.main_font} 14 bold', 
        fg = Constant.white_color, bg = Constant.main_color)
        self.detail_day_time = Label(self.detail_infor, text = "Today time workout: 00:00", font = f'{Constant.main_font} 11', 
        fg = Constant.white_color, bg = Constant.main_color)
        self.detail_week_time = Label(self.detail_infor, text = "This week time workout: 00:00", font = f'{Constant.main_font} 11', 
        fg = Constant.white_color, bg = Constant.main_color)
        self.detail_prev_week_time = Label(self.detail_infor, text = "Previous week time workout: 00:00", font = f'{Constant.main_font} 11', 
        fg = Constant.white_color, bg = Constant.main_color)

        self.detail_day_calories = Label(self.detail_infor, text = "Today calories burn: 2000", font = f'{Constant.main_font} 11', 
        fg = Constant.white_color, bg = Constant.main_color)
        self.detail_week_calories = Label(self.detail_infor, text = "This week calories burn: 2000", font = f'{Constant.main_font} 11', 
        fg = Constant.white_color, bg = Constant.main_color)
        self.detail_prev_week_calories = Label(self.detail_infor, text = "Previous week calories burn: 2000", font = f'{Constant.main_font} 11', 
        fg = Constant.white_color, bg = Constant.main_color)

        self.week_process = Frame(self.main_block, bg = Constant.list_color, pady = 20)
        self.process_chart = Canvas(self.week_process, bg = Constant.main_color, width= 420, height=260, highlightthickness= 0)
        self.days = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

        self.process_chart.create_line(20, 220, 20, 10, arrow = 'last')
        self.process_chart.create_line(15, 220, 25, 220, fill = Constant.white_color)
        self.process_chart.create_text(10, 210, text = '0', fill = Constant.white_color)

        self.process_chart.create_line(15, 130, 25, 130, fill = Constant.white_color)
        self.process_chart.create_text(10, 120, text = '5', fill = Constant.white_color)

        self.process_chart.create_line(15, 30, 25, 30, fill = Constant.white_color)
        self.process_chart.create_text(10, 40, text = '10', fill = Constant.white_color)


        x = 35 
        for i in range(7):
            self.process_chart.create_rectangle(x, 220, x + 20, 30, fill=f'{Constant.white_color}')
            self.process_chart.create_rectangle(x, 220, x + 20, 100 - 10*i, fill=f'{Constant.list_color}')
            self.process_chart.create_text(x + 10, 240, text= f'{self.days[i]}\n00:00', justify= CENTER, fill= Constant.white_color)

            x += 55

        self.time_on_exercises = Frame(self.main_block, bg = Constant.main_color) 

        exercise = ['Upper Body', 'Lower Body', 'Back', 'Head', 'ABS&Core']
        self.exercise_blocks = []

        for i in range(len(exercise)):
            frame = Frame(self.time_on_exercises, bg = Constant.white_color)
            block = {
                'frame': frame,
                'name': Label(frame, text = exercise[i], bg = Constant.white_color),
                'time': Label(frame, text = '0:00', bg = Constant.white_color)
            }

            block['name']['fg'] = Constant.main_color
            block['name']['font'] = f'{Constant.main_font} 14 bold'
            block['time']['fg'] = Constant.list_color
            block['time']['font'] = f'{Constant.main_font} 14'

            self.exercise_blocks.append(block)

    def createViews(self):
        self.backgroundImage.create(self.bgrPath)
        self.configWidgets()

    def backToHome(self):
        self.screen.destroy()   

    def configWidgets(self):
        self.title_screen.pack(fill = X, ipady = 20)

        path = os.path.join(sys.path[0], '../assets/img/prev-icon.png')
        self.btnBackImg = Image.open(path)
        self.btnBackImg = self.btnBackImg.resize((30, 30), Image.ANTIALIAS)
        self.btnBackImg = ImageTk.PhotoImage(self.btnBackImg) 
    
        self.btnBack['image'] = self.btnBackImg
        self.btnBack['borderwidth'] = 0
        self.btnBack['bg'] = Constant.main_color
        self.btnBack['command'] = self.backToHome
        self.btnBack['activebackground'] = Constant.main_color

        self.btnBack.place(x = 40, y = 20)

        self.main_block.pack(fill = X, pady = 40, ipady = 20)
        self.main_block.grid_columnconfigure(0, weight=1)
        self.main_block.grid_columnconfigure(1, weight=1)

        self.detail_infor.grid(row = 0, column = 0, padx = 80, pady = 20, ipady = 10, sticky = "NSEW")
        self.detail_title.grid(row = 0, column = 0, sticky = W, padx = 30, pady = 10)

        self.detail_day_time.grid(row = 1, column = 0, sticky = W, pady = 5, padx = 30)
        self.detail_week_time.grid(row = 2, column = 0, sticky = W, pady = 5, padx = 30)
        self.detail_prev_week_time.grid(row = 3, column = 0, sticky = W, pady = 5, padx = 30)

        self.detail_day_calories.grid(row = 4, column = 0, sticky = W, pady = 5, padx = 30)
        self.detail_week_calories.grid(row = 5, column = 0, sticky = W, pady = 5, padx = 30)
        self.detail_prev_week_calories.grid(row = 6, column = 0, sticky = W, pady = 5, padx = 30)

        self.week_process.grid(row = 0, column = 1, padx = 20,  sticky = "NSEW")
        self.process_chart.pack()

        self.time_on_exercises.grid(row = 1, column = 0, columnspan= 2, padx = 80, sticky = "NSEW")
        for i in range(len(self.exercise_blocks)):
            self.time_on_exercises.grid_columnconfigure(i, weight = 1)

        for i in range(len(self.exercise_blocks)):
            block = self.exercise_blocks[i]
            block['frame'].grid(row = 0, column = i, pady = 40, padx =20, sticky = "NSEW")
            block['name'].pack(ipady = 5)
            block['time'].pack(ipady = 5)

if __name__ == '__main__':
    path = "../assets/img/dashboard-bgr.jpg"
    screen = statisticsScreen(path)
    screen.onCreate()
    screen.run()
