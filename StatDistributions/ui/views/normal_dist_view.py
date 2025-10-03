import tkinter as tk

import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
from scipy.stats import norm

class NormalDistView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        plt.style.use("dark_background")

        self.mu = tk.DoubleVar(value=0.0)
        self.mu.trace_add("write", lambda *args: self.plot_dist(*args))
        self.sigma = tk.DoubleVar(value=0.0)
        self.sigma.trace_add("write", lambda *args: self.plot_dist(*args))

        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.plot.set_title("Normal Distribution")

        self.setup_ui()
    
    def setup_ui(self):
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        self.input_frame = tk.Frame(self, bg=self["background"])
        self.input_frame.pack(side="bottom", fill="both")

        self.mu_input_frame = tk.Frame(self.input_frame, bg=self["background"])
        self.mu_input_frame.grid(row=0, column=0)

        tk.Label(self.mu_input_frame, font="Verdana 12", text="\u03BC: ", bg=self["background"], fg="white").grid(row=0, column=0)
        tk.Entry(self.mu_input_frame, font="Verdana 12", bg=self["background"], fg="white", textvariable=self.mu).grid(row=1, column=0)

        self.sigma_input_frame = tk.Frame(self.input_frame, bg=self["background"])
        self.sigma_input_frame.grid(row=0, column=1)

        tk.Label(self.sigma_input_frame, font="Verdana 12", text="\u03C3: ", bg=self["background"], fg="white").grid(row=0, column=0)
        tk.Entry(self.sigma_input_frame, font="Verdana 12", bg=self["background"], fg="white", textvariable=self.sigma).grid(row=1, column=0)
        


    def plot_dist(self, *args):
        mu, sigma = None, None
        try:
            mu, sigma = self.mu.get(), self.sigma.get() 
            self.plot.clear()
        except:
            return

        x = np.linspace(mu - 3 * sigma - .2, mu + 3 * sigma + .2, 100)
        y = norm.pdf(x, mu, sigma)
        self.plot.plot(x, y, lw=2, color="cyan")
        self.plot.set_title("Normal Distribution")
        self.plot.fill_between(x, y, alpha=0.3)
        self.canvas.draw()        
