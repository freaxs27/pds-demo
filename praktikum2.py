'''
analisa pertemuan 5 tentang 5.Feature Addition.py
'''

import streamlit as st
import pandas as pd     

st.title("Cek Judul dan Status SKP")

#1. Membaca file Excel
df = pd.read_excel('data_skp.xlsx')

#2. Membuat kolom status (nilai default: Lulus)
df["status"] = "Lulus"

#3. Membuat kolom status_judul 9cek apakah judul kosong atau ada)
df["ststus_judul"] = df["JUDUL"].apply(
    lambda x: "judul Kososng" if pd.isnull(x) or x == "" else "Ada judul"
)

#4. Tampilkan isi dataframe di Streamlit
st.subheader("Data SKP")
st.dataframe(df)