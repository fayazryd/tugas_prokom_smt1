pizzas = ["sosis", "keju mozzarella", "jamur"]
friend_pizzas = pizzas[:]

pizzas.append("barbeque")
friend_pizzas.append("sosis keju")

print("Pizza favorit saya adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(pizza)