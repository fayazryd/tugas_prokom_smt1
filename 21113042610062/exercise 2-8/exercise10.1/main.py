
with open("learning_python.txt") as file:
    isi = file.read()

print(isi)


with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())