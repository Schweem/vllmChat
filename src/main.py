# author : Seamus Jackson 

# Simple vLLM test implementation
# Loads facebook gemma3-1b-it into a simple, 
# conversational chat-like interface.
from vllm import LLM, SamplingParams

# offload helpers to secondary files
from helpers import handle_commands
from parameters import SPECIAL_CHARS, MODEL_TEMP, TOP_P, MODEL, MAX_VRAM, SYSTEM_PROMPT, MAX_TOKENS
from logger import write_log

# TODO : Make this not a list
# Init with system prompt now
chat_history = [{"role": "system", "content": SYSTEM_PROMPT},]

def store_message(role : str, content)->None:
    try:
        message = {"role":role, "content":content}
        chat_history.append(message)
        write_log(f"{role} - message stored : {content[:5]}...")

    except Exception as e:
        write_log(f"Error: {e}")

def chat(llm, sampling_params, chat_history)->None:
    """
    Main chat method
    """
    try:
        prompt = input("Prompt: ")

        # Handle commands
        if prompt in SPECIAL_CHARS:
            write_log(f"Entered command: {prompt}")
            chat_history = handle_commands(prompt, chat_history)
            
            chat(llm, sampling_params, chat_history)

        # Otherwise its just a message exchange
        else:            
            write_log("User chat message")
            store_message("user", prompt)
            
            outputs = llm.chat(chat_history, sampling_params)
            for output in outputs:
                prompt = output.prompt
                generated_text = output.outputs[0].text
                
                print(f"Response: {generated_text}")
                store_message("model", generated_text)
                write_log("Model chat message")
                
            chat(llm, sampling_params, chat_history)

    except Exception as e:
        write_log(f"Error: {e}")

def main()->None:
    """
    Entry point
    """
    try:
        write_log("Init")
        # model params 
        sampling_params = SamplingParams(temperature = MODEL_TEMP,
                                         top_p = TOP_P, 
                                         max_tokens = MAX_TOKENS)
        
        llm = LLM(model=MODEL, 
                  gpu_memory_utilization=MAX_VRAM)

        # Initial chat entry, no longer a loop    
        chat(llm, sampling_params, chat_history)

    except Exception as e:
        write_log(f"Error: {e}")

if __name__ == "__main__":
    main()