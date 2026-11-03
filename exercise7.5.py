prompt = "\nBerapa umur Anda? (ketik 'quit' untuk keluar) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Tiketnya gratis.")
    elif age <= 12:
        print("Harga tiketnya $10.")
    else:
        print("Harga tiketnya $15.")