import streamlit as st

from data import PROFILE, PROJECTS, SKILLS

st.title(f"Bonjour, je suis {PROFILE['name']}")
# st.title(f"Hi, I'm {PROFILE['name']}")
st.subheader(PROFILE["title"])
left, right = st.columns([1, 2])

with left:
    st.image("assets/lala.png", width=220)
    
with right:
    st.write(PROFILE["about"])
    st.write(PROFILE["city"])
    st.write(PROFILE["email"])
    st.link_button("Send me a mail",f"https://mail.google.com/mail/?view=cm&fs=1&to={PROFILE['email']}")
    
    with open("assets/cv.pdf", "rb") as f:
        st.download_button("Télécharger mon CV", f, file_name="cv.pdf")
    #   st.download_button("Download my CV", f, file_name="cv.pdf")
    
st.divider()
    
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Nombre de projets", len(PROJECTS))
with col2:
    st.metric("Nombre de compétences", len(SKILLS))
    
meilleur_competence = ""
meilleur_score = 0 
    
for competence, score in SKILLS.items():
    if score > meilleur_score:
         meilleur_score = score
         meilleur_competence = competence

with col3:
    st.metric("Meilleur Compétence", meilleur_competence)        
