import streamlit as st
from langchain_community.llms import Ollama

# Initialize Llama3 via Ollama
llm = Ollama(model="llama3")

# Function for summarization
def summarize_text(text):
    prompt = f"""
    You are an expert summarizer.
    Summarize the following text in 5 bullet points in simple language.

    Text:
    {text}
    """
    return llm.invoke(prompt)

# -----------------------
# STREAMLIT UI
# -----------------------
st.title("🧠 AI Text Summarizer (Llama3 + Ollama)")

# User input box
user_text = st.text_area("Enter your text here")

# Button
if st.button("Summarize"):
    if user_text.strip() != "":
        result = summarize_text(user_text)
        st.subheader("Summary")
        st.write(result)
    else:
        st.warning("Please enter some text first.")