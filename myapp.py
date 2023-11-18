import streamlit as st
import cohere
from dotenv import load_dotenv
import os

load_dotenv()

co = cohere.Client

@st.cache(persist=True)
def co_chat(message, model, temperature, chat_history, prompt_truncation, stream, citation_quality, connectors, documents):
    co = cohere.Client(os.getenv('COHERE_API_KEY'))
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

response = co_chat(
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

st.markdown(response)
