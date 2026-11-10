try:
    first_number = int(input("Masukkan angka pertama: "))
    second_number = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Maaf, masukan harus berupa angka.")
else:
    print(f"Hasil penjumlahan: {first_number + second_number}")
