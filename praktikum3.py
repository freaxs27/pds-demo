import streamlit as st 
import folium 
from streamlit_folium import st_folium

# Title
st.title("COntoh Integrasi Folium + Streamlit")

# Titik peta Indonesia
center_lat = -2.5489
center_lon = 118.0149

# BUat peta Folium
m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

# Tampilkan di Streamllit
st_folium(m, width=700, height=500)