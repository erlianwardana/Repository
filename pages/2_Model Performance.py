import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

st.title("📊 Model Performance - SuperStore")

# Load dataset
df = pd.read_csv("SuperStore_Sales_Updated.csv")
st.subheader("📥 Data Awal")
st.write(df.head())

# Preprocessing
df = df.dropna()
df = pd.get_dummies(df, drop_first=True)

# Target klasifikasi untung/rugi
st.subheader("🎯 Klasifikasi Profit")
df['profit_class'] = pd.qcut(df['profit'], q=2, labels=[0, 1])
X = df.drop(['profit', 'profit_class'], axis=1)
y = df['profit_class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Tampilkan metrik
tab1, tab2 = st.tabs(["📈 Akurasi", "🧮 Confusion Matrix"])

with tab1:
    st.metric("Akurasi", f"{acc:.2f}")
    st.text("Classification Report")
    st.json(report)

with tab2:
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

# Simpan model dan metrik
joblib.dump(model, "trained_model.pkl")
with open("model_metrics.txt", "w") as f:
    f.write(f"Akurasi: {acc:.4f}\n")
    f.write(classification_report(y_test, y_pred))
