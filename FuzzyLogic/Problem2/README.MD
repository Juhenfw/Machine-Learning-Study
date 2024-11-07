# Sistem Perhitungan Tip Menggunakan Logika Fuzzy Tsukamoto

## Gambaran Umum
Sistem ini memodelkan bagaimana seorang pelanggan menentukan jumlah tip yang diberikan di restoran. Keputusan untuk memberikan tip didasarkan pada kualitas pelayanan dan kualitas makanan, yang dinilai dalam rentang 0 hingga 10. Output dari sistem ini adalah jumlah tip yang akan diberikan dalam persentase, antara 0% hingga 25% dari total pembayaran.

## Input (Anteseden)
1. **Kualitas Pelayanan**: Mengukur seberapa baik pelayanan staf restoran, dalam skala 0 hingga 10. Himpunan fuzzy yang digunakan adalah:
   - **Buruk**: Kualitas pelayanan yang buruk.
   - **Rata-rata**: Kualitas pelayanan yang sedang.
   - **Baik**: Kualitas pelayanan yang baik.

2. **Kualitas Makanan**: Mengukur seberapa enak makanan yang disajikan, dalam skala 0 hingga 10. Himpunan fuzzy yang digunakan adalah:
   - **Buruk**: Kualitas makanan yang buruk.
   - **Layak**: Kualitas makanan yang sedang.
   - **Sangat Enak**: Kualitas makanan yang sangat enak.

## Output (Konsekuensi)
1. **Tip**: Persentase tip yang akan diberikan dari total pembayaran, dalam skala 0% hingga 25%. Himpunan fuzzy yang digunakan adalah:
   - **Rendah**: Tip yang kecil (0-13%).
   - **Sedang**: Tip yang sedang (13-20%).
   - **Tinggi**: Tip yang besar (20-25%).

## Aturan Fuzzy
Keputusan pemberian tip dimodelkan dengan aturan-aturan fuzzy berikut:
- Jika **pelayanan baik** atau **makanan sangat enak**, maka tip yang diberikan adalah **tinggi**.
- Jika **pelayanan rata-rata**, maka tip yang diberikan adalah **sedang**.
- Jika **pelayanan buruk** dan **makanan buruk**, maka tip yang diberikan adalah **rendah**.

## Cara Penggunaan
Sistem ini menggunakan pengendali logika fuzzy untuk menentukan persentase tip yang sesuai berdasarkan input dari kualitas pelayanan dan kualitas makanan.

### Contoh Input/Output

Sebagai contoh:
- **Kualitas Pelayanan**: 9.8
- **Kualitas Makanan**: 6.8
- **Tip yang diberikan**: 21.34%

### Kasus Uji Lainnya

Sistem dapat menghitung tip berdasarkan berbagai kombinasi kualitas pelayanan dan kualitas makanan seperti yang ditunjukkan dalam tabel di bawah ini:

| Kualitas Layanan | Kualitas Makanan | Tip yang Diberikan (%) |
|------------------|------------------|------------------------|
| 9.8              | 6.8              | (Hasil)                |
| 9.5              | 9.2              | (Hasil)                |
| 6.4              | 9.6              | (Hasil)                |
| 5.7              | 6.3              | (Hasil)                |
| 1.3              | 2.5              | (Hasil)                |
| 7.4              | 6.8              | (Hasil)                |

Untuk mendapatkan output (persentase tip), Anda dapat menjalankan program Python yang disediakan di bagian utama repositori ini.

## Instalasi

1. Instal paket Python yang diperlukan:
   ```bash
   pip install numpy scikit-fuzzy

