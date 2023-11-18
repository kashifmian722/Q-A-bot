import streamlit as st
from cohere import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Cohere client
co = Client(os.getenv('COHERE_API_KEY'))

@st.cache(persist=True)
def co_chat(message, model, temperature, chat_history, prompt_truncation, stream, citation_quality, connectors, documents):
    response = co.chat(
        model=model,
        message=message,
        temperature=temperature,
        chat_history=chat_history,
        prompt_truncation=prompt_truncation,
        stream=stream,
        citation_quality=citation_quality,
        connectors=connectors,
        documents=documents,
    )
    return response

message = st.text_input("Enter your message:")

# Get the response as a list of messages
response_messages = co_chat(
    message=message,
    model="command",
    temperature=0.3,
    chat_history=[],
    prompt_truncation="auto",
    stream=True,
    citation_quality="accurate",
    connectors=[{"id": "web-search", "options": {"site": "https://myvitaminstore.pk"}}],
    documents=[],
)

# Stream each message
for msg in response_messages:
    st.markdown(msg["text"], unsafe_allow_html=False)  # Display chatbot response
