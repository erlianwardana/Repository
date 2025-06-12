import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv("SuperStore_Sales_Updated.csv")

# Tambahkan ship_mode sebagai fitur
features = ['category', 'sub_category', 'segment', 'region', 'ship_mode',
            'price', 'quantity', 'sales', 'profit', 'payment_mode']
target = 'returns'

