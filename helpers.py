def clear_chat()->list:
    """
    Clears chat history
    """
    chat_history=[]
    return chat_history

def help_menu(options)->None:
    """
    displays command options
    """
    for k,v in options.items():
        print(f"{k}: {v}")
    
