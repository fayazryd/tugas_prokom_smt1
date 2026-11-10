favorite_languages = {
    'abi': {'language': 'python', 'level': 'mahir'},
    'iyan': {'language': 'c', 'level': 'menengah'},
    'rasya': {'language': 'rust', 'level': 'pemula'},
}

print("Hasil Polling Bahasa Pemrograman\n")
for name, info in favorite_languages.items():
    print(f"{name.title():<8} -> {info['language'].title():<7} ({info['level']})")