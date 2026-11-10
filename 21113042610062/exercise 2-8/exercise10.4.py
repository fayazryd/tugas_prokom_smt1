from pathlib import Path

name = input("Siapa nama Anda? ")

path = Path('guest.txt')
path.write_text(name)

print(f"Nama {name} sudah ditulis ke {path}.")
print("Isi guest.txt:", path.read_text())
