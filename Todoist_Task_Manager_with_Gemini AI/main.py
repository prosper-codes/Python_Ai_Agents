from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import  tool
from langchain.agents import create_openai_tools_agent,AgentExecutor
from todoist_api_python.api import TodoistAPI
load_dotenv()

todolist_api_key= os.getenv("TODOLIST_API_KEY")
gemini_api_key= os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todolist_api_key)


@tool
def add_todo(todo):
    """ add a new task to the todolist .Use this when the user wants to add or create a task"""
    todoist.add_task(content=todo)


@tool
def show_todos():
    """ show the todos for Todoist. Use this tool when the user wants see their todos """
    results_paginator = todoist.get_tasks()
    todos=[]
    for todo_list in results_paginator:
        for todo in todo_list:
            todos.append(todo.content)
    return todos


tools=[add_todo]

llm =ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_api_key,
    temperature=0.3,
    streaming=False,
)

system_prompt = """You are a helpful assistant. You will help user add tasks
                you will help the user show their existing tasks. If the user asks to show the tasks: for example, 
                "show me the tasks" print out the tasks to the user. Print them un bullet form
"""
user_input = "i want to run 2km"

prompt = ChatPromptTemplate([
    ("system",system_prompt),
    MessagesPlaceholder("history"),
    ("user","{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])


# chain = prompt | llm | StrOutputParser()
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=False)

# response = chain.invoke({"input":user_input})




history =[]

while True:
    user_input = input("You: ")
    response = agent_executor.invoke({"input": user_input,"history":history})
    print(response['output'])
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response["output"]))


