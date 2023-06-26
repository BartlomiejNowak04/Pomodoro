import subprocess
import time

i = 0
while True:
    time.sleep(1)
    i += 1
    if i == 5:
        subprocess.run(["python", "breakgui.py"])
        i = 0
    else:
        print(i)
