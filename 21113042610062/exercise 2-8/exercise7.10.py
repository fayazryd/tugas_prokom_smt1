polling = {}

while True:
    nama = input("Siapa nama Anda? ").strip()
    tempat = input(
        "Jika bisa mengunjungi satu tempat di dunia, "
        "Anda ingin pergi ke mana? "
    ).strip()

    polling[nama] = tempat

    while True:
        ulang = input("Apakah orang lain ingin menjawab? (ya/tidak) ").strip().lower()
        if ulang in ("ya", "tidak"):
            break
        print("Mohon jawab dengan 'ya' atau 'tidak'.")

    if ulang == "tidak":
        break

print("\n--- Hasil Jajak Pendapat ---")

for nama, tempat in polling.items():
    print(f"{nama} ingin berlibur ke {tempat}.")