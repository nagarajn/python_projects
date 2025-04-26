import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class StatusFrame:
    def __init__(self, top_frame: tk.ttk.Frame):
        self.status_frame = ttk.Frame(top_frame, bootstyle="dark")
        self.status_label = ttk.Label(
            self.status_frame, text="Status", background="blue"
        )
        self.status_label.pack(pady=10, padx=10)
        # self.status_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")
