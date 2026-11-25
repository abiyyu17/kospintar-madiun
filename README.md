# 🏠 KosPintar Madiun

Sistem Cerdas Estimasi Tarif Sewa dan Rekomendasi Kos di Madiun berbasis Web (**Django**) dan **Machine Learning (Linear Regression)**.

Proyek ini dibangun untuk memenuhi Mini Proyek Kelompok pada mata kuliah Sistem Cerdas (Pertemuan 14).

---

## 📌 Fitur Utama

1. **Estimasi Tarif Sewa Cerdas:** Menghitung perkiraan harga wajar sewa kos bulanan berdasarkan jarak ke kampus (km), kelengkapan fasilitas AC, dan rating kualitas kos.
2. **Kategori Kelayakan Tarif:** Memberikan indikator status harga (Ekonomis, Standar, atau Premium).
3. **Rekomendasi Kos Nyata:** Mencari kos dari data nyata yang selisih tarifnya paling mendekati hasil estimasi pengguna.
4. **Dashboard Statistik Pasar:** Menampilkan visualisasi grafik batang perbandingan rata-rata tarif kos dengan fasilitas AC vs tanpa AC menggunakan Chart.js.

---

## 🗂️ Struktur Direktori Proyek

```text
kospintar/
├── katalog/                # Aplikasi fitur (views, template HTML, routing)
│   ├── templates/katalog/  # Tampilan web (Bootstrap 5 & Chart.js)
│   ├── urls.py
│   └── views.py
├── kospintar/              # Konfigurasi utama Django (settings, urls, wsgi)
├── kos_madiun.csv          # Dataset kos di Madiun
├── model_kos.joblib        # Model Linear Regression yang sudah dilatih
├── train.py                # Skrip pelatihan model machine learning
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📊 Informasi Dataset

* **File:** `kos_madiun.csv`
* **Jumlah Data:** 30 data kos di area sekitar kampus Madiun.
* **Fitur:** `nama`, `jarak_km`, `harga`, `ac`, `rating`.
* **Lisensi Data:** Public Domain / Open Data untuk keperluan akademis.

---

## 🚀 Panduan Menjalankan Proyek Secara Lokal

### 1. Prasyarat
Pastikan komputer Anda telah terpasang **Python** (versi 3.10 atau yang lebih baru).

### 2. Kloning Repositori
```bash
git clone https://github.com/<username-github-anda>/kospintar-madiun.git
cd kospintar-madiun
```

### 3. Instalasi Kebutuhan Pustaka
```bash
pip install -r requirements.txt
```

### 4. Pelatihan Model (Opsional)
File `model_kos.joblib` sudah disertakan. Namun jika ingin melatih ulang:
```bash
python train.py
```

### 5. Jalankan Server Web Django
```bash
python manage.py runserver
```

Akses aplikasi melalui peramban web di alamat:
👉 `http://127.0.0.1:8000/`

---

## 👥 Kontribusi Tim

| Nama Anggota | Peran & Kontribusi |
| :--- | :--- |
| *Nama Anggota 1* | Data Preparation, EDA, Training Model & Evaluasi (`train.py`, `joblib`) |
| *Nama Anggota 2* | Backend Architecture Django, routing URL, dan Controller logic (`views.py`) |
| *Nama Anggota 3* | Frontend UI/UX, Integrasi Bootstrap 5 dan Visualisasi Data (`index.html`) |
| *Nama Anggota 4* | QA Testing, Dokumentasi Repositori, dan Persiapan Materi Demo UAS |

---

## 📄 Lisensi

Proyek ini dirilis di bawah lisensi terbuka [MIT License](LICENSE).
