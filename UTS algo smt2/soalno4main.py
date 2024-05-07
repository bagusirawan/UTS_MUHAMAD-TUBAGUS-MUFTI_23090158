# File: main.py
from soalno4 import hitung_bmi, kategori_bmi, rekomendasi_kesehatan

def main():
    print("Selamat datang di Kalkulator BMI")
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (cm): "))

    bmi = hitung_bmi(berat_badan, tinggi_badan)
    kategori = kategori_bmi(bmi)
    rekomendasi = rekomendasi_kesehatan(bmi)

    print("\nHasil perhitungan BMI:")
    print("Berat badan Anda:", berat_badan, "kg")
    print("Tinggi badan Anda:", tinggi_badan, "cm")
    print("Nilai BMI Anda:", round(bmi, 2))
    print("Kategori BMI Anda:", kategori)
    print("Rekomendasi kesehatan:", rekomendasi)

if __name__ == "__main__":
    main()
