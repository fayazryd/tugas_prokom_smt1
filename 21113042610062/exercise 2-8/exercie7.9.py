sandwich_orders = ['tuna', 'pastrami', 'ayam', 'pastrami', 'telur', 'pastrami']
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {sandwich} Anda.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang telah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")