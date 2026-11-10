pet_1 = {'animal': 'kucing', 'owner': 'abi'}
pet_2 = {'animal': 'anjing', 'owner': 'iyan'}
pet_3 = {'animal': 'kelinci', 'owner': 'andi'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Hewan: {pet['animal']}, pemilik: {pet['owner']}")