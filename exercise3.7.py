guests = ["abi", "fayaz", "rasyid", "mubarok", "dimas", "budi"]

print("Maaf, meja baru tidak datang tepat waktu. Hanya 2 orang yang bisa diundang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda makan malam.")

for guest in guests:
    print(f"{guest}, Anda masih diundang makan malam.")

del guests[0]
del guests[0]
print(guests)
