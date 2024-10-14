data = []
for angka in range (0, 5):
    angka = float(input(f"masukkan angka ke-{angka+1} :"))
    data.append(angka)
    print(data)
jumlah_data = sum(data)
rata_rata = sum(data)/5
pilihan = str(input("ingin melihat hasil jumlah atau rata-rata :"))
if pilihan == "jumlah":
    print("hasil jumlah dari nilai datanya adalah:", jumlah_data)
elif pilihan == "rata-rata":
    print("rata-rata dari nilai datanya adalah :", rata_rata)
else:
    print('maaf, mohon tuliskan pilihan antara "jumlah" atau "rata-rata"')
