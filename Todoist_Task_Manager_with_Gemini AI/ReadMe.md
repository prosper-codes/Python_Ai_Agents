

---

# Todoist Task Manager with Gemini AI

This project is a Python-based AI assistant that integrates **Todoist** and **Google Gemini AI** to help users manage their tasks. The assistant can add tasks to your Todoist account and show existing tasks using natural language commands.

---

## Features

* Add new tasks to Todoist using natural language.
* Show existing Todoist tasks.
* Interactive command-line interface powered by **Google Gemini AI**.
* Maintains conversation history for context-aware responses.

---

## Requirements

* Python 3.10+
* Todoist account
* Google Cloud account for Gemini API

---

## Installation

1. **Clone the repository**

```bash
git clone (https://github.com/prosper-codes/Python_Ai_Agents.git)
cd Todoist_Task_Manager_with_Gemini AI
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

**`requirements.txt` should include:**

```
python-dotenv
langchain-core
langchain-google-genai
todoist-api-python
```

3. **Set up environment variables**

Create a `.env` file in the project root:

```
TODOLIST_API_KEY=your_todoist_api_key
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## Usage

Run the script:

```bash
python main.py
```

You will see a prompt:

```
You:
```

Type natural language commands, for example:

* `I want to run 2km` → Adds a task to Todoist.
* `Show me my tasks` → Displays all your current Todoist tasks.

The AI will respond with confirmations and display your tasks when requested.

---

## How It Works

1. **Todoist Integration**

* Uses `todoist_api_python` to interact with Todoist tasks.
* `add_todo` tool adds tasks.
* `show_todos` tool retrieves all tasks.

2. **AI Integration**

* Uses `ChatGoogleGenerativeAI` (Gemini) from LangChain.
* The AI processes user input and decides whether to add a task or show tasks.
* Maintains conversation history to provide contextually relevant responses.

3. **Agent Execution**

* The LangChain agent maps natural language to the correct tools (`add_todo` or `show_todos`).
* The agent executor handles interaction between the AI and the tools.

---

## Example Interaction

```
You: I want to run 2km
AI: Added "I want to run 2km" to your Todoist tasks.

You: Show me my tasks
AI:
1. I want to run 2km
2. Buy groceries
3. Finish project report
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

MIT License

---

