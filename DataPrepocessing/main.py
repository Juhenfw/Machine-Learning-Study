import pandas as pd
import matplotlib.pyplot as plt

# Memuat file CSV
file_path = r'D:\Materi Kuliah UNAIR\Semester 5\Pembelajaran Mesin (Praktikum) RK-A2\accelerometer.csv'  # isikan path CSV yang sesuai
data = pd.read_csv(file_path)

# Pilih salah satu nilai kecepatan rotasi (pctid) dari 17 variasi kecepatan yang ada
pctid_value = 50  # Ganti dengan nilai pctid
filtered_data = data[data['pctid'] == pctid_value]

# Reset index untuk memulai dari 0
filtered_data = filtered_data.reset_index(drop=True)

# Plot data x, y, dan z
plt.figure(figsize=(10, 6))
plt.plot(filtered_data.index, filtered_data['x'], label='X', color='r')
plt.plot(filtered_data.index, filtered_data['y'], label='Y', color='g')
plt.plot(filtered_data.index, filtered_data['z'], label='Z', color='b')

# Label sumbu dan judul
plt.xlabel('Data')
plt.ylabel('Vibrasi')
plt.title(f'Filter Data (pctid = {pctid_value})')
plt.legend()

# Tampilkan grafik
plt.show()
