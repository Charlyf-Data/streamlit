import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import json


with open("utilisateurs.json", "r") as file:
    user_data = json.load(file)



authenticator = Authenticate(user_data, "cookie_name", "cookie_key", 30)

authenticator.login()

def accueil():
    st.title("🐧Bienvenu sur le contenu réservé aux utilisateurs connectés🐧")
    st.image("pingouin.png")
    
    
    

def photos_oiseaux():
    st.title("Mes plus belles photos de profil")
    cols = st.columns(3)
    with cols[0]:
        st.image("potoo.png")
    with cols[1]:
        st.image("ahah.png")
    with cols[2]: 
        st.image('moi_et_monpoto.png')
      
    

if st.session_state["authentication_status"]: 
    with st.sidebar:
        authenticator.logout("Déconnexion", key = "logout_sidebar")
        selection = option_menu(
        menu_title=None,
        options =["Accueil", "Photos"],
        icons =["house", "oiseaux"],
        default_index = 0
        )  
    
    
    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        photos_oiseaux()

    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
    


