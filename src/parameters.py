# author : Seamus Jackson 

# Model params
# Kinda weird in its own python file
# we will see what happens, its clean

# main model params
MODEL_TEMP : float = 0.65
TOP_P : float = 0.95
MAX_VRAM : float = 0.5
MAX_TOKENS : int = 250

# model to be first loaded
MODEL : str = "google/gemma-3-1b-it"

# models internal dialouge at birth
SYSTEM_PROMPT : str = "You are a helpful assistant. Answer helpfully and honestly."

# cases to be treated as commands
SPECIAL_CHARS : dict = {
    "help" : "Show help menu",
    "/h" : "History",
    "/c" : "Clear history",
    "/p" : "Model parameters",
    "/logs" : "Print program logs",
    "/models" : "Lists availible models from HF",
    "/q" : "Quit",
}

# name of output file for logging
LOG_FILE : str = "status.log"