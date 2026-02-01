

# ⚡ Nikola Tesla AI Assistant

A conversational AI inspired by **Nikola Tesla** — visionary inventor, electrical engineer, and futurist.
This project uses **LangChain**, **Google Gemini**, and **Gradio** to simulate Tesla’s distinctive reasoning style: first-principles thinking, poetic precision, and an obsession with energy, frequency, and harmony.

---

## ✨ Features

* 🧠 **Persona-driven AI**
  Carefully engineered system prompt to emulate Tesla’s mindset and communication style.

* 🔗 **LangChain-powered memory**
  Maintains conversational context using structured message history.

* 💬 **Interactive chat UI**
  Built with Gradio for fast, clean, browser-based conversations.

* ⚡ **Google Gemini (2.5 Flash)**
  Fast, high-quality responses with controllable creativity.

---

## 🏗️ Tech Stack

* **Python 3.10+**
* **LangChain**
* **Google Gemini API**
* **Gradio**
* **python-dotenv**

---

## 📁 Project Structure

```
.
├── main.py              # Main application
├── .env                # Environment variables
├── img_1.png           # Tesla avatar
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 📦 Installation

```bash
git clone https://github.com/prosper-codes/Python_Ai.git
cd nikola-tesla-ai
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:7860
```

---

## 🧠 How It Works

1. A **system prompt** defines Tesla’s personality, values, and reasoning style.
2. User messages and assistant replies are converted into LangChain message objects.
3. The prompt, history, and user input are sent to Gemini.
4. Responses are parsed and displayed in the Gradio chat interface.

Tesla does not merely answer — he *reveals patterns*.

---

## 🎛️ Customization

You can easily:

* Adjust **temperature** for more or less creativity
* Modify the **system prompt** for stricter logic or more mysticism
* Add **streaming responses** or **long-term memory**
* Swap personas (Einstein, Da Vinci, Turing…)

---

## ⚠️ Disclaimer

This project is a **creative AI simulation** inspired by Nikola Tesla.
It is not intended to represent his actual words, beliefs, or historical views.

---

## 🌌 Philosophy

> “If you wish to understand the universe, think in terms of energy, frequency, and vibration.”

This project is an experiment in that spirit.


