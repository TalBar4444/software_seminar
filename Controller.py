import tkinter as tk
from GameModel import GameModel
from GameView import GameView
class Controller:
    def __init__(self):
        """
        Initialize the controller in the MVC model, controller has the view and model as variables.
        """
        self.root = tk.Tk()
        self.view = GameView(self.root, self)
        self.model = GameModel(self)
        self.root.mainloop()

    def make_grid(self):
        self.model.make_grid()

    def set_list(self,numList):
        self.view.set_list(numList)
        #self.view.grid_of_numbers.config(text=numList)
        # for i in range(4):
        #     for j in range(4):



    def btn_clicked(self,choose):
        self.model.yesNo_selection(choose)

    def result(self,result):
        if result == 0:
            self.view.show_result('impossible date !')
        else:
            self.view.show_result(f"The date of your birthday is: {result}")

    def btn_start_again(self):
        self.model.reset_game()
