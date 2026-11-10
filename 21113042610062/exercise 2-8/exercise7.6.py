#1
topping = ""
while topping != 'quit':
    topping = input("\nMasukkan topping (ketik 'quit' untuk selesai): ")
    if topping != 'quit':
        print(f"Topping {topping} akan ditambahkan.")
    
#2
active = True
while active:
    topping = input("\nMasukkan topping (ketik 'quit' untuk selesai): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Topping {topping} akan ditambahkan.")
        

#3
while True:
    topping = input("\nMasukkan topping (ketik 'quit' untuk selesai): ")
    if topping == 'quit':
        break
    print(f"Topping {topping} akan ditambahkan.")