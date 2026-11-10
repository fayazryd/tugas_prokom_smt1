def describe_pet(animal_type, pet_name='tanpa nama'):
    print(f"\nSaya punya seekor {animal_type}.")
    print(f"Nama {animal_type} saya adalah {pet_name.title()}.")


describe_pet('hamster', 'mumu')
describe_pet(animal_type='kucing', pet_name='bubu')