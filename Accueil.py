import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
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
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)


def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")

# --- 2. GESTION DE LA CONNEXION ---
# Affiche le formulaire de login (et rien d'autre pour l'instant)

authenticator.login()

# --- 3. CONTENU PROTÉGÉ ---
if st.session_state["authentication_status"]:
    with st.sidebar:
    # Le bouton de déconnexion
        st.write(f"Connecté en tant que : {st.session_state['name']}")
        authenticator.logout("Déconnexion")
    
    # B. Le Menu (Visible uniquement si connecté)
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"],
        orientation="horizontal"
    )

    # C. Les Pages (Visibles uniquement si connecté)
    if selection == "Accueil":
        accueil()

    elif selection == "Photos":
        st.subheader("Album Photo Privé")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://static.streamlit.io/examples/cat.jpg", caption="Chat")
        with col2:
            st.image("https://static.streamlit.io/examples/dog.jpg", caption="Chien")
        with col3:
            st.image("https://static.streamlit.io/examples/owl.jpg", caption="Hibou")

# --- 4. GESTION DES ERREURS DE CONNEXION ---
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez vous connecter pour accéder aux photos.')







