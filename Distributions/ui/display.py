import tkinter as tk

from .components import Button

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
        self.footer_frame = tk.Frame(self, bg=self["background"])
        self.footer_frame.pack(side="bottom", fill="x")

        Button(self.footer_frame, text="Close", style="default", command=exit).pack(side="right", pady=5, padx=5)
        Button(self.footer_frame, text="Help", style="default").pack(side="left", padx=5)