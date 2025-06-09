import tkinter as tk
from tkinter import ttk 

from ui.components import Button

class TabView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.style = ttk.Style()
        self.style.theme_use("classic")

        self.tab_bar = tk.Frame(self, bg="#292a30")
        self.tab_bar.pack(side="left", fill="y")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(side="right", fill="both", expand=True)
        # do some notebook styling -> remove border and make color correct
        self.style.layout("TNotebook.Tab", [])  # turn off tabs
        self.style.layout("TNotebook", [])
        self.style.configure("TNotebook", highlightbackground=self["background"], tabmargins=0,
                             borderwidth=0, highlightthickness=0, background=self["background"])

    def add_tab(self, view, title: str):
        self.notebook.add(view)
        ind = len(self.notebook.tabs()) - 1
        # add a tabbar button
        Button(self.tab_bar, text=title, style="default", hpadding=30,
               command=lambda: self.select_view(ind)).pack(padx=5, pady=10)

    def select_view(self, index: int):
        self.notebook.select(index)