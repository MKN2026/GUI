# Start!
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=800, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="#800000")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

root.mainloop()