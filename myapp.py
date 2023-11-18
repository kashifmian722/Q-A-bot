import streamlit as st
from cohere import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Cohere client
co = Client(os.getenv('COHERE_API_KEY'))

def co_chat(message, model, temperature, chat_history, prompt_truncation, connectors, documents):
    response = co.chat(
        message=message,
        model=model,
        temperature=temperature,
        chat_history=chat_history,
        prompt_truncation=prompt_truncation,
        connectors=connectors,
        documents=documents,
    )
    return response

message = st.text_input("Enter your message:")

# Define the chat history
chat_history = [
    {"user_name": "User", "text": message},
]

# Define the model settings
model = "command"
temperature = 0.9
prompt_truncation = "auto"

# Define the connectors and documents
connectors = [{"id": "web-search", "options": {"site": "https://myvitaminstore.pk"}}]
documents = []

# Get the response
response = co_chat(
    message=message,
    model=model,
    temperature=temperature,
    chat_history=chat_history,
    prompt_truncation=prompt_truncation,
    connectors=connectors,
    documents=documents,
)

# Stream each message
for msg in response.messages:
    if msg.role == "system":
        st.write(f"System: {msg.content}")
    elif msg.role == "assistant":
        st.write(f"Chatbot: {msg.content}")
    else:
        st.write(f"User: {msg.content}")
