import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from single_button import SingleButton


class CenterFrame:
    def __init__(self, top_frame: tk.ttk.Frame):
        self.center_frame = ttk.Frame(top_frame, bootstyle="light")
        for i in range(10):
            self.center_frame.columnconfigure(i, weight=1)
            self.center_frame.rowconfigure(i, weight=1)
        # self.center_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")
        self.single_button = list()
        for i in range(100):
            self.single_button.append(
                SingleButton(self.center_frame, i + 1, int(i / 10), i % 10)
            )
