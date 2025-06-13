import streamlit as st
import pandas as pd

# Load data
data_url = "SuperStore_Sales_Updated.csv"
df = pd.read_csv(data_url)

# Title
st.title("📊 SuperStore Sales Dashboard")

# Show data
st.subheader("🧾 Raw Data")
st.dataframe(df)

# Show basic info
st.subheader("📌 Dataset Characteristics")
st.write("Jumlah baris:", df.shape[0])
st.write("Jumlah kolom:", df.shape[1])
st.write("Kolom:", list(df.columns))

# Unique values summary
if st.checkbox("Lihat jumlah nilai unik tiap kolom"):
    st.write(df.nunique())

# Data types
if st.checkbox("Lihat tipe data tiap kolom"):
    st.write(df.dtypes)

# Describe numerik
if st.checkbox("Lihat statistik deskriptif numerik"):
    st.write(df.describe())

