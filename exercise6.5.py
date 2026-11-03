sungai = {
    "nil": "mesir",
    "amazon": "brasil",
    "kapuas": "indonesia",
}

# Menampilkan sungai dan negara yang dilalui
for nama, negara in sungai.items():
    print(f"Sungai {nama.title()} mengalir melalui {negara.title()}.")

print("\nNama-nama sungai:")

# Menampilkan nama setiap sungai
for nama in sungai.keys():
    print(nama.title())

print("\nNama-nama negara:")

# Menampilkan nama setiap negara
for negara in sungai.values():
    print(negara.title())