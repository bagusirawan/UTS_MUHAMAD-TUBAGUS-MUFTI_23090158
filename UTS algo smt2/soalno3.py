jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = 0

for i in range(jumlah_barang):
    harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
    total_harga += harga

print("Total harga belanjaan:", total_harga)
