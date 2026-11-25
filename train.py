import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

print("Semua library berhasil dimuat!")

# Membaca dataset
df = pd.read_csv("kos_madiun.csv")

# Menampilkan 5 data teratas
df.head()

# Ubah kategori 'ya'/'tidak' menjadi 1/0
df["ac_num"] = df["ac"].map({"ya": 1, "tidak": 0})

# Periksa kembali tabel
df[["nama", "ac", "ac_num"]].head()

# Menentukan variabel X (input) dan y (target)
X = df[["jarak_km", "rating", "ac_num"]]
y = df["harga"]

print("Bentuk data fitur X :", X.shape)
print("Bentuk data target y:", y.shape)

# Inisialisasi dan pelatihan model
model = LinearRegression()
model.fit(X, y)

print("Model selesai dilatih!")

print("Konstanta (Intercept):", round(model.intercept_, 2))
print("Koefisien Fitur:")
for kolom, nilai in zip(X.columns, model.coef_):
    print(f"- {kolom}: {round(nilai, 2)}")

# Prediksi harga untuk data yang sudah ada
y_prediksi = model.predict(X)

mae = mean_absolute_error(y, y_prediksi)
r2 = r2_score(y, y_prediksi)

print(f"Mean Absolute Error (MAE): Rp {mae * 1000:,.0f}")
print(f"R-squared Score (R2)     : {r2:.2f}")

# Simpan model ke file berekstensi .joblib
nama_file_model = "model_kos.joblib"
joblib.dump(model, nama_file_model)

print(f"Sukses! Model telah dibekukan dan disimpan sebagai '{nama_file_model}'")

# 1. Muat kembali model dari file
model_terbangun = joblib.load("model_kos.joblib")

# 2. Buat simulasi input data calon penyewa:
# Misal: Jarak 1.5 km, Rating 4.0, Ada AC (1)
data_simulasi = pd.DataFrame({
    "jarak_km": [1.5],
    "rating": [4.0],
    "ac_num": [1]
})

# 3. Lakukan prediksi
hasil_ribu = model_terbangun.predict(data_simulasi)[0]
hasil_rupiah = hasil_ribu * 1000

print(f"Perkiraan Harga Kos: Rp {hasil_rupiah:,.0f} / bulan")