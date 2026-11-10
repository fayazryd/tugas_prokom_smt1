person_1 = {'first_name': 'abi', 'last_name': 'Santoso', 'age': 25, 'city': 'Semarang'}
person_2 = {'first_name': 'iyan', 'last_name': 'Wijaya', 'age': 30, 'city': 'Surabaya'}
person_3 = {'first_name': 'andi', 'last_name': 'Pratama', 'age': 22, 'city': 'Bandung'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name}, umur {person['age']}, tinggal di {person['city']}.")