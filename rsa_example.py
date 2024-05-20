import numpy as np

# Private key (Alice)
p = 12346253
q = 77745281

# Public key
n = p*q
e = 3

# Sanity check
print(f'{(np.gcd(e,p-1)==np.gcd(e,q-1))=}')

# She calculates d
d = pow(3,-1,(p-1)*(q-1))

# Bob's original message
m = 330104112106 

# Bob's encrypted message
c = pow(m, e, n) 

# Decryption

decrypted_message = pow(c, d, n)

# Check
print(f'{decrypted_message=}')
print(f'{m=}')


