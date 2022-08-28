# task_manager

--- task manager like project ---

The script starts a process determined by
the user by entering the full path. After that,
the user is prompted to enter the interval in seconds
at which the information is collected. The
information is written in a .csv file which
can be overwritten at the next run. Check 
the notes below.


Notes:

- the process path must be absolute
- csv path is defaulted to C:/Temp/log.csv
- the user will be prompted to choose 
another path for the process if 
the access is denied or the path is incorrect
- there is also a Linux version 
of this application located on the Linux branch
