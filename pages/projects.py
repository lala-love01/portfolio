import streamlit as st
from data import PROJECTS, all_tags, filter_projects

st.title("Mes projets")

options = all_tags(PROJECTS)

chosen = st.multiselect("Filter by tag ",options)

filtered = filter_projects(PROJECTS, chosen)

sort_order = st.selectbox("sort project by year",["Most recent first","Oldest first"])

if sort_order == "Most recent first":
    filtered = sorted(filtered, key=lambda p: p["year"], reverse=True)
else:
   filtered = sorted(filtered, key=lambda p: p["year"], reverse=False)
   
st.write(f"{len(filtered)} projet(s) trouvé(s)")

columns = st.columns(2)

for i, project in enumerate(filtered):
    with columns[i % 2]:
        with st.container(border=True):
            st.subheader(project["title"])
            st.write(project["description"])
            st.write("Tags :",",".join(project["tags"]))
            st.caption(project["year"])
            st.link_button("see the code", url=project["link"])
            

   