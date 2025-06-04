import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import class(fication_report,accuracy_score)

st.set_page_config(page_title="Model Performance", page_icon="🦈")
st.sidebar.header("Model Performance")

df = pd.read_csv("model/Data_COVID19_Indonesia.csv")
dataset = pd.read_csv("https://github.com/erlianwardana/Repository/blob/main/Data_COVID19_Indonesia.csv")


