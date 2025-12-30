from parameters import MODEL, MODEL_TEMP, TOP_P, SPECIAL_CHARS, SYSTEM_PROMPT
from logger import write_log

def clear_chat()->list:
    """
    Clears chat history
    """
    try:
        chat_history=[{"role": "system", "content": SYSTEM_PROMPT}]
        return chat_history
    except Exception as e:
        print(f"Error: {e}")
        return[]

def handle_commands(prompt, chat_history):
    """
    Runs different commands
    """
    # different commands
    # TODO : More elegant handling here 
    try:
        match prompt:
            case "/h":
                print(chat_history)
            case "/c":
                chat_history = clear_chat()
                write_log("Chat cleared")
                print("History cleared")
            case "/q":
                exit()
            case "/p":
                print(f"Model: {MODEL}\nTemperature: {MODEL_TEMP}\nTop P: {TOP_P}")
            case "help":
                help_menu(SPECIAL_CHARS)
                
        return chat_history
    except Exception as e:
        print(f"Error: {e}")

def help_menu(options)->None:
    """
    displays command options
    """
    try:
        for k,v in options.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")
    
