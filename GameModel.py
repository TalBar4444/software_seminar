from tkinter import PhotoImage

class GameModel:
    def __init__(self, controller):
        """
        initialize Game model variables
        """
        self.round = 1
        self.test = 1
        self.controller = controller
        self.date = 0

        #self.goat_photo = PhotoImage(file="images/goat.png")


    def yesNo_selection(self,choose): #choose 0 = no, 1= yes
        if self.round <=5:
            if choose == 1:
                #self.round = format(self.round,'06b')
                self.date |= self.test
                #self.result = ('{0:06b}'.format(self.date))
                print(self.date)

            self.test *= 2
            self.round += 1
            if self.round <=5:
                self.make_grid()
            if self.round>5:
                print(self.date)
                self.controller.result(self.date)

    def make_grid(self):
        curList = []
        # self.controller.get_List(1)
        for i in range(1, 32):
            x = '{0:06b}'.format(i)
            if x[-self.round] == "1":
                curList.append(i)
        self.controller.set_list(curList)
        curList.clear()

    def reset_game(self):
        self.round=1
        self.test = 1
        self.date = 0
