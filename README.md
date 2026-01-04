# modAi

Personal project made to **experiment with agent-like behavior**, function calling, and iterative prompting using the **Google Gemini API**.

This is not meant to be a robust CLI tool or a general-purpose assistant, **MUST NOT BE USED IF YOU DON'T KNOW WHAT YOU DOING**.
It exists mainly as a playground to explore how tool calls, system prompts, and feedback loops behave.

## What it is

A minimal command-line program that:
- Sends a user prompt to a Gemini model
- Allows the model to call predefined functions
- Feeds function responses back into the conversation
- Iterates until a final text response is produced or a limit is reached

The control flow is intentionally explicit and iterative to keep behavior observable.

## Core ideas explored

- Tool / function calling  
- System prompt steering  
- Message accumulation across turns  
- Verbose inspection of model behavior  
- Simple retry / iteration loop  

## How it works (high level)

1. User provides a prompt via CLI  
2. Prompt is sent to the model with:
   - A system prompt
   - A list of available functions
3. If the model calls a function:
   - The function is executed locally
   - The result is sent back to the model
4. Loop continues until:
   - A final text response is returned
   - A hard iteration limit is reached

## Requirements

- Python 3.x  
- Google Gemini API key  
- `python-dotenv`  

## Setup

Create a `.env` file:



```env
GEMINI_API_KEY=your_api_key_here
```

## Usage
First, you have to declare your ```WORKINGDIR``` in the ```config.py``` file

and then, you can use like this:
```
python main.py "your prompt here"
```

If you prefer seing debugging output:
```
python main.py "your prompt here" --verbose
```

## Notes
- Error handling is minimal by design
- Iteration count is hard-limited
- Naming and behavior are intentionally informal
- The goal is learning and inspection, not reliability



