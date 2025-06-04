import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="🦈")
st.sidebar.header("Dashboard")
st.title("DATA COVID19 INDONESIA")

data = pd.read_csv("Data_COVID19_Indonesia.csv")
st.write(data)
