def point_doubling(P, A, p=13):
    u_1, v_1 = P

    slope = (3 * u_1**2 + A) * pow(2 * v_1, -1, p) % p

    u_2 = (slope**2 - 2 * u_1) % p
    v_2 = (slope * (u_1 - u_2) - v_1) % p

    return (u_2, v_2)

P = [3,2]
p_multi = ['O', (3,2)]

for i in range(11):
    P = point_doubling(P, A=3)
    p_multi.append(P)

print(p_multi)
