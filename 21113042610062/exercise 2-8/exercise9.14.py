from random import choice

tickets = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

winning_ticket = []
while len(winning_ticket) < 4:
    pulled_item = choice(tickets)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print("Tiket yang cocok dengan 4 angka/huruf berikut akan memenangkan hadiah:")
print(winning_ticket)
