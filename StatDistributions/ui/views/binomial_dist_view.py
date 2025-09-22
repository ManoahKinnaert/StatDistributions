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

        
        self.figure1 = Figure(figsize=(5, 5), dpi=100)
        self.pmf_plot = self.figure1.add_subplot(111)
        self.pmf_plot.set_title("PMF (Probability Mass Function)")
        
        self.figure2 = Figure(figsize=(5, 5), dpi=100)
        self.cdf_plot = self.figure2.add_subplot(111)
        self.cdf_plot.set_title("CDF (Cumulative Distribution Function)")



        self.setup_ui()
    
    def setup_ui(self):
        self.chart_frame = tk.Frame(self, bg=self["background"])
        self.chart_frame.pack(side="top", fill="both")

        self.canvas1 = FigureCanvasTkAgg(self.figure1, master=self.chart_frame)
        self.canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

        self.canvas2 = FigureCanvasTkAgg(self.figure2, master=self.chart_frame)
        self.canvas2.get_tk_widget().pack(side="right", fill="both", expand=True)

        self.input_frame = tk.Frame(self, bg=self["background"])
        self.input_frame.pack(side="bottom", fill="x")

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
            self.cdf_plot.cla()
        except:
            return 
        
        # plot the pmf
        k = np.arange(0, n + 1)
        y = binom.pmf(k, n, p)
        self.pmf_plot.plot(k, y, "bo", ms=8)
        self.pmf_plot.vlines(k, 0, y, colors="b", lw=5, alpha=0.5)
        self.pmf_plot.set_title("PMF (Probability Mass Function)")
        
        # plot the cdf
        y = binom.cdf(k, n, p)
        self.cdf_plot.plot(k, y, "go", ms=8)
        self.cdf_plot.set_title("CDF (Cumulative Distribution Function)")
        
        self.canvas1.draw()
        self.canvas2.draw()
