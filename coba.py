import streamlit as st 
import pandas as pd

data = pd.read_csv('data_wisata_bogor_finalz.csv')

df = pd.DataFrame(data)

df = pd.read_csv('data_wisata_bogor_finalz.csv')

df_clean = df.drop_duplicates(subset=['nama_tempat_wisata'], keep='first')

df_clean["harga_tiket"] = pd.to_numeric(df["harga_tiket"], errors="coerce")

df = df_clean[df_clean["jumlah_rating"] > 50]


st.title('Data Wisata Bogor')
st.write(df)
