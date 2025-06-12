import pandas as pd

# Load data
df = pd.read_csv("SuperStore_Sales_Updated.csv")

# Tambahkan ship_mode sebagai fitur
features = ['category', 'sub_category', 'segment', 'region', 'ship_mode',
            'price', 'quantity', 'sales', 'profit', 'payment_mode']
target = 'returns'

# Encode kolom kategorikal
df_encoded = df.copy()
le_dict = {}  # Untuk menyimpan label encoder tiap kolom

for col in features:
    if df_encoded[col].dtype == 'object':
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])
        le_dict[col] = le

# Split data
X = df_encoded[features]
y = df_encoded[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Fungsi prediksi dari input pengguna
def prediksi_returns(input_data):
    # Contoh input_data (dict):
    # {
    #   'category': 'Office Supplies',
    #   'sub_category': 'Binders',
    #   'segment': 'Consumer',
    #   'region': 'West',
    #   'ship_mode': 'Standard Class',
    #   'price': 100.0,
    #   'quantity': 2,
    #   'sales': 200.0,
    #   'profit': 50.0,
    #   'payment_mode': 'Online'
    # }
    
    input_df = pd.DataFrame([input_data])

    # Encode input sesuai label encoder yang disimpan
    for col in input_df.columns:
        if col in le_dict:
            input_df[col] = le_dict[col].transform(input_df[col])

    prediction = model.predict(input_df)[0]
    return "✅ Akan Dikembalikan" if prediction else "❌ Tidak Dikembalikan"

# Contoh penggunaan
sample_input = {
    'category': 'Office Supplies',
    'sub_category': 'Binders',
    'segment': 'Consumer',
    'region': 'West',
    'ship_mode': 'Standard Class',
    'price': 100.0,
    'quantity': 2,
    'sales': 200.0,
    'profit': 50.0,
    'payment_mode': 'Online'
}

hasil_prediksi = prediksi_returns(sample_input)
print("Hasil Prediksi:", hasil_prediksi)
