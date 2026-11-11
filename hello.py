import streamlit as st
print("run")
st.title("Hello!")
name = st.text_input("What is your name?")
if name:
    st.write(f"Nice to meet you, {name}.")
    
age = st.slider("Your age", 15, 70, 20)

if age <= 30:
    st.write(f"You will be 30 in {30 - age} years")
else:
    st.write("your age is over 30 years")
    
    # reponse 7 : on a small screan the column stack on top of reach
    