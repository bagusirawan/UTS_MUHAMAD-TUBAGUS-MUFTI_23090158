tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0) or ((tahun % 4 == 0) and (tahun % 100 != 0)):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")
