import subprocess
from time import sleep

import psutil

process = psutil.Process(subprocess.Popen("C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2022.2/bin/idea64.exe").pid)
#process1 = psutil.Process(4)
#print(process1)

while True:
    try:
        print("Percentage of CPU drained by the process: " + str(process.cpu_percent()/psutil.cpu_count()))
        sleep(1)
    except psutil.NoSuchProcess:
        print("Proccess exited.")
        break