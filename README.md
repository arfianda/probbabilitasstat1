Nama    : Arfianda Firsta Satritama
Kelas   : TI.24.A3
NIM     : 312410377

---

```markdown
# 📊 Program Perhitungan Probabilitas MK Mahasiswa

Program ini dibuat untuk menghitung probabilitas mahasiswa yang mengambil **mata kuliah Aljabar, Kalkulus, dan Statistika** berdasarkan data jumlah mahasiswa dan irisan antar mata kuliah.

## 🔎 Latar Belakang
Diberikan data jumlah mahasiswa yang mengambil 3 mata kuliah beserta irisan-irisannya. Kita ingin mengetahui probabilitas:
- a) Mahasiswa mengambil ketiga MK
- b) Mengambil Aljabar tetapi **bukan** Kalkulus
- c) Mengambil Statistika tetapi **bukan** Aljabar
- d) Mengambil Kalkulus tetapi **bukan** Statistika

## 📝 Cara Kerja Program
1. Menyimpan data jumlah mahasiswa tiap MK dan irisan MK.
2. Menghitung jumlah **hanya** pada tiap irisan (Venn Diagram).
3. Menghitung probabilitas setiap kasus dengan rumus:
```

P(X) = Jumlah Mahasiswa Kasus X / Total Mahasiswa

````
4. Menampilkan hasil probabilitas di terminal.

## 💻 Cara Menjalankan
1. Simpan file Python ini, misalnya `probabilitas_mk.py`.
2. Jalankan di terminal:
```bash
python probabilitas_mk.py
````

3. Hasil probabilitas akan tampil di terminal.

## 🧮 Hasil

```
Probabilitas (a) Ketiga MK: 0.106
Probabilitas (b) Aljabar tetapi bukan Kalkulus: 0.224
Probabilitas (c) Statistika tetapi bukan Aljabar: 0.206
Probabilitas (d) Kalkulus tetapi bukan Statistika: 0.464
```
