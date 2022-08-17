import subprocess
import psutil
import csv
from time import sleep


# declare process and interval variables and initialize them
process = None
interval = ""

# initialize the user path
user_path = str(input("Choose the process (enter the full path): ").strip())

# initialize the analysis interval
while interval == "":
    try:
        interval = int(input("Choose the interval of analysis (Seconds): "))
    except ValueError:
        print("Warning: Invalid value for the interval, please enter a number.")

# try to get the process pid (if the process path is validated)
while process is None:
    try:
        process = psutil.Process(subprocess.Popen(user_path.replace("\\", '/')).pid)
    except FileNotFoundError:
        print("Warning: process not found.")
        user_path = str(input("Choose the process (enter the full path): ").strip())
    except OSError:
        print("Warning: OSError encountered.")
        user_path = str(input("Choose the process (enter the full path): ").strip())


while True:
    try:
        print("Name: " + str(process.name()))
        print("Percentage of CPU drained by the process: " + str(process.cpu_percent()/psutil.cpu_count()))
        print("Number of handles: " + str(process.num_handles()))
        print("Working Set: {0}\nPrivate Bytes: {1}".format(str(process.memory_info().wset),
                                                            str(process.memory_info().private)))
        sleep(interval)
    except psutil.NoSuchProcess:
        print("Proccess exited.")
        break