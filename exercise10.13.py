import json
from pathlib import Path

path = Path('user_info.json')

if path.exists():
    user = json.loads(path.read_text())
    print("Program ini mengingat:")
    print(f"Nama: {user['name']}")
    print(f"Umur: {user['age']}")
    print(f"Kota: {user['city']}")
else:
    user = {
        'name': input("Siapa nama Anda? "),
        'age': input("Berapa umur Anda? "),
        'city': input("Di kota mana Anda tinggal? "),
    }
    path.write_text(json.dumps(user))
    print("Informasi Anda sudah disimpan.")
