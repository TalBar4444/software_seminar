import time
import tkinter as tk
from random import randint
import math
from tkinter.font import Font

import pygame


class SlavesAndJugs(tk.Tk):
    def __init__(self, canvas, game_view):
        self.animated_image = None
        self.game_view = game_view
        #super().__init__()
        #self.root = tk.Tk
        # self.root.title("Slaves & Jugs")
        # self.root.geometry("1000x700")
        self.base_bg = tk.PhotoImage(file="images/slavesBG.png")
        self.img_back_to_menu = tk.PhotoImage(file="images/back.png")
        self.canvas = canvas
        self.create_gui(self.canvas)
        self.slaves_num = 10
        self.jugs_num = 1000
        self.lines = 20
        self.column = 50
        self.dead_slave_txt = None
        self.alive_slave_txt = None
        self.slave_num_txt = None
        self._build_widgets()
        self.speed = 3
        # self._create_animation()
        self.font_size = 10
        self.bold_font = Font(weight="bold", size=self.font_size)
        self.count_dead = 0
        pygame.mixer.init()

    @staticmethod
    def create_gui(new_canvas):
        new_canvas.pack(fill="both", expand=True)

    def _build_widgets(self):
        # self.create_gui(self.canvas)
        self.lbl_title = tk.Label(self.canvas,background="sienna",bg = "white", text="The Poisoned Jug", font=("Cooper Black", 40), anchor="n")
        self.lbl_title.pack(pady=20)

        # self.btn_start = tk.Button(self.options_frame, text="Find the Poisoned Jug", command=self.find_poisoned_jug)
        # self.btn_start.place(relx=0.5, rely=0.39, anchor="center")

        self.lbl_result = tk.Label(self.canvas, font=("Arial", 18))
        self.lbl_total = tk.Label(self.canvas, font=("Arial", 12))
        self.binary_label = tk.Label(self.canvas, text="Binary: ", font=("Arial", 12))

        #self.options_frame = tk.Frame(self.canvas,width=150,height=150)
        self.options_frame = tk.Frame(self.canvas, padx=100,bg="sienna3")
        self.options_frame.pack(side="top", padx=20,pady=20)

        self.jugs_label = tk.Label(self.options_frame, text="Number of jugs 1-1000:",font=("Cooper Black",10))
        self.jugs_entry = tk.Entry(self.options_frame, width=30)
        self.jugs_label.pack()
        self.jugs_entry.pack()

        self.speed_label = tk.Label(self.options_frame, text="Choose speed 1 - 10:", font=("Cooper Black", 10))
        self.speed_entry = tk.Entry(self.options_frame, width=30)
        self.speed_label.pack()
        self.speed_entry.pack()

            # Add a button to update the number of jugs and slaves
        self.update_btn_jugs = tk.Button(self.options_frame, text="Update", command=self.update_jugs)
        self.update_btn_jugs.pack(pady=10)
            #add the start button
        self.btn_start = tk.Button(self.options_frame, text="Find the Poisoned Jug", command=self.find_poisoned_jug)
        self.btn_start.pack(pady=10)

            # Add a separator

        self.back_to_menu_btn = tk.Button(self.canvas, width=40, height=40, bd=7,
                                            fg='#009999', bg='#ffcc99', highlightbackground="blue",
                                            relief="raised", image=self.img_back_to_menu,
                                          command=self.back_to_options)
        self.back_to_menu_btn.place(relx=0.95, rely=0.08, anchor="center")

        # self.canvas = tk.Canvas(self, width=780, height=480, bg="white")
        # self.canvas.pack(pady=10)

    def _create_animation(self):
        self.canvas_jugs = tk.Canvas(self.canvas, width=480, height=380)
        self.canvas_jugs.place(relx=0.73, rely=0.7, anchor='center')
        self.canvas_jugs.config(bg="#cd7c2a")

        v_scrollbar = tk.Scrollbar(self.canvas, orient=tk.VERTICAL, width=10, relief='raised', borderwidth=2)
        v_scrollbar.place(relx=0.97, rely=0.7, relheight=0.45, anchor='center')

        h_scrollbar = tk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, width=10, relief='raised', borderwidth=2)
        h_scrollbar.place(relx=0.73, rely=0.965, relwidth=0.45, anchor='center')

        self.canvas_jugs.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        v_scrollbar.config(command=self.canvas_jugs.yview)
        h_scrollbar.config(command=self.canvas_jugs.xview)

        # self.canvas_jugs = tk.Canvas(self.canvas_jugs, bg="#cd7c2a")
        # self.canvas_jugs.create_window(0, 0, anchor='nw', window=self.canvas_jugs)

        self.jug_width = 20
        self.jug_height = 40
        self.spacing = 8
        self.jug_fill = "sienna"
        self.jug_outline = "black"
        self.jugs = []

        for i in range(self.lines):
            for j in range(self.column):
                x1 = self.spacing + j * (self.jug_width + self.spacing)
                y1 = self.spacing + i * (self.jug_height + self.spacing)
                x2 = x1 + self.jug_width
                y2 = y1 + self.jug_height
                jug_number = i * self.column + j + 1
                if jug_number > self.jugs_num:
                    break
                # Define the jug shape
                points = [x1, y1, x1, y1 + self.jug_height * 0.6, x1 + self.jug_width * 0.2, y2,
                          x1 + self.jug_width * 0.8, y2, x2,
                          y1 + self.jug_height * 0.6, x2, y1]
                jug = self.canvas_jugs.create_polygon(points, fill=self.jug_fill, outline=self.jug_outline)
                self.canvas_jugs.create_text(x1 + self.jug_width // 2, y1 + self.jug_height // 2,
                                             text=str(jug_number), font=("Arial", 8), fill="white")
                self.jugs.append(jug)

        self.canvas_jugs.update_idletasks()
        self.canvas_jugs.config(scrollregion=self.canvas_jugs.bbox("all"))

    def update_jugs(self):
        self._create_animation()
        self.jugs_entry.config(foreground='black')
        self.jugs_label.config(foreground='black')
        input_jugs = self.jugs_entry.get()

        self.speed_entry.config(foreground='black')
        self.speed_label.config(foreground='black')
        input_speed = self.speed_entry.get()

        if(not input_jugs.isdigit() or int(input_jugs)<1 or int(input_jugs)>1000):
            self.jugs_entry.config(foreground='red')
            self.jugs_label.config(foreground='red')
            print("ERROR")
            return

        if (not input_speed.isdigit() or int(input_speed) < 1 or int(input_speed) > 10):
            self.speed_entry.config(foreground='red')
            self.speed_label.config(foreground='red')
            print("ERROR")
            return

        else:
            self.jugs_num = int(input_jugs)
            self.slaves_num = int(math.log2(self.jugs_num)) + 1
            self.speed = int(input_speed)

            if int(self.jugs_entry.get()) <= 50:
                self.lines = 1
                self.column = int(self.jugs_entry.get())
            else:
                self.column = 50
                if int(self.jugs_entry.get()) % 50 == 0:
                    self.lines = int(self.jugs_entry.get()) // 50
                else:
                    self.lines = int(self.jugs_entry.get()) // 50 + 1
            print(self.jugs_num)
            self.jugs_entry.delete(0,'end')
            self.speed_entry.delete(0, 'end')
            self.canvas_jugs.forget()
            self._create_animation()

    # def update_slaves(self):
    #     self.slaves_entry.config(foreground='black')
    #     self.slaves_label.config(foreground='black')
    #     input_slaves = self.slaves_entry.get()
    #     if (not input_slaves.isdigit() or int(input_slaves) < 1 or int(input_slaves) > 8):
    #         self.slaves_entry.config(foreground='red')
    #         self.slaves_label.config(foreground='red')
    #         print("ERROR")
    #         return
    #     else:
    #         self.slaves_num = int(input_slaves)
    #         self.jugs_num = 2**self.slaves_num - 1
    #         if int(self.jugs_num) <= 30:
    #             self.lines = 1
    #             self.column = int(self.jugs_num)
    #         else:
    #             self.column = 30
    #             if self.jugs_num % 30 == 0:
    #                 self.lines = self.jugs_num // 30
    #             else:
    #                 self.lines = self.jugs_num // 30 + 1
    #
    #         print(self.jugs_num)
    #         self.slaves_entry.delete(0, 'end')
    #         self.canvas_jugs.forget()
    #         self._create_animation()



    def reset_jugs(self):
        for i, jug in enumerate(self.jugs):
            self.canvas_jugs.itemconfig(jug, fill=self.jug_fill, outline=self.jug_outline)

    def find_poisoned_jug(self):
        pygame.mixer.music.load("music/GraveYard.mp3")
        pygame.mixer.music.play()  # Play the music sound
        self.canvas.delete(self.alive_slave_txt)
        self.canvas.delete(self.dead_slave_txt)
        self.canvas.delete(self.slave_num_txt)
        self.update_btn_jugs.forget()
        self.btn_start.forget()
        self._create_animation()
        for item in self.canvas_jugs.find_withtag("slave"):
            self.canvas_jugs.delete(item)

        slave_status = [0] * self.slaves_num

        self.reset_jugs()
        poisoned_jug = randint(1, self.jugs_num)
        slave_bitmask = [1 << i for i in range(self.slaves_num)][::-1]  # reverse the order of the list
        dead_slave = sum([mask for mask in slave_bitmask if poisoned_jug & mask])

        self.lbl_result.place(relx=0.74, rely=0.20)
        self.lbl_result.config(text=f"Poisoned Jug: {poisoned_jug}")
        self.canvas_jugs.itemconfig(self.jugs[poisoned_jug - 1], fill="blue", outline="blue")

        self.binary_label.place(relx=0.78, rely=0.24)
        self.binary_label.config(text="Binary: {}".format(bin(poisoned_jug)[2:].zfill(self.slaves_num)))

        for i, mask in enumerate(slave_bitmask):
            if dead_slave & mask:
                text_color = "red"
                num_text = "1"
                alive_status = "Dead"
                slave_status[i] = 1  # Set the status of the slave to dead
                self.count_dead += 1
            else:
                text_color = "green"
                num_text = "0"
                alive_status = "Alive"
            x_pos = 25 + i * (self.jug_width + self.spacing + 20)
            y_pos = 630
            self.slave_num_txt = self.canvas.create_text(x_pos, y_pos, text=f"Slave {self.slaves_num-i}", fill=text_color, font=self.bold_font,
                                                         tags=("slave",))
            self.dead_slave_txt = self.canvas.create_text(x_pos, y_pos + 20, text=num_text, fill=text_color, font=self.bold_font, tags=("slave",))
            self.alive_slave_txt = self.canvas.create_text(x_pos, y_pos + 40, text=alive_status, fill=text_color, font=self.bold_font, tags=("slave",))
        self.image = tk.PhotoImage(file="images/Slave.png")
        dead_image = tk.PhotoImage(file="images/skull.png")  # New image for dead slave

        # self.lbl_total.place(relx=0.70, rely=0.28)
        # self.lbl_total.config(text=f"Total slaves dead: {self.count_dead} out of {self.slaves_num} slaves")

        canvas_width = self.canvas_jugs.winfo_width()
        canvas_height = self.canvas_jugs.winfo_height()
        slaves_width = self.jug_width + self.spacing + 20
        slaves_height = 40
        num_slaves = self.slaves_num
        initial_x = -self.image.width()  # Starting position outside the left edge of the canvas
        initial_y = canvas_height // 2 - slaves_height // 2 +175  # Center vertically
        final_x = canvas_width // 2 - slaves_width * num_slaves // 2+30
        final_y = canvas_height // 2 - slaves_height // 2+175
        animation_duration = 3000
        num_steps = 50


        for i in range(num_slaves):  # Change the number of times the image enters here (e.g., 2 times)
            self.animated_image = self.canvas.create_image(initial_x, initial_y, image=self.image, anchor="nw")

            # Calculate the change in position for each step
            delta_x = (final_x - initial_x) / num_steps
            delta_y = (final_y - initial_y) / num_steps

            # Move the image gradually using a loop
            for step in range(num_steps):
                x = initial_x + step * delta_x
                y = initial_y + step * delta_y
                self.canvas.coords(self.animated_image, x, y)
                self.canvas.update()  # Update the canvas to show the changes
                self.canvas.after((animation_duration//self.speed) // num_steps)  # Delay between steps

            wine1_img = tk.PhotoImage(file="images/spilling1.png")
            wine2_img = tk.PhotoImage(file="images/spilling2.png")
            wine3_img = tk.PhotoImage(file="images/spilling3.png")
            wine4_img = tk.PhotoImage(file="images/spilling4.png")


            # create image objects on the canvas
            wine_images = [wine1_img, wine2_img, wine3_img, wine4_img]
            wine_image_ids = []
            for j in range(len(wine_images)):
                wine_image = self.canvas.create_image(final_x+180, final_y-65, image=wine_images[j])
                wine_image_ids.append(wine_image)
                self.canvas.update()
                time.sleep(0.5 / self.speed)
                self.canvas.delete(wine_image)

            # replace the prisoner image with a drinking images
            drinking_img = tk.PhotoImage(file="images/Slave.png")

            self.canvas.itemconfigure(self.image, image=drinking_img)
            self.canvas.update()
            time.sleep(0.0001)
            self.canvas.coords(self.canvas.find_all()[0])

           # self.canvas.grid_forget()

            if (slave_status[self.slaves_num - i - 1] == 1):  # Set the status of the slave to dead:  # Add the dead slave image on top
                self.dead_image = self.canvas.create_image(final_x, final_y, image=dead_image, anchor="nw")
                self.canvas.update()
                time.sleep(2)
                self.canvas.delete(self.dead_image)  # Remove the dead slave image

            # Move the image back to the starting position
            self.canvas.coords(self.animated_image, initial_x, initial_y)
        self.update_btn_jugs.pack(pady=10)
        self.btn_start.pack(pady=10)

        pygame.mixer.music.stop()
        self.lbl_total.place(relx=0.70, rely=0.28)
        self.lbl_total.config(text=f"Total slaves dead: {self.count_dead} out of {self.slaves_num} slaves")


    def back_to_options(self):
        self.lbl_result.destroy()
        self.binary_label.destroy()
        self.game_view.back_to_options()

