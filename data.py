TRANSLATIONS = {
  "fr":{
    "home" : "Accueil",
    "projects" : "Projets",
    "skills" : "Compétences",
    "contact" : "Contact"
  },
  
  "en":{
   "home" : "Home",
   "projects" : "Projects",
   "skills" : "Skills",
   "contact" : "Contact"
 }
}
PROFILE = {"name": "ALCIMA Dieula", "title": "Informaticienne || Etudiante en première année de master",
           "city": "Dijon, France", "email": "dieulaalcima10@gmail.com",
           "github": "https://github.com/dieulaalcima",
           "about": "Je suis informaticienne diplômée en Sciences Informatiques actuellement en première année de Master en Sante et Intelligence Artificielle à l'Université de Bourgogne Europe. Je m'intéresse au développement informatique, l'analyse de données, et intelligence artificielle appliquée à la santé. Mon objectif est de contribuer à la conception des solutions numériques intelligentes pour améliorer les systèmes d'information hospitaliers et soutenir les professionnels de santé"}
SKILLS = {"Python": 85, "scikit-learn": 70, "SQL": 60, "Git": 65}  # niveau sur 100
PROJECTS = [
  {"title": "Morpion avec tkinter", "description": "Un jeu graphique avec un adversaire informatique.",
   "tags": ["Python", "GUI"], "year": 2026, "link": ""},
  
  {"title": "Morpion avec tkinter", "description": "Un jeu graphique avec un adversaire informatique.",
     "tags": ["Python", "GUI"], "year": 2026, "link": ""},
  
  {"title": "Morpion avec tkinter", "description": "Un jeu graphique avec un adversaire informatique.",
     "tags": ["Python", "GUI"], "year": 2026, "link": ""},
  
  {"title": "Morpion avec tkinter", "description": "Un jeu graphique avec un adversaire informatique.",
     "tags": ["Python", "GUI"], "year": 2026, "link": ""},
  # NB:je vais ajouter d'autres projets plus tard, donc je laisse les liens vides pour l'instant
]
TIMELINE = [("2026 - 2027", "Master SIA, Université Bourgogne Europe"), ("2022 - 2025", "Licence Sciences Informatiques, Universite d'Etat d'haiti Campus Henry Christophe de Limonade")]

# reponse :The data structures used are dictionaries, 
# lists, and tuples. A list of dictionaries works well for projects because the list holds several projects,
# while each dictionary groups information about one project, such as its title, description, 
# tags, year, and link.


def all_tags(projects):
  tags = set()
  for project in projects:
    for tag in project["tags"]:
      tags.add(tag)
  return sorted(tags)
print(all_tags(PROJECTS))


def filter_projects(projects, chosen):
  if not chosen:
    return projects
  
  filtered = []
  
  for project in projects:
    if any(tag in chosen for tag in project["tags"]):
      filtered.append(project)
      
  return filtered

print(filter_projects(PROJECTS, ["GUI"]))
print(filter_projects(PROJECTS, []))
