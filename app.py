import streamlit as st

# Title of the app
st.title("Mock Interviewer")

# Instructions
st.write("Welcome to the Mock Interviewer. Please fill in your details below.")

# User input fields
name = st.text_input("Name:")
email = st.text_input("Email:")

if st.button("Start Interview"):
    if name and email:
        st.success(f"Starting the interview for {name}...")
        # Here you could integrate your interview questions and logic
    else:
        st.error("Please enter your name and email to start the interview.")
