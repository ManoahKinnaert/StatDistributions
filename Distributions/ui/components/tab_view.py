import tkinter as tk
from tkinter import ttk 

class TabView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.style = ttk.Style()
        self.style.theme_use("classic")

        