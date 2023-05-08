import tkinter as tk
from PIL import ImageTk

class GameView:
    def __init__(self, root, controller):
        root.wm_attributes("-topmost", 1)
        self.topLbl = None
        self.controller = controller
        root.title("my gui")
        root.geometry("1000x700")

        self.base_bg = ImageTk.PhotoImage(file="images/background.png")
        self.birthday = ImageTk.PhotoImage(file="images/birthday.png")
        self.slaves = ImageTk.PhotoImage(file="images/slaves.png")


        self.my_gui = tk.Canvas(root,width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.my_gui.create_image(0, 0, image=self.base_bg, anchor="nw")
        self.create_gui(self.my_gui)

        self.my_gui.create_text(350,100,text="Choose one option",fill="white",font=("Helvetica", 30),anchor="nw", justify="left")

        self.btn_option1 = tk.Button(self.my_gui, text="Guess the birthday", fg='#009999', bg='#ffcc99', highlightbackground="blue",
                                    relief="raised",bd=10,padx=5,pady=5,font=('Sans Serif',20,'bold'),image=self.birthday,compound='bottom',
                                     command=lambda:[self.my_gui.pack_forget(),self.create_gui(self.birthday_canvas) ,self.make_grid(), self.place_widgets_in_birthday_page()])
        self.btn_option2 = tk.Button(self.my_gui, text="The poisoned jug", fg='#00FF00', bg="black", highlightbackground="orange",
                                     relief="raised",bd=10,padx=10,pady=16,font=('Sans Serif',20,'bold'),image=self.slaves,compound='bottom',
                                     command=lambda:[self.my_gui.pack_forget(), self.make_grid(), self.place_widgets_in_birthday_page()])

        self.place_widgets_in_gui()

        self.birthday_canvas = tk.Canvas(root, width=root.winfo_screenwidth(),height=root.winfo_screenheight())
        self.birthday_canvas.create_image(0, 0, image=self.base_bg, anchor="nw")
        self.create_gui(self.birthday_canvas)

        self.topLbl = tk.Label(self.birthday_canvas,text="Is your birthday here ?",font=('Sans Serif',20))

        #self.grid_of_numbers = tk.Label(self.birthday_canvas,text="",font=('Sans Serif', 15))
        self.chart_frame = tk.Frame(self.birthday_canvas,bg='black', borderwidth=2, relief="ridge")


        self.btnYes = tk.Button(self.birthday_canvas,width=5,height=2, text="YES",padx=15,pady=7,bg='#856ff8',font=('Sans Serif',15),
                                command=self.btnYes_click)
        self.btnNo = tk.Button(self.birthday_canvas,text="NO",width=5,height=2, padx=15,pady=7,bg='#856ff8',font=('Sans Serif',15),
                                command=self.btnNo_click)

        self.result = tk.Label(self.birthday_canvas,text="",font=("Sans Serif",20))

        self.btn_start_again = tk.Button(self.birthday_canvas, text="Start again",width=10,height=2, padx=15,pady=7,
                                         bg='#856ff8',font=('Sans Serif',15),command=self.btn_start_again)
        self.btn_back = tk.Button(self.birthday_canvas, text="Back to menu",width=10,height=2, padx=15,pady=7,
                                  bg='#856ff8',font=('Sans Serif',15),command=self.btn_back_clicked)

    @staticmethod
    def create_gui(new_canvas):
        new_canvas.pack(fill="both", expand=True)

    def place_widgets_in_gui(self):
        self.btn_option1.place(relx=0.3, rely=0.6, anchor="center")
        self.btn_option2.place(relx=0.7, rely=0.6, anchor="center")
    def place_widgets_in_birthday_page(self):
        self.topLbl.place(relx=0.5, rely=0.1, anchor="center")
        self.btnYes.place(relx=0.43, rely=0.75, anchor="center")
        self.btnNo.place(relx=0.58, rely=0.75, anchor="center")

    def make_grid(self):
        self.controller.make_grid()

    def set_list(self,numList):
        for row in range(4):
            for col in range(4):
                index = row * 4 + col  # calculate the index based on row and column
                grid_of_numbers = tk.Label(self.chart_frame, text=f"{numList[index]}",font=('Sans Serif',15),
                                           width=6, height=3,bg='orange', borderwidth=3,relief="groove")
                grid_of_numbers.grid(row=row, column=col)
        self.chart_frame.place(relx=0.5, rely=0.4, anchor="center")

    def btnYes_click(self):
        self.controller.btn_clicked(1)

    def btnNo_click(self):
        self.controller.btn_clicked(0)

    def show_result(self,result):
        self.result["text"] = result
        self.result.place(relx=0.5, rely=0.2, anchor="center")
        self.btnNo.place_forget()
        self.btnYes.place_forget()
        self.topLbl.place_forget()
        self.chart_frame.place_forget()
        self.btn_start_again.place(relx=0.5, rely=0.4, anchor="center")
        self.btn_back.place(relx=0.5, rely=0.6, anchor="center")


    def btn_start_again(self):
        #self.birthday_canvas.pack_forget()
        self.result.place_forget()
        self.btn_start_again.place_forget()
        self.btn_back.place_forget()

        self.create_gui(self.birthday_canvas)
        self.controller.btn_start_again()
        self.make_grid()
        self.place_widgets_in_birthday_page()


    def btn_back_clicked(self):
        self.result.place_forget()
        self.btn_start_again.place_forget()
        self.btn_back.place_forget()

        #self.create_gui(self.my_gui)
        #self.my_gui.create_image(0, 0, image=self.base_bg, anchor="nw")
        self.birthday_canvas.pack_forget()
        self.create_gui(self.my_gui)
        #self.my_gui.pack(fill="both", expand=True)
        self.controller.btn_start_again()
        self.place_widgets_in_gui()







