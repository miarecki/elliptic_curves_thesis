# Edwards Curve Example: List of points, addition, doubling.

def list_of_points(d, p):

	lst = set()

	for x in range(p):
		for y in range(p):
			if (x**2 + y**2 - 1 - d*x**2*y**2) % p == 0:
				lst.add((x,y))

	return sorted(list(lst))

def addition(x1, y1, x2, y2, d, p):

	lst = list_of_points(d, p)

	if d*x1*x2*y1*y2 in [-1,1]:
		msg = f"Additon not defined."
		return msg

	if (x1, y1) not in lst or (x2, y2) not in lst:
		msg = f"Points not on curve."
		return msg

	return ((x1*y2 + x2*y1)*pow(1 + d*x1*x2*y1*y2, -1, p)%p, (y1*y2 - x2*x1)*pow(1 - d*x1*x2*y1*y2, -1, p)%p)

def doubling(x, y, d, p):

	lst = list_of_points(d, p)

	if (x, y) not in lst:
		msg = f"Point not on curve."
		return msg

	return ((2*x*y)*pow(1 + d*x**2*y**2, -1, p)%p, (y**2-x**2)*pow(1 - d*x**2*y**2, -1, p)%p)

if __name__ == '__main__':
	print(list_of_points(5, 17))
	# P = (5, 7), Q = (6, 6)      #    (5/17)_L = -1.
	print(addition(5, 7, 6, 6, 5, 17))
	print(doubling(5, 7, 5, 17))