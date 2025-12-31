## vllmChat
I have been looking to learn vllm for a while, this is me doing that. I have created a simple interface for chatting with models. Currently it uses **Google's** *Gemma3-1b-it*.

I want to make a simple model runner and chat client like Ollama to learn the vLLM tooling. Ideally I will integrate the same kinds of MCP support and RAG features I've built out with other higher level libraries. 

---

`Current Features`:
- Turn based chat
- Simple in-memory conversation history
- Commands to see chat history, clear chat history, model parameters, and availible models *from HuggingFace*
- Simple logging backend *(built from the ground up rather than using standard libraries for practice)*

`Features to come`:
- Model selection
- DB for memory / RAG
- More chat information

---

### Project Layout
```bash
vllmChat
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    └── src/
        ├── helpers.py
        ├── logger.py
        ├── main.py
        └── parameters.py
```
