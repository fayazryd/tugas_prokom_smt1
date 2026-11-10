glosarium = {
    "variabel": "Tempat untuk menyimpan suatu nilai atau data.",
    "list": "Kumpulan beberapa data dalam satu variabel.",
    "loop": "Perulangan untuk menjalankan kode beberapa kali.",
    "if": "Digunakan untuk memeriksa suatu kondisi.",
    "dictionary": "Kumpulan data yang disimpan dalam pasangan key dan value."
}

print("GLOSARIUM PYTHON")

for kata, arti in glosarium.items():
    print(f"\n{kata}:")
    print(f"    {arti}")