import pandas as pd
import random
import matplotlib.pylot as plt

# Membaca dataset
data = pd.read_csv('SuperStore_Sales_Updated.csv')

# Membuat kolom total_revenue
data['total_revenue'] = data['price'] * data['quantity']

# Menghitung batas bin secara manual dengan menghindari duplikasi
bin_edges = [0, data['quantity'].quantile(0.2), data['quantity'].quantile(0.5), data['quantity'].max()]

# Mendefinisikan label kategori
segment_labels = ['Low', 'Normal', 'Popular']

# Membuat kolom segmentation_volume
data['segmented_vol'] = pd.cut(data['quantity'], bins=bin_edges, labels=segment_labels, include_lowest=True)

# Menyimpan hasil program ke dalam segmented_vol.csv
data.to_csv('segmented_vol3.csv', index=False)

# Menghitung jumlah transaksi dari setiap kategori
transaction_counts = data['segmented_vol'].value_counts()

# Mencetak jumlah transaksi dari setiap kategori
print("Jumlah Transaksi untuk Setiap Kategori:")
print(transaction_counts)

# Mencetak 10 baris random dari kolom product_no, total_revenue, dan segmentation_volume
random_rows = data.sample(10, random_state=1)[['product_name', 'total_revenue', 'segmented_vol']]
print("\n10 Baris Random:")
print(random_rows)

# Deskripsi kolom "quantity"
print("\n")
quantity_description = data['quantity'].describe()
print("Deskripsi Kolom 'quantity':")
print(quantity_description)

# Mencetak 10 baris random dari kolom product_no, quantity, dan segmentation_volume
random_rows = data.sample(10, random_state=1)[['product_name', 'quantity', 'segmented_vol']]
print("\n10 Baris Random:")
print(random_rows)

# Mengambil jumlah transaksi dari setiap kategori
transaction_counts = data['segmented_vol'].value_counts()

# Deskripsi kolom "quantity"
quantity_description = data['quantity'].describe()

# Membuat grafik batang
plt.figure(figsize=(8, 6))
plt.bar(transaction_counts.index, transaction_counts.values, color='blue', edgecolor='none')

# Menambahkan label nilai pada tiap bar
for i, v in enumerate(transaction_counts.values):
    plt.text(i, v, str(v), ha='center', va='bottom', fontsize=12)

# Menambahkan deskripsi statistik quantity di dalam grafik
plt.text(0.98, 0.98, f'Statistik Quantity:\n{quantity_description}', transform=plt.gca().transAxes, fontsize=10, ha='right', va='top')

# Menambahkan judul grafik
plt.title('Jumlah Transaksi untuk Setiap Kategori segmented_vol')
plt.xlabel('Kategori Segmentation Volume')
plt.ylabel('Jumlah Transaksi')

# Menghilangkan garis frame atas dan garis frame samping kanan
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Menampilkan grafik
plt.show()

