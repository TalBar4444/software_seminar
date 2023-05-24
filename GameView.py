import tkinter as tk
from BirthdayFeature import BirthdayFeature
from SlavesAndJugs import SlavesAndJugs
#from PIL import ImageTk


class GameView:
    def __init__(self):
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

        # self.create_gui(self.birthday_canvas)
        #
        # self.topLbl = tk.Label(self.birthday_canvas,text="Is your birthday here ?",font=('Sans Serif',20))
        #
        # #self.grid_of_numbers = tk.Label(self.birthday_canvas,text="",font=('Sans Serif', 15))
        # self.chart_frame_bd = tk.Frame(self.birthday_canvas,bg='black', borderwidth=2, relief="ridge")
        #
        #
        # self.btnYes = tk.Button(self.birthday_canvas,width=5,height=2, text="YES",padx=15,pady=7,bg='#856ff8',font=('Sans Serif',15),
        #                         command=self.btnYes_click)
        # self.btnNo = tk.Button(self.birthday_canvas,text="NO",width=5,height=2, padx=15,pady=7,bg='#856ff8',font=('Sans Serif',15),
        #                         command=self.btnNo_click)

        # self.result_lbl = tk.Label(self.birthday_canvas,text="",font=("Sans Serif",20))
        #
        # self.btn_start_again = tk.Button(self.birthday_canvas, text="Start again",width=10,height=2, padx=15,pady=7,
        #                                  bg='#856ff8',font=('Sans Serif',15),command=self.btn_start_again)
        # self.btn_back = tk.Button(self.birthday_canvas, text="Back to menu",width=10,height=2, padx=15,pady=7,
        #                            bg='#856ff8',font=('Sans Serif',15),command=self.btn_back_clicked)

    def back_to_options(self):
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
        # self.birthday_canvas.pack_forget()
        # self.slaves_canvas.pack_forget()
        # self.create_gui(self.my_gui)
        self.my_gui.pack(fill="both", expand=True)
        self.place_widgets_in_gui()

    @staticmethod
    def create_gui(new_canvas):
        new_canvas.pack(fill="both", expand=True)

    def place_widgets_in_gui(self):
        self.btn_option1.place(relx=0.3, rely=0.6, anchor="center")
        self.btn_option2.place(relx=0.7, rely=0.6, anchor="center")
    # def place_widgets_in_birthday_page(self):
    #     self.topLbl.place(relx=0.5, rely=0.1, anchor="center")
    #     self.btnYes.place(relx=0.43, rely=0.75, anchor="center")
    #     self.btnNo.place(relx=0.58, rely=0.75, anchor="center")

    def playSlavesGame(self):
        SlavesAndJugs(self.slaves_canvas, self)

    def playBirthday(self):
        BirthdayFeature(self.birthday_canvas, self.chart_frame_bd, self)

    def make_slaves_grid(self):
        self.slaves_num = 8
        self.jugs_num = 240
        self.lines = 8
        self.column = 30
        self.jug_width = 20
        self.jug_height = 40
        self.spacing = 5
        self.jug_fill = "sienna"
        self.jug_outline = "black"
        self.jugs = []
        print(self.jugs_num)

        for i in range(self.lines):
            for j in range(self.column):
                x1 = self.spacing + j * (self.jug_width + self.spacing)
                y1 = self.spacing + i * (self.jug_height + self.spacing)
                x2 = x1 + self.jug_width
                y2 = y1 + self.jug_height
                jug_number = i * 30 + j + 1
                if jug_number > self.jugs_num:
                    return
                # Define the jug shape
                points = [x1, y1, x1, y1 + self.jug_height * 0.6, x1 + self.jug_width * 0.2, y2,
                          x1 + self.jug_width * 0.8, y2, x2, y1 + self.jug_height * 0.6, x2, y1]
                jug = self.slaves_canvas.create_polygon(points, fill=self.jug_fill, outline=self.jug_outline)
                self.slaves_canvas.create_text(x1 + self.jug_width // 2, y1 + self.jug_height // 2,
                                        text=str(jug_number), font=("Arial", 8), fill="white")
                self.jugs.append(jug)

    def make_grid(self):
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
        for row in range(4):
            for col in range(4):
                index = row * 4 + col  # calculate the index based on row and column
                grid_of_numbers = tk.Label(self.chart_frame_bd, text=f"{numList[index]}", font=('Sans Serif', 15),
                                           width=6, height=3, bg='orange', borderwidth=3, relief="groove")
                grid_of_numbers.grid(row=row, column=col)
        self.chart_frame_bd.place(relx=0.5, rely=0.4, anchor="center")
    # def set_list(self,numList):
    #     for row in range(4):
    #         for col in range(4):
    #             index = row * 4 + col  # calculate the index based on row and column
    #             grid_of_numbers = tk.Label(self.chart_frame_bd, text=f"{numList[index]}",font=('Sans Serif',15),
    #                                        width=6, height=3,bg='orange', borderwidth=3,relief="groove")
    #             grid_of_numbers.grid(row=row, column=col)
    #     self.chart_frame_bd.place(relx=0.5, rely=0.4, anchor="center")
    #
    # def btnYes_click(self):
    #     self.controller.btn_clicked(1)
    #
    # def btnNo_click(self):
    #     self.controller.btn_clicked(0)
    #
    # def show_result(self,result_lbl):
    #     self.result_lbl["text"] = result_lbl
    #     self.result_lbl.place(relx=0.5, rely=0.2, anchor="center")
    #     self.btnNo.place_forget()
    #     self.btnYes.place_forget()
    #     self.topLbl.place_forget()
    #     self.chart_frame_bd.place_forget()
    #     self.btn_start_again.place(relx=0.5, rely=0.4, anchor="center")
    #     self.btn_back.place(relx=0.5, rely=0.6, anchor="center")
    #
    #
    # def btn_start_again(self):
    #     #self.birthday_canvas.pack_forget()
    #     self.result_lbl.place_forget()
    #     self.btn_start_again.place_forget()
    #     self.btn_back.place_forget()
    #
    #     self.create_gui(self.birthday_canvas)
    #     self.controller.btn_start_again()
    #     self.make_grid()
    #     self.place_widgets_in_birthday_page()
    #
    #
    # def btn_back_clicked(self):
    #     self.create_gui(self.my_gui)
    #     self.my_gui.create_image(0, 0, image=self.base_bg, anchor="nw")
    #     self.birthday_canvas.pack_forget()
    #     self.slaves_canvas.pack_forget()
    #     self.create_gui(self.my_gui)
    #     self.my_gui.pack(fill="both", expand=True)
    #     self.place_widgets_in_gui()







