import streamlit as st

st.title("Streamlit test widgets")

name = st.text_input("Enter your name", "Type here ...")
if name:
    st.write(f"Hello {name}")

age = st.slider("Enter your age", 0, 100, 10)
st.write(f"I see you are {age} years old")

option = st.selectbox("Choose an option", ["Raj Comix", "DC", "Marvel"])
st.write(f"You selected {option}")