import time
import tkinter as tk
from random import randint
import math
from tkinter.font import Font
import pygame


class SlavesAndJugs(tk.Tk):
    def __init__(self, canvas, game_view):
        """
             Initialize the SlavesAndJugs class.

             Parameters:
             - canvas (tk.Canvas): The canvas on which the game is displayed.
             - game_view: The game view object.
        """
        self.num_of_jugs_in_frame = 0
        self.animated_image = None
        self.game_view = game_view
        self.base_bg = tk.PhotoImage(file="images/slavesBG.png")
        self.img_back_to_menu = tk.PhotoImage(file="images/back.png")
        self.canvas = canvas
        self.create_gui(self.canvas)
        self.lbl_title = self.canvas.create_text(500, 50, text="The Poisoned Jug", font=("Cooper Black", 50),
                                                 fill="white")
        self.slaves_num = 10
        self.jugs_num = 1000

        self.lines = 20
        self.column = 50
        self.dead_slave_txt = ["", "", "", "", "", "", "", "", "", ""]
        self.alive_slave_txt = ["", "", "", "", "", "", "", "", "", ""]
        self.slave_num_txt = ["", "", "", "", "", "", "", "", "", ""]
        self._build_widgets()
        self.speed = 3
        self.font_size = 10
        self.bold_font = Font(weight="bold", size=self.font_size)
        self.count_dead = 0
        pygame.mixer.init()

    @staticmethod
    def create_gui(new_canvas):
        """
               Create the graphical user interface (GUI) for the game.

               Parameters:
               - new_canvas (tk.Canvas): The canvas on which the GUI is created.
        """
        new_canvas.pack(fill="both", expand=True)

    def _build_widgets(self):
        """
            Build the widgets for the game GUI.
        """
        # start frame widgets
        self.options_frame = tk.Frame(self.canvas, padx=30, pady=10, bg="#E1A95F", borderwidth=5, relief="ridge")
        self.options_frame.pack(pady=100)
        self.jugs_label = tk.Label(self.options_frame, text="Number of jugs 1-1000:", bg="#E1A95F",
                                   font=("Cooper Black", 20))
        self.jugs_entry = tk.Entry(self.options_frame, width=35, borderwidth=3, font=("Cooper Black", 15))
        self.jugs_label.pack()
        self.jugs_entry.pack(pady=3)
        self.speed_label = tk.Label(self.options_frame, text="Choose speed 1 - 10:", bg="#E1A95F",
                                    font=("Cooper Black", 20))
        self.speed_entry = tk.Entry(self.options_frame, width=35, borderwidth=3, font=("Cooper Black", 15))
        self.speed_label.pack(pady=3)
        self.speed_entry.pack(pady=3)
        self.btn_start = tk.Button(self.options_frame, text="Find the Poisoned Jug", font=("Cooper Black", 11),
                                   command=self.find_poisoned_jug)
        self.btn_start.pack(pady=10)

        # primary details
        self.num_of_jugs_lbl = tk.Label(self.canvas, font=("Cooper Black", 12))
        self.lbl_result = tk.Label(self.canvas, font=("Cooper Black", 12))
        self.lbl_result_binary = tk.Label(self.canvas, font=("Cooper Black", 12))
        self.lbl_jug_num_in_frame = tk.Label(self.canvas, font=("Cooper Black", 12))

        self.slave_label = tk.Label(self.canvas, text="", font=("Cooper Black", 18))
        self.lbl_total = tk.Label(self.canvas, font=("Cooper Black", 12))

        self.back_to_menu_btn = tk.Button(self.canvas, width=40, height=40, bd=7,fg='#009999', bg='#ffcc99',
                                          highlightbackground="blue",relief="raised", image=self.img_back_to_menu,
                                          command=self.back_to_options)
        self.back_to_menu_btn.place(relx=0.95, rely=0.08, anchor="center")

    def _create_animation(self):
        """
            Creates the animation canvas and initializes the jugs based on the user input.
        """
        self.canvas_jugs = tk.Canvas(self.canvas, width=450, height=300, bg="#E1A95F")
        self.canvas_jugs.place(relx=0.75, rely=0.72, anchor='center')

        self.jug_width = 20
        self.jug_height = 40
        self.spacing = 9
        self.jug_fill = "sienna"
        self.jug_outline = "black"
        self.jugs = []
        self.all_jugs = []

        for i in range(self.lines):
            for j in range(self.column):
                jug_number = i * self.column + j + 1
                if jug_number > self.jugs_num:
                    break

        self.canvas_jugs.update_idletasks()

    def reset_jugs(self):
        """
           Resets the color of all jugs on the animation canvas.
        """
        for i, jug in enumerate(self.jugs):
            self.canvas_jugs.itemconfig(jug, fill=self.jug_fill, outline=self.jug_outline)



    def reset_data(self):
        self.count_dead = 0
        for i in range(10):
            self.canvas.delete(self.slave_num_txt[i])
            self.canvas.delete(self.dead_slave_txt[i])
            self.canvas.delete(self.alive_slave_txt[i])


        for item in self.canvas.find_withtag("rectangle"):
            self.canvas.delete(item)


        self.lbl_total.place_forget()
        self.options_frame.pack_forget()
        self.back_to_menu_btn.place_forget()

    def show_primary_details(self, poisoned_jug):

        self.num_of_jugs_lbl.config(text=f"Total number of jugs: {self.jugs_num}")
        self.num_of_jugs_lbl.place(relx=0.75, rely=0.17)

        self.lbl_result.config(text=f"The Poisoned Jug: {poisoned_jug}")
        self.lbl_result.place(relx=0.76, rely=0.22)

        self.lbl_result_binary.config(text="Binary: {}".format(bin(poisoned_jug)[2:].zfill(self.slaves_num)))
        self.lbl_result_binary.place(relx=0.79, rely=0.26)



    def find_poisoned_jug(self):
        """
            Starts the process of finding the poisoned jug.
        """
        self.num_of_jugs_in_frame = 0
        self.jugs_entry.config(foreground='black')
        self.jugs_label.config(foreground='black')
        input_jugs = self.jugs_entry.get()

        self.speed_entry.config(foreground='black')
        self.speed_label.config(foreground='black')
        input_speed = self.speed_entry.get()

        if not input_jugs.isdigit() or int(input_jugs) < 1 or int(input_jugs) > 1000:
            self.jugs_entry.config(foreground='red')
            self.jugs_label.config(foreground='red')
            print("ERROR")
            return

        if not input_speed.isdigit() or int(input_speed) < 1 or int(input_speed) > 10:
            self.speed_entry.config(foreground='red')
            self.speed_label.config(foreground='red')
            print("ERROR")
            return

        else:
            self.jugs_num = int(input_jugs)
            self.slaves_num = int(math.log2(self.jugs_num)) + 1

            self._create_animation()
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

            self.jugs_entry.delete(0, 'end')
            self.speed_entry.delete(0, 'end')

        self.reset_data()  # reset all data in the window for a new round

        pygame.mixer.music.load("music/GraveYard.mp3")
        pygame.mixer.music.play()  # Play the music sound
        self._create_animation()
        slave_status = [0] * self.slaves_num

        self.reset_jugs()
        poisoned_jug = randint(1, self.jugs_num)  # raffle the number of the poisoned jug

        self.show_primary_details(poisoned_jug)

        slave_bitmask = [1 << i for i in range(self.slaves_num)][::-1]  # reverse the order of the list
        dead_slave = sum([mask for mask in slave_bitmask if poisoned_jug & mask])

        for i, mask in enumerate(slave_bitmask):
            if dead_slave & mask:
                slave_status[i] = 1  # Set the status of the slave to dead

        self.image = tk.PhotoImage(file="images/Slave.png")
        dead_image = tk.PhotoImage(file="images/skull.png")  # New image for dead slave

        canvas_width = self.canvas_jugs.winfo_width()
        canvas_height = self.canvas_jugs.winfo_height()
        slaves_width = self.jug_width + self.spacing + 20
        slaves_height = 40
        num_slaves = self.slaves_num
        initial_x = -self.image.width()  # Starting position outside the left edge of the canvas
        initial_y = canvas_height // 2 - slaves_height // 2 + 175  # Center vertically
        final_x = canvas_width // 2 - slaves_width * num_slaves // 2 + 30
        final_y = canvas_height // 2 - slaves_height // 2 + 175
        animation_duration = 3000
        num_steps = 50

        for i in range(num_slaves):  # Change the number of times the image enters here (e.g., 2 times)
            self.create_table(i + 1)
            self.slave_label.config(text=f"Slave: {i+1}")
            self.slave_label.place(relx=0.06,rely=0.83)
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
                self.canvas.after((animation_duration // self.speed) // num_steps)  # Delay between steps

            wine1_img = tk.PhotoImage(file="images/jug1.png")
            wine2_img = tk.PhotoImage(file="images/jug2.png")
            wine3_img = tk.PhotoImage(file="images/jug3.png")
            wine4_img = tk.PhotoImage(file="images/jug4.png")

            # create image objects on the canvas
            wine_images = [wine1_img, wine2_img, wine3_img, wine4_img]

            wine_image_ids = []
            for j in range(len(wine_images)):
                wine_image = self.canvas.create_image(final_x + 180, final_y - 65, image=wine_images[j])
                wine_image_ids.append(wine_image)
                self.canvas.update()
                time.sleep(0.5 / self.speed)
                self.canvas.delete(wine_image)

            # replace the slave image with a drinking images
            drinking_img = tk.PhotoImage(file="images/Slave.png")

            self.canvas.itemconfigure(self.image, image=drinking_img)
            self.canvas.update()
            time.sleep(0.0001)
            self.canvas.coords(self.canvas.find_all()[0])

            # Set the status of the slave to dead:  # Add the dead slave image on top
            if slave_status[i] == 1:
                self.dead_image = self.canvas.create_image(final_x, final_y, image=dead_image, anchor="nw")
                self.canvas.update()
                time.sleep(2)
                self.canvas.delete(self.dead_image)  # Remove the dead slave image

            # Move the image back to the starting position
            self.canvas.coords(self.animated_image, initial_x, initial_y)
            self.canvas_jugs.delete("all")

        self.canvas_jugs.delete("all")
        self.slave_label.place_forget()
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

                self.all_jugs.append(jug)


        self.canvas_jugs.update_idletasks()
        self.canvas_jugs.config(scrollregion=self.canvas_jugs.bbox("all"))
        self.canvas_jugs.itemconfig(self.all_jugs[poisoned_jug - 1], fill="blue", outline="blue")

        pygame.mixer.music.stop()  # Stop the music
        for i, mask in enumerate(slave_bitmask):
            if dead_slave & mask:
                text_color = "red"  # Apply a different color according to the slave status
                num_text = "1"
                alive_status = "Dead"
                slave_status[i] = 1  # Set the status of the slave to dead
                self.count_dead += 1
            else:
                text_color = "green"
                num_text = "0"
                alive_status = "Alive"
            x_pos = 37 + i * (self.jug_width + self.spacing + 22)
            y_pos = 540

            # define shaped background to the text
            self.slave_num_txt[i] = self.canvas.create_text(x_pos, y_pos, text=f"Slave {i+1}",
                                                            fill=text_color, font=self.bold_font, tags="slave")
            s = self.canvas.create_rectangle(self.canvas.bbox(self.slave_num_txt[i]), fill="white",tags="rectangle")
            self.canvas.tag_lower(s, self.slave_num_txt[i])
            self.dead_slave_txt[i] = self.canvas.create_text(x_pos, y_pos + 20, text=num_text, fill=text_color,
                                                             font=self.bold_font, tags="slave")
            d = self.canvas.create_rectangle(self.canvas.bbox(self.dead_slave_txt[i]), fill="white",tags="rectangle")
            self.canvas.tag_lower(d, self.dead_slave_txt[i])
            self.alive_slave_txt[i] = self.canvas.create_text(x_pos, y_pos + 40, text=alive_status,
                                                              fill=text_color,
                                                              font=self.bold_font, tags="slave")
            a = self.canvas.create_rectangle(self.canvas.bbox(self.alive_slave_txt[i]), fill="white",tags="rectangle")
            self.canvas.tag_lower(a, self.alive_slave_txt[i])

        self.options_frame.pack(pady=100)
        self.back_to_menu_btn.place(relx=0.95, rely=0.08, anchor="center")

        self.lbl_total.place(relx=0.11, rely=0.71)
        self.lbl_total.config(text=f"Total slaves dead: {self.count_dead} out of {self.slaves_num} slaves")
        self.num_of_jugs_in_frame = self.jugs_num
        self.lbl_jug_num_in_frame.config(text=f"Number of jugs in frame: {self.num_of_jugs_in_frame}")
        self.lbl_jug_num_in_frame.place(relx=0.75, rely=0.47)

    def back_to_options(self):
        """
            Handles the action of going back to the option's menu.
            """
        self.lbl_result.destroy()
        self.game_view.back_to_options()

    def create_table(self, number_of_slave):
        """
          Creates a table of jugs based on the specified number of slaves.

          Args:
              number_of_slave (int): The number of slaves.
          """
        # Define the scrollbar to the canvas
        v_scrollbar = tk.Scrollbar(self.canvas, orient=tk.VERTICAL, width=12, relief='raised', borderwidth=2)
        v_scrollbar.place(relx=0.983, rely=0.719, relheight=0.43, anchor='center')

        h_scrollbar = tk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, width=12, relief='raised', borderwidth=2)
        h_scrollbar.place(relx=0.75, rely=0.946, relwidth=0.452, anchor='center')

        self.canvas_jugs.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        v_scrollbar.config(command=self.canvas_jugs.yview)
        h_scrollbar.config(command=self.canvas_jugs.xview)
        count_i = 0
        count_j = 0
        for i in range(self.lines):
            for j in range(self.column):
                jug_number = i * self.column + j + 1
                if jug_number > self.jugs_num:
                    break
                formatted_binary = format(jug_number, '0{}b'.format(self.slaves_num))

                if number_of_slave < 1 or number_of_slave > len(formatted_binary):
                    pass
                elif formatted_binary[number_of_slave-1] == '1':
                    x1 = self.spacing + count_j * (self.jug_width + self.spacing)
                    y1 = self.spacing + count_i * (self.jug_height + self.spacing)
                    x2 = x1 + self.jug_width
                    y2 = y1 + self.jug_height
                    points = [x1, y1, x1, y1 + self.jug_height * 0.6, x1 + self.jug_width * 0.2, y2,
                              x1 + self.jug_width * 0.8, y2, x2,
                              y1 + self.jug_height * 0.6, x2, y1]
                    jug = self.canvas_jugs.create_polygon(points, fill=self.jug_fill, outline=self.jug_outline)
                    self.canvas_jugs.create_text(x1 + self.jug_width // 2, y1 + self.jug_height // 2,
                                                 text=str(jug_number), font=("Arial", 8), fill="white")
                    self.num_of_jugs_in_frame = self.num_of_jugs_in_frame + 1

                    self.jugs.append(jug)
                    count_j = count_j+1
                    if count_j > self.column:
                        count_j = 0
                        count_i = count_i + 1

        self.lbl_jug_num_in_frame.config(text=f"Number of jugs in frame: {self.num_of_jugs_in_frame}")
        self.lbl_jug_num_in_frame.place(relx=0.75, rely=0.47)
        self.num_of_jugs_in_frame = 0
        self.canvas_jugs.update_idletasks()
        self.canvas_jugs.config(scrollregion=self.canvas_jugs.bbox("all"))
