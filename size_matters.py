from Crypto.Util.number import inverse, long_to_bytes

Ciphertext = 0x2526512a4abf23fca755defc497b9ab
e = 257
n = 0x592f144c0aeac50bdf57cf6a6a6e135

Ciphertext = int(Ciphertext)
n = int(n)
print(f'N: {n}')

p = 430535396861370041
q = 17209058493553260637

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(Ciphertext,d,n)
print(long_to_bytes(m))