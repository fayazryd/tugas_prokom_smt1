import json
from pathlib import Path

number = input("Apa angka favorit Anda? ")
Path('favorite_number.json').write_text(json.dumps(number))
print("Angka favorit Anda sudah disimpan.")
