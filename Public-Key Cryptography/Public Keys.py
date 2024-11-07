e = 65537
p = 17
q = 23
N = p * q
plaintext = 12
ciphertext = pow(plaintext, e, N)
print(ciphertext)
