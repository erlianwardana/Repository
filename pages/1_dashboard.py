import streamlit as st
import pandas as pd

st.title("Dataset SuperStore Sales")
st.write("Dataset SuperStore Sales adalah dataset yang bermanfaat untuk analisis perilaku pelanggan. Dataset ini dapat digunakan untuk mempelajari produk apa yang paling laris, produk apa yang paling sering dibeli oleh pelanggan tertentu, dan segmen pelanggan mana yang paling menguntungkan.")

# Baca dataset CSV
df = pd.read_csv('SuperStore_Sales_Updated.csv')

# Konversi kolom 'Date' menjadi tipe data datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Temukan tanggal awal dan tanggal akhir
tanggal_awal = df['order_date'].min()
tanggal_akhir = df['order_date'].max()

# Cetak hasilnya
print(f"Rentang waktu data dalam dataset: dari {tanggal_awal} hingga {tanggal_akhir}")

# Tampilkan seluruh kolom dengan nomor urut
for i, kolom in enumerate(df.columns, start=1):
    print(f"{i}. {kolom}")

# Cetak jumlah nilai null
print(df.isnull().sum())

# Menampilkan jumlah data duplikat sebelum membersihkan
jumlah_duplikat_sebelum = df.duplicated().sum()
print(f"Jumlah data duplikat: {jumlah_duplikat_sebelum}")

df
