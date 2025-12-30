# Model params
# Kinda weird in its own python file
# we will see what happens, its clean

MODEL_TEMP = 0.65
TOP_P = 0.95
MAX_VRAM = 0.5
MAX_TOKENS = 250

#MODEL= "facebook/opt-125m"
MODEL= "google/gemma-3-1b-it"
SYSTEM_PROMPT = "You are a helpful assistant. Answer helpfully and honestly."

SPECIAL_CHARS = {
    "help" : "Show help menu",
    "/h" : "History",
    "/c" : "Clear history",
    "/p" : "Model parameters",
    "/logs" : "Print program logs",
    "/models" : "Lists availible models from HF",
    "/q" : "Quit",
}

LOG_FILE = "status.log"