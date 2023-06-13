import pickle
import streamlit as st

# baca model
# mlp_model=pickle.load(open("mlp.pkl"))

# judul web
st.title("implementasi MLP dengan data Wine yoooo")

Alcohol = st.text_input('input nilai Alcohol')
Malic_acid = st.text_input('input nilai Malic Acid')
Ash = st.text_input('input nilai Ash')
Acl = st.text_input('input nilai Acl')
Mg = st.text_input('input nilai Mg')
Phenols = st.text_input('input nilai Phenols')
Flavanoids = st.text_input('input nilai Flavanoids')
Nonflavanoid_phenols = st.text_input('input nilai NonFlavanoid')
Proanth = st.text_input('input nilai Proanth')
Color_int = st.text_input('input nilai Color')
Hue = st.text_input('input nilai Hue')
OD = st.text_input('input nilai OD')
Proline = st.text_input('input nilai Proline')

if st.button("test prediksi kelas wine"):
    y_pred = classifier.predict([[]])
