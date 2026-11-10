from pathlib import Path

names = []
print("Ketik 'q' untuk berhenti.")

while True:
    name = input("Siapa nama Anda? ")
    if name == 'q':
        break
    names.append(name)
    print(f"Halo, {name}!")

contents = "\n".join(names) + "\n"
Path('guest_book.txt').write_text(contents)

print("\nIsi guest_book.txt:")
print(Path('guest_book.txt').read_text())
