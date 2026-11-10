from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
    else:
        print(f"\nIsi {filename}:")
        print(contents)
