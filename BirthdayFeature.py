import tkinter as tk
import pygame


class BirthdayFeature(tk.Tk):
    def __init__(self, canvas, chart_frame, game_view):
        """
        Initializes the BirthdayFeature class.

        Parameters:
        - canvas: The Tkinter canvas object.
        - chart_frame: The Tkinter frame object for the chart.
        - game_view: The game view object.
        """
        # Initialize class variables
        self.game_view = game_view
        self.round = 1
        self.test = 1
        self.canvas = canvas
        self.chart_frame = chart_frame
        self.date = 0

        # Load images and initialize Pygame mixer
        self.base_bg = tk.PhotoImage(file="images/background.png")
        self.img_back_to_menu = tk.PhotoImage(file="images/back.png")
        pygame.mixer.init()

        # Create GUI and place widgets
        self.create_gui(self.canvas)
        self.topLbl = tk.Label(self.canvas, text="Is your birthday here ?", font=("Cooper Black", 25), bg="#498a9c")
        self.btn_back_from_game = tk.Button(self.canvas, width=40, height=40, bd=7,
                                            fg='#009999', bg="#ffcc99", highlightbackground="blue",
                                            relief="raised", image=self.img_back_to_menu, command=self.btn_back_clicked)
        self.btnYes = tk.Button(self.canvas, width=5, height=2, text="YES", padx=15, pady=7, bg='#856ff8',
                                font=("Cooper Black", 15), command=self.btnYes_click)
        self.btnNo = tk.Button(self.canvas, text="NO", width=5, height=2, padx=15, pady=7, bg='#856ff8',
                               font=("Cooper Black", 15), command=self.btnNo_click)
        self.result_lbl = tk.Label(self.canvas, text="", font=("Cooper Black", 25), bg="#498a9c")
        self.btn_start_again = tk.Button(self.canvas, text="Start again", width=10, height=2, padx=15, pady=7,
                                         bg='#856ff8', font=("Cooper Black", 15), command=self.btn_start_again)
        self.btn_back = tk.Button(self.canvas, text="Back to menu", width=10, height=2, padx=15, pady=7,
                                  bg='#856ff8', font=("Cooper Black", 15), command=self.btn_back_clicked)
        self.place_widgets_in_birthday_page()

    @staticmethod
    def create_gui(new_canvas):
        """
        Creates the GUI and packs the canvas.

        Parameters:
        - new_canvas: The Tkinter canvas object.
        """
        new_canvas.pack(fill="both", expand=True)

    def place_widgets_in_birthday_page(self):
        """Places the widgets in the birthday page."""
        self.topLbl.place(relx=0.5, rely=0.1, anchor="center")
        self.btn_back_from_game.place(relx=0.95, rely=0.08, anchor="center")
        self.btnYes.place(relx=0.43, rely=0.75, anchor="center")
        self.btnNo.place(relx=0.58, rely=0.75, anchor="center")

    def make_grid(self):
        """Generates the number grid based on the current round."""
        curList = []
        for i in range(1, 32):
            x = '{0:06b}'.format(i)
            if x[-self.round] == "1":
                curList.append(i)
        self.set_list(curList)
        curList.clear()

    def set_list(self, numList):
        """
        Sets the number grid based on the given list.

        Parameters:
        - numList: The list of numbers to display in the grid.
        """
        for row in range(4):
            for col in range(4):
                index = row * 4 + col
                grid_of_numbers = tk.Label(self.chart_frame, text=f"{numList[index]}", font=('Sans Serif', 15),
                                           width=6, height=3, bg='orange', borderwidth=3, relief="groove")
                grid_of_numbers.grid(row=row, column=col)
        self.chart_frame.place(relx=0.5, rely=0.4, anchor="center")

    def result(self, result):
        """
        Displays the result of the birthday date.

        Parameters:
        - result: The result to display.
        """
        pygame.mixer.music.load("music/Happy_Birthday.mp3")
        pygame.mixer.music.play()
        if result == 0:
            self.show_result('impossible date !')
        else:
            self.show_result(f"The date of your birthday is: {result}")

    def btnYes_click(self):
        """Handles the button click event for 'YES'."""
        if self.round <= 5:
            self.date |= self.test

        self.test *= 2
        self.round += 1
        if self.round <= 5:
            self.make_grid()
        if self.round > 5:
            self.result(self.date)

    def btnNo_click(self):
        """Handles the button click event for 'NO'."""
        self.test *= 2
        self.round += 1
        if self.round <= 5:
            self.make_grid()
        if self.round > 5:
            self.result(self.date)

    def show_result(self, result):
        """
        Displays the result message.

        Parameters:
        - result: The result message to display.
        """
        self.result_lbl["text"] = result
        self.result_lbl.place(relx=0.5, rely=0.2, anchor="center")
        self.topLbl.place_forget()
        self.btnNo.place_forget()
        self.btnYes.place_forget()
        self.btn_back_from_game.place_forget()
        self.chart_frame.place_forget()
        self.btn_start_again.place(relx=0.5, rely=0.4, anchor="center")
        self.btn_back.place(relx=0.5, rely=0.6, anchor="center")

    def btn_start_again(self):
        """Handles the button click event for 'Start again'."""
        pygame.mixer.music.stop()
        self.canvas.pack_forget()
        self.result_lbl.place_forget()
        self.btn_start_again.place_forget()
        self.btn_back.place_forget()

        self.create_gui(self.canvas)
        self.reset_game()
        self.make_grid()
        self.place_widgets_in_birthday_page()

    def btn_back_clicked(self):
        """Handles the button click event for 'Back to menu'."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.topLbl.place_forget()
        self.result_lbl.place_forget()
        self.btnNo.place_forget()
        self.btnYes.place_forget()
        self.btn_start_again.place_forget()
        self.btn_back.place_forget()
        self.btn_back_from_game.place_forget()
        self.game_view.back_to_options()
        self.reset_game()

    def reset_game(self):
        """Resets the game variables."""
        self.round = 1
        self.test = 1
        self.date = 0
