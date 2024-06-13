import matplotlib.pyplot as plt
import pandas as pd
from sympy import primerange, legendre_symbol
import numpy as np


# generate J_p
def give_a_list(p):
	
	temp = set()
	inv_p = pow(16, p-2, p) # FLT
	
	for d in range(2,p):

		delta = d*pow(1-d,4,p)%p
		num = (16*pow(1+14*d+d**2,3,p))%p
		j = num*pow(delta, -1, p)%p
		temp.add(j)

	return temp


def equivclasses_sum(lower, upper):

	file = open(f'eq_sum_{lower}_{upper}.txt','w')

	start_time = time.time()

	primes_list = list(primerange(lower, upper))

	results_list = [sum(give_a_list(p))%p for p in primes_list]
	for a in results_list:
		file.write(str(a)+"\n")

	print(time.time() - start_time)

	return plt.plot(primes_list, results_list)

# equivclasses_sum(5, 2000)
# plt.show()

def equiv_prop_check(lower, upper):
	# 1 := sum = 396
	# 2 := sum = 424
	# 3 := sum = p - 468

	file = open(f'eq_sum_check_{lower}_{upper}.txt','w')

	start_time = time.time()

	primes_list = list(primerange(lower, upper))

	c = 0

	for p in primes_list:

		line = f'{p}: 0'

		classification = sum(give_a_list(p))%p
		c += 1
		print(f'{100*c/len(primes_list)}') #, flush=True) # ?

		if classification == 396%p:
			line = f'{p}: 1'
		if classification == 424%p:
			line = f'{p}: 2'
		if classification == -468%p:
			line = f'{p}: 3'

		file.write(line + "\n")


def equiv_sum_which_prime():

	# file = open(f'eq_sum_check_467_4999.txt','r')
	file = open(f'eq_sum_check_general_5_467.txt','r')

	class1 = []
	class2 = []
	class3 = []

	for line in file:
		if line[-2]=='1':
			class1.append(int(line.split(":")[0]))
		if line[-2]=='2':
			class2.append(int(line.split(":")[0]))
		if line[-2]=='3':
			class3.append(int(line.split(":")[0]))

	results = [None, class1, class2, class3]
	return results



def modify_file_for_plot(filename, new):

	with open(f'{filename}.txt', 'r') as file:
		lines = file.readlines()

	modified_lines = []
	c = 0

	for line in lines:
		parts = line.split(':')
		prime = int(parts[0].strip()) 
		number_after_colon = int(parts[1].strip())

		if number_after_colon == 1:
			modified_lines.append(f"{prime} {396%prime} {number_after_colon}\n")
		elif number_after_colon == 2:
			modified_lines.append(f"{prime} {424%prime} {number_after_colon}\n")
		elif number_after_colon == 3:
			modified_lines.append(f"{prime} {-468%prime} {number_after_colon}\n")
		c += 1

	with open(f'{new}.txt', 'w') as file:
		file.writelines(modified_lines)


# modify_file_for_plot('eq_sum_check_5_5987', 'file_for_general_plot')


# data = np.loadtxt('file_for_general_plot.txt')

# S_p_1 = data[data[:,2] == 1][:, :2]
# S_p_2 = data[data[:,2] == 2][:, :2]
# S_p_3 = data[data[:,2] == 3][:, :2]

''' # up to 467
plt.scatter(S_p_1[:,0], S_p_1[:,1], color = 'red', s = 8)
plt.scatter(S_p_2[:,0], S_p_2[:,1], color = 'green', s = 8)
plt.scatter(S_p_3[:,0], S_p_3[:,1], color = 'blue', s = 8)

plt.legend(['$p \\equiv 3 (mod 8)$', '$p \\equiv 1,5 (mod 8)$', '$p \\equiv 7 (mod 8)$'])

plt.xlim(0,467)
plt.ylim(0,500)

plt.show()
'''

'''
plt.scatter(S_p_1[:,0], S_p_1[:,1], color = 'red', s = 8)
plt.scatter(S_p_2[:,0], S_p_2[:,1], color = 'green', s = 8)
plt.scatter(S_p_3[:,0], S_p_3[:,1], color = 'blue', s = 8)

plt.legend(['$p \\equiv 3 (mod 8)$', '$p \\equiv 1,5 (mod 8)$', '$p \\equiv 7 (mod 8)$'])

plt.xlim(467,5988)
# plt.ylim(0,500)

plt.show()