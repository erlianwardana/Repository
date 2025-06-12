import streamlit as st
import pandas as pd

st.title('aku')
# Baca dataset CSV
df = pd.read_csv('SuperStore_Sales_Updated.csv')
