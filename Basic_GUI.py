# Start!
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=800, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="#800000")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#80000" command="addApp")
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#800000")
runApps.pack()



root.mainloop()