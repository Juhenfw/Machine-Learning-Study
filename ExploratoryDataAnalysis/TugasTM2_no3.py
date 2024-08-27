import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_regression
from pandas.plotting import parallel_coordinates

# Langkah 1: Membuat dataset
np.random.seed(42)  # Untuk hasil yang dapat direproduksi
X, y = make_regression(n_samples=100, n_features=5, noise=0.3, bias=10)

# Membuat DataFrame dari data yang dihasilkan
df = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(5)])
df['Target'] = y

# Visualisasi 1: Heatmap untuk melihat korelasi antar variabel
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap Korelasi antara Variabel')
plt.show()

# Visualisasi 2: Parallel Coordinates Plot
# Membuat kategori target menjadi kategori berdasarkan kuantilis
df['Target_Category'] = pd.qcut(df['Target'], q=3, labels=['Low', 'Medium', 'High'])

plt.figure(figsize=(12, 8))
parallel_coordinates(df, 'Target_Category', color=['#556270', '#4ECDC4', '#C7F464'])
plt.title('Parallel Coordinates Plot dari 5 Feature dan Target')
plt.xlabel('Fitur')
plt.ylabel('Nilai')
plt.show()

# Visualisasi 3: Radar Chart (Spider Chart)
from math import pi

# Menormalisasi data
df_norm = (df.drop(columns='Target_Category') - df.drop(columns='Target_Category').min()) / (df.drop(columns='Target_Category').max() - df.drop(columns='Target_Category').min())

# Menyiapkan data untuk radar chart
categories = list(df_norm.columns)
num_vars = len(categories)

# Membuat radar chart untuk 3 contoh data pertama
for i in range(3):
    values = df_norm.iloc[i].tolist()
    values += values[:1]  # Ulangi nilai pertama di akhir untuk menutup lingkaran
    
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]
    
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=f'Sample {i+1}')
    ax.fill(angles, values, alpha=0.4)
    
    plt.title(f'Radar Chart untuk Sample {i+1}')
    plt.show()
