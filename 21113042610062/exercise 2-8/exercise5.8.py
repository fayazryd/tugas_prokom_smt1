usernames = ["admin", "mubarok", "abi", "iyan"]
for username in usernames:
    if username == 'admin':
        print("Halo admin, apakah barang masih tersedia?")
    else:
        print(f"Halo {username.title()},silahkan kembalikan uangnya")