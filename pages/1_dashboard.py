import streamlit as st
import numpy as np
import pandas as pd
import matpotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("bread_basker.csv")
print("DataFrame Shape :",data.shape)
data.head()

#format data waktu
data ['date_time'] = pd.to_datetime(data['date_time'], format ="%d-%m-%Y %H:%M")
data ["date_time"].dtype
data['month']= data['date_time'].dt.month
data['day']= data['date_time'].dt.weekday
data['hour']= data['date_time'].dt.hour
data.head()

#menampilkan 10 item paling laris
plt.figure(figsize=(13,4))
sns.set_palette("muted")

sns.barplot(x = data["item"].value_counts()[:10].index,
            y = data["item"].value_counts()[:10].values)
plt.xlabel("");plt.ylabel("")
plt.xticks(size = 13, rotation = 45)
plt.title('10 produk yang paling laris'), size = 17)
plt.show()
