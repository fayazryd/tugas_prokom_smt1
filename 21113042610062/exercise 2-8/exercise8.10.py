def send_messages(pesan, sent_messages):
    while pesan:
        teks = pesan.pop(0)
        print(teks)
        sent_messages.append(teks)

pesan = [
    "Selamat pagi!",
    "Semangat belajar Python!",
    "Jangan lupa mengerjakan tugas.",
    "Tetap rajin belajar.",
    "Semoga harimu menyenangkan!"
]

sent_messages = []

send_messages(pesan, sent_messages)

print("\nDaftar pesan awal:")
print(pesan)

print("\nDaftar pesan yang sudah dikirim:")
print(sent_messages)