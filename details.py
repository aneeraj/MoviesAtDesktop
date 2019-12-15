from tkinter import *
import tkinter as tk


def det():
    window = Tk()
    # window.overrideredirect(1)
    window.geometry("400x400+400+125")
    window.configure(background='black')
    topimg = "logo.png"
    imag = tk.PhotoImage(file=topimg)
    # la = tk.Label(window, image=imag)
    # la.pack(side="top")
    canvass = tk.Canvas(window, height=50, width=110, bg="black", highlightthickness=0)
    canvass.create_image(58, 30, image=imag)
    canvass.pack(side=TOP, anchor=W)
    window.mainloop()
det()