sandwich_orders = ['tuna', 'ayam', 'telur', 'keju']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {sandwich} Anda.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang telah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")