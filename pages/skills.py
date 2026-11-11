import streamlit as st
import pandas as pd
from data import SKILLS, TIMELINE

st.title("Mes competences")

tab1, tab2 = st.tabs(["Skills","Education"])
with tab1:
    for skill, level in SKILLS.items():
        st.markdown(skill)
        st.progress(level/100)

df = pd.DataFrame({
    "skill": list(SKILLS.keys()),
    "level": list(SKILLS.values())
})
st.bar_chart(df,x="skill", y="level")

with tab2:
    for date, formation in TIMELINE:
        st.markdown(f"**{date}**, -{formation}")