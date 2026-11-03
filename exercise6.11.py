cities = {
    'jakarta': {
        'country': 'Indonesia',
        'population': 10_878_676,
        'fact': 'Kota terbesar di Indonesia.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': 33_400_000,
        'fact': 'Pernah menjadi tuan rumah Olimpiade tahun 1964 dan 2020.',
    },
    'paris': {
        'country': 'Prancis',
        'population': 2_047_602,
        'fact': 'Menara Eiffel berdiri di kota ini.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Negara: {info['country']}")
    print(f"  Populasi (perkiraan): {info['population']:,}")
    print(f"  Fakta: {info['fact']}")