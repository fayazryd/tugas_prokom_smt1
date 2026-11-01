#program pertama
hewan = ["kucing", "ikan", "burung"]

for nama in hewan:
    print(nama)
    
print()

print("kucing adalah hewan berbulu")
print("ikan adalah hewan yang hidup di air")
print("burung adalah hewan yang bisa terbang")

print("\nKetiga hewan tersebut dapat dijadikan hewan peliharaan")

#program kedua
angka = [1, 2, 3, 4, 5]

for nilai in angka:
    kubik = nilai ** 3
    print(f"Nilai {nilai} pangkat 3 adalah {kubik}.")
    
#program ketiga
threes = list(range(3, 31, 3))

for number in threes:
    print(number, end=" ")

print()
