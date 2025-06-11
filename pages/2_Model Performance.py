import pandas as pd
import streamlit as st
import random
import matplotlib.pyplot as plt
import seaborn as sns

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

# Membaca dataset
data = pd.read_csv('segmented_vol3.csv')
# Cetak jumlah nilai null
print(df.isnull().sum())
# Menampilkan jumlah data duplikat sebelum membersihkan
jumlah_duplikat_sebelum = df.duplicated().sum()
print(f"Jumlah data duplikat: {jumlah_duplikat_sebelum}")

# Membaca dataset
data = pd.read_csv('segmented_vol3.csv')

# Menghitung persentil untuk segmentasi berdasarkan total revenue
quantiles = [0, 0.2, 0.8, 1]
segment_labels = ['Low', 'Normal', 'Popular']

# Membuat kolom total_revenue
data['total_revenue'] = data['price'] * data['quantity']

# Membuat kolom segmented_rev berdasarkan total revenue
data['segmented_rev'] = pd.cut(data['total_revenue'], data['total_revenue'].quantile(quantiles), labels=segment_labels)

# Menyimpan hasil program ke dalam segmented_rev.csv
data.to_csv('segmented_rev3.csv', index=False)

# Menghitung jumlah transaksi dari setiap kategori
transaction_counts = data['segmented_rev'].value_counts()

# Mencetak jumlah transaksi dari setiap kategori
print("Jumlah Transaksi untuk Setiap Kategori:")
print(transaction_counts)

# Deskripsi kolom "total_revenue"
print("\n")
total_revenue_description = data['total_revenue'].describe()
print("Deskripsi Kolom 'total_revenue':")
print(total_revenue_description)

# Mencetak 10 baris random dari kolom product_no, total_revenue, dan segmented_rev
random_rows = data.sample(10, random_state=1)[['product_name', 'total_revenue', 'segmented_rev']]
print("\n10 Baris Random:")
print(random_rows)

# Mengambil jumlah transaksi dari setiap kategori
transaction_counts = data['segmented_rev'].value_counts()

# Deskripsi kolom "total_revenue"
total_revenue_description = data['total_revenue'].describe()

# Membuat grafik batang
plt.figure(figsize=(8, 6))
plt.bar(transaction_counts.index, transaction_counts.values, color='green', edgecolor='none')

# Menambahkan label nilai pada tiap bar
for i, v in enumerate(transaction_counts.values):
    plt.text(i, v, str(v), ha='center', va='bottom', fontsize=12)

# Menambahkan deskripsi statistik "total_revenue" di dalam grafik
plt.text(0.98, 0.98, f'Deskripsi Total Revenue:\n{total_revenue_description}', transform=plt.gca().transAxes, fontsize=10, ha='right', va='top')

# Menambahkan judul grafik
plt.title('Jumlah Transaksi untuk Setiap Kategori (Berdasarkan Total Revenue)')
plt.xlabel('Kategori Segmentation Revenue')
plt.ylabel('Jumlah Transaksi')

# Menghilangkan garis frame atas dan garis frame samping kanan
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Menampilkan grafik
plt.show()

# Membaca dataset
df = pd.read_csv("segmented_rev3.csv")

# Memeriksa berapa banyak nilai null (NaN) dalam dataset
null_counts = df.isnull().sum()

# Menampilkan jumlah nilai null dalam setiap kolom
print(null_counts)

# Menampilkan jumlah data duplikat sebelum membersihkan
jumlah_duplikat_sebelum = df.duplicated().sum()
print(f"Jumlah data duplikat: {jumlah_duplikat_sebelum}")

# Mengisi nilai null dalam kolom segmented_rev dengan mode
mode_segmented_rev = df['segmented_rev'].mode()[0]
df['segmented_rev'].fillna(mode_segmented_rev, inplace=True)

# Memeriksa kembali jumlah nilai null setelah imputasi
null_counts_after_imputation = df.isnull().sum()
print(null_counts_after_imputation)

# Membaca dataset
df = pd.read_csv("segmented_rev3_clean.csv")

# Menampilkan tipe data setiap kolom
print(df.dtypes)

# Menggabungkan kolom 'segmentation_volume' dan 'segmented_rev' dengan tanda '-'
data['segmented_combine'] = data['segmented_vol'].astype(str) + '-' + data['segmented_rev'].astype(str)

# Mengaturnya sesuai dengan aturan yang telah Anda tentukan
def determine_segmented_final(row):
    if row['segmented_combine'] == 'Popular-Popular':
        return 'Super Popular'
    elif row['segmented_combine'] == 'Popular-Normal' or row['segmented_combine'] == 'Normal-Popular':
        return 'Popular'
    elif row['segmented_combine'] == 'Low-Low':
        return 'Low'
    return 'Normal'

data['segmented_final'] = data.apply(determine_segmented_final, axis=1)

# Menyimpan hasil program ke dalam segmented_final.csv
data.to_csv('segmented_final3.csv', index=False)

# Menghitung jumlah produk dalam masing-masing kategori di kolom segmented_final
# Ini menghitung frekuensi kemunculan setiap nilai unik dalam kolom "segmented_final."
product_counts = data['segmented_final'].value_counts()

# Cetak hasilnya
print("Jumlah (count) Produk ditransaksikan dalam Setiap Kategori (segmented_final):")
print(product_counts)

# Mencetak 10 baris random dari kolom product_no, total_revenue, dan segmented_final
random_rows = data.sample(10, random_state=1)[['product_name', 'total_revenue', 'segmented_final']]
print("\n10 Baris Random:")
print(random_rows)

# Mengelompokkan data berdasarkan kolom 'segmented_final' dan menjumlahkan jumlah produk
category_counts = data.groupby('segmented_final')['quantity'].sum()

# Mencetak hasilnya
print("\n")
print("Jumlah (amount) Produk yang Ditransaksikan Berdasarkan Kategori:")
print(category_counts)

# Menyimpan hasil ke file CSV jika diperlukan
df.to_csv('segmented_rev3_clean.csv', index=False)

# Filter data untuk setiap kategori dalam kolom segmented_final
low_category = data[data['segmented_final'] == 'Low']
normal_category = data[data['segmented_final'] == 'Normal']
popular_category = data[data['segmented_final'] == 'Popular']
super_popular_category = data[data['segmented_final'] == 'Super Popular']

# Deskripsi kolom 'quantity' untuk setiap kategori
low_quantity_description = low_category['quantity'].describe().reset_index()
low_quantity_description['Category'] = 'Low'
normal_quantity_description = normal_category['quantity'].describe().reset_index()
normal_quantity_description['Category'] = 'Normal'
popular_quantity_description = popular_category['quantity'].describe().reset_index()
popular_quantity_description['Category'] = 'Popular'
super_popular_quantity_description = super_popular_category['quantity'].describe().reset_index()
super_popular_quantity_description['Category'] = 'Super Popular'

# Gabungkan deskripsi dalam satu tabel
quantity_descriptions = pd.concat([low_quantity_description, normal_quantity_description, popular_quantity_description, super_popular_quantity_description])
quantity_descriptions = quantity_descriptions.pivot(index='Category', columns='index', values='quantity')

# Cetak tabel deskripsi
quantity_descriptions

# Mengambil jumlah transaksi dari setiap kategori
transaction_counts = data['segmented_final'].value_counts()

# Membuat grafik batang
plt.figure(figsize=(8, 6))
plt.bar(transaction_counts.index, transaction_counts.values, color='orange', edgecolor='none')

# Menambahkan label nilai pada tiap bar
for i, v in enumerate(transaction_counts.values):
    plt.text(i, v, str(v), ha='center', va='bottom', fontsize=12)

# Menambahkan judul grafik
plt.title('Jumlah Transaksi untuk Setiap Kategori (segmented_final)')
plt.xlabel('Kategori Segmentation Final')
plt.ylabel('Jumlah Transaksi')

# Menghilangkan garis frame atas dan garis frame samping kanan
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Menampilkan grafik
plt.show()

# Mengambil jumlah transaksi dari setiap kategori
transaction_counts = data['segmented_final'].value_counts()

# Membuat tabel deskripsi untuk kolom 'quantity'
quantity_descriptions = pd.concat([low_quantity_description, normal_quantity_description, popular_quantity_description, super_popular_quantity_description])
quantity_descriptions = quantity_descriptions.pivot(index='Category', columns='index', values='quantity')

# Membuat subplot dengan 1 baris dan 2 kolom
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot grafik batang menggunakan Seaborn
bar_plot = sns.barplot(x=transaction_counts.index, y=transaction_counts.values, ax=axes[0], palette='pastel')
axes[0].set_title('Jumlah Transaksi untuk Setiap Kategori (segmented_final)')
axes[0].set_xlabel('Kategori Segmentation Final')
axes[0].set_ylabel('Jumlah Transaksi')

# Menambahkan nilai di atas setiap bar pada grafik batang
for p in bar_plot.patches:
    bar_plot.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

# Plot tabel deskripsi dengan Seaborn dan mengatur warna latar belakang
sns.heatmap(quantity_descriptions, annot=True, fmt=".2f", cmap='YlGnBu', ax=axes[1], cbar=False)
axes[1].set_title('Deskripsi Kolom "quantity"')
axes[1].set_xlabel('Statistik')
axes[1].set_ylabel('Kategori')

# Mengatur warna latar belakang kolom kedua menjadi hijau muda
colormap = sns.light_palette("green", as_cmap=True)
sns.heatmap(quantity_descriptions, annot=True, fmt=".2f", cmap=colormap, ax=axes[1], cbar=False)

plt.tight_layout()

# Menampilkan grafik
plt.show()

# Baca data dari file CSV
df = pd.read_csv('segmented_final3.csv')

# Memeriksa kembali jumlah nilai null dalam dataset
null_counts = df.isnull().sum()
print(null_counts)

# Mengambil kolom 'price' untuk distribusi
prices = df['price']

# Membuat histogram untuk distribusi harga
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='blue', alpha=0.7, density=True, label='Histogram')
sns.kdeplot(prices, color='red', label='Kurva Distribusi')
plt.title('Distribusi Harga dengan Kurva Distribusi')
plt.xlabel('Harga')
plt.ylabel('Frekuensi')
plt.legend()
plt.grid(True)

# Menambahkan deskripsi statistik di dalam grafik
plt.text(0.65, 0.85, df['price'].describe().to_string(), transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'))

# Menampilkan grafik
plt.show()

# Melakukan describe kolom "price"
price_description = data['price'].describe()

# Cetak hasil describe
print(price_description)

# Menampilkan data kolom "sales" dan "total_revenue"
selected_columns = df[["sales", "total_revenue"]]
print(selected_columns)

# Hapus kolom "sales"
df = df.drop("sales", axis=1)

# Simpan dataset yang sudah dimodifikasi ke file "segmented_final3.csv"
df.to_csv('segmented_final3.csv', index=False)

