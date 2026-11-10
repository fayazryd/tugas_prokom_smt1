usernames = ["admin", "mubarok", "abi", "iyan"]
def greet(users):
    if users:
        for username in users:
            if username == 'admin':
                print("Halo admin, apakah barang masih tersedia?")
            else:
                print(f"Halo {username.title()}, terima kasih telah berbelanja di toko kami.")
    else:
        print("Kita perlu mencari pelanggan baru")

greet(usernames)
usernames.clear()    