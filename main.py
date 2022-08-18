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


with open('C:/Temp/log.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    header = ['name', 'cpu_percent', 'num_handles', 'wset (bytes) ', 'private_bytes']

    writer.writerow(header)
    writer.writerow('')

    while True:
        try:
            cpu_percent = round(process.cpu_percent() / float(psutil.cpu_count()), 2)
            print("Name: " + str(process.name()))
            print("Percentage of CPU drained by the process: " + str(cpu_percent))
            print("Number of handles: " + str(process.num_handles()))
            print("Working Set: {0}\n"
                  "Private Bytes: {1}".format(str(process.memory_info().wset),
                                              str(process.memory_info().private)))
            data = [process.name(),
                    cpu_percent,
                    process.num_handles(),
                    process.memory_info().wset,
                    process.memory_info().private]

            writer.writerow(data)
            sleep(interval)

        except psutil.NoSuchProcess:
            print("Proccess exited.")
            break
