tamu = ["abi", "fayaz", "rasyid"]
print(f"{tamu[0]} tidak bisa hadir makan malam.")
tamu[0] = "mubarok"

print("\nSaya menemukan meja makan yang lebih besar!")
tamu.insert(0, "zaki")
tamu.insert(2, "iyan")
tamu.append("rani")

for tamu in tamu:
    print(f"{tamu}, saya mengundang anda makan malam.")