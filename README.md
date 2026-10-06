# Pertemuan 06 Nested Loop Python

Nama: Amandita Pebriana Putri  
NIM: 2225250134  
Kelas: 3A  

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
`python3 tugas/tabel_perkalian_dan_statistik.py`

## Algoritma Tugas 3
- **Loop Luar (`i`):** Mengontrol nomor baris dari 1 sampai n.
- **Loop Dalam (`j`):** Mengontrol nomor kolom dari 1 sampai n.
- **Akumulator (`total_baris`):** Menjumlahkan hasil kali `i * j` untuk baris tertentu (direset setiap iterasi loop luar).
- **Akumulator (`total_semua`):** Menjumlahkan seluruh hasil kali dari $n \times n$ pasangan.
- **Counter (`count_genap`):** Menghitung berapa banyak hasil kali `i * j` yang bernilai genap (`hasil % 2 == 0`).

## Hasil Pengujian
| Input `n` | Hasil yang Diharapkan | Keluaran Aktual | Status |
| :---: | :---: | :---: | :---: |
| 1 | Total = 1, Genap = 0 | Total = 1, Genap = 0 | Sesuai |
| 2 | Total = 9, Genap = 3 | Total = 9, Genap = 3 | Sesuai |
| 3 | Total = 36, Genap = 5 | Total = 36, Genap = 5 | Sesuai |

## Analisis Efisiensi
Badan loop dalam berjalan sebanyak $n \times n$ ($n^2$) kali. 
- Jika $n=1$, berjalan 1 kali.
- Jika $n=2$, berjalan 4 kali.
- Jika $n=3$, berjalan 9 kali.

## Refleksi
Kesalahan umum pada nested loop adalah menempatkan inisialisasi `total_baris` di luar kedua loop. Hal ini menyebabkan jumlah per baris terus membesar karena akumulasi baris sebelumnya tidak direset. Solusinya adalah meletakkan `total_baris = 0` tepat di dalam loop luar sebelum loop dalam dimulai.