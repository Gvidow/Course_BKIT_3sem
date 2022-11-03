a = [1, 2, 3]
squar = [x ** 2 for x in a]

b = [(1, 1), (2, 4), (3, 9)]
b1 = ((x, x ** 2) for x in a)
print(*b1)

b2 = zip(a, squar)
print(*b2)

b3 = map(lambda x: (x, x ** 2), a)
print(*b3)

b4 = map(lambda x, y: (x, y), a, squar)
print(*b4)
