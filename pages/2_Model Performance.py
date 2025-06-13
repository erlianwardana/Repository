import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load dataset
df = pd.read_csv("SuperStore_Sales_Updated.csv")

# Contoh preprocessing (ubah sesuai dataset kamu)
df = df.dropna()  # buang missing values
df = pd.get_dummies(df, drop_first=True)  # encoding kategorikal

# Misalnya target kolomnya adalah 'profit' dikategorikan (contoh fiktif)
df['profit_class'] = pd.qcut(df['profit'], q=2, labels=[0, 1])  # klasifikasi untung/rugi
X = df.drop(['profit', 'profit_class'], axis=1)
y = df['profit_class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
print("Akurasi:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Simpan model (opsional)
joblib.dump(model, "trained_model.pkl")
