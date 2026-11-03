current_users = ["admin", "mubarok", "abi", "iyan"]
new_users = ["admin", "ABI", "joko", "sari", "nina"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah dipakai. Silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")