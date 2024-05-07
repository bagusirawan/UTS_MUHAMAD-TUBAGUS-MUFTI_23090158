def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / ((tinggi_badan/100) ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

def rekomendasi_kesehatan(bmi):
    if bmi < 18.5:
        return "Anda perlu menambah berat badan dengan pola makan yang sehat."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan Anda berada dalam kisaran sehat. Pertahankan gaya hidup sehat."
    elif 25 <= bmi < 29.9:
        return "Anda berada dalam kategori gemuk. Pertahankan pola makan sehat dan lakukan olahraga teratur."
    else:
        return "Anda mengalami obesitas. Konsultasikan dengan dokter untuk mendapatkan saran dan perencanaan yang tepat."
