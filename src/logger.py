# author : Seamus Jackson 

# Simple logging backend for a paper trail

import sys
import os

from datetime import datetime
from parameters import LOG_FILE

class Levels:
    """
    ANSI escape codes for logging levels
    """
    GREEN = '\033[92m'    # 1
    YELLOW = '\033[93m'   # 2
    RED = '\033[91m'      # 3
    ENDC = '\033[0m'      # clear

def write_log(msg : str, level : int = 1) -> None:
    """
    Writing my own logging stuff for no good reason
    """
    match level:
        case 1:
            color = Levels.GREEN
        case 2: 
            color = Levels.YELLOW
        case 3:
            color = Levels.RED

    try:
        print(f"{color}Logging{Levels.ENDC}: {msg}")
        with open(LOG_FILE, "a") as file:
            file.write(str(datetime.now()) + " : " + msg + "\n")

    except Exception as e:
        print(f"{Levels.RED}!!! Error logging: {e} !!!{Levels.ENDC}")

def read_logs() -> None:
    """
    Read in the log file. 
    Good for passing to LLM context or just viewing
    """
    try:
        print(f"{Levels.GREEN}Pulling in logs{Levels.ENDC}")
        with open(LOG_FILE, "r") as file:
            contents = file.read()
            print(contents)

    except Exception as e:
        print(f"{Levels.RED}!!! Error reading in logs: {e} !!!{Levels.ENDC}")