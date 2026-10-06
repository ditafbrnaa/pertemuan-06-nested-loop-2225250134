# Pertemuan 06 Nested Loop Python

Nama: Amandita Pebriana Putri  
NIM: 2225250134  
Kelas: 3A Pendidikan Matematika  

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
- **Loop Luar (`i`):** Mengontrol nomor baris dari 1 sampai n.
- **Loop Dalam (`j`):** Mengontrol nomor kolom dari 1 sampai n dan menghitung `hasil = i * j`.
- **Akumulator (`total_baris`):** Menjumlahkan nilai `hasil` khusus untuk baris `i` (direset menjadi 0 di setiap awal loop luar).
- **Akumulator (`total_semua`):** Menjumlahkan seluruh `hasil` perkalian dari semua pasangan $n \times n$.
- **Counter (`count_genap`):** Menghitung berapa kali `hasil` perkalian bernilai genap (`hasil % 2 == 0`).

## Hasil Pengujian
| Input `n` | Hasil yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| `0` lalu `1` | Ditolak `n <= 0`, input ulang. Total = 1, Genap = 0, Baris 1 = 1 | Menampilkan "n harus positif", Total = 1, Genap = 0, Baris 1 = 1 | Sesuai |
| `2` | Total = 9, Genap = 3, Baris 1 = 3, Baris 2 = 6 | Total = 9, Genap = 3, Baris 1 = 3, Baris 2 = 6 | Sesuai |
| `3` | Total = 36, Genap = 5, Baris 1 = 6, Baris 2 = 12, Baris 3 = 18 | Total = 36, Genap = 5, Baris 1 = 6, Baris 2 = 12, Baris 3 = 18 | Sesuai |

## Analisis Efisiensi
Badan loop dalam berjalan sebanyak $n \times n$ ($n^2$) kali untuk input $n$.
- Untuk $n = 1$, badan loop dalam berjalan 1 kali.
- Untuk $n = 2$, badan loop dalam berjalan 4 kali.
- Untuk $n = 3$, badan loop dalam berjalan 9 kali.

## Refleksi
Kesalahan yang sering terjadi pada nested loop adalah menempatkan akumulator per baris (`total_baris = 0`) di luar kedua perulangan. Akibatnya, nilai `total_baris` tidak ter-reset di setiap baris baru dan jumlahnya terus membengkak karena menambahkan nilai dari baris sebelumnya. Cara memperbaikinya adalah meletakkan `total_baris = 0` tepat di dalam loop luar sebelum loop dalam dimulai.
