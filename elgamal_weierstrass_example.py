from itertools import product
from ecdsa import ellipticcurve, numbertheory
from ecdsa.ellipticcurve import CurveFp, Point

p = 53
list_of_points = []

u = list(range(p))

for x, y in product(u, repeat=2):
    if (y**2 - (x**3 - 4*x + 20))%p == 0:
        list_of_points.append((x, y))

list_of_points.sort(key=lambda point: point[0])

N = len(list_of_points) + 1

def create_curve(a, b, p):
    return CurveFp(p, a, b)

def point_multiplication(P, k):
    return k * P

curve = create_curve(-4, 20, p)

P = Point(curve, 7, 21)

a = 15
aP = (point_multiplication(P, a).x()%p, point_multiplication(P, a).y()%p)
aP = Point(curve, point_multiplication(P, a).x()%p, point_multiplication(P, a).y()%p)


b = 3
bP = (point_multiplication(P, b).x()%p, point_multiplication(P, b).y()%p)
bP = Point(curve, point_multiplication(P, b).x()%p, point_multiplication(P, b).y()%p)

M = (18, 20)
m1, m2 = M
baP = point_multiplication(aP, b)
second_part = ((m1 + baP.x())%p, (m2 + baP.y())%p)

secret_message = ((bP.x(), bP.y()), second_part)

# decryption

abP = point_multiplication(bP, a)
x1, y1 = second_part
x2, y2 = abP.x(), abP.y()
decrypted_M = ((x1-x2)%p , (y1-y2)%p)


print(curve)
print(f'N:{N}')
print(f'P:{P}')
print(f'M:{M}')
print(f'a:{a}')
print(f'aP:{aP}')
print(f'b:{b}')
print(f'bP:{bP}')
print(f'baP:{baP}')
print(f'M + b(aP):{second_part}')
print(f'secret message:{secret_message}')
print(f'abP:{abP}')
print(f'decrypted message:{decrypted_M}')