# author : Seamus Jackson 

# Simple vLLM test implementation
# Loads facebook opt-125m into a simple, 
# conversational chat-like interface.

from vllm import LLM, SamplingParams

# offload helpers to secondary file
from helpers import clear_chat, help_menu

# Model params
# Might move to another file, not that bad having it here 
MODEL_TEMP = 0.1
TOP_P = 0.95

MODEL= "facebook/opt-125m"

SPECIAL_CHARS = {
    "help" : "Show help menu",
    "/h" : "History",
    "/c" : "Clear history",
    "/p" : "Model parameters",
    "/q" : "Quit",
}

# TODO : Make this not a list
chat_history = []   

def chat(llm, sampling_params, chat_history)->None:
    """
    Main chat method
    """
    prompt = input("Prompt: ")

    if prompt in SPECIAL_CHARS:
        # different commands 
        # TODO : More elegant handling here 
        match prompt:
            case "/h":
                print(chat_history)
            case "/c":
                chat_history = clear_chat()
                print("History cleared")
            case "/q":
                exit()
            case "/p":
                print(f"Temperature: {MODEL_TEMP}\n Top P: {TOP_P}")
            case "help":
                help_menu(SPECIAL_CHARS)

        chat(llm, sampling_params, chat_history)
    else: 
        outputs = llm.generate(prompt, sampling_params)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            chat_history.append(generated_text)

            print(f"Response: {generated_text}")
            
        chat(llm, sampling_params, chat_history)

def main()->None:
    """
    Entry point
    """
    # model params 
    sampling_params = SamplingParams(temperature=MODEL_TEMP, top_p=TOP_P)
    llm = LLM(model=MODEL)

    # Initial chat entry, no longer a loop    
    chat(llm, sampling_params, chat_history)

main()
