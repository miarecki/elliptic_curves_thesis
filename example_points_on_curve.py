from itertools import product

p = 13
list_of_points = []

u = list(range(p))

for x, y in product(u, repeat=2):
    if (y**2 - (x**3 + 3*x + 7))%p == 0:
        list_of_points.append((x, y))

list_of_points.sort(key=lambda point: point[0])

print(list_of_points)