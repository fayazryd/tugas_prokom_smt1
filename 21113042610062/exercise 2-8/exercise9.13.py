from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Cetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides), end=" ")


for sides in (6, 10, 20):
    die = Die(sides)
    print(f"Melempar dadu {sides} sisi 10 kali:")
    for roll in range(10):
        die.roll_die()
    print("\n")
