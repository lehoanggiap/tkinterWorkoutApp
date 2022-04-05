from loginScreen import loginScreen

class main():
    def run(self):
        path = "../assets/img/fitify_cover.jpg"
        self.screen = loginScreen(path)
        self.screen.onCreate()
        self.screen.run()

app = main()
app.run()