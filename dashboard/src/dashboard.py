import streamlit as st

# Titre du tableau de bord
st.title('Tableau de bord de la ferme urbaine')

# Exemple de visualisation
st.header('Visualisation en temps réel')
st.line_chart([20, 30, 40, 50, 60, 70])

# Afficher quelques données
st.header('Dernières données reçues')
st.write('Température: 20°C')
st.write('Humidité: 35%')

# Formulaires et interaction utilisateur
st.header('Réglages')
temperature = st.slider('Choisir la température idéale', min_value=10, max_value=35, value=25)
st.write(f'Température idéale réglée sur: {temperature}°C')
