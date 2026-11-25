from django.shortcuts import render
import pandas as pd
import joblib
import os

# Menemukan path folder utama (root project)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model_kos.joblib')
CSV_PATH = os.path.join(BASE_DIR, 'kos_madiun.csv')

# Muat model AI dan dataset saat server pertama kali dijalankan
model = joblib.load(MODEL_PATH)
df_kos = pd.read_csv(CSV_PATH)

def index(request):
    hasil_prediksi = None
    status_kategori = None
    badge_class = None
    input_user = {}
    rekomendasi = []

    # Hitung rata-rata tarif kos ber-AC vs Non-AC untuk grafik Chart.js (dalam Rupiah)
    rata_ac = df_kos.groupby('ac')['harga'].mean()
    rata_ada_ac = float(rata_ac.get('ya', 0)) * 1000
    rata_tanpa_ac = float(rata_ac.get('tidak', 0)) * 1000

    is_ac = True  # Default ada AC

    if request.method == 'POST':
        jarak_km = float(request.POST.get('jarak_km', 1.5))
        ac = request.POST.get('ac', 'ya')
        rating = float(request.POST.get('rating', 4.0))
        is_ac = (ac == 'ya')

        input_user = {
            'jarak_km': jarak_km,
            'ac': ac,
            'rating': rating
        }

        # 2. Susun format input DataFrame persis seperti saat melatih model
        data_baru = pd.DataFrame({
            'jarak_km': [jarak_km],
            'rating': [rating],
            'ac_num': [1 if ac == 'ya' else 0]
        })

        # 3. Prediksi harga menggunakan model joblib
        prediksi_ribu = model.predict(data_baru)[0]
        hasil_prediksi = prediksi_ribu * 1000  # Ubah dari satuan ribu ke Rupiah utuh

        # 4. Berikan label cerdas (Indikator status kelayakan harga)
        if hasil_prediksi < 850000:
            status_kategori = "💡 Kategori Ekonomis / Hemat"
            badge_class = "bg-info text-dark"
        elif hasil_prediksi <= 1200000:
            status_kategori = "✨ Kategori Standar / Menengah"
            badge_class = "bg-success"
        else:
            status_kategori = "⭐ Kategori Premium / Eksklusif"
            badge_class = "bg-warning text-dark"

        # 5. Cari 3 kos nyata dari kos_madiun.csv yang harganya paling mendekati hasil prediksi
        df_temp = df_kos.copy()
        df_temp['selisih'] = (df_temp['harga'] * 1000 - hasil_prediksi).abs()
        kos_terpilih = df_temp.sort_values(by='selisih').head(3)

        for _, row in kos_terpilih.iterrows():
            rekomendasi.append({
                'nama': row['nama'],
                'jarak_km': row['jarak_km'],
                'ac': row['ac'],
                'rating': row['rating'],
                'harga_rp': row['harga'] * 1000
            })

    context = {
        'hasil_prediksi': hasil_prediksi,
        'status_kategori': status_kategori,
        'badge_class': badge_class,
        'input_user': input_user,
        'is_ac': is_ac,
        'rekomendasi': rekomendasi,
        'rata_ada_ac': rata_ada_ac,
        'rata_tanpa_ac': rata_tanpa_ac,
    }
    return render(request, 'katalog/index.html', context)