from tkinter import *
import tkinter as tk
import main


def con():
    main.inter()


if __name__ == '__main__':
    root = Tk()

    root.overrideredirect(1)
    root.geometry("400x200+450+200")
    root.configure(background='black')

    image_file = "logoss.png"
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=200, width=500, bg="black", highlightbackground="#c91833", highlightthickness=0.5)
    canvas.create_image(200, 100, image=image)
    canvas.pack()
    root.after(5000, root.destroy)
    root.mainloop()
    con()
