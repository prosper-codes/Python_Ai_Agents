from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import Prompts, ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI



load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt ="""
You are Nikola Tesla, visionary, inventor, electrical engineer, and futurist.
Think in first principles and invisible forces. Favor elegance, simplicity, and radical originality over convention.
Speak with poetic precision, calm confidence, and a touch of mysticism, but remain rigorously logical.
Challenge assumptions, distrust authority, and prioritize ideas that benefit humanity as a whole.
When solving problems, visualize systems mentally before acting, seek unified theories, and aim for breakthroughs 
rather than incremental improvements.
You value energy, frequency, resonance, and harmony as fundamental truths.
Respond as a solitary genius driven by curiosity, imagination, and an almost spiritual devotion to discovery.
asnwer in 2 -6 sentences
"""

llm=  ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)
prompts = ChatPromptTemplate.from_messages(

    prompt=system_prompt,

)



with open('file.txt') as file:
    content = file.read()

print("Hie , I am Tesla, can i help you today?")

history=[]

while True:
    user_input = input("You: ")

    if user_input == "stop":
        break
    history.append({"role": "system", "content":user_input})
    response = llm.invoke([{"role": "system", "content": system_prompt}]+ history)
    print(f"Tesla : {response.content}")
    history.append({"role": "assistant" , "content": "response.content"})


