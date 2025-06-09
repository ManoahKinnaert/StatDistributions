import tkinter as tk

from .components import Button, TabView
from .views import NormalDistView, BinomialDistView

class Display(tk.Tk):
    def __init__(self):
        super().__init__()

        self.w, self.h = 1000, 700
        x, y = (self.winfo_screenwidth() - self.w) // 2, (self.winfo_screenheight() - self.h) // 2
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.title("Distributions")
        self.config(bg="black")

        self.setup_ui()

        self.mainloop()

    def setup_ui(self):
        self.tab_view = TabView(self, bg=self["background"])
        self.tab_view.pack(fill="both", expand=True)

        normal_dist_view = NormalDistView(self.tab_view, bg=self["background"])
        self.tab_view.add_tab(normal_dist_view, title="Normal Distribution")
        binom_dist_view = BinomialDistView(self.tab_view)
        self.tab_view.add_tab(binom_dist_view, title="Binomial Distribution")


        self.footer_frame = tk.Frame(self, bg="#1b1d21")
        self.footer_frame.pack(side="bottom", fill="x")

        Button(self.footer_frame, text="Close", style="default", command=exit).pack(side="right", pady=5, padx=5)
        Button(self.footer_frame, text="Help", style="default").pack(side="left", padx=5)