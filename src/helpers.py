# author : Seamus Jackson 

# Helper functions to be called elsewhere

from parameters import MODEL, MODEL_TEMP, TOP_P, SPECIAL_CHARS, SYSTEM_PROMPT
from logger import write_log, read_logs

from huggingface_hub import scan_cache_dir

def clear_chat() -> list:
    """
    Clears chat history
    """
    try:
        chat_history=[{"role": "system", "content": SYSTEM_PROMPT}]
        return chat_history
    
    except Exception as e:
        write_log(f"Error: {e}")
        return[]
    
def list_models() -> None:
    """
    Lists availible cached huggingface models
    """
    try:
        model_cache = scan_cache_dir()

        count = 1
        for repo in model_cache.repos:
            if repo.repo_type == "model":
                print(f"{count}. {repo.repo_id}")
                count += 1

        write_log(f"Model query - count : {count}")

    except Exception as e:
        write_log(f"Error: {e}")

def view_history(chat_history) -> None:
    """
    Displays message history in a human-readable format
    """
    try:
        count = 0
        for message in chat_history:
            role = message.get("role", "N/A")
            content = message.get("content", "N/A")
            print(f"{count}. {role}: {content}\n")
            count += 1

    except Exception as e:
        write_log(f"Error: {e}")

def handle_commands(prompt, chat_history):
    """
    Runs different commands
    """
    # different commands
    # TODO : More elegant handling here 
    try:
        match prompt:
            case "/h":
                view_history(chat_history)
            case "/c":
                chat_history = clear_chat()
                write_log("Chat cleared")
                print("History cleared")
            case "/q":
                write_log("Shutting down now.")
                exit()
            case "/p":
                print(f"Model: {MODEL}\nTemperature: {MODEL_TEMP}\nTop P: {TOP_P}")
            case "/models":
                list_models()
            case "/logs":
                print("Displaying logs:\n")
                read_logs()
            case "help":
                help_menu(SPECIAL_CHARS)
                
        return chat_history
    
    except Exception as e:
        write_log(f"Error: {e}")

def help_menu(options) -> None:
    """
    displays command options
    """
    try:
        for k,v in options.items():
            print(f"{k}: {v}")
            
    except Exception as e:
        write_log(f"Error: {e}")
    
