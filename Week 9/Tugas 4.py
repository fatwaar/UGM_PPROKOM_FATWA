jumlah_elemen = int(input("Masukkan jumlah elemen dalam array :"))
array = list(range(1, jumlah_elemen + 1))
print("Array yang dihasilkan :", array)

bil_bulat = int(input("Masukkan bilangan untuk mencari kelipatan :"))

kelipatan = [num for num in array if num % bil_bulat == 0]
if kelipatan :
    print("Bilangan yang merupakan kelipatan dari", bil_bulat, ":", kelipatan)
else :
    print("Tidak ada satupun elemen dalam array yang merupakan kelipatan dari", bil_bulat)
