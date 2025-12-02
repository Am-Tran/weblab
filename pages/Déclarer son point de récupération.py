import streamlit as st

st.title("Bienvenue sur le site web de TADAM")


location = st.selectbox("Indiquez votre arrondissement de récupération",
             ['Manhattan', 'Bronx', 'Queens', 'Autre']) 
st.write('___')

st.text(f"Tu as choisi: {location}")

st.markdown("<break>", unsafe_allow_html=True)

if location == 'Manhattan':
    st.image("https://images.ctfassets.net/1aemqu6a6t65/2PNzt4fJkl0Y34ko5d2FOf/50453d858cd38d2d5396bc2fcfb15595/Time-Square-Manhattan-NYC-Photo-Courtesy-Timelapse-Company-1.jpg") 
elif location == 'Bronx':
    st.image("https://thegoodlife.fr/wp-content/thumbnails/uploads/sites/2/2016/03/TGL-P-022-188-V-H-06-tt-width-2000-height-1282-fill-0-crop-0-bgcolor-eeeeee.jpg")
elif location == 'Queens':
    st.image("https://content.r9cdn.net/rimg/dimg/94/0b/176edc87-city-47598-177452c7f24.jpg?crop=true&width=1366&height=768&xhint=3839&yhint=3164")
else:
    st.image("https://cdn-icons-png.flaticon.com/512/9908/9908159.png")

st.markdown("<break>", unsafe_allow_html=True)



