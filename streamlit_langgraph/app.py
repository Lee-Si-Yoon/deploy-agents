import os
import streamlit as st
from langchain_core.messages import HumanMessage

from agent import CONVERSATION, receive_message_from_caller
from tools import APPOINTMENTS

os.environ["LANGSMITH_PROJECT"] = st.secrets["LANGSMITH_PROJECT"]
os.environ["MISTRAL_API_KEY"] = st.secrets["MISTRAL_API_KEY"]

def submit_message():
    receive_message_from_caller(st.session_state["message"])

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Appointment Manager")

    for message in CONVERSATION:
        if type(message) == HumanMessage:
            with st.chat_message("user"):
                st.write(message.content)
        else:
            with st.chat_message("assistant"):
                st.write(message.content)
    
    message = st.chat_input("Type message here", on_submit=submit_message, key="message")


with col2:
    st.header("Appointments")
    st.write(APPOINTMENTS)