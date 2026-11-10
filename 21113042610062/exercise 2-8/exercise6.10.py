favorite_numbers = {
    'abi': [7, 14],
    'iyan': [3],
    'fayaz': [12, 5, 9],
    'dewi': [8, 88],
    'mubarok': [21, 1],
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(f"- {number}")