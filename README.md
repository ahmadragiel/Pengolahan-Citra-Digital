# Studi Perbaikan Kualitas Citra Digital
## Menggunakan Metode Spatial dan Frequency Domain

---

## 👤 Tentang Project
Project ini dibuat sebagai bagian dari tugas mata kuliah pengolahan citra digital.  
Tujuan utama dari project ini adalah untuk memahami serta mengimplementasikan teknik perbaikan citra digital, khususnya dalam mengurangi noise dan meningkatkan kualitas visual gambar.

Selain sebagai tugas akademik, project ini juga menjadi bagian dari pengembangan portofolio pribadi di bidang teknologi.

---

## 🎯 Tujuan
- Memahami konsep dasar perbaikan citra digital  
- Mengidentifikasi jenis-jenis noise pada citra  
- Mengimplementasikan metode perbaikan citra  
- Membandingkan hasil sebelum dan sesudah proses  

---

## 🧠 Landasan Teori

### 1. Citra Digital
Citra digital adalah representasi visual dalam bentuk data numerik yang dapat diolah menggunakan komputer.

---

### 2. Noise pada Citra
Noise adalah gangguan yang muncul pada citra sehingga menurunkan kualitas gambar.  
Beberapa jenis noise:
- Gaussian Noise  
- Salt & Pepper Noise  
- Speckle Noise  

---

### 3. Metode Perbaikan Citra

#### 🔹 Spatial Domain
Metode ini bekerja langsung pada nilai piksel citra.

Contoh:
- Mean Filter  
- Median Filter  

Kelebihan:
- Mudah diimplementasikan  

Kekurangan:
- Dapat mengurangi detail gambar  

---

#### 🔹 Frequency Domain
Metode ini bekerja dengan mengubah citra ke domain frekuensi.

Contoh:
- Low-pass filter  
- High-pass filter  

Kelebihan:
- Lebih fleksibel dalam memisahkan noise  

Kekurangan:
- Lebih kompleks  

---asdasd

## ⚙️ Implementasi

Tools yang digunakan:
- Python  
- OpenCV / scikit-image  
- NumPy  

Langkah-langkah:
1. Membaca citra  
2. Menambahkan noise (simulasi)  
3. Menerapkan metode perbaikan  
4. Membandingkan hasil  

---

## 🖼️ Hasil

| Sebelum | Sesudah |
|--------|--------|
| (gambar noise) | (gambar hasil) |

---

## 📊 Analisis
- Metode yang digunakan mampu mengurangi noise pada citra  
- Terjadi sedikit penurunan detail pada beberapa bagian gambar  
- Pemilihan metode sangat mempengaruhi hasil akhir  

---

## 🚀 Kesimpulan
Perbaikan citra digital merupakan proses penting dalam pengolahan citra untuk meningkatkan kualitas visual.

Dari project ini dapat disimpulkan bahwa:
- Tidak ada metode yang sempurna  
- Diperlukan keseimbangan antara pengurangan noise dan menjaga detail  

---

## 💬 Refleksi Pribadi
Project ini bukan hanya tentang menyelesaikan tugas, tetapi juga tentang proses belajar dan pengembangan diri.

Saya percaya bahwa selama masih memiliki kesempatan, saya harus terus belajar, mencoba, dan berkembang.

> “Bertarunglah sehancur-hancurnya selagi muda, sampai tak tersisa sedikitpun kerusakan di masa depanmu.”

---

## 📎 Penutup
Terima kasih telah melihat project ini.  
Semoga project ini dapat memberikan manfaat dan menjadi langkah awal dalam pengembangan kemampuan di bidang teknologi.