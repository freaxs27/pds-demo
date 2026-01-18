import pandas as pd

df = pd.read_excel('data_wisata_bogor.xlsx')

df_clean = df.drop_duplicates(subset=['nama_tempat_wisata'], keep='first')

df_clean["harga_tiket"] = pd.to_numeric(df["harga_tiket"], errors="coerce")

df = df_clean[df_clean["jumlah_rating"] > 50]

print(df.reset_index)


