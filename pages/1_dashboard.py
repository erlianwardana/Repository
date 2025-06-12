import streamlit as st
import pandas as pd

data = pd.read_csv("bread_basker.csv")
print("DataFrame Shape :",data.shape)
data.head()

