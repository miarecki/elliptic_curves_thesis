def point_addition(P, Q, p=13):

    u_1, v_1 = P
    u_2, v_2 = Q

    slope = (v_2 - v_1) * pow(u_2 - u_1, -1, p) % p

    u_3 = (slope**2 - u_1 - u_2) % p
    v_3 = (slope * (u_1 - u_3) - v_1) % p

    return (u_3, v_3)

print(point_addition([3,11],[5,2]))

def point_doubling(P, A, p=13):
    u_1, v_1 = P

    slope = (3 * u_1**2 + A) * pow(2 * v_1, -1, p) % p

    u_2 = (slope**2 - 2 * u_1) % p
    v_2 = (slope * (u_1 - u_2) - v_1) % p

    return (u_2, v_2)

print(point_doubling([5,2], A=3))