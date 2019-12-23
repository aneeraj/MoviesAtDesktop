from tkinter import *
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk


def det():
    window = Tk()
    window.title('Movies At')
    window.iconbitmap("Images/ic.ico")
    # window.overrideredirect(1)
    window.geometry("400x400+400+125")
    window.configure(background='black')
    topimg = "Images/logo.png"
    imag = tk.PhotoImage(file=topimg)
    basewidth = 125
    canvass = tk.Canvas(window, height=50, width=110, bg="black", highlightthickness=0)
    canvass.create_image(58, 30, image=imag)
    canvass.grid(row=0, column=0, sticky=W)
    p = 'Images/images.png'
    img = PhotoImage(file=p)
    canvasss = tk.Canvas(window, height=300, width=110, bg="black", highlightthickness=0)
    canvasss.create_image(50, 30, image=img)
    canvasss.grid(row=2, column=0, pady=15, padx=5)
    window.mainloop()
det()