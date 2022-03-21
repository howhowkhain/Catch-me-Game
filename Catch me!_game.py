"""

Catch me! - Game

Game for fun and relax build in python 3 and tkinter.

"""


import tkinter as tk
import random
from tkinter import messagebox


def jump(event):
    random.seed()
    x_limit = 420
    y_limit = 475
    x_initial = button.winfo_x()
    y_initial = button.winfo_y()
    x_final = random.randint(0, x_limit)
    y_final = random.randint(0, y_limit)
    x_clearance = x_final - x_initial
    y_clearance = y_final - y_initial
    while abs(x_clearance) < 50:
        x_final = random.randint(0, x_limit)
        x_clearance = x_final - x_initial
    while abs(y_clearance) < 50:
        y_final = random.randint(0, y_limit)
        y_clearance = y_final - y_initial
    button.place(x=x_final, y=y_final)


def game_over():
    window.bell()
    messagebox.showinfo(title="Game Over", message="Game is over!\nYou won!")


# function for closing the application before game over
def closing_app():
    window.bell()
    if messagebox.askyesno(
            title="Exit!", message="Are you sure you\nwant to exit\nthis beautiful game?"):
        window.destroy()


# create main window
window = tk.Tk(className="Game")

# configure main window
window.title("Catch me!")
window.geometry("500x500")
window.resizable(width=False, height=False)

# create a frame widget
frame = tk.Frame(window, width=500, height=500, background="#03fce3")
frame.place(x=0, y=0)

# # create "Catch me!" button
button = tk.Button(frame, text="Catch me!", width=10,
                   background="#f5f582", font=("bold"), command=game_over)
button.place(x=0, y=0)
button.bind("<Enter>", jump)

# binding the main window to a callback for closing the app
window.protocol("WM_DELETE_WINDOW", closing_app)
window.mainloop()
