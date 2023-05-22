import tkinter as tk
from tkinter import ttk
from random import randint
import math
import time

class SlavesAndJugs(tk.Tk):
    def __init__(self, canvas, game_view):
        self.image = None
        self.animated_image = None
        self.game_view = game_view
        #super().__init__()
        #self.root = tk.Tk
        # self.root.title("Slaves & Jugs")
        # self.root.geometry("1000x700")
        self.base_bg = tk.PhotoImage(file="images/background.png")
        self.canvas = canvas
        self.create_gui(self.canvas)
        self.slaves_num = 8
        self.jugs_num = 255
        self.lines = 8
        self.column = 30
        self._build_widgets()
        self._create_animation()

    @staticmethod
    def create_gui(new_canvas):
        new_canvas.pack(fill="both", expand=True)

    def _build_widgets(self):
        self.create_gui(self.canvas)
        self.lbl_title = ttk.Label(self.canvas, text="The poisoned jug", font=("Arial", 24))
        self.lbl_title.pack(pady=20)

        self.btn_start = ttk.Button(self.canvas, text="Find the Poisoned Jug", command=self.find_poisoned_jug)
        self.btn_start.pack(pady=10)

        self.lbl_result = ttk.Label(self.canvas, text="", font=("Arial", 18))
        self.lbl_result.pack(pady=10)

        self.binary_label = tk.Label(self.canvas, text="Binary: ", font=("Arial", 12))
        self.binary_label.pack(pady=10)

        self.options_frame = ttk.Frame(self.canvas)
        self.options_frame.pack(side="left", padx=10)

        #ttk.Separator(self.options_frame, orient="horizontal").pack(fill="x", pady=10)

        # Add a label and entry widget for the number of jugs
        # self.slaves_label = ttk.Label(self.options_frame, text="Number of slaves 1-8:")
        # self.slaves_label.pack(pady=5)
        # self.slaves_entry = ttk.Entry(self.options_frame, width=10)
        # self.slaves_entry.pack(pady=5)

        # self.update_btn_slaves = ttk.Button(self.options_frame, text="Update", command=self.update_slaves)
        # self.update_btn_slaves.pack(pady=10)

        ttk.Separator(self.options_frame, orient="horizontal").pack(fill="x", pady=10)

        self.jugs_label = ttk.Label(self.options_frame, text="Number of jugs 1-255:")
        self.jugs_label.pack(pady=5)
        self.jugs_entry = ttk.Entry(self.options_frame, width=10)
        self.jugs_entry.pack(pady=5)


            # Add a button to update the number of jugs and slaves
        self.update_btn_jugs = ttk.Button(self.options_frame, text="Update", command=self.update_jugs)
        self.update_btn_jugs.pack(pady=10)

            # Add a separator
        ttk.Separator(self.options_frame, orient="horizontal").pack(fill="x", pady=10)

        self.back_to_menu_btn = ttk.Button(self.options_frame, text="Back to main menu", command=self.back_to_options)
        self.back_to_menu_btn.pack(pady=10)

        # self.canvas = tk.Canvas(self, width=780, height=480, bg="white")
        # self.canvas.pack(pady=10)

    def _create_animation(self):
        self.canvas_jugs = tk.Canvas(self.canvas, width=780, height=480, bg="white")
        self.canvas_jugs.pack(pady=10)
        self.canvas_jugs.create_image(0, 0, image=self.base_bg, anchor="nw")
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
                points = [x1, y1, x1, y1 + self.jug_height * 0.6, x1 + self.jug_width * 0.2, y2, x1 + self.jug_width * 0.8, y2, x2, y1 + self.jug_height * 0.6, x2, y1]
                jug = self.canvas_jugs.create_polygon(points, fill=self.jug_fill, outline=self.jug_outline)
                self.canvas_jugs.create_text(x1 + self.jug_width // 2, y1 + self.jug_height // 2,
                                        text=str(jug_number), font=("Arial", 8), fill="white")
                self.jugs.append(jug)

    def update_jugs(self):
        self.jugs_entry.config(foreground='black')
        self.jugs_label.config(foreground='black')
        input_jugs = self.jugs_entry.get()
        if(not input_jugs.isdigit() or int(input_jugs)<1 or int(input_jugs)>255):
            self.jugs_entry.config(foreground='red')
            self.jugs_label.config(foreground='red')
            print("ERROR")
            return

        else:
            self.jugs_num = int(input_jugs)
            self.slaves_num = int(math.log2(self.jugs_num)) + 1

            if int(self.jugs_entry.get()) <= 30:
                self.lines = 1
                self.column = int(self.jugs_entry.get())
            else:
                self.column = 30
                if int(self.jugs_entry.get()) % 30 == 0:
                    self.lines = int(self.jugs_entry.get()) // 30
                else:
                    self.lines = int(self.jugs_entry.get()) // 30 + 1
            print(self.jugs_num)
            self.jugs_entry.delete(0,'end')
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

    import time

    # ...

    def find_poisoned_jug(self):
        for item in self.canvas_jugs.find_withtag("slave"):
            self.canvas_jugs.delete(item)

        slave_status = [0] * self.slaves_num
        self.reset_jugs()
        poisoned_jug = randint(1, self.jugs_num)
        slave_bitmask = [1 << i for i in range(self.slaves_num)][::-1]  # reverse the order of the list
        dead_slave = sum([mask for mask in slave_bitmask if poisoned_jug & mask])

        self.lbl_result.config(text=f"Poisoned Jug: {poisoned_jug}")
        self.canvas_jugs.itemconfig(self.jugs[poisoned_jug - 1], fill="blue", outline="blue")

        self.binary_label.config(text="Binary: {}".format(bin(poisoned_jug)[2:].zfill(self.slaves_num)))
        for i, mask in enumerate(slave_bitmask):
            if dead_slave & mask:
                text_color = "red"
                num_text = "1"
                alive_status = "Dead"
                slave_status[i] = 1  # Set the status of the slave to dead
            else:
                text_color = "green"
                num_text = "0"
                alive_status = "Alive"
                slave_status[i] = 0  # Set the status of the slave to dead
            x_pos = 410 + i * (self.jug_width + self.spacing + 20)
            y_pos = 390
            self.canvas_jugs.create_text(x_pos, y_pos, text=f"Slave {i}", fill=text_color,
                                         tags=("slave",))
            self.canvas_jugs.create_text(x_pos, y_pos + 20, text=num_text, fill=text_color, tags=("slave",))
            self.canvas_jugs.create_text(x_pos, y_pos + 40, text=alive_status, fill=text_color, tags=("slave",))

        self.image = tk.PhotoImage(file="images/Slave.png")
        dead_image = tk.PhotoImage(file="images/skull.png")  # New image for dead slave

        canvas_width = self.canvas_jugs.winfo_width()
        canvas_height = self.canvas_jugs.winfo_height()
        slaves_width = self.jug_width + self.spacing + 20
        slaves_height = 40
        num_slaves = self.slaves_num
        initial_x = -self.image.width()  # Starting position outside the left edge of the canvas
        initial_y = canvas_height // 2 - slaves_height // 2  # Center vertically
        final_x = canvas_width // 2 - slaves_width * num_slaves // 2
        final_y = canvas_height // 2 - slaves_height // 2
        animation_duration = 2000
        num_steps = 50

        for i in range(num_slaves):  # Change the number of times the image enters here (e.g., 2 times)
            self.animated_image = self.canvas_jugs.create_image(initial_x, initial_y, image=self.image, anchor="nw")

            # Calculate the change in position for each step
            delta_x = (final_x - initial_x) / num_steps
            delta_y = (final_y - initial_y) / num_steps

            # Move the image gradually using a loop
            for step in range(num_steps):
                x = initial_x + step * delta_x
                y = initial_y + step * delta_y
                self.canvas_jugs.coords(self.animated_image, x, y)
                self.canvas_jugs.update()  # Update the canvas to show the changes
                self.canvas_jugs.after(animation_duration // num_steps)  # Delay between steps

            if (slave_status[i] == 1) :  # Set the status of the slave to dead:  # Add the dead slave image on top
                self.dead_image = self.canvas_jugs.create_image(final_x, final_y, image=dead_image, anchor="nw")
                self.canvas_jugs.update()
                time.sleep(2)
                self.canvas_jugs.delete(self.dead_image)  # Remove the dead slave image

            # Move the image back to the starting position
            self.canvas_jugs.coords(self.animated_image, initial_x, initial_y)

    def back_to_options(self):
        self.lbl_result.destroy
        self.binary_label.destroy
        self.canvas.destroy()
        self.canvas_jugs.destroy()
        self.game_view.back_to_options()
