import tkinter as tk

class Button(tk.Canvas):
    """Express button styling colors"""
    DEFAULT = {
        "bg": "#292a30",
        "fg": "#ffffff",
        "hover-bg": "#11cfff",
        "hover-fg": "#292a30",

        "font": "Verdana 12 bold",
        "radius": 25
    }
    ACTIVE = {
        "bg": "#11cfff",
        "fg": "#292a30",
        "hover-bg": "#11ffb7",
        "hover-fg": "#292a30",

        "font": "Verdana 15 bold",
        "radius": 15
    }
    WARNING = {
        "bg": "#ffc311",
        "fg": "#292a30",
        "hover-bg": "#ff7811",
        "hover-fg": "#292a30",

        "font": "Verdana 15 bold",
        "radius": 15
    }
    def __init__(self, master, text, style="default", vpadding=25, hpadding=20, command=None, *args, **kwargs):
        super().__init__(master, highlightthickness=0, bg=master["background"], *args, **kwargs)
        
        self.master = master 
        self.font = "Verdana 12 bold" 
        self.text = text 
        self.style = getattr(self, style.upper())
        self.command = command 
        self.hover = False
        self.vpadding = vpadding
        self.hpadding = hpadding
        # setup the interface of the button
        self.setup_ui()
        # configure bindings
        self.bind("<Enter>", lambda e: self.hover_event(e))
        self.bind("<Leave>", lambda e: self.hover_event(e))
        self.bind("<Button-1>", lambda e: self.click_event(e))

    def setup_ui(self):
        self.delete("all")
        self.config(bg=self.master["background"])
        # create a rounded rectangle
        font = self.style["font"].split(" ")
        w = int(font[1]) * len(self.text) + self.hpadding
        h = int(font[1]) + self.vpadding
        self.config(width=w + 1, height=h + 1)
        self.__round_rect(0, 0, w, h, fill=self.style["hover-bg" if self.hover else "bg"],
                          radius=self.style["radius"])
        # render the text
        self.create_text(w // 2, h // 2, text=self.text, font=self.style["font"],
                         fill=self.style["hover-fg" if self.hover else "fg"])
    
    def __round_rect(self, x1, y1, x2, y2, radius=15, **kwargs):
        points = [x1 +radius, y1,
                x1 + radius, y1,
                x2 - radius, y1,
                x2 - radius, y1,
                x2, y1,
                x2, y1 + radius,
                x2, y1 + radius,
                x2, y2 - radius,
                x2, y2 - radius,
                x2, y2,
                x2 - radius, y2,
                x2 - radius, y2,
                x1 + radius, y2,
                x1 + radius, y2,
                x1, y2,
                x1, y2 - radius,
                x1, y2 - radius,
                x1, y1 + radius,
                x1, y1 + radius,
                x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True, outline="")

    def hover_event(self, e):
        self.hover = not self.hover 
        self.setup_ui()

    def click_event(self, e):
        if self.command is not None:
            self.command()