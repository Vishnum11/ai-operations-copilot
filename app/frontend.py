import streamlit as st
import requests

st.set_page_config(page_title="AI Operations Copilot", layout="wide")

st.title("AI Operations Copilot")
st.write("Free local AI agent built with LangGraph, FastAPI, SQLite, and Ollama.")

message = st.text_area("Enter customer message:")

if st.button("Send"):
    if message.strip():
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": message}
        )

        st.subheader("AI Response")
        st.write(response.json()["response"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Customers")
    try:
        customers = requests.get("http://127.0.0.1:8000/customers").json()["customers"]
        st.write(customers)
    except:
        st.write("Backend not running.")

with col2:
    st.subheader("Appointments")
    try:
        appointments = requests.get("http://127.0.0.1:8000/appointments").json()["appointments"]
        st.write(appointments)
    except:
        st.write("Backend not running.")