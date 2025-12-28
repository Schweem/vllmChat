# author : Seamus Jackson 

# Simple vLLM test implementation
# Loads facebook opt-125m into a simple, 
# conversational chat-like interface.
from vllm import LLM, SamplingParams

# offload helpers to secondary files
from helpers import handle_commands
from parameters import SPECIAL_CHARS, MODEL_TEMP, TOP_P, MODEL

# TODO : Make this not a list
chat_history = []

def store_message(role : str, content)->None:
    try:
        message = {"role":role, "content":content}
        chat_history.append(message)
    except Exception as e:
        print(f"Error: {e}")

def chat(llm, sampling_params, chat_history)->None:
    """
    Main chat method
    """
    try:
        prompt = input("Prompt: ")

        if prompt in SPECIAL_CHARS:
            handle_commands(prompt, chat_history)

            chat(llm, sampling_params, chat_history)
            
        else:            
            #prompt = str(chat_history) + "\n\n user prompt:" + prompt
            store_message("user", prompt)
            
            outputs = llm.generate(prompt, sampling_params)
            for output in outputs:
                prompt = output.prompt
                generated_text = output.outputs[0].text
                
                print(f"Response: {generated_text}")
                store_message("model", generated_text)
                
            chat(llm, sampling_params, chat_history)
    except Exception as e:
        print(f"Error: {e}")

def main()->None:
    """
    Entry point
    """
    try:
        # model params 
        sampling_params = SamplingParams(temperature=MODEL_TEMP, top_p=TOP_P)
        llm = LLM(model=MODEL)

        # Initial chat entry, no longer a loop    
        chat(llm, sampling_params, chat_history)
    except Exception as e:
        print(f"Error: {e}")

main()