import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title("Pie Chart Keilmuan SKP")

# !.Membaca file Excel
df = pd.read_excel('data_skp.xlsx')

# 2. Group berdasarkan keilmuan
grouped = df.groupby("keilmuan")["JUDUL"].count().reset_index()

labels = grouped["keilmuan"]
values = grouped["JUDUL"]

# 3. Plot Pie Chart
fig, ax = plt.subplots(figsize=(7,7))
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title("Proporsi judul Penelitian Berdasarkan Keilmuan")

# 4. Tampilkan ke Streamlit
st.pyplot(fig)

# 5. Tampilkan tabel datanya juga
st.subheader("Tabel Data Per Keilmuan")
st.dataframe(grouped)
