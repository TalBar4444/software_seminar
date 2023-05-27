import tkinter as tk
from BirthdayFeature import BirthdayFeature
from SlavesAndJugs import SlavesAndJugs

class GameView:
    def __init__(self):
        """
            Initializes the GameView class.
        """
        self.root = tk.Tk()
        self.root.wm_attributes("-topmost", 1)
        self.topLbl = None
        # self.slaves = SlavesAndJugs
        self.root.title("Software Engineering Seminar")
        self.root.geometry("1000x700")
        self.root.resizable(False,False)

        self.base_bg = tk.PhotoImage(file="images/background.png")
        self.birthday = tk.PhotoImage(file="images/birthday.png")
        self.slaves = tk.PhotoImage(file="images/slaves.png")
        self.slavesBG = tk.PhotoImage(file="images/slavesBG.png")


        self.my_gui = tk.Canvas(self.root,width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.my_gui.create_image(0, 0, image=self.base_bg, anchor="nw")
        self.create_gui(self.my_gui)
        self.birthday_canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.birthday_canvas.create_image(0, 0, image=self.base_bg, anchor="nw")
        self.slaves_canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.slaves_canvas.create_image(0, 0, image=self.slavesBG, anchor="nw")
        self.chart_frame_bd = tk.Frame(self.birthday_canvas, bg='black', borderwidth=2, relief="ridge")
        self.chart_frame_slaves = tk.Frame(self.slaves_canvas, bg='black', borderwidth=2, relief="ridge")
        self.my_gui.create_text(500, 100, text="Choose One Option", font=("Cooper Black", 50),fill='#ffffff', anchor="n")

        self.btn_option1 = tk.Button(self.my_gui, text="Guess the birthday", fg='#009999', bg='#ffcc99', highlightbackground="blue",
                                    relief="raised",bd=10,padx=5,pady=5,font=('Sans Serif',20,'bold'),image=self.birthday,compound='bottom',
                                     command=lambda:[self.my_gui.pack_forget(),self.create_gui(self.birthday_canvas) ,self.make_grid(), self.playBirthday()])
        self.btn_option2 = tk.Button(self.my_gui, text="The poisoned jug", fg='#00FF00', bg="black", highlightbackground="orange",
                                     relief="raised",bd=10,padx=10,pady=16,font=('Sans Serif',20,'bold'),image=self.slaves,compound='bottom',
                                     command=lambda:[self.my_gui.pack_forget(), self.make_grid(), self.playSlavesGame()])

        self.place_widgets_in_gui()

    def back_to_options(self):
        """
            Resets the GUI to the options screen.

            - Packs and displays the main canvas.
            - Removes the birthday canvas and recreates the slaves canvas.
            - Resets the background images.
            - Displays the "Choose One Option" text.
            - Recreates the option buttons.
        """
        self.create_gui(self.my_gui)
        self.birthday_canvas.pack_forget()
        self.slaves_canvas.destroy()
        self.slaves_canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(),
                                       height=self.root.winfo_screenheight())
        self.slaves_canvas.create_image(0, 0, image=self.slavesBG, anchor="nw")
        self.my_gui.create_image(0, 0, image=self.base_bg, anchor="nw")
        self.my_gui.create_text(500, 100, text="Choose One Option", font=("Cooper Black", 50),fill='#ffffff', anchor="n")


        self.btn_option1 = tk.Button(self.my_gui, text="Guess the birthday", fg='#009999', bg='#ffcc99',
                                     highlightbackground="blue",
                                     relief="raised", bd=10, padx=5, pady=5, font=('Sans Serif', 20, 'bold'),
                                     image=self.birthday, compound='bottom',
                                     command=lambda: [self.my_gui.pack_forget(), self.create_gui(self.birthday_canvas),
                                                      self.make_grid(), self.playBirthday()])
        self.btn_option2 = tk.Button(self.my_gui, text="The poisoned jug", fg='#00FF00', bg="black",
                                     highlightbackground="orange",
                                     relief="raised", bd=10, padx=10, pady=16, font=('Sans Serif', 20, 'bold'),
                                     image=self.slaves, compound='bottom',
                                     command=lambda: [self.my_gui.pack_forget(), self.create_gui(self.slaves_canvas),
                                                      self.playSlavesGame()])

        self.my_gui.pack(fill="both", expand=True)
        self.place_widgets_in_gui()

    @staticmethod
    def create_gui(new_canvas):
        """
            Packs and displays the specified canvas.

            Args:
                new_canvas (tkinter.Canvas): The canvas to be displayed.
        """
        new_canvas.pack(fill="both", expand=True)

    def place_widgets_in_gui(self):
        """
            Places the option buttons in the GUI.
        """
        self.btn_option1.place(relx=0.3, rely=0.6, anchor="center")
        self.btn_option2.place(relx=0.7, rely=0.6, anchor="center")

    def playSlavesGame(self):
        """
            Starts the SlavesAndJugs game.
        """
        SlavesAndJugs(self.slaves_canvas, self)

    def playBirthday(self):
        """
            Starts the BirthdayFeature game.
        """
        BirthdayFeature(self.birthday_canvas, self.chart_frame_bd, self)

    def make_grid(self):
        """
            Generates and sets the numbers grid for the BirthdayFeature game.
        """
        self.round = 1
        curList = []
        # self.controller.get_List(1)
        for i in range(1, 32):
            x = '{0:06b}'.format(i)
            if x[-self.round] == "1":
                curList.append(i)
        self.set_list(curList)
        curList.clear()

    def set_list(self, numList):
        """
            Sets the numbers grid for the BirthdayFeature game.

            Args:
                   numList (list): List of numbers to be displayed in the grid.
        """
        for row in range(4):
            for col in range(4):
                index = row * 4 + col  # calculate the index based on row and column
                grid_of_numbers = tk.Label(self.chart_frame_bd, text=f"{numList[index]}", font=('Sans Serif', 15),
                                           width=6, height=3, bg='orange', borderwidth=3, relief="groove")
                grid_of_numbers.grid(row=row, column=col)
        self.chart_frame_bd.place(relx=0.5, rely=0.4, anchor="center")
