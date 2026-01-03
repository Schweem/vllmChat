# author : Seamus Jackson 

# Helper functions to be called elsewhere

from parameters import MODEL, MODEL_TEMP, TOP_P, SPECIAL_CHARS, SYSTEM_PROMPT
from logger import write_log, read_logs

from huggingface_hub import scan_cache_dir

def clear_chat() -> list:
    """
    Clears chat history to fresh state. 
    Retains system prompt.
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

        count : int = 0
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

    ---
    - chat_history - list object containing chat message dictionaries
    """
    try:
        count : int = 0

        for message in chat_history:
            role = message.get("role", "N/A")
            content = message.get("content", "N/A")

            print(f"{count}. {role}: {content}\n")
            count += 1
        write_log(f"{count} {"messages" if count > 1 else "message"} retrieved", 2)

    except Exception as e:
        write_log(f"Error: {e}")

def handle_commands(prompt, chat_history):
    """
    Runs different commands

    ---
    - prompt - input message string 
    - chat_history - list object containing chat message dictionaries
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
            case "/q" | "quit" | "bye":
                write_log("Bye.", 3)
                exit()
            case "/p":
                write_log(f"Checked settings")
                print(f"Model: {MODEL}\nTemperature: {MODEL_TEMP}\nTop P: {TOP_P}")
            case "/models":
                list_models()
            case "/logs":
                write_log(f"Checked logs")
                read_logs()
            case "help":
                write_log(f"Checked settings")
                help_menu(SPECIAL_CHARS)
                
        return chat_history
    
    except Exception as e:
        write_log(f"Error: {e}")

def help_menu(options) -> None:
    """
    displays command options

    ---
    - options - list of values to be displayed
    """
    try:
        for k,v in options.items():
            print(f"{k}: {v}")
            
    except Exception as e:
        write_log(f"Error: {e}")

def abbreviate(content : str) -> str:
    try:
        return f"{content[:10]} {"..." if len(content) > 10 else "."}"
    except Exception as e:
        print(f"Error: {e}")
        return f"{e}"