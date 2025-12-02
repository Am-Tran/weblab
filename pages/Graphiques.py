import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng
from streamlit_authenticator import Authenticate

# --- 1. CONFIGURATION ---
# --- CHARGEMENT DES UTILISATEURS DEPUIS LE CSV ---
try:
    # 1. On lit le fichier CSV
    df_users = pd.read_csv('users.csv')

    # 2. On convertit le tableau Pandas en dictionnaire pour l'authenticator
    # L'astuce : on utilise la colonne "name" comme clé principale
    users_dict = df_users.set_index('name', drop=False).to_dict(orient='index')

    # 3. On remet ça dans la structure attendue : {'usernames': ...}
    lesDonneesDesComptes = {'usernames': users_dict}

except FileNotFoundError:
    st.error("Le fichier users.csv est introuvable. Veuillez lancer create_users.py d'abord.")
    st.stop()

authenticator = Authenticate(
    lesDonneesDesComptes,  
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# --- 2. VÉRIFICATION DE SÉCURITÉ ---
if st.session_state.get("authentication_status") is not True:
    st.warning("Veuillez vous connecter sur la page d'accueil.")
    st.stop() # Arrête le chargement du reste de la page

# --- 3. LE BOUTON DANS LA SIDEBAR ---
with st.sidebar:
    st.write(f"Connecté : {st.session_state['name']}")
    authenticator.logout("Déconnexion")

# --- 4. Graphiques ---

st.title("Manipulation de données et création de graphiques")

choix_dataset = st.selectbox("Quel dataset veux-tu utiliser",
             ['Taxis', 'Autre'])
st.markdown("<break>", unsafe_allow_html=True)

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)
df = df.drop(["pickup", "dropoff", "color"], axis = 1)
st.dataframe(df)

axe_x = st.selectbox("Choisis l'axe X", df.columns)
axe_y = st.selectbox("Choisis l'axe Y", df.columns)
type_graph = st.selectbox("Quel graphique veux-tu utiliser?", 
                          ["bar_chart", "scatter_chart", "line_chart"])
fonction_graphique = getattr(st, type_graph)
st.markdown("<break>", unsafe_allow_html=True)
                             
st.write(f"Graphique : {axe_y} en fonction de {axe_x}")
fonction_graphique(df, x=axe_x, y=axe_y)
st.markdown("<break>", unsafe_allow_html=True)

show_corr = st.checkbox("Afficher la matrice de corrélation")
st.markdown("<break>", unsafe_allow_html=True)

if show_corr:
    st.header("Ma matrice de corrélation")
    st.markdown("<break>", unsafe_allow_html=True)
    corr = df.corr(numeric_only = True)
    fig, ax = plt.subplots()
    sns.heatmap(corr, cmap = "Spectral")
    st.pyplot(fig)

