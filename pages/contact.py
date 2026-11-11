import streamlit as st
import pandas as pd
import csv
import os

from datetime import datetime
from data import PROFILE

st.title("CONTACT")

def check(name, email, message):
    problems = []
    
    if not name.strip():
        problems.append("Name is required.")
    if "@" not in email or "." not in email.split("@")[-1]:
        problems.append("Invalid mail address.")
    if len(message)<10:
        problems.append("Message must contain at least 10 characters.")
    return problems

def save(name, email, message):
    date = datetime.now().strftime("%d-%m-%Y  %H-%M-%S")
    file_exists = os.path.exists("message.csv")
    with open("message.csv", "a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        if not file_exists:
            writer.writerow(["date","name","email","message"])
        writer.writerow([date,name,email,message])
        
with st.form("contact"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")
    sent = st.form_submit_button("Send")       # True only on the run that follows the click
if sent:
    problems = check(name, email, message)
    if problems:
        for problem in problems:
            st.error(problem)
    else:
        save(name, email, message)
        st.success("Your message has been sent successfully!")
st.title("My location")  
st.divider()      
st.markdown(f"**{PROFILE['city']}**")
location = pd.DataFrame({"latitude":[47.322047],"longitude":[5.04148]})
st.map(location, zoom=12, use_container_width=True)