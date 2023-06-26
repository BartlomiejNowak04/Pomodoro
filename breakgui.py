import tkinter as tk
import time


def foo():
    pass


times = 0
limit = 5


def clock():
    global limit
    limit -= 1
    minute = limit // 60
    second = limit % 60
    timerLabel.config(text=f'{minute}:{second}')
    if times != limit:
        timerLabel.after(1000, clock)
    else:
        root.destroy()
        # nowy frame


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


clock()


root.mainloop()
