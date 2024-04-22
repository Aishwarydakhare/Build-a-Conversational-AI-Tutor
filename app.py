import streamlit as st

import google.generativeai as gemini

st.set_page_config(page_title="Conversation_AI_Tutor", page_icon="🚀", layout="wide")

# Define title & Subtitle styling
title_style = {
    "color": "Black",
    "font-size": "40px",
    "font-weight": "bold",
    "text-align": "center",
    "padding": "20px"
}

subtitle_style = {
    "color": "grey",
    "font-size": "28px",
    "font-weight": "bold",
    "text-align": "center",
    "padding": "10px"
}

# Title and subtitle
st.markdown('<p style="{}">🤖 Welcome to AI Tutor </p>'.format(";".join([f"{k}:{v}" for k, v in title_style.items()])), unsafe_allow_html=True)
st.markdown('<p style="{}">🚀 Explore the Possibilities with AI </p>'.format(";".join([f"{k}:{v}" for k, v in subtitle_style.items()])), unsafe_allow_html=True)

# Configure the Gemini API
f = open(r"keys/.gemini_api_key.txt") 

api_key = f.read()

gemini.configure(api_key=api_key)
model = gemini.GenerativeModel(model_name="gemini-1.5-pro-latest",
                               system_instruction="""You are tasked to resolve only data science
                               doubts of the user.""")

# Check for messages in session 
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello,Gemini here how can I help you today?"}
    ]
    

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Receive user input
user_input = st.chat_input()

# Store user input in session
if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
# Generate AI response and display
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)
