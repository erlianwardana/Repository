import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Performance", page_icon="🦈")
st.sidebar.header("Model Performance")

data = pd.read_csv("Data_COVID19_Indonesia.csv")
st.write(data)



