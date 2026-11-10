places = ["jakarta", "bandung", "surabaya", "yogyakarta", "bali"]

print("Urutan asli:", places)
print("Urutan abjad (sorted):", sorted(places))
print("Urutan asli lagi:", places)
print("Abjad terbalik (sorted):", sorted(places, reverse=True))
print("Urutan asli lagi:", places)

places.reverse()
print("Setelah reverse():", places)
places.reverse()
print("Setelah reverse() lagi:", places)

places.sort()
print("Setelah sort():", places)
places.sort(reverse=True)
print("Setelah sort(reverse=True):", places)