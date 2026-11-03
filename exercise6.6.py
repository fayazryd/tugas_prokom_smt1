favorite_languages = {
    "abi": "python",
    "sarah": "c",
    "iyan": "rust",
    "mubarok": "python"
}

people = ["abi", "sarah", "iyan", "mubarok", "rasyid", "andi"]

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()}, Anda sudah mengisi polling.")
    else:
        print(f"{person.title()}, silakan ikut polling bahasa pemrograman favorit!")