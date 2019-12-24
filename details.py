from tkinter import *
import tkinter as tk
import PIL
import db
import requests
from PIL import Image
from time import sleep
from PIL import ImageTk
from io import BytesIO
import main


def det():
    print(1)
    window2 = Tk()
    window2.title('Movies At')
    window2.iconbitmap("Images/ic.ico")
    # window.overrideredirect(1)
    window2.geometry("400x400+400+125")
    window2.configure(background='black')
    topimg = "Images/logo.png"
    imag = tk.PhotoImage(file=topimg)
    basewidth = 125
    canvasss = tk.Canvas(window2, height=50, width=110, bg="black", highlightthickness=0)
    canvasss.create_image(58, 30, image=imag)
    canvasss.grid(row=0, column=0, sticky=W)
   # p = 'Images/images.png'
    img = db.myList[main.index]
    response = requests.get(img)

    img = Image.open(BytesIO(response.content))
    idth = (basewidth / float(img.size[0]))
    hsie = int((float(img.size[1]) * float(idth)))
    img = img.resize((basewidth, hsie), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    # img = img.zoom(25)  # with 250, I e
    l = tk.Label(window2, image=img)
    #img = PhotoImage(file=img)
    #canvasss = tk.Canvas(window, height=200, width=110, bg="black", highlightthickness=0)
    #canvasss.create_image(100, 150, image=img)
    #canvasss.grid(row=2, column=0, pady=15, padx=5)
    l.grid(row=2, column=0, pady=15, padx=5)
    window2.mainloop()
