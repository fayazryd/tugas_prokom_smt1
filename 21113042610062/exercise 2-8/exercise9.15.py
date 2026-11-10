from random import choice


def get_winning_ticket(possibilities):
    """Tarik 4 angka/huruf berbeda secara acak."""
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket


possibilities = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
my_ticket = [3, 7, 'b', 'e']

attempts = 0
while True:
    attempts += 1
    winning_ticket = get_winning_ticket(possibilities)
    if sorted(map(str, winning_ticket)) == sorted(map(str, my_ticket)):
        break

print(f"Tiket saya {my_ticket} menang setelah {attempts} kali undian.")
