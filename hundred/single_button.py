import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# SingleButton contains a button that on clicking will open a new window
class SingleButton:
    def __init__(self, center_frame: tk.ttk.Frame, idx: int, row: int, column: int):
        self.single_button = ttk.Button(center_frame, text=str(idx))
        self.single_button.grid(row=row, column=column, sticky="nswe")
