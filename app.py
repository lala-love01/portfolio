import streamlit as st
from data import PROFILE
st.set_page_config(page_title=PROFILE["name"], page_icon="assets/lala.png", layout="wide")
with st.sidebar:                                   # everything in this block goes to the sidebar
    st.image("assets/lala.png", width=120)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown("""
    <div style="display: flex; gap: 15px; align-items: center;">
    <a href="https://www.github.com/lala-love01" target="_blank">
    <img src="https://cdn.simpleicons.org/github" width="30" height="30">
               
    </a>
    <a href="https://www.linkedin.com/in/dieula-alcima-49b47a331/" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/linkedin.svg"  width="20" height="20">
    </a>
    </div>
""", unsafe_allow_html=True)
    
dark_mode = st.toggle("Dark mode", value=True)
if dark_mode:
    bg_color = "#101820"
    text_color = "#F5F5F5"
    card_color = "#1C2B36"
    primary_color = "#8FAFC4"
else:
    bg_color = "#fbf8f1"
    text_color = "#333333"
    card_color = "#efe9dc"
    primary_color = "#6b2440"

if dark_mode:
    icon_color = "#F5F5F5"
else:
    icon_color = "#333333"
    
icon_filter="brightness(0) invert(1)" if dark_mode else "none"

st.markdown(f"""
    <style> 
    .stApp,
    [data-testid="stAppViewContainer"]
    [data-testid="stMain"], section.main, .main,
    [data-testid="stMainBlockContainer"] {{
        background-color: {bg_color}!important;
    }}
    [data-testid="stSidebar"] {{
        background: {card_color}!important;
    }}
    .stApp h1, 
    .stApp h2, 
    .stApp h3, 
    .stApp p, 
    .stApp label{{ color: {text_color}!important; }} 
    .stApp a, .stApp a {{ color: {primary_color}!important; }}
    
    [data-testid="stSidebar"] svg{{
        color: {icon_color}!important;
        fill: {icon_color}!important;
    }}
    [data-testid="stSidebar"] a img {{
        filter: {icon_filter};
    }}
    [data-testid="stMainBlockContainer]{{
        padding-top: 1rem !important;
    }}
    [data-testid="stHeader"] {{
        background: {bg_color}!important;
    }}
    [data-testid="stToolbar"] {{
        background: {bg_color}!important;
    }} 
    [data-testid="stMain"] {{
        background: {bg_color}!important;
    }}
    </style>
""", unsafe_allow_html=True)

# languages=st.select_slider("Francais / English", options=["fr", "en"], value="fr")

    
pages = [st.Page("pages/acceuil.py", title="Home", icon=":material/home:", default=True),
         st.Page("pages/home.py", title="About me", icon=":material/person:"),
         st.Page("pages/projects.py", title="Projects", icon=":material/code:"),
         st.Page("pages/skills.py", title="Skills", icon=":material/bar_chart:"),
         st.Page("pages/contact.py", title="Contact", icon=":material/mail:")]
st.navigation(pages).run()                         # shows the menu and runs the chosen page