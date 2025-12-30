import sys
import os

from datetime import datetime

LOG_FILE = "status.log"

def write_log(msg : str)->None:
    try:
        print(f"Logging: {msg}")
        with open(LOG_FILE, "a") as file:
            file.write(str(datetime.now()) + " : " + msg + "\n")

    except Exception as e:
        print(f"Error logging: {e}")