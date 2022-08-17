import subprocess
import psutil
import csv
from time import sleep



process = psutil.Process(subprocess.Popen("C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2022.2/bin/idea64.exe").pid)
#process1 = psutil.Process(4)
#print(process1)

while True:
    try:
        print("Percentage of CPU drained by the process: " + str(process.cpu_percent()/psutil.cpu_count()))
        print("Number of handles: " + str(process.num_handles()))
        print("Working Set: " + str(process.memory_info().wset) + ", Private Bytes: " + str(process.memory_info().private))
        sleep(1)
    except psutil.NoSuchProcess:
        print("Proccess exited.")
        break
        