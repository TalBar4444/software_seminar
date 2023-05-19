import tkinter as tk
from tkinter import ttk
from random import randint
import math

class SlavesAndJugs(tk.Tk):
    def __init__(self, canvas, game_view):
        self.game_view = game_view
        #super().__init__()
        #self.root = tk.Tk
        # self.root.title("Slaves & Jugs")
        # self.root.geometry("1000x700")
        self.base_bg = tk.PhotoImage(file="images/background.png")
        self.canvas = canvas
        self.create_gui(self.canvas)
        self.slaves_num = 8
        self.jugs_num = 240
        self.lines = 8
        self.column = 30
        self._build_widgets()
        self._create_animation()

    @staticmethod
    def create_gui(new_canvas):
        new_canvas.pack(fill="both", expand=True)

    def _build_widgets(self):
        self.create_gui(self.canvas)
        self.lbl_title = ttk.Label(self.canvas, text="Slaves & Jugs", font=("Arial", 24))
        self.lbl_title.pack(pady=20)

        self.btn_start = ttk.Button(self.canvas, text="Find the Poisoned Jug", command=self.find_poisoned_jug)
        self.btn_start.pack(pady=10)

        self.lbl_result = ttk.Label(self.canvas, text="", font=("Arial", 18))
        self.lbl_result.pack(pady=10)

        self.binary_label = tk.Label(self.canvas, text="Binary: ", font=("Arial", 12))
        self.binary_label.pack(pady=10)

        self.options_frame = ttk.Frame(self.canvas)
        self.options_frame.pack(side="left", padx=10)

        ttk.Separator(self.options_frame, orient="horizontal").pack(fill="x", pady=10)

        # Add a label and entry widget for the number of jugs
        self.jugs_label = ttk.Label(self.options_frame, text="Number of slaves 1-8:")
        self.jugs_label.pack(pady=5)
        self.slaves_entry = ttk.Entry(self.options_frame, width=10)
        self.slaves_entry.pack(pady=5)

        self.update_btn_slaves = ttk.Button(self.options_frame, text="Update", command=self.update_slaves)
        self.update_btn_slaves.pack(pady=10)

        ttk.Separator(self.options_frame, orient="horizontal").pack(fill="x", pady=10)

        self.jugs_label = ttk.Label(self.options_frame, text="Number of jugs 1-240:")
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
            self.jugs_num = int(self.jugs_entry.get())
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

    def update_slaves(self):

        self.slaves_num = int(self.slaves_entry.get())
        self.jugs_num = 2**self.slaves_num - 1
        if int(self.jugs_num) <= 30:
            self.lines = 1
            self.column = int(self.jugs_num)
        else:
            self.column = 30
            if self.jugs_num % 30 == 0:
                self.lines = self.jugs_num // 30
            else:
                self.lines = self.jugs_num // 30 + 1

        print(self.jugs_num)
        self.slaves_entry.delete(0, 'end')
        self.canvas_jugs.forget()
        self._create_animation()



    def reset_jugs(self):
        for i, jug in enumerate(self.jugs):
            self.canvas_jugs.itemconfig(jug, fill=self.jug_fill, outline=self.jug_outline)

    def find_poisoned_jug(self):
        for item in self.canvas_jugs.find_withtag("slave"):
            self.canvas_jugs.delete(item)

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
            else:
                text_color = "green"
                num_text = "0"
                alive_status = "Alive"
            x_pos = 40 + i * (self.jug_width + self.spacing + 20)
            y_pos = 370
            self.canvas_jugs.create_text(x_pos, y_pos, text=f"Slave {self.slaves_num - i}", fill=text_color,
                                    tags=("slave",))
            self.canvas_jugs.create_text(x_pos, y_pos + 20, text=num_text, fill=text_color, tags=("slave",))
            self.canvas_jugs.create_text(x_pos, y_pos + 40, text=alive_status, fill=text_color, tags=("slave",))

    def back_to_options(self):
        self.lbl_result.destroy
        self.binary_label.destroy
        self.canvas.destroy()
        self.canvas_jugs.destroy()
        self.game_view.back_to_options()
