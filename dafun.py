print("Selamat datang di dafun")
nama = input("Masukan Namamu : ")
umur = int(input("Masukan Umurmu : "))

print("Haloo ", nama, " Selamat Menikmati Wahana di dafun")

total_pembelian = 0
harga_wahana = [13000, 10000, 15000, 20000]

print("Daftar Wahana")
print("1. Biang Lala RP. 13.000")
print("2. Istana Boneka RP. 10.000")
print("3. Rumah Kaca RP. 15.000")
print("4. Roller Coaster RP. 20.000")
print("Silahkan Pilih Wahana mu")
wahana = int(input("Pilih Wahana > "))

if(wahana < 0):
    print("Input Pilihan anda tidak bole kurang dari 0")
elif (wahana > len(harga_wahana)):
    print("Input yang ada perintahkan tidak ada dalam daftar wahana")
else:
    total_pembelian += harga_wahana[wahana - 1]

    print("Harga Tiket Wahana : RP.", total_pembelian)
    total_pembelian += 2000
    print("+ Pajak: RP. 2000")
    print("Jadi Total Pembelian nya", total_pembelian)





