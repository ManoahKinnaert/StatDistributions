import tkinter as tk

import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
from scipy.stats import binom

class BinomialDistView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        plt.style.use("dark_background")

        self.n = tk.IntVar()
        self.p = tk.DoubleVar()
        self.n.trace_add("write", lambda *args: self.plot_dist(*args))
        self.p.trace_add("write", lambda *args: self.plot_dist(*args))

        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.pmf_plot = self.figure.add_subplot(111)
        self.pmf_plot.set_title("Probability Mass Function")
        
        self.setup_ui()
    
    def setup_ui(self):
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.input_frame = tk.Frame(self, bg=self["background"])
        self.input_frame.pack(side="bottom", fill="both", expand=True)

        self.n_input_frame = tk.Frame(self.input_frame, bg=self["background"])
        self.n_input_frame.grid(row=0, column=0)

        tk.Label(self.n_input_frame, font="Verdana 12", text="n: ", bg=self["background"], fg="white").grid(row=0, column=0)
        tk.Entry(self.n_input_frame, font="Verdana 12", bg=self["background"], fg="white", textvariable=self.n).grid(row=1, column=0)

        self.p_input_frame = tk.Frame(self.input_frame, bg=self["background"])
        self.p_input_frame.grid(row=0, column=1)

        tk.Label(self.p_input_frame, font="Verdana 12", text="p: ", bg=self["background"], fg="white").grid(row=0, column=0)
        tk.Entry(self.p_input_frame, font="Verdana 12", bg=self["background"], fg="white", textvariable=self.p).grid(row=1, column=0)

    def plot_dist(self, *args):
        n, p = None, None 
        try:
            n, p = self.n.get(), self.p.get()
            self.pmf_plot.cla()
        except:
            return 
        
        # plot the pmf
        k = np.arange(0, n + 1)
        y = binom.pmf(k, n, p)
        self.pmf_plot.plot(k, y, "bo", ms=8)
        self.pmf_plot.vlines(k, 0, y, colors="b", lw=5, alpha=0.5)
        self.pmf_plot.set_title("PMF (Probability Mass Function)")
        
        # plot the cdf
        
        self.canvas.draw()

