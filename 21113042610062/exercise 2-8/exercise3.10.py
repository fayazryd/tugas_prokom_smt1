mountains = ["semeru", "rinjani", "bromo", "merbabu"]

print(mountains)
mountains.append("sumbing")
mountains.insert(0, "lawu")
print(mountains)
del mountains[2]
print(mountains)
popped  = mountains.pop()
print(f"dikeluarkan dengan pop(): {popped}")
mountains.remove("bromo")
print(mountains)
mountains.sort()
print(mountains)
mountains.reverse()
print(mountains)
print(sorted(mountains))
print(f"Jumlah gunung: {len(mountains)}")
print(mountains[-1])
