import subprocess
import time


"""The program waits for 25 minutes, and then opens a 5-minute break script."""
"""Additionally, the program can display the remaining time."""
i = 0
while True:
    time.sleep(1)
    i += 1
    if i == 25*60:
        # The program executes the 'breakgui' script, and then resets the timer.
        subprocess.run(["python", "breakgui.py"])
        i = 0
    else:
        # The program simply prints the time spent.
        print(i)
