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

# Visualisasi kategori produk
st.subheader("🛒 Penjualan per Kategori")
category_sales = df.groupby("category")["sales"].sum().sort_values(ascending=False)
st.bar_chart(category_sales)

# Visualisasi segment pelanggan
st.subheader("👥 Distribusi Segmen Pelanggan")
fig, ax = plt.subplots()
df["segment"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
ax.set_ylabel("")
st.pyplot(fig)

# Visualisasi profit per region
st.subheader("🌍 Profit per Region")
region_profit = df.groupby("region")["profit"].sum()
st.bar_chart(region_profit)

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
