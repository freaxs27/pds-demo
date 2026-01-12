import streamlit as st 
import pandas as pd

data = pd.read_csv('data_wisata_bogor.csv')

df = pd.DataFrame(data)

df_preferensi = df["preferensi"].value_counts()
df_kategori = df["kategori"].value_counts()
df_kecamatan = df["kecamatan"].value_counts()

df_rating4 = df[df["rating"] >= 4.0]
df_baik = df_rating4[df["jumlah_rating"] > 497].reset_index()

harits = df["jumlah_rating"].mean()

st.title('Data Wisata Bogor')
st.write(df)
st.title("kategori")
st.write(df_kategori)
st.title("kecamatan")
st.write(df_kecamatan)
st.title("rating > 4")
st.write(df_rating4)
st.title("rating jumlah rating > 1000")
st.write(df_baik)
st.write(harits)