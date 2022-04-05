from tkinter import *
import sys
import os
from tkinter import messagebox
from utils.constant import Constant
from fillInforScreen import fillInforScreen

class loginForm:
    def __init__(self, screen):
        self.screen = screen
        self.form = Frame(screen)
        self.form.place(relx = .5, rely = .5, anchor = CENTER)

    def register(self):
        pass    

    def login(self):
        name = self.nameInput.get()
        pw = self.passInput.get()
        
        if(name == ''):
            messagebox.showwarning('Warning', 'Please fill your username')
        elif(pw == ''):
            messagebox.showwarning('Warning', 'Please fill your password')
        else:     
            path = os.path.join(sys.path[0], './data/user.dat')
            with open(path,'r') as file:
                users = file.read()
                res = users.find(f'{name},{pw},')
                if(res >= 0):
                    self.screen.destroy()
                    self.inforScreen = fillInforScreen()
                    self.inforScreen.onCreate()
                    self.inforScreen.run()
                else:
                    messagebox.showwarning('Warning', 'User name or password is in correct')

                

        

    def create(self):
        #cải thiện: cần đặt 2 cái frame nằm ở giữa, dùng place anchor mà gặp lỗi
        self.title = Label(self.form, text = "LOGIN HERE", font = ('Impact', 35, 'bold'), fg = Constant.main_color) 
        self.title.grid(row=0, column=0, columnspan= 2, pady = 20)

        self.nameLabel = Label(self.form, text='User Name', padx = 20, pady = 20, font = (Constant.main_font, 12))
        self.nameLabel.grid(row=1, column=0, sticky = W)

        self.passLabel = Label(self.form, text='Password', padx = 20, pady = 20, font = (Constant.main_font, 12))
        self.passLabel.grid(row=2, column=0, sticky=W)

        self.nameInput = Entry(self.form, width=30, font = (Constant.main_font, 12))
        self.nameInput.grid(row=1, column=1, ipady = 1,  padx = 20)
        self.nameInput.focus()

        self.passInput = Entry(self.form, width=30, font = (Constant.main_font, 12), show = "*")
        self.passInput.grid(row=2, column=1, ipady = 1,  padx = 20)

        self.btnLogin = Button(self.form, text = "Login", width = 10,font = (Constant.main_font,12), fg = Constant.main_color, command= self.login)
        self.btnLogin.grid(row=3, column=0, columnspan=2, pady = 10, ipady = 2)

        self.bottomFrame = Frame(self.form)
        self.bottomFrame.grid(row = 4, column = 0, columnspan=2, ipady = 20)

        self.txtQuestion = Label(self.bottomFrame, text = "New to fitify? ", font = (Constant.main_font,12))
        self.txtQuestion.pack(side = LEFT)
        self.btnRegister = Button(self.bottomFrame, text = "Register",font = (Constant.main_font,12), fg = Constant.main_color, borderwidth= 0)
        self.btnRegister['command'] = self.register
        self.btnRegister.pack(side = LEFT)
        

