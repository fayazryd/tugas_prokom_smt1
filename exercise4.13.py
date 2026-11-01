makanan = ("nasi", "ayam goreng", "sayur asem", "es teh")
print("menu awal:")
for item in makanan:
    print(makanan)
    
try:
    makanan[0] = "nasi goreng"
except TypeError as error:
    print(f"\nphython menolak perubahan: {error}")
    
makanan = ("nasi", "ayam bakar", "sayur lodeh", "es jeruk")
print("\nmenu baru:")
for item in makanan:
    print(makanan)
    