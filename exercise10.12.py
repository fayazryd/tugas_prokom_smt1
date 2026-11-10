import json
from pathlib import Path

path = Path('favorite_number.json')

if path.exists():
    number = json.loads(path.read_text())
    print(f"Saya tahu angka favorit Anda! Yaitu {number}.")
else:
    number = input("Apa angka favorit Anda? ")
    path.write_text(json.dumps(number))
    print("Angka favorit Anda sudah disimpan.")
