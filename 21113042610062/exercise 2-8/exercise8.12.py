def make_sandwich(*items):
    print("\nSandwich Anda berisi:")
    for item in items:
        print(f"- {item}")

make_sandwich('tuna')
make_sandwich('ayam', 'selada', 'tomat')
make_sandwich('telur', 'keju', 'mayones', 'timun')