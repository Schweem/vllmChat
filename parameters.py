# Model params
# Kinda weird in its own python file
# we will see what happens, its clean

MODEL_TEMP = 0.65
TOP_P = 0.95

#MODEL= "facebook/opt-125m"
MODEL= "google/gemma-3-1b-it"

SPECIAL_CHARS = {
    "help" : "Show help menu",
    "/h" : "History",
    "/c" : "Clear history",
    "/p" : "Model parameters",
    "/q" : "Quit",
}