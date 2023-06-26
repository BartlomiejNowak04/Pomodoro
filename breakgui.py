import tkinter as tk
import time


def foo():
    pass


"""This program creates a fullscreen image and keeps it displayed 
on the screen for 5 minutes to prevent work during that time."""


"""Time is set up for the Pomodoro technique
 with a default work period of 25 minutes (1500 seconds) 
 and a 5-minute break."""
times = 0
limit = 300


""" Refreshing clock"""


def clock():
    global limit
    limit -= 1
    minute = limit // 60
    second = limit % 60
    timerLabel.config(text=f'{minute}:{second}')
    # If the 5-minute duration has been reached,
    # the program destroys the screen. Otherwise,
    # it waits and refreshes the time.
    if times != limit:
        timerLabel.after(1000, clock)
        # program is waiting
    else:
        root.destroy()
        # destroy screen


"""Tkinter is used for creating and modifying the screen."""

root = tk.Tk()
root.attributes("-fullscreen", True, "-topmost", True)
root.protocol("WM_DELETE_WINDOW", foo)

root.config(bg='#38858a')
but = tk.Button(root, font=("ArialRounded", 1),
                text=" 5 minutes Break", command=root.destroy)
but.grid()

timerLabel = tk.Label(root, text="", font=(
    "ArialRounded", 110), bg='#4c9196', fg='white', border=200)
timerLabel.grid(padx=1000, pady=400)


"""Initialization function."""
clock()


root.mainloop()
