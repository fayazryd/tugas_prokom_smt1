favorite_places = {
    'abi': ['Pantai Parangtritis', 'Candi Borobudur'],
    'iyan': ['Bromo', 'Raja Ampat', 'Danau Toba'],
    'fayaz': ['Lawang Sewu', 'Bali', 'Karimunjawa'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")