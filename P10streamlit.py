# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:04:25 2022

@author: jordane carton
"""
import streamlit as st
import pandas as pd
import pickle

st.title("Projet 10 Carton Jordane")
st.header("Détection de faux billets")
st.markdown("Merci de faire un glisser déposer du fichier csv à analyser ensuite cliquer sur le bouton lancer le calcul")

uploaded_file = st.file_uploader("glisser votre CSV ici")
if uploaded_file is not None:
    df_res = pd.read_csv(uploaded_file, sep=',')

if st.button('Lancer le calcul'):
     
    #ouverture du modèle de régression logistique
    loaded_model = pickle.load(open('model_final.sav', 'rb'))
    #calcul du modèle
    resultat = loaded_model.predict(df_res[["diagonal","height_left","height_right","margin_low","margin_up","length"]])
    #ajout de la colone de résultat et affichage ensuite
    df_res['vrais/faux billet'] = resultat.tolist()
    st.dataframe(df_res)
     
    st.success('Calcul terminé')
    
    csv =df_res.to_csv().encode('utf-8')
    st.download_button(
        label="Télécharger le résultat en CSV",
        data=csv,
        file_name='resultat.csv',
        mime='text/csv',
        )
