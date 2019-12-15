from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import PIL
from PIL import Image
import requests
import db
from io import BytesIO

def on_click(event=None):
    # `command=` calls function without argument
    # `bind` calls function with one argument
    print(i)
    print("image clicked")


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)

        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((50, 0), window=self.scrollable_frame, anchor="nw")
        canvas.config(background="blue")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def inter():
    global img
    global i
    window = Tk()
    #window.overrideredirect(1)
    window.geometry("400x350+400+125")
    window.configure(background='black')
    nr = 3  # number of rows
    nc = 3  # number of columns
    topimg = "logo.png"
    imag = tk.PhotoImage(file=topimg)
    #la = tk.Label(window, image=imag)
    #la.pack(side="top")
    canvass = tk.Canvas(window, height=50, width=110, bg="black", highlightthickness=0)
    canvass.create_image(58, 30, image=imag)
    canvass.pack(side=TOP, anchor=W)
    frame = ScrollableFrame(window)
    #p = 'images.png'
    #img = PhotoImage(file=p)
    myimg=[]
    photo_list = []
    basewidth = 125
    for img in db.myList:
        response = requests.get(img)
        img = Image.open(BytesIO(response.content))
        idth = (basewidth / float(img.size[0]))
        hsie = int((float(img.size[1]) * float(idth)))
        img = img.resize((basewidth, hsie), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        #img = img.zoom(25)  # with 250, I ended up running out of memory
        #img = img.subsample(42)  # mechanically, here it is adjusted to 32 instead of 320
        myimg.append(img)
    #for i in range(nr * nc):
    for i in range(0, len(myimg)):
        l = tk.Label(frame.scrollable_frame, image=myimg[i])
        l.bind('<Button-1>', on_click)
        photo_list.append(l)
        photo_list[-1].grid(row=i // nc, column=i % nc)
    frame.pack(pady=(20, 10))
    window.mainloop()