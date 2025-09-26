import tkinter as tk

from ui.components import Button

class HelpView(tk.Tk):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master 

        self.width, self.height = 500, 300
        x, y = (self.winfo_screenwidth() - self.width) // 2, (self.winfo_screenheight() - self.height) // 2
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.title("Help window")

        self.setup_ui()

        self.mainloop()

    def setup_ui(self):
        title_frame = tk.Frame(self, bg=self["background"], height=25)
        title_frame.pack(side="top", fill="x") 

        content_frame = tk.Frame(self, bg=self["background"])
        content_frame.pack(fill="both", expand=1)

        footer_frame = tk.Frame(self, bg="#1b1d21", height=25)
        footer_frame.pack(side="bottom", fill="x")

        Button(footer_frame, text="Close", command=self.close_command).pack(side="right", padx=15)

    def close_command(self):
        self.master.help_view_showing = False 
        self.destroy()