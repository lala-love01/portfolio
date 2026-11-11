import pandas as pd
import streamlit as st
@st.cache_data
def load_results():
    return pd.read_csv("assets/lab_results.csv")
st.title("Resultats du TP2")
results = load_results()
st.line_chart(results, x="n", y="temps")