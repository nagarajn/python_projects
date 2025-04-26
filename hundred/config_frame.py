import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PIL import Image


class ConfigFrame:
    def __init__(self, top_frame: tk.ttk.Frame):
        self.config_frame = ttk.Frame(top_frame)
        self.left_label = ttk.Label(self.config_frame, text="100", font=("Arial", 32))
        self.left_label.pack(pady=10, padx=10)
        image_path = tk.PhotoImage(file="images/plus.png")
        image_path = image_path.subsample(15, 15)
        self.plus = tk.Button(self.config_frame, text="", width=2, image=image_path)
        self.plus.pack(pady=10, padx=10)
        self.minus = ttk.Button(self.config_frame, text="-", width=2)
        self.minus.pack(pady=10, padx=10)
        self.dropdown = ttk.Combobox(self.config_frame)
        self.dropdown.pack(pady=10, padx=10)
        # self.left_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")
