import sys
import os

from datetime import datetime

LOG_FILE = "status.log"

def write_log(msg : str)->None:
    """
    Writing my own logging stuff for no good reason
    """
    try:
        print(f"Logging: {msg}")
        with open(LOG_FILE, "a") as file:
            file.write(str(datetime.now()) + " : " + msg + "\n")

    except Exception as e:
        print(f"Error logging: {e}")

def read_logs()->None:
    """
    Read in the log file. 
    Good for passing to LLM context or just viewing
    """
    try:
        print("Pulling in logs...")
        with open(LOG_FILE, "r") as file:
            contents = file.read()
            print(contents)

    except Exception as e:
        print(f"Error reading in logs: {e}")