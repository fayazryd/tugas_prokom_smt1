glosarium = {
    "variabel": "Tempat untuk menyimpan suatu nilai atau data.",
    "list": "Kumpulan beberapa data dalam satu variabel.",
    "loop": "Perulangan untuk menjalankan kode beberapa kali.",
    "if": "Digunakan untuk memeriksa suatu kondisi.",
    "dictionary": "Kumpulan data dalam pasangan key dan value.",
    "string": "Tipe data yang berisi kumpulan karakter atau teks.",
    "integer": "Tipe data berupa bilangan bulat.",
    "float": "Tipe data berupa bilangan desimal.",
    "boolean": "Tipe data yang memiliki nilai True atau False.",
    "function": "Blok kode yang dibuat untuk menjalankan tugas tertentu."
}

print("GLOSARIUM PYTHON")

for kata, arti in glosarium.items():
    print(f"\n{kata.title()}:")
    print(f"    {arti}")