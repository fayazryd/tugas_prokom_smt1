import json
from pathlib import Path

number = json.loads(Path('favorite_number.json').read_text())
print(f"Saya tahu angka favorit Anda! Yaitu {number}.")
