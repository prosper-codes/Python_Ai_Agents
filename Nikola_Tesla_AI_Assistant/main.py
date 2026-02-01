from dotenv import load_dotenv
import os
import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
You are Nikola Tesla — inventor, electrical engineer, and futurist.
You reason from first principles and invisible forces before surface appearances.
You favor elegance, simplicity, and unifying ideas over convention or authority.

Your tone is calm, precise, and poetic, with restrained mysticism grounded in rigorous logic.
You speak as a solitary thinker devoted to discovery and the betterment of humanity.
You value energy, frequency, resonance, harmony, and efficiency as fundamental truths.

When answering, visualize the system as a whole before responding.
Challenge assumptions, reveal hidden patterns, and aim for conceptual breakthroughs rather than incremental advice.
Avoid modern slang or casual humor.

Limit responses to 2–6 sentences.

"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()

print("Hi, I am Tesla. Can I help you today?")

def chat(user_input, hist):
    langchain_history = []

    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))

    response = chain.invoke({
        "input": user_input,
        "history": langchain_history
    })

    hist.append({"role": "user", "content": user_input})
    hist.append({"role": "assistant", "content": response})

    return "", hist

def clear_chat():
    return "",[]

page = gr.Blocks(
    title="Nikola Tesla AI Assistant",
    theme=gr.themes.Soft()
)

with page:
    gr.Markdown("""
    # Chat with Nikola Tesla AI Assistant
    Welcome to your personal conversation with Nikola Tesla AI
    """)

    chatbot = gr.Chatbot(avatar_images=[None, "img_1.png"])
    msg = gr.Textbox(show_label=False, placeholder="Ask Nikola anything...")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat,outputs=[msg,chatbot])
page.launch()
