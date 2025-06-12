import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("SuperStore_Sales_Updated.csv")

# Title
st.title("📊 SuperStore Sales Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", df["year"].unique())
filtered_df = df[df["year"] == selected_year]

# KPI Section
total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_orders = filtered_df["order_id"].nunique()
returns_count = filtered_df["returns"].sum()

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")
st.metric("Total Orders", total_orders)
st.metric("Total Returns", returns_count)


