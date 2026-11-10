my_foods = ["rendang", "sate", "nasi goreng"]
friend_foods = my_foods[:]

my_foods.append("bakso")
friend_foods.append("es krim")

print("Makanan favorit saya adalah:")
for food in my_foods:
    print(food)

print("\nMakanan favorit teman saya adalah:")
for food in friend_foods:
    print(food)